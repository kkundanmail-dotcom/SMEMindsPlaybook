// ═══════════════════════════════════════════════════════════
// SMEMINDS STUDIO — in-app animated module video engine (v2)
// Audio-led timeline (no transition gaps), crossfade scenes,
// dedicated caption band (no overlap with animation), topical
// emoji visuals + modern motion, Indian-English male voiceover
// with sentence/marker pauses. No external services / files.
// ═══════════════════════════════════════════════════════════
(function () {
    var SCRIPTS = (typeof VIDEO_SCRIPTS !== 'undefined') ? VIDEO_SCRIPTS : {};
    var INTRO_SEC = 6, OUTRO_SEC = 7;
    var LOGO = (typeof SMEMINDS_LOGO !== 'undefined') ? SMEMINDS_LOGO : '';
    var SENT_PAUSE = 320, MARK_PAUSE = 560, SCENE_PAUSE = 650; // ms — clear sentence + transition pauses
    var SPEEDS = [0.75, 1, 1.25, 1.5, 2];
    var _vspeed = 1;
    try { var sv = parseFloat(localStorage.getItem('smeminds_vspeed')); if (SPEEDS.indexOf(sv) !== -1) _vspeed = sv; } catch (e) {}

    // ── Indian-English voice selection (voices load async, user-overridable) ──
    var _voice = null, _voiceName = '', _hasIndian = false;
    try { _voiceName = localStorage.getItem('smeminds_voice') || ''; } catch (e) {}

    function isIndian(v) {
        return /en[-_]?IN/i.test(v.lang) ||
               /(prabhat|neerja|ravi|heera|aarav|kavya|hemant|madhur|aria.*india|india)/i.test(v.name);
    }
    function rankVoice(v) {              // higher = preferred (Indian male, natural)
        var s = 0;
        if (isIndian(v)) s += 100;
        if (/en[-_]?IN/i.test(v.lang)) s += 25;
        if (/(prabhat|ravi|aarav|hemant|madhur)/i.test(v.name)) s += 18;   // male Indian
        if (/(natural|online)/i.test(v.name)) s += 8;                      // higher quality
        if (/^en/i.test(v.lang)) s += 5;
        if (/(david|mark|guy|aaron|daniel|\bmale\b)/i.test(v.name)) s += 3;
        return s;
    }
    function allVoices() { return window.speechSynthesis ? (speechSynthesis.getVoices() || []) : []; }
    function pickVoice() {
        var vs = allVoices(); if (!vs.length) return;
        _hasIndian = vs.some(isIndian);
        if (_voiceName) {
            var pref = vs.find(function (v) { return v.name === _voiceName; });
            if (pref) { _voice = pref; return; }
        }
        var best = null, bs = -1;
        vs.forEach(function (v) { var r = rankVoice(v); if (r > bs) { bs = r; best = v; } });
        _voice = best || vs[0];
    }
    function loadVoices() { pickVoice(); if (window.SMVideo) SMVideo._refreshVoices(); }
    if (window.speechSynthesis) { loadVoices(); speechSynthesis.onvoiceschanged = loadVoices; }

    // ── Sarvam premium voices (server-proxied; cached) ──
    var SARVAM = { enabled: false, voices: [], loaded: false };
    var _sarvamCache = {};
    var _api = (typeof API_BASE !== 'undefined') ? API_BASE : 'http://127.0.0.1:8000/api';
    function sarvamSpeaker() { return (_voiceName && _voiceName.indexOf('sarvam:') === 0) ? _voiceName.slice(7) : null; }
    function sarvamFetch(spk, text) {
        var key = spk + '|' + text;
        if (_sarvamCache[key]) return Promise.resolve(_sarvamCache[key]);
        return fetch(_api + '/tts', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ text: text, speaker: spk }) })
            .then(function (r) { return r.ok ? r.json() : null; })
            .then(function (d) { var a = d && d.audio; if (a) _sarvamCache[key] = a; return a; })
            .catch(function () { return null; });
    }
    (function loadSarvam() {
        try {
            fetch(_api + '/tts/voices').then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
                if (d && d.enabled && d.voices && d.voices.length) { SARVAM.enabled = true; SARVAM.voices = d.voices; }
                SARVAM.loaded = true;
                // Default to the first premium voice when the user hasn't chosen one
                if (SARVAM.enabled && (!_voiceName || _voiceName.indexOf('sarvam:') !== 0 && !allVoices().some(function (v) { return v.name === _voiceName; }))) {
                    if (!_voiceName) { _voiceName = 'sarvam:' + SARVAM.voices[0].id; try { localStorage.setItem('smeminds_voice', _voiceName); } catch (e) {} }
                }
                if (window.SMVideo) SMVideo._refreshVoices();
            }).catch(function () { SARVAM.loaded = true; });
        } catch (e) { SARVAM.loaded = true; }
    })();

    var EMOJI_FALLBACK = { p1: '🧭', p2: '🗂️', p3: '⚡', p4: '📈', p5: '🎯', p6: '🚚', p7: '🧰', p8: '🛡️', p9: '🔒' };

    // ── Bespoke vector icon set (the on-screen "images", crisp on every device) ──
    var IP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">';
    var ICONS = {
        account: IP + '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2.2"/><path d="M5.5 16c.6-1.6 2-2.4 3.5-2.4S11.9 14.4 12.5 16"/><path d="M15 10h4M15 13h4"/></svg>',
        growth: IP + '<path d="M4 19h16"/><path d="M5 16l4-4 3 2 5-6"/><path d="M17 7h3v3"/></svg>',
        money: IP + '<circle cx="12" cy="12" r="8.5"/><path d="M9.5 8.5h5M9.5 11h5M13.8 8.5c.2 2-1.3 2.5-2.8 2.5h-1l4 5"/></svg>',
        coins: IP + '<ellipse cx="12" cy="7" rx="7" ry="3"/><path d="M5 7v5c0 1.66 3.13 3 7 3s7-1.34 7-3V7"/><path d="M5 12v4c0 1.66 3.13 3 7 3s7-1.34 7-3v-4"/></svg>',
        chart: IP + '<path d="M4 20h16"/><rect x="6" y="11" width="3" height="6" rx="1"/><rect x="11" y="7" width="3" height="10" rx="1"/><rect x="16" y="13" width="3" height="4" rx="1"/></svg>',
        search: IP + '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/></svg>',
        box: IP + '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5"/><path d="M12 12v9"/></svg>',
        truck: IP + '<rect x="2" y="7" width="11" height="9" rx="1"/><path d="M13 10h4l3 3v3h-7z"/><circle cx="6.5" cy="18" r="1.6"/><circle cx="17.5" cy="18" r="1.6"/></svg>',
        tag: IP + '<path d="M3 12l8.5-8.5a2 2 0 0 1 1.4-.6H19a2 2 0 0 1 2 2v5.7a2 2 0 0 1-.6 1.4L12 20.5a2 2 0 0 1-2.8 0L3 14.8a2 2 0 0 1 0-2.8z"/><circle cx="16.5" cy="7.5" r="1.3"/></svg>',
        shield: IP + '<path d="M12 3l7 3v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
        star: IP + '<path d="M12 3.5l2.6 5.3 5.9.9-4.25 4.1 1 5.8L12 17l-5.25 2.6 1-5.8L3.5 9.7l5.9-.9z"/></svg>',
        megaphone: IP + '<path d="M3 11v2l3 1v-4z"/><path d="M6 10l11-5v14L6 14z"/><path d="M9 15v3.4a1.5 1.5 0 0 0 3 0V16"/></svg>',
        target: IP + '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.6" fill="currentColor"/></svg>',
        gear: IP + '<circle cx="12" cy="12" r="3.2"/><path d="M12 3v2.5M12 18.5V21M21 12h-2.5M5.5 12H3M18.4 5.6l-1.8 1.8M7.4 16.6l-1.8 1.8M18.4 18.4l-1.8-1.8M7.4 7.4 5.6 5.6"/></svg>',
        document: IP + '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="M9.5 12h6M9.5 15h6M9.5 9h2"/></svg>',
        image: IP + '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="10" r="1.6"/><path d="M21 16l-5-5-7 7"/></svg>',
        warning: IP + '<path d="M12 4l9 15H3z"/><path d="M12 10v4M12 17h.01"/></svg>',
        check: IP + '<circle cx="12" cy="12" r="8.5"/><path d="M8.3 12.4l2.4 2.4 4.9-5.2"/></svg>',
        rocket: IP + '<path d="M12 3c3 1.5 5 4.5 5 8 0 1.6-.4 3-1 4H8c-.6-1-1-2.4-1-4 0-3.5 2-6.5 5-8z"/><circle cx="12" cy="9.5" r="1.6"/><path d="M9 15l-2 4 3-1M15 15l2 4-3-1"/></svg>',
        calculator: IP + '<rect x="5" y="3" width="14" height="18" rx="2"/><rect x="8" y="6" width="8" height="3" rx="1"/><path d="M8.5 13h.01M12 13h.01M15.5 13h.01M8.5 16.5h.01M12 16.5h.01M15.5 16.5h.01"/></svg>',
        globe: IP + '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 2.5 14.4 0 17M12 3.5c-2.5 2.6-2.5 14.4 0 17"/></svg>',
        lock: IP + '<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><circle cx="12" cy="15" r="1.2"/></svg>',
        trophy: IP + '<path d="M7 4h10v4a5 5 0 0 1-10 0z"/><path d="M7 5H4v2a3 3 0 0 0 3 3M17 5h3v2a3 3 0 0 1-3 3"/><path d="M12 13v4M9 20h6M10 20v-3h4v3"/></svg>',
        idea: IP + '<path d="M9 17h6M10 20h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.6.6 1 1.4 1 2.5h6c0-1.1.4-1.9 1-2.5A6 6 0 0 0 12 3z"/></svg>',
        percent: IP + '<path d="M6 18 18 6"/><circle cx="8" cy="8" r="2"/><circle cx="16" cy="16" r="2"/></svg>',
        calendar: IP + '<rect x="4" y="5" width="16" height="16" rx="2"/><path d="M4 9h16M8 3v4M16 3v4"/><path d="M8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01"/></svg>',
        clock: IP + '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5l3.5 2"/></svg>',
        users: IP + '<circle cx="9" cy="9" r="3"/><path d="M3.5 19c.5-3 2.8-4.5 5.5-4.5s5 1.5 5.5 4.5"/><path d="M16 6.5a3 3 0 0 1 0 5.5M17 14.5c2 .6 3.3 2 3.6 4"/></svg>',
        store: IP + '<path d="M4 9l1.5-5h13L20 9"/><path d="M4 9c0 1.4 1 2.4 2.3 2.4S8.6 10.4 8.6 9c0 1.4 1 2.4 2.3 2.4S13.3 10.4 13.3 9c0 1.4 1 2.4 2.3 2.4S18 10.4 18 9"/><path d="M5 12v8h14v-8"/><path d="M9.5 20v-5h5v5"/></svg>',
        layers: IP + '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/></svg>',
        cart: IP + '<circle cx="9" cy="20" r="1.4"/><circle cx="17" cy="20" r="1.4"/><path d="M3 4h2l2.2 11h10l2-7H6"/></svg>',
        compass: IP + '<circle cx="12" cy="12" r="8.5"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/></svg>',
        sparkle: IP + '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M18.5 15.5l.6 1.8 1.8.6-1.8.6-.6 1.8-.6-1.8-1.8-.6 1.8-.6z"/></svg>'
    };
    function iconSVG(name) { return ICONS[name] || ICONS.sparkle; }

    function esc(s) {
        return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
            .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }
    function fmt(t) {
        t = Math.max(0, Math.round(t));
        return Math.floor(t / 60) + ':' + ((t % 60) < 10 ? '0' : '') + (t % 60);
    }
    // Split narration into spoken chunks at sentence ends and ' | ' markers
    function chunkVO(vo) {
        if (!vo) return [];
        var out = [];
        vo.split('|').forEach(function (seg, si, arr) {
            seg = seg.trim(); if (!seg) return;
            var sentences = seg.match(/[^.!?]+[.!?]*/g) || [seg];
            sentences.forEach(function (s) {
                s = s.trim(); if (s) out.push({ text: s, pause: SENT_PAUSE });
            });
            if (si < arr.length - 1 && out.length) out[out.length - 1].pause = MARK_PAUSE;
        });
        return out;
    }
    // Plain caption text (no pause markers)
    function clean(vo) { return (vo || '').replace(/\s*\|\s*/g, ' ').replace(/\s+/g, ' ').trim(); }

    var PLAY = '<svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>';
    var PAUSE = '<svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>';
    var ICON = {
        cc: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm5.5 6.5c0-.83.67-1.5 1.5-1.5.55 0 1 .3 1.3.74l1.2-.7A2.99 2.99 0 0 0 10 9a3 3 0 0 0 0 6c1.06 0 1.98-.55 2.5-1.38l-1.2-.7c-.3.44-.75.73-1.3.73-.83 0-1.5-.67-1.5-1.5v-.65zm7 0c0-.83.67-1.5 1.5-1.5.55 0 1 .3 1.3.74l1.2-.7A2.99 2.99 0 0 0 17 9a3 3 0 0 0 0 6c1.06 0 1.98-.55 2.5-1.38l-1.2-.7c-.3.44-.75.73-1.3.73-.83 0-1.5-.67-1.5-1.5v-.65z"/></svg>',
        vol: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M5 9v6h4l5 5V4L9 9H5zm11.5 3a3.5 3.5 0 0 0-2-3.16v6.32A3.5 3.5 0 0 0 16.5 12z"/></svg>',
        mute: '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M5 9v6h4l5 5V4L9 9H5z"/><path d="M19 5L5 19" stroke="currentColor" stroke-width="2"/></svg>',
        fs: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5"/></svg>',
        replay: '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>'
    };

    function Player(mid, container) {
        this.mid = mid;
        this.container = container;
        this.data = SCRIPTS[mid];
        this.pillar = (this.data && this.data.pillar) || ('p' + String(mid).split('.')[0]);
        this.speed = _vspeed; this.muted = false; this.captions = false; // speed persists; captions OFF by default — viewer enables via CC button
        this.t = 0; this.displayed = 0; this.sceneStart = 0;
        this.idx = -1; this.playing = false; this._last = null;
        this.narrationDone = false; this._chunkTimer = null;
        this._renderDurs = null; this._renderTimer = null; // offline render mode (timer-driven, deterministic)
        this.accent = (getComputedStyle(container).getPropertyValue('--pf-accent') || '#ff6b35').trim() || '#ff6b35';
        this.buildTimeline();
        this.render();
    }

    Player.prototype.buildTimeline = function () {
        var d = this.data, tl = [];
        tl.push({ type: 'intro', dur: INTRO_SEC });
        var nc = (d.scenes || []).length;
        (d.scenes || []).forEach(function (sc, i) {
            var layout = sc.layout || (sc.highlight && /\d/.test(sc.highlight) ? 'stat' : (i === 0 ? 'hook' : (i === nc - 1 ? 'takeaway' : 'list')));
            tl.push({
                type: 'scene', n: i + 1,
                heading: sc.heading, points: sc.points || [], vo: sc.vo || '',
                emoji: sc.emoji || '', highlight: sc.highlight || '',
                icon: sc.icon || '', layout: layout,
                dur: Math.max(8, Math.min(26, sc.sec || 16))
            });
        });
        tl.push({ type: 'outro', dur: OUTRO_SEC });
        if (LOGO) tl.push({ type: 'logo', dur: 4.5 });   // animated SMEMinds logo sting (code, full-frame)
        this.timeline = tl;
        this.total = tl.reduce(function (a, s) { return a + s.dur; }, 0);
    };

    Player.prototype.render = function () {
        var self = this;
        this.container.classList.add('vplayer-host');
        this.container.innerHTML =
            '<div class="vplayer" tabindex="0" style="--vacc:' + esc(this.accent) + '">' +
                '<div class="vp-stage">' +
                    '<div class="vp-bg"></div>' +
                    '<div class="vp-particles" aria-hidden="true"></div>' +
                    (LOGO ? '<img class="vp-logo-wm" src="' + LOGO + '" alt="SMEMinds">' : '') +
                    '<div class="vp-dots" id="vp-dots"></div>' +
                    '<div class="vp-content" id="vp-content"></div>' +
                    '<div class="vp-captionband"><p class="vp-caption" id="vp-cap"></p></div>' +
                    '<button class="vp-bigplay" id="vp-bigplay" aria-label="Play">' + PLAY + '</button>' +
                '</div>' +
                '<div class="vp-controls">' +
                    '<button class="vp-btn" id="vp-pp" aria-label="Play / pause">' + PLAY + '</button>' +
                    '<span class="vp-time" id="vp-time">0:00</span>' +
                    '<input class="vp-seek" id="vp-seek" type="range" min="0" max="1000" value="0" aria-label="Seek">' +
                    '<span class="vp-time vp-dur" id="vp-dur">' + fmt(this.total) + '</span>' +
                    '<select class="vp-voice" id="vp-voice" title="Narration voice" aria-label="Narration voice"></select>' +
                    '<button class="vp-btn vp-mini" id="vp-speed" aria-label="Audio speed" title="Audio speed">' + this.speed + '×</button>' +
                    '<button class="vp-btn vp-mini" id="vp-cc" aria-label="Captions">' + ICON.cc + '</button>' +
                    '<button class="vp-btn vp-mini" id="vp-mute" aria-label="Mute">' + ICON.vol + '</button>' +
                    '<button class="vp-btn vp-mini" id="vp-fs" aria-label="Fullscreen">' + ICON.fs + '</button>' +
                '</div>' +
            '</div>';
        var q = function (s) { return self.container.querySelector(s); };
        this.el = {
            root: q('.vplayer'), content: q('#vp-content'), cap: q('#vp-cap'),
            big: q('#vp-bigplay'), pp: q('#vp-pp'), time: q('#vp-time'),
            seek: q('#vp-seek'), speed: q('#vp-speed'), cc: q('#vp-cc'),
            mute: q('#vp-mute'), fs: q('#vp-fs'), voice: q('#vp-voice'), dots: q('#vp-dots')
        };
        // Captions start hidden (band collapsed); the CC button shows their state
        this.el.root.classList.toggle('no-cc', !this.captions);
        this.el.cc.classList.toggle('vp-on', this.captions);
        this.el.voice.onchange = function () { self.onVoiceChange(); };
        this.fillVoices();
        // particles
        var pz = '';
        for (var i = 0; i < 14; i++) pz += '<span style="--i:' + i + '"></span>';
        this.container.querySelector('.vp-particles').innerHTML = pz;
        // scene progress dots (one per content scene)
        var dots = '';
        this.timeline.forEach(function (s, k) { if (s.type === 'scene') dots += '<span data-k="' + k + '"></span>'; });
        this.el.dots.innerHTML = dots;

        this.el.big.onclick = function () { self.toggle(); };
        this.el.pp.onclick = function () { self.toggle(); };
        this.el.seek.oninput = function () { self.seek(self.total * (this.value / 1000)); };
        this.el.speed.onclick = function () { self.cycleSpeed(); };
        this.el.cc.onclick = function () { self.toggleCaptions(); };
        this.el.mute.onclick = function () { self.toggleMute(); };
        this.el.fs.onclick = function () { self.toggleFs(); };
        this.el.root.addEventListener('keydown', function (e) {
            if (e.key === ' ' || e.key === 'k') { e.preventDefault(); self.toggle(); }
            else if (e.key === 'ArrowRight') self.seek(self.t + 5);
            else if (e.key === 'ArrowLeft') self.seek(self.t - 5);
            else if (e.key === 'f') self.toggleFs();
        });
        if ('IntersectionObserver' in window) {
            this._io = new IntersectionObserver(function (en) {
                if (!en[0].isIntersecting && self.playing) self.pause();
            }, { threshold: 0.12 });
            this._io.observe(this.el.root);
        }
        // Re-fit the current scene whenever the stage resizes (fullscreen, rotate…)
        if ('ResizeObserver' in window) {
            this._ro = new ResizeObserver(function () { self.fitStat(); self.fitCard(); });
            this._ro.observe(this.el.content);
        }
        this.paintScene(0, true);
        this._tick = this.tick.bind(this);
    };

    // Scale a scene's card down if it would overflow the content zone, so text
    // never spills outside the safe area (over the caption band / controls).
    Player.prototype.fitCard = function (card) {
        card = card || this._curCard;
        if (!card) return;
        var inner = card.querySelector('.vp-card');
        if (!inner) return;
        if (inner.classList.contains('vp-logo-sting')) return;   // sting sizes itself
        inner.style.transform = 'none';
        var cs = getComputedStyle(card);
        var padV = parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom);
        var padH = parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight);
        var availH = this.el.content.clientHeight - padV;
        var availW = this.el.content.clientWidth - padH;
        var h = inner.scrollHeight, w = inner.scrollWidth;
        if (h <= 0 || availH <= 0) return;
        var s = Math.min(1, availH / h, availW / (w || 1));
        if (s < 0.998) {
            inner.style.transformOrigin = 'center center';
            inner.style.transform = 'scale(' + Math.max(0.42, s) + ')';
        }
    };

    // Shrink the donut's stat value until it fits inside the ring (e.g. "24 hours"
    // must not spill outside the circle).
    Player.prototype.fitStat = function (card) {
        card = card || this._curCard;
        if (!card) return;
        var ring = card.querySelector('.vp-stat-ring');
        var hv = card.querySelector('.vp-stat-ring .vp-hl-val');
        if (!ring || !hv) return;
        var d = Math.min(ring.clientWidth, ring.clientHeight);
        if (!d) return;
        var box = d * 0.66;                 // inscribed safe area inside the ring
        hv.style.maxWidth = box + 'px';
        hv.style.fontSize = '';             // reset to the CSS-driven size
        var fs = parseFloat(getComputedStyle(hv).fontSize) || 24, guard = 0;
        while ((hv.scrollWidth > box + 1 || hv.scrollHeight > box + 1) && fs > 8 && guard < 60) {
            fs -= 1; hv.style.fontSize = fs + 'px'; guard++;
        }
    };

    // ── Composition helpers ──
    Player.prototype.medallion = function (s, big) {
        var emoji = s.emoji || EMOJI_FALLBACK[this.pillar] || '';
        return '<div class="vp-medal' + (big ? ' vp-medal-lg' : '') + '">' +
            '<span class="vp-medal-ring"></span>' +
            '<span class="vp-medal-core">' + iconSVG(s.icon || 'sparkle') + '</span>' +
            (emoji ? '<span class="vp-medal-emoji">' + emoji + '</span>' : '') +
            '</div>';
    };
    Player.prototype.kheading = function (text) {
        var words = String(text || '').split(/\s+/).filter(Boolean);
        return '<h3 class="vp-heading">' + words.map(function (w, k) {
            return '<span style="--w:' + (0.05 * k).toFixed(2) + 's">' + esc(w) + '</span>';
        }).join(' ') + '</h3>';
    };
    Player.prototype.bullets = function (points, start) {
        start = start == null ? 0.35 : start;
        return '<ul class="vp-points">' + (points || []).map(function (p, k) {
            return '<li style="--d:' + (start + 0.15 * k).toFixed(2) + 's">' + esc(p) + '</li>';
        }).join('') + '</ul>';
    };
    Player.prototype.stepList = function (points) {
        return '<ol class="vp-steps">' + (points || []).map(function (p, k) {
            return '<li style="--d:' + (0.3 + 0.16 * k).toFixed(2) + 's"><span class="vp-step-no">' + (k + 1) + '</span><span>' + esc(p) + '</span></li>';
        }).join('') + '</ol>';
    };
    Player.prototype.donut = function (hl) {
        return '<div class="vp-stat-ring">' +
            '<svg class="vp-donut" viewBox="0 0 120 120"><circle class="vp-donut-track" cx="60" cy="60" r="52"/><circle class="vp-donut-fill" cx="60" cy="60" r="52"/></svg>' +
            '<span class="vp-hl-val">' + esc(hl) + '</span></div>';
    };

    Player.prototype.cardHTML = function (s, i) {
        if (s.type === 'intro') {
            return '<div class="vp-card vp-card-intro">' +
                (LOGO ? '<img class="vp-card-logo" src="' + LOGO + '" alt="SMEMinds">' : '') +
                '<div class="vp-kicker">SMEMinds Studio presents</div>' +
                '<div class="vp-title">' + esc(this.data.title || this.mid) + '</div>' +
                '<div class="vp-tagline">' + esc(this.data.tagline || '') + '</div>' +
                '<div class="vp-chip">' + esc((function (n, mid) { n = String(n); return (mid === 'overview' || /^\s*module\b/i.test(n)) ? n : ('Module ' + n); })(this.data.number || this.mid, this.mid)) + '</div></div>';
        }
        if (s.type === 'outro') {
            return '<div class="vp-card vp-card-outro">' +
                '<div class="vp-medal vp-medal-lg"><span class="vp-medal-ring"></span><span class="vp-medal-core">' + iconSVG('check') + '</span></div>' +
                '<div class="vp-cta">' + esc(this.data.cta || 'Keep growing with SMEMinds.') + '</div>' +
                (LOGO ? '<img class="vp-out-logo" src="' + LOGO + '" alt="SMEMinds">' : '') +
                '<div class="vp-url">smeminds.com</div></div>';
        }
        if (s.type === 'logo') {
            return '<div class="vp-card vp-logo-sting">' +
                '<span class="vp-sting-rings"><span></span><span></span><span></span></span>' +
                '<span class="vp-sting-burst"></span>' +
                '<span class="vp-sting-logo-wrap">' +
                    (LOGO ? '<img class="vp-sting-logo" src="' + LOGO + '" alt="SMEMinds">' : '') +
                    '<span class="vp-sting-shine"></span>' +
                '</span>' +
                '<span class="vp-sting-tag">smeminds.com</span>' +
            '</div>';
        }
        var layout = s.layout || 'list';
        var head = this.kheading(s.heading);
        var hl = (s.highlight || '').trim();
        var inner;
        if (layout === 'hook') {
            inner = '<div class="vp-l-hook">' + this.medallion(s, true) + head +
                (s.points && s.points[0] ? '<p class="vp-lead">' + esc(s.points[0]) + '</p>' : '') + '</div>';
        } else if (layout === 'stat' && hl) {
            inner = '<div class="vp-l-stat">' + this.donut(hl) +
                '<div class="vp-stat-side"><span class="vp-ico-chip">' + iconSVG(s.icon || 'sparkle') + '</span>' +
                head + this.bullets(s.points, 0.4) + '</div></div>';
        } else if (layout === 'steps') {
            inner = '<div class="vp-l-steps"><div class="vp-head-row">' + this.medallion(s) + head + '</div>' + this.stepList(s.points) + '</div>';
        } else if (layout === 'takeaway') {
            inner = '<div class="vp-l-take">' + this.medallion(s, true) + head + this.bullets(s.points, 0.3) + '</div>';
        } else {
            inner = '<div class="vp-l-list"><div class="vp-head-row">' + this.medallion(s) + head + '</div>' + this.bullets(s.points, 0.4) + '</div>';
        }
        return '<div class="vp-card vp-card-scene vp-lay-' + layout + '">' + inner + '</div>';
    };

    Player.prototype.updateDots = function (i) {
        if (!this.el.dots) return;
        Array.prototype.forEach.call(this.el.dots.children, function (d) {
            var k = parseInt(d.getAttribute('data-k'), 10);
            d.classList.toggle('on', k <= i);
            d.classList.toggle('cur', k === i);
        });
    };

    Player.prototype.paintScene = function (i, silent) {
        this.idx = i;
        var s = this.timeline[i];
        var card = document.createElement('div');
        card.className = 'vp-cardwrap';
        card.innerHTML = this.cardHTML(s, i);
        // crossfade: fade old out, new in
        var old = this.el.content.lastElementChild;
        this.el.content.appendChild(card);
        void card.offsetWidth;
        card.classList.add('in');
        card.querySelector('.vp-card').classList.add('in');
        if (old) { old.classList.add('out'); setTimeout(function () { if (old.parentNode) old.parentNode.removeChild(old); }, 560); }
        // count-up highlight if numeric
        var hv = card.querySelector('.vp-hl-val');
        if (hv) this.countUp(hv);
        this.updateDots(i);
        // Auto-fit content to the safe area + fit the donut stat (now + after fonts)
        this._curCard = card;
        this.fitStat(card);
        this.fitCard(card);
        var self2 = this;
        setTimeout(function () { if (self2._curCard === card) { self2.fitStat(card); self2.fitCard(card); } }, 90);
        // ── Offline render mode: deterministic, timer-driven, no audio (muxed later) ──
        if (this._renderDurs) {
            this.el.root.classList.toggle('logo-mode', s.type === 'logo');
            this.setCaption('');                                   // clean frame (audio is muxed in)
            this.narrationDone = true;
            try { (window.__SMRENDER_MARKS = window.__SMRENDER_MARKS || []).push({ i: i, type: s.type, t: performance.now() }); } catch (e) {}
            return;   // advancement is driven externally by the renderer (immune to bg-tab timer throttling)
        }
        // Logo sting fills the whole player (no caption band); it's purely timed.
        this.el.root.classList.toggle('logo-mode', s.type === 'logo');
        if (s.type === 'logo') {
            this.setCaption('');
            if (window.speechSynthesis) { try { speechSynthesis.cancel(); } catch (e) {} }
            this.narrationDone = true;
            return;
        }
        this.setCaption(clean(s.vo) || (s.type === 'outro' ? clean(this.data.cta) : (s.type === 'intro' ? (this.data.title + '. ' + this.data.tagline) : '')));
        if (!silent) this.speakScene(i);
    };

    Player.prototype.countUp = function (el) {
        var raw = el.textContent, m = raw.match(/^(\D*)(\d[\d,]*)(.*)$/);
        if (!m) return;
        var pre = m[1], target = parseInt(m[2].replace(/,/g, ''), 10), post = m[3];
        if (!target || target > 100000) return;
        var start = null, dur = 900;
        function step(ts) {
            if (!start) start = ts;
            var p = Math.min((ts - start) / dur, 1), e = 1 - Math.pow(1 - p, 3);
            el.textContent = pre + Math.round(target * e).toLocaleString('en-IN') + post;
            if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    };

    Player.prototype.setCaption = function (text) {
        this.el.cap.textContent = this.captions ? (text || '') : '';
    };

    // ── Voice picker: ONLY the SMEMinds HD voices (Ritu & Shubh) ──
    Player.prototype.fillVoices = function () {
        var sel = this.el.voice; if (!sel) return;
        if (SARVAM.enabled && SARVAM.voices.length) {
            sel.innerHTML = SARVAM.voices.map(function (v) {
                var val = 'sarvam:' + v.id;
                return '<option value="' + esc(val) + '"' + (_voiceName === val ? ' selected' : '') +
                    '>🟢 ' + esc(v.label) + ' · HD' + (v.gender ? ' (' + esc(v.gender) + ')' : '') + '</option>';
            }).join('');
            sel.disabled = false;
            // Always keep a Ritu/Shubh voice selected (never a device voice)
            if (!sarvamSpeaker()) {
                _voiceName = 'sarvam:' + SARVAM.voices[0].id; sel.value = _voiceName;
                try { localStorage.setItem('smeminds_voice', _voiceName); } catch (e) {}
            }
            sel.classList.remove('vp-voice-warn');
            sel.title = 'SMEMinds HD voice';
            return;
        }
        // Fallback only if Sarvam is unavailable, so narration still works on-device.
        var vs = allVoices().filter(function (v) { return /^en/i.test(v.lang) || isIndian(v); });
        vs.sort(function (a, b) { return (isIndian(b) ? 1 : 0) - (isIndian(a) ? 1 : 0) || a.name.localeCompare(b.name); });
        if (!vs.length) { sel.innerHTML = '<option>System voice</option>'; sel.disabled = true; return; }
        sel.disabled = false;
        sel.innerHTML = vs.map(function (v) {
            var nm = v.name.replace('Microsoft ', '').replace(' Online (Natural)', '').replace(' Desktop', '');
            var label = (isIndian(v) ? '🇮🇳 ' : '') + nm + (/en[-_]?IN/i.test(v.lang) ? ' · India' : '');
            return '<option value="' + esc(v.name) + '"' + (_voiceName === v.name ? ' selected' : '') + '>' + esc(label) + '</option>';
        }).join('');
        sel.classList.toggle('vp-voice-warn', !_hasIndian);
        sel.title = _hasIndian ? 'Narration voice' : 'Connect to enable SMEMinds HD voices (Ritu / Shubh)';
    };
    Player.prototype.onVoiceChange = function () {
        _voiceName = this.el.voice.value;
        try { localStorage.setItem('smeminds_voice', _voiceName); } catch (e) {}
        pickVoice();
        if (window.SMVideo) SMVideo._refreshVoices();
        if (this.playing) this.speakScene(this.idx);
    };

    // Stop any narration audio (Web Speech utterances + Sarvam clip)
    Player.prototype._stopAudio = function () {
        clearTimeout(this._chunkTimer); clearTimeout(this._renderTimer);
        if (window.speechSynthesis) { try { speechSynthesis.cancel(); } catch (e) {} }
        if (this._audio) { try { this._audio.pause(); this._audio.onended = null; this._audio.onerror = null; } catch (e) {} }
    };

    // ── Narration: route to the premium Sarvam voice or on-device Web Speech ──
    Player.prototype.speakScene = function (i) {
        var s = this.timeline[i];
        this.narrationDone = false;
        this._stopAudio();
        var text = s.type === 'intro' ? ((this.data.title || '') + '. | ' + (this.data.tagline || ''))
                 : s.type === 'outro' ? (this.data.cta || '')
                 : (s.vo || '');
        if (this.muted) { this.narrationDone = true; return; }
        var spk = sarvamSpeaker();
        if (spk && SARVAM.enabled) { this.speakSarvam(i, spk, clean(text)); return; }
        this.speakWebSpeech(i, text);
    };

    // Premium Sarvam clip: one HD audio per scene, advance on its end (Web Speech fallback on failure)
    Player.prototype.speakSarvam = function (i, spk, text) {
        var self = this;
        if (!text) { this.narrationDone = true; this._chunkTimer = setTimeout(function () { if (self.playing && self.idx === i) self.goNext(); }, SCENE_PAUSE); return; }
        this.setCaption(text);
        sarvamFetch(spk, text).then(function (uri) {
            if (!self.playing || self.idx !== i) return;
            if (!uri) { self.speakWebSpeech(i, text); return; }          // graceful fallback
            var a = self._audio || (self._audio = new Audio());
            a.onended = null; a.onerror = null;
            a.src = uri; a.muted = self.muted; try { a.playbackRate = self.speed; } catch (e) {}
            a.onended = function () {
                if (!self.playing || self.idx !== i) return;
                self.narrationDone = true;
                self._chunkTimer = setTimeout(function () { if (self.playing && self.idx === i) self.goNext(); }, SCENE_PAUSE);
            };
            a.onerror = function () { if (self.playing && self.idx === i) self.speakWebSpeech(i, text); };
            // brief lead-in so the scene's visuals land before the voice (calm pacing)
            self._chunkTimer = setTimeout(function () {
                if (!self.playing || self.idx !== i) return;
                var p = a.play(); if (p && p.catch) p.catch(function () {});
            }, 240 / self.speed);
            // warm the next scene's clip for gapless playback
            var nx = self.timeline[i + 1];
            if (nx && (nx.type === 'scene' || nx.type === 'outro' || nx.type === 'intro')) {
                var nt = clean(nx.type === 'outro' ? self.data.cta : nx.type === 'intro' ? (self.data.title + '. ' + self.data.tagline) : nx.vo);
                if (nt) sarvamFetch(spk, nt);
            }
        }).catch(function () { if (self.playing && self.idx === i) self.speakWebSpeech(i, text); });
    };

    // On-device Web Speech: chunk-by-chunk with pauses, then advance
    Player.prototype.speakWebSpeech = function (i, text) {
        var self = this;
        var chunks = chunkVO(text);
        if (!window.speechSynthesis || !chunks.length) { this.narrationDone = true; return; }
        var k = 0;
        function next() {
            if (!self.playing || self.idx !== i) return;
            if (k >= chunks.length) {
                self.narrationDone = true;
                self._chunkTimer = setTimeout(function () { if (self.playing && self.idx === i) self.goNext(); }, SCENE_PAUSE);
                return;
            }
            var c = chunks[k++];
            self.setCaption(c.text);
            var u = new SpeechSynthesisUtterance(c.text);
            if (_voice) u.voice = _voice;
            u.lang = 'en-IN';
            u.rate = Math.max(0.6, Math.min(1.5, 0.88 * self.speed));
            u.pitch = 1.0;
            u.onend = function () { if (!self.playing || self.idx !== i) return; self._chunkTimer = setTimeout(next, c.pause / self.speed); };
            u.onerror = function () { if (self.playing && self.idx === i) self._chunkTimer = setTimeout(next, 120); };
            try { speechSynthesis.speak(u); } catch (e) { next(); }
        }
        this._chunkTimer = setTimeout(next, 260);
    };

    // ── Timeline clock (drives progress bar; audio drives scene advance) ──
    Player.prototype.startLoop = function () {
        if (this._looping) return;       // exactly one rAF loop at a time
        this._looping = true; this._last = null;
        requestAnimationFrame(this._tick);
    };
    Player.prototype.tick = function (ts) {
        if (!this.playing) { this._looping = false; return; }
        if (this._last == null) this._last = ts;
        var dt = Math.min(0.25, (ts - this._last) / 1000) * this.speed;
        this._last = ts;
        this.t += dt;
        var s = this.timeline[this.idx];
        var intra = this.t - this.sceneStart;
        // Scene advance never stops the loop (the tail reschedule keeps it single).
        if (this._renderDurs) { this.paintProgress(Math.min(intra, s.dur)); }        // render mode: timers advance, clock only paints
        else if (s.type === 'logo' && intra >= s.dur) { this.goNext(); }             // logo sting: timed
        else if (intra >= s.dur + 6) { this.goNext(); }                             // stall safety
        else if (this.narrationDone && (this.muted || !window.speechSynthesis) && intra >= s.dur) { this.goNext(); } // muted: clock-driven
        else { this.paintProgress(Math.min(intra, s.dur)); }
        if (this.playing) requestAnimationFrame(this._tick);
    };

    Player.prototype.paintProgress = function (intra) {
        var cur = Math.min(this.total, this.displayed + intra);
        this.el.seek.value = Math.round((cur / this.total) * 1000);
        this.el.time.textContent = fmt(cur);
        this.el.root.style.setProperty('--vp-prog', ((cur / this.total) * 100) + '%');
    };

    Player.prototype.goNext = function () {
        var prev = this.timeline[this.idx];
        this.displayed = Math.min(this.total, this.displayed + (prev ? prev.dur : 0));
        var ni = this.idx + 1;
        if (ni >= this.timeline.length) { this.finish(); return; }
        this.sceneStart = this.t;
        this.paintScene(ni, false);
        // Note: no requestAnimationFrame here — tick()'s tail keeps the single loop alive.
    };

    Player.prototype._curIsLogo = function () { var s = this.timeline[this.idx]; return !!(s && s.type === 'logo'); };
    Player.prototype.startSegment = function (i) {   // start narration, or hold on the (timed) logo sting
        var s = this.timeline[i];
        if (s && s.type === 'logo') { this.narrationDone = true; }
        else this.speakScene(i);
    };

    Player.prototype.play = function () {
        if (this.idx >= this.timeline.length - 1 && this.narrationDone && this.t >= this.total) this.reset();
        SMVideo._stopOthers(this);
        this.playing = true; this._last = null;
        this.el.root.classList.add('playing'); this.el.root.classList.remove('ended');
        this.el.pp.innerHTML = PAUSE; this.el.big.innerHTML = PAUSE;
        if (this.idx < 0) { this.sceneStart = this.t; this.paintScene(0, false); }
        else this.startSegment(this.idx);
        if (!this._renderDurs) this.startLoop();   // render mode advances via timers, not the rAF clock
    };
    Player.prototype.startRenderMode = function (durs) {
        this._renderDurs = durs || [];
        this.muted = true;                          // no live audio — narration is muxed in afterwards
        try { window.__SMRENDER_MARKS = []; window.__SMRENDER_DONE = false; } catch (e) {}
    };
    Player.prototype.pause = function () {
        this.playing = false;
        this.el.root.classList.remove('playing');
        this.el.pp.innerHTML = PLAY; this.el.big.innerHTML = PLAY;
        clearTimeout(this._renderTimer);
        this._stopAudio();
    };
    Player.prototype.toggle = function () { this.playing ? this.pause() : this.play(); };
    Player.prototype.reset = function () {
        this.t = 0; this.displayed = 0; this.sceneStart = 0; this.idx = -1; this.narrationDone = false;
        this.el.content.innerHTML = '';
    };
    Player.prototype.finish = function () {
        this.pause();
        this.t = this.total; this.paintProgress(0);
        this.el.seek.value = 1000; this.el.time.textContent = fmt(this.total);
        this.el.root.style.setProperty('--vp-prog', '100%');
        this.el.root.classList.add('ended');
        this.el.big.innerHTML = ICON.replay;
        if (this._renderDurs) { try { window.__SMRENDER_DONE = true; window.__SMRENDER_END = performance.now(); } catch (e) {} }
    };

    Player.prototype.seek = function (target) {
        target = Math.max(0, Math.min(this.total, target));
        // locate scene by cumulative dur
        var acc = 0, i = 0;
        for (; i < this.timeline.length; i++) {
            if (target < acc + this.timeline[i].dur || i === this.timeline.length - 1) break;
            acc += this.timeline[i].dur;
        }
        this.displayed = acc; this.t = target; this.sceneStart = acc;
        this.t = Math.max(target, acc); // keep clock >= scene start
        this.el.root.classList.remove('ended');
        this.paintScene(i, true);
        this.paintProgress(target - acc);
        if (this.playing) { this._last = null; this.startSegment(i); this.startLoop(); }
    };

    Player.prototype.cycleSpeed = function () {
        var i = SPEEDS.indexOf(this.speed); if (i < 0) i = 1;
        var n = SPEEDS[(i + 1) % SPEEDS.length];
        this.speed = n; _vspeed = n;
        try { localStorage.setItem('smeminds_vspeed', String(n)); } catch (e) {}  // persists across scenes & videos
        this.el.speed.textContent = n + '×';
        if (this._audio) { try { this._audio.playbackRate = n; } catch (e) {} }    // premium clip: retime live
        if (this.playing && !this._curIsLogo() && !(this._audio && !this._audio.paused)) this.speakScene(this.idx); // re-pace Web Speech
    };
    Player.prototype.toggleCaptions = function () {
        this.captions = !this.captions;
        this.el.cc.classList.toggle('vp-on', this.captions);
        this.el.root.classList.toggle('no-cc', !this.captions);
        if (!this.captions) this.el.cap.textContent = '';
    };
    Player.prototype.toggleMute = function () {
        this.muted = !this.muted;
        this.el.mute.innerHTML = this.muted ? ICON.mute : ICON.vol;
        this.el.mute.classList.toggle('vp-off', this.muted);
        if (this.muted) { this._stopAudio(); this.narrationDone = true; }
        else if (this.playing && !this._curIsLogo()) this.speakScene(this.idx);
    };
    Player.prototype.toggleFs = function () {
        var el = this.el.root;
        if (document.fullscreenElement || document.webkitFullscreenElement) {
            (document.exitFullscreen || document.webkitExitFullscreen).call(document);
        } else (el.requestFullscreen || el.webkitRequestFullscreen).call(el);
    };
    Player.prototype.destroy = function () { this.pause(); if (this._audio) { try { this._audio.src = ''; } catch (e) {} } if (this._io) this._io.disconnect(); if (this._ro) this._ro.disconnect(); };

    window.SMVideo = {
        _active: [],
        open: function (mid, container) {
            if (!SCRIPTS[mid]) return;
            var p = new Player(mid, container);
            this._active.push(p); p.play(); return p;
        },
        // Mount a player WITHOUT autoplay — shows scene 0 as a poster + big play button.
        mount: function (mid, container) {
            if (!SCRIPTS[mid]) return null;
            var p = new Player(mid, container);
            this._active.push(p);
            return p;
        },
        _stopOthers: function (keep) { this._active.forEach(function (p) { if (p !== keep) p.pause(); }); },
        _refreshVoices: function () { this._active.forEach(function (p) { if (p.fillVoices) p.fillVoices(); }); },
        stopAll: function () { this._active.forEach(function (p) { p.pause(); }); },
        has: function (mid) { return !!SCRIPTS[mid]; },
        list: function () { return Object.keys(SCRIPTS); },
        // Exact per-slot narration text (matches what the player speaks) for the offline renderer.
        renderTexts: function (mid) {
            var d = SCRIPTS[mid]; if (!d) return null;
            var out = [{ type: 'intro', text: clean((d.title || '') + '. | ' + (d.tagline || '')) }];
            (d.scenes || []).forEach(function (sc) { out.push({ type: 'scene', text: clean(sc.vo || '') }); });
            out.push({ type: 'outro', text: clean(d.cta || '') });
            if (LOGO) out.push({ type: 'logo', text: '' });
            return out;
        },
        // Offline render: play deterministically with per-scene durations (ms), audio muxed later.
        renderPlay: function (mid, container, dursMs) {
            if (!SCRIPTS[mid]) return null;
            var p = new Player(mid, container);
            this._active.push(p);
            p.captions = false;   // recorded films stay clean — captions ship as a sidecar .vtt / soft track
            try { p.el.root.classList.add('no-cc'); p.el.cc.classList.remove('vp-on'); p.el.cap.textContent = ''; } catch (e) {}
            p.startRenderMode(dursMs);
            try { window.__SMPLAYER = p; } catch (e) {}   // renderer drives goNext() on this instance
            p.play();
            return p;
        },
        // Called by the offline renderer to advance one scene (wall-clock timed in Node).
        renderStep: function () { if (window.__SMPLAYER) window.__SMPLAYER.goNext(); }
    };
})();
