"""
Seed `modules` table from content_*.py source files.

Run once after creating/migrating the DB:
    python seed_modules.py            # only inserts modules that don't exist
    python seed_modules.py --force    # overwrite all (drops backend edits!)
"""
import os, sys, json, sqlite3, time, argparse

BASE = os.path.dirname(os.path.abspath(__file__))
PLAYBOOK_ROOT = os.path.dirname(BASE)
DB_PATH = os.path.join(BASE, "smeminds.db")

# Make content_*.py importable
sys.path.insert(0, PLAYBOOK_ROOT)


def load_source_modules():
    from content_1 import pillar1_modules
    from content_2 import pillar2_modules
    from content_3 import pillar3_modules
    from content_4 import pillar4_modules
    from content_5 import pillar5_modules
    from content_6 import pillar6_modules
    from content_7 import pillar7_modules
    from content_8 import pillar8_modules
    from content_9 import pillar9_modules
    pillars = {
        "p1": pillar1_modules, "p2": pillar2_modules, "p3": pillar3_modules,
        "p4": pillar4_modules, "p5": pillar5_modules, "p6": pillar6_modules,
        "p7": pillar7_modules, "p8": pillar8_modules, "p9": pillar9_modules,
    }
    rows = []
    for pillar, mods in pillars.items():
        for m in mods:
            data = {
                "id": m.get("id"),
                "pillar": pillar,
                "number": m.get("number", m.get("id", "")),
                "title": m.get("title", ""),
                "difficulty": m.get("difficulty", ""),
                "time": m.get("time", ""),
                "overview": m.get("overview", ""),
                "content": m.get("content", ""),
                "process_flow": m.get("process_flow", ""),
                "tools": m.get("tools", ""),
                "videos": m.get("videos", []),
                "checklist": m.get("checklist", []),
                "quiz": m.get("quiz", []),
            }
            rows.append((data["id"], pillar, data["number"], data["title"], data))
    return rows


def seed(force: bool = False):
    if not os.path.exists(DB_PATH):
        print(f"[!] DB not found at {DB_PATH}. Start the backend once to initialise it, then re-run.")
        sys.exit(1)
    rows = load_source_modules()
    now = int(time.time())
    inserted = updated = skipped = 0
    with sqlite3.connect(DB_PATH) as c:
        c.row_factory = sqlite3.Row
        for mid, pillar, number, title, data in rows:
            existing = c.execute("SELECT id FROM modules WHERE id=?", (mid,)).fetchone()
            if existing and not force:
                skipped += 1
                continue
            payload = json.dumps(data, ensure_ascii=False)
            if existing:
                c.execute(
                    "UPDATE modules SET pillar=?, number=?, title=?, data=?, updated_at=? WHERE id=?",
                    (pillar, number, title, payload, now, mid),
                )
                updated += 1
            else:
                c.execute(
                    "INSERT INTO modules (id, pillar, number, title, data, updated_at) VALUES (?,?,?,?,?,?)",
                    (mid, pillar, number, title, payload, now),
                )
                inserted += 1
        c.commit()
    print(f"[OK] seed complete: {inserted} inserted, {updated} updated, {skipped} skipped (use --force to overwrite).")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--force", action="store_true", help="Overwrite existing rows (discards backend edits)")
    args = p.parse_args()
    seed(force=args.force)
