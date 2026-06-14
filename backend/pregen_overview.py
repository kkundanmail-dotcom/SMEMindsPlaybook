"""Pre-generate Sarvam narration for the dashboard OVERVIEW film into the TTS cache
(so it plays free, exactly like the module films). Run once after editing overview_video.json:
    cd backend && python pregen_overview.py
"""
import json, os, sys
import pregen_tts as P

OV = os.path.join(os.path.dirname(P.BASE), 'src', 'overview_video.json')

def main():
    ov = json.load(open(OV, encoding='utf-8'))
    texts = [P.clean((ov.get('title', '') + '. | ' + ov.get('tagline', '')))]
    for sc in ov.get('scenes', []):
        t = P.clean(sc.get('vo', ''))
        if t:
            texts.append(t)
    texts.append(P.clean(ov.get('cta', '')))
    texts = [t for t in dict.fromkeys(texts) if t]   # de-dupe, drop empties

    key, model = P.resolve_key_model()
    if not key:
        print('ERROR: No Sarvam key (save it in /admin AI Voice or set SARVAM_API_KEY).')
        sys.exit(1)
    os.makedirs(P.CACHE_DIR, exist_ok=True)
    made = cached = failed = 0
    for spk in P.VOICES:
        for t in texts:
            p = P.cache_path(model, spk, t)
            if os.path.exists(p):
                cached += 1; continue
            try:
                open(p, 'w').write(P.synth(key, model, spk, t)); made += 1
            except Exception as e:
                failed += 1; print(f'  ! {spk}: {t[:46]!r} -> {e}')
    print(f'Overview narration: {len(texts)} lines x {len(P.VOICES)} voices | made={made} cached={cached} failed={failed}')
    if failed == 0:
        print('[OK] Overview film narration cached. Plays with zero further API cost.')

if __name__ == '__main__':
    main()
