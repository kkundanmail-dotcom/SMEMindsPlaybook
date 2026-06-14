"""
One-off migration: cyclic pillar renumber so Account Management becomes Pillar 1.

Mapping (old -> new pillar index):  1->2, 2->3, ... 8->9, 9->1
  - old p9 (Account Mgmt, 9.x)  -> p1 (1.x)
  - old p1 (Selection, 1.x)     -> p2 (2.x)
  - ...
  - old p8 (Brand Protection)   -> p9 (9.x)

The sub-number (the part after the dot) is preserved: 9.3 -> 1.3, 3.2 -> 4.2.
Also rewrites safe textual cross-references inside content/quiz/checklist:
"Pillar N" and "Module N.M".

After migrating the DB it regenerates content_1..9.py so the seed/build
fallback stays consistent with the live data.
"""
import os, sys, re, json, sqlite3, time

BASE = os.path.dirname(os.path.abspath(__file__))
PLAYBOOK_ROOT = os.path.dirname(BASE)
DB_PATH = os.path.join(BASE, "smeminds.db")

DIGIT_MAP = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 1}

PILLAR_NAME = {
    1: "Account Management & Compliance", 2: "Selection", 3: "Efficiency",
    4: "Traffic", 5: "Conversion", 6: "Speed", 7: "Tools",
    8: "Brand Registry", 9: "Brand Protection",
}

_re_pillar = re.compile(r"\bPillar ([1-9])\b")
_re_module = re.compile(r"\bModule ([1-9])\.([0-9])\b")


def remap_text(s):
    if not isinstance(s, str) or not s:
        return s
    s = _re_pillar.sub(lambda mo: f"Pillar {DIGIT_MAP[int(mo.group(1))]}", s)
    s = _re_module.sub(lambda mo: f"Module {DIGIT_MAP[int(mo.group(1))]}.{mo.group(2)}", s)
    return s


def remap_module(data):
    """Return a new module dict with renumbered ids + remapped cross-refs."""
    old_id = data["id"]                       # e.g. "9.3"
    head, sub = old_id.split(".")
    new_head = DIGIT_MAP[int(head)]
    new_id = f"{new_head}.{sub}"
    new_pillar = f"p{new_head}"

    out = dict(data)
    # Text fields first (do NOT touch id/number — set explicitly below)
    for f in ("overview", "content", "process_flow", "tools"):
        if f in out:
            out[f] = remap_text(out[f])
    if isinstance(out.get("checklist"), list):
        out["checklist"] = [remap_text(x) for x in out["checklist"]]
    if isinstance(out.get("quiz"), list):
        nq = []
        for q in out["quiz"]:
            q = dict(q)
            q["question"] = remap_text(q.get("question", ""))
            q["explanation"] = remap_text(q.get("explanation", ""))
            q["answer"] = remap_text(q.get("answer", ""))
            if isinstance(q.get("options"), list):
                q["options"] = [remap_text(o) for o in q["options"]]
            nq.append(q)
        out["quiz"] = nq

    out["id"] = new_id
    out["pillar"] = new_pillar
    out["number"] = f"Module {new_id}"
    return new_id, new_pillar, out


def migrate():
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory = sqlite3.Row
        rows = c.execute("SELECT id, data FROM modules").fetchall()
        new_rows = []
        for r in rows:
            data = json.loads(r["data"])
            new_id, new_pillar, new_data = remap_module(data)
            new_rows.append((new_id, new_pillar, new_data["number"],
                             new_data["title"], json.dumps(new_data, ensure_ascii=False)))
        now = int(time.time())
        c.execute("DELETE FROM modules")
        c.executemany(
            "INSERT INTO modules (id, pillar, number, title, data, updated_at) VALUES (?,?,?,?,?,?)",
            [(nid, pil, num, title, payload, now) for (nid, pil, num, title, payload) in new_rows],
        )
        c.commit()
    print(f"[OK] DB migrated: {len(new_rows)} modules renumbered.")


def sort_key(mid):
    h, s = mid.split(".")
    return (int(h), int(s))


def regenerate_content():
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory = sqlite3.Row
        rows = c.execute("SELECT id, pillar, data FROM modules").fetchall()
    by_pillar = {}
    for r in rows:
        by_pillar.setdefault(r["pillar"], []).append(json.loads(r["data"]))
    for n in range(1, 10):
        pid = f"p{n}"
        mods = sorted(by_pillar.get(pid, []), key=lambda d: sort_key(d["id"]))
        body = json.dumps(mods, indent=2, ensure_ascii=False)
        header = (
            "# " + "=" * 62 + "\n"
            f"# PILLAR {n} — {PILLAR_NAME[n].upper()}  ({len(mods)} Modules)\n"
            "# Auto-generated from the backend DB by _renumber.py.\n"
            "# Edit modules in the admin panel (source of truth = smeminds.db).\n"
            "# " + "=" * 62 + "\n\n"
        )
        path = os.path.join(PLAYBOOK_ROOT, f"content_{n}.py")
        with open(path, "w", encoding="utf-8") as f:
            f.write(header + f"pillar{n}_modules = " + body + "\n")
        print(f"  wrote content_{n}.py  ({len(mods)} modules, pillar {n} = {PILLAR_NAME[n]})")


if __name__ == "__main__":
    migrate()
    regenerate_content()
    print("[DONE] Renumber complete.")
