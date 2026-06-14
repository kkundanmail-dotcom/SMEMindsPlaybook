// ═══════════════════════════════════════════════════════════
// SMEMINDS AMAZON ACCOUNT MANAGEMENT PLAYBOOK — CORE APP
// ═══════════════════════════════════════════════════════════

// ── COPY PROTECTION ─────────────────────────────────────────
// Form fields stay usable: protection never blocks typing/copying inside
// the user's own inputs and textareas.
function isEditableTarget(e) {
    return !!(e.target && e.target.closest && e.target.closest('input, textarea, select, [contenteditable]'));
}
document.addEventListener('contextmenu', e => { if (!isEditableTarget(e)) e.preventDefault(); });
document.addEventListener('keydown', e => {
    if (isEditableTarget(e)) return;
    if (e.key === 'F12' ||
        (e.ctrlKey && ['u','U','c','C','a','A','s','S','p','P'].includes(e.key)) ||
        (e.metaKey && ['u','c','a','s'].includes(e.key))) {
        e.preventDefault(); showToast();
    }
});
document.addEventListener('copy', e => {
    if (isEditableTarget(e)) return;
    e.preventDefault(); showToast();
});

// ── SHARED HELPERS ──────────────────────────────────────────
function escHtml(s) {
    return String(s == null ? '' : s)
        .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// Assign the single shared logo embed to every branded <img>
function applyBrandLogos(root) {
    if (typeof SMEMINDS_LOGO === 'undefined' || !SMEMINDS_LOGO) return;
    (root || document).querySelectorAll('img.brand-logo').forEach(function(img) {
        if (!img.src) img.src = SMEMINDS_LOGO;
    });
}

// Authenticated fetch that detects expired/invalid sessions: on 401 the stale
// session is cleared and the login overlay returns instead of silent failure.
async function authFetch(url, opts) {
    const sess = getSession();
    opts = opts || {};
    opts.headers = Object.assign({}, opts.headers || {});
    if (sess && sess.token) opts.headers['Authorization'] = 'Bearer ' + sess.token;
    const r = await fetch(url, opts);
    if (r.status === 401 && sess) {
        clearSession();
        const overlay = document.getElementById('login-overlay');
        const app = document.getElementById('main-app');
        if (overlay) { overlay.style.display = ''; overlay.setAttribute('data-view', 'signin'); }
        if (app) app.style.display = 'none';
        showToastMsg('Your session expired — please sign in again.');
    }
    return r;
}

function showToast() {
    const t = document.getElementById('copy-toast');
    if (!t) return;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3000);
}

// ── MODULE REGISTRY ──────────────────────────────────────────
const MODULES_LIST = [
    // P1 — Account Management & Compliance (8 modules)
    { id:'1.1', title:'Marketplace Foundations',    pillar:'p1' },
    { id:'1.2', title:'Account Setup & Registration',pillar:'p1' },
    { id:'1.3', title:'Seller Central Console',     pillar:'p1' },
    { id:'1.4', title:'Account Health & Metrics',   pillar:'p1' },
    { id:'1.5', title:'Suspension & Appeals',       pillar:'p1' },
    { id:'1.6', title:'Tax & Compliance: GST/TDS/TCS',pillar:'p1' },
    { id:'1.7', title:'Returns & Reconciliation',   pillar:'p1' },
    { id:'1.8', title:'Fee & Economics Reference',  pillar:'p1' },
    // P2 — Selection (8 modules)
    { id:'2.1', title:'Catalogue Strategy',         pillar:'p2' },
    { id:'2.2', title:'Catalogue Building',         pillar:'p2' },
    { id:'2.3', title:'Catalogue Health',           pillar:'p2' },
    { id:'2.4', title:'Localisation',               pillar:'p2' },
    { id:'2.5', title:'Fee Schedule & Cost Mastery',pillar:'p2' },
    { id:'2.6', title:'Flat File Bulk Management',  pillar:'p2' },
    { id:'2.7', title:'FBA Shipment Creation',      pillar:'p2' },
    { id:'2.8', title:'Variations & Size Charts',   pillar:'p2' },
    // P3 — Efficiency (7 modules)
    { id:'3.1', title:'Listing Quality',            pillar:'p3' },
    { id:'3.2', title:'Image Optimisation',         pillar:'p3' },
    { id:'3.3', title:'Pricing Strategy',           pillar:'p3' },
    { id:'3.4', title:'Review & Rating',            pillar:'p3' },
    { id:'3.5', title:'A+ & Brand Content',         pillar:'p3' },
    { id:'3.6', title:'Buy Box Strategy',           pillar:'p3' },
    { id:'3.7', title:'Deals & Promotions',         pillar:'p3' },
    // P4 — Traffic (6 modules)
    { id:'4.1', title:'Sponsored Ads',              pillar:'p4' },
    { id:'4.2', title:'DSP & Display',              pillar:'p4' },
    { id:'4.3', title:'External Traffic',           pillar:'p4' },
    { id:'4.4', title:'Organic SEO',                pillar:'p4' },
    { id:'4.5', title:'Deals & Events',             pillar:'p4' },
    { id:'4.6', title:'Sponsored Ads Deep-Dive',    pillar:'p4' },
    // P5 — Conversion (5 modules)
    { id:'5.1', title:'Detail Page CRO',            pillar:'p5' },
    { id:'5.2', title:'Promotions & Deals',         pillar:'p5' },
    { id:'5.3', title:'Social Proof',               pillar:'p5' },
    { id:'5.4', title:'Post-Purchase',              pillar:'p5' },
    { id:'5.5', title:'Cross-sell & Upsell',        pillar:'p5' },
    // P6 — Speed (7 modules)
    { id:'6.1', title:'FBA Management',             pillar:'p6' },
    { id:'6.2', title:'FBM & Easy Ship',            pillar:'p6' },
    { id:'6.3', title:'Inventory Planning',         pillar:'p6' },
    { id:'6.4', title:'Account Health & SLA',       pillar:'p6' },
    { id:'6.5', title:'Easy Ship Prime & GD',       pillar:'p6' },
    { id:'6.6', title:'Seller Flex',                pillar:'p6' },
    { id:'6.7', title:'IXD Programme',              pillar:'p6' },
    // P7 — Tools (8 modules)
    { id:'7.1', title:'Seller Central',             pillar:'p7' },
    { id:'7.2', title:'Brand Analytics',            pillar:'p7' },
    { id:'7.3', title:'Advertising Console',        pillar:'p7' },
    { id:'7.4', title:'3P Tools',                   pillar:'p7' },
    { id:'7.5', title:'Manage Your Experiments',    pillar:'p7' },
    { id:'7.6', title:'Kitna Milega — Profitability',pillar:'p7' },
    { id:'7.7', title:'Subscribe & Save + MOQ + AUR',pillar:'p7' },
    { id:'7.8', title:'LTSF & Inventory Age',       pillar:'p7' },
    // P8 — Brand Registry (6 modules)
    { id:'8.1', title:'BR Enrolment',               pillar:'p8' },
    { id:'8.2', title:'Brand Store',                pillar:'p8' },
    { id:'8.3', title:'A+ Content (BR)',             pillar:'p8' },
    { id:'8.4', title:'Sponsored Brands',           pillar:'p8' },
    { id:'8.5', title:'MYE via Brand Registry',     pillar:'p8' },
    { id:'8.6', title:'Vine Programme',             pillar:'p8' },
    // P9 — Brand Protection (8 modules)
    { id:'9.1', title:'IP & Trademark',             pillar:'p9' },
    { id:'9.2', title:'Transparency Programme',     pillar:'p9' },
    { id:'9.3', title:'Project Zero',               pillar:'p9' },
    { id:'9.4', title:'Listing Hijacking',          pillar:'p9' },
    { id:'9.5', title:'Review Manipulation',        pillar:'p9' },
    { id:'9.6', title:'Account Safety',             pillar:'p9' },
    { id:'9.7', title:'Amazon B2B',                 pillar:'p9' },
    { id:'9.8', title:'GIS & Sale Planning',        pillar:'p9' }
];

// ── STATE ─────────────────────────────────────────────────────
let userData = { visited: [], checklists: {}, quizScores: {}, feedback: [] };

// Backend base URL (overridable via window.SMEMINDS_API_BASE before script loads).
const API_BASE = (typeof window !== 'undefined' && window.SMEMINDS_API_BASE) || 'http://127.0.0.1:8000/api';

// ── SUBSCRIPTION / SOFT PAYWALL STATE ────────────────────────
let SUBSCRIPTION = { plan: 'free', is_premium: false, paywall: { free_modules: 3 }, plan_detail: null };
let PLANS_CACHE = [];
let PAYMENTS_MOCK = true;
let BILLING_CYCLE = 'monthly';

// ── TRAFFIC TRACKING ─────────────────────────────────────────
function getOrCreateSessionId() {
    try {
        let sid = sessionStorage.getItem('smeminds_sid');
        if (!sid) {
            sid = 's_' + Date.now().toString(36) + '_' + Math.random().toString(36).slice(2, 10);
            sessionStorage.setItem('smeminds_sid', sid);
        }
        return sid;
    } catch (e) { return null; }
}

function getUtmParams() {
    try {
        const q = new URLSearchParams(location.search);
        return {
            utm_source:   q.get('utm_source')   || null,
            utm_medium:   q.get('utm_medium')   || null,
            utm_campaign: q.get('utm_campaign') || null
        };
    } catch (e) { return { utm_source: null, utm_medium: null, utm_campaign: null }; }
}

function trackEvent(eventType, extra) {
    extra = extra || {};
    const sess = getSession();
    const headers = { 'Content-Type': 'application/json' };
    if (sess && sess.token) headers['Authorization'] = 'Bearer ' + sess.token;
    const body = Object.assign({
        event_type: eventType,
        session_id: getOrCreateSessionId(),
        path: (location && location.pathname) || null
    }, extra);
    try {
        fetch(API_BASE + '/events', {
            method: 'POST', headers: headers,
            body: JSON.stringify(body), keepalive: true
        }).catch(function(){ /* offline */ });
    } catch (e) {}
}

function trackAppOpen() {
    // Fire once per session
    try {
        if (sessionStorage.getItem('smeminds_open_tracked')) return;
        sessionStorage.setItem('smeminds_open_tracked', '1');
    } catch (e) {}
    const utm = getUtmParams();
    trackEvent('app_open', {
        referrer: document.referrer || null,
        utm_source: utm.utm_source,
        utm_medium: utm.utm_medium,
        utm_campaign: utm.utm_campaign
    });
}

const USERDATA_KEY = 'smeminds_playbook_v2';

// Drop duplicate and non-module ids so visited never exceeds the real count
function sanitizeVisited() {
    if (!Array.isArray(userData.visited)) { userData.visited = []; return; }
    const valid = new Set(MODULES_LIST.map(m => m.id));
    userData.visited = Array.from(new Set(userData.visited)).filter(id => valid.has(id));
}
function loadUserData() {
    try { const s = localStorage.getItem(USERDATA_KEY); if (s) userData = JSON.parse(s); } catch(e) {}
    sanitizeVisited();
}
function saveUserData() {
    try { localStorage.setItem(USERDATA_KEY, JSON.stringify(userData)); } catch(e) {}
    updateProgress();
    pushProgressToServer();
}
// The local progress blob belongs to one account. When a different user signs
// in, start fresh instead of merging the previous user's progress into theirs.
function claimLocalDataFor(email) {
    const owner = (email || '').toLowerCase();
    if (userData._owner && userData._owner !== owner) {
        userData = { visited: [], checklists: {}, quizScores: {}, feedback: [], _owner: owner };
    } else {
        userData._owner = owner;
    }
    try { localStorage.setItem(USERDATA_KEY, JSON.stringify(userData)); } catch(e) {}
}

// ── BACKEND SYNC ──────────────────────────────────────────────
let _pushTimer = null;
function pushProgressToServer() {
    const sess = getSession();
    if (!sess || !sess.token) return;
    if (_pushTimer) clearTimeout(_pushTimer);
    _pushTimer = setTimeout(function() {
        authFetch(API_BASE + '/progress', {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                visited: userData.visited || [],
                checklists: userData.checklists || {},
                quizScores: userData.quizScores || {},
                feedback: userData.feedback || []
            })
        }).catch(function(){ /* offline — localStorage already saved */ });
    }, 800);
}

async function pullProgressFromServer() {
    const sess = getSession();
    if (!sess || !sess.token) return;
    try {
        const r = await authFetch(API_BASE + '/progress');
        if (!r.ok) return;
        const data = await r.json();
        // Merge: union of visited, server-wins for the rest (server is authoritative once user signs in).
        const localVisited = userData.visited || [];
        const serverVisited = data.visited || [];
        userData = {
            visited: Array.from(new Set(localVisited.concat(serverVisited))),
            checklists: Object.assign({}, userData.checklists || {}, data.checklists || {}),
            quizScores: Object.assign({}, userData.quizScores || {}, data.quizScores || {}),
            feedback: (data.feedback && data.feedback.length) ? data.feedback : (userData.feedback || []),
            _owner: (sess.email || '').toLowerCase()
        };
        sanitizeVisited();   // drop dupes/junk so progress can't exceed 100%
        try { localStorage.setItem(USERDATA_KEY, JSON.stringify(userData)); } catch(e) {}
        initNav();
        updateProgress();
        pushProgressToServer();  // sync the cleaned state back up
    } catch (e) { /* offline */ }
}

// ── NAV INIT ──────────────────────────────────────────────────
function initNav() {
    ['p1','p2','p3','p4','p5','p6','p7','p8','p9'].forEach(p => {
        const ul = document.getElementById(`nav-${p}`);
        if (!ul) return;
        ul.innerHTML = '';
        MODULES_LIST.filter(m => m.pillar === p).forEach(m => {
            const li = document.createElement('li');
            li.id = `nav_item_${m.id}`;
            const visited = userData.visited.includes(m.id);
            li.innerHTML =
                '<span class="nav-num">' + m.id + '</span>' +
                '<span class="nav-title">' + escHtml(m.title) + '</span>' +
                '<svg class="nav-tick" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>';
            li.title = `${m.id} — ${m.title}`;   // full name on hover (when truncated)
            if (visited) li.classList.add('done');
            li.onclick = () => navToModule(m.id);
            // Keyboard access: nav items are focusable and Enter/Space activate
            li.tabIndex = 0;
            li.setAttribute('role', 'link');
            li.onkeydown = (e) => {
                if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); navToModule(m.id); }
            };
            ul.appendChild(li);
        });
    });
    // innerHTML reset wiped any 🔒 badges — restore them
    if (typeof refreshNavLocks === 'function') refreshNavLocks();
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const main    = document.getElementById('main-content');
    if (!sidebar) return;
    sidebar.classList.toggle('collapsed');
    const collapsed = sidebar.classList.contains('collapsed');
    if (main) main.style.marginLeft = collapsed ? '0' : '';
}

// Accordion: open one pillar at a time, collapsing all the others.
function openPillarExclusive(p) {
    ['p1','p2','p3','p4','p5','p6','p7','p8','p9'].forEach(function(x){
        const on = (x === p);
        const list  = document.getElementById('nav-' + x);
        const group = document.getElementById('group-' + x);
        if (list)  list.classList.toggle('open', on);
        if (group) group.classList.toggle('open', on);
    });
}

function toggleNav(listId, groupId) {
    const list = document.getElementById(listId);
    if (!list) return;
    if (list.classList.contains('open')) {
        // Clicking the open pillar collapses it
        list.classList.remove('open');
        const group = document.getElementById(groupId);
        if (group) group.classList.remove('open');
    } else {
        openPillarExclusive(listId.replace('nav-', ''));
    }
}

// ── NAVIGATION ────────────────────────────────────────────────
function hideAllSections() {
    document.querySelectorAll('.module-section').forEach(el => el.style.display = 'none');
    const dash = document.getElementById('dashboard');
    if (dash) dash.classList.remove('active');
    document.querySelectorAll('.nav-list li').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-home-btn').forEach(b => b.classList.remove('active'));
}

function showDashboard() {
    hideAllSections();
    const dash = document.getElementById('dashboard');
    if (dash) dash.classList.add('active');
    // Always land on the dashboard with every pillar's curriculum collapsed; user expands per need.
    EXPANDED_PILLARS = {};
    document.querySelectorAll('.jp-step.expanded').forEach(function (el) { el.classList.remove('expanded'); });
    setBreadcrumb('Dashboard');
    if (location.hash && location.hash !== '#home') {
        try { location.hash = 'home'; } catch (e) {}
    }
    // Highlight home nav btn
    document.querySelectorAll('.nav-home-btn').forEach(b => b.classList.add('active'));
}

// ── 3-MINUTE OVERVIEW FILM (medium player embedded in the dashboard hero) ──
var _ovPlayer = null;
function mountOverviewPlayer() {
    var host = document.getElementById('overview-video-host');
    if (!host || host.getAttribute('data-mounted')) return;
    if (!(window.SMVideo && SMVideo.mount && SMVideo.has && SMVideo.has('overview'))) return;
    _ovPlayer = SMVideo.mount('overview', host);   // paused poster (scene 0) + play button
    host.setAttribute('data-mounted', '1');
}
function openOverviewVideo() {
    if (typeof showDashboard === 'function') showDashboard();
    mountOverviewPlayer();
    var host = document.getElementById('overview-video-host');
    if (host) host.scrollIntoView({ behavior: 'smooth', block: 'center' });
    if (_ovPlayer && _ovPlayer.play) _ovPlayer.play();
    else if (typeof showToastMsg === 'function') showToastMsg('Overview film is loading — try again in a moment.');
}

// ── HASH DEEP-LINKING ────────────────────────────────────────
// #m-4.1 opens module 4.1 (paywall still enforced inside navToModule);
// back/forward buttons work between modules and the dashboard.
function routeFromHash() {
    const h = location.hash || '';
    const m = h.match(/^#m-(\d+\.\d+)$/);
    if (m) {
        const modEl = document.getElementById('module_' + m[1]);
        if (!modEl || modEl.style.display !== 'block') navToModule(m[1]);
    } else if (h === '#home' || h === '') {
        const dash = document.getElementById('dashboard');
        if (dash && !dash.classList.contains('active')) showDashboard();
    }
}
window.addEventListener('hashchange', routeFromHash);

// Modules ship as inert <template> elements; instantiate into the live DOM on
// first visit so the initial page holds ~1k elements instead of ~13k.
function ensureModuleDom(id) {
    let modEl = document.getElementById(`module_${id}`);
    if (modEl) return modEl;
    const tpl = document.querySelector(`template.module-tpl[data-module="${id}"]`);
    if (!tpl) return null;
    const container = document.getElementById('modules-container');
    if (!container) return null;
    container.appendChild(tpl.content.cloneNode(true));
    modEl = document.getElementById(`module_${id}`);
    if (modEl) applyBrandLogos(modEl);
    return modEl;
}

function pillarNameOf(pillarId) {
    const meta = (typeof PILLAR_META !== 'undefined') && PILLAR_META.find(function(p){ return p.p === pillarId; });
    return meta ? meta.name : pillarId;
}

function navToModule(id) {
    const mObj = MODULES_LIST.find(m => m.id === id);
    if (!mObj) return;
    const modEl = ensureModuleDom(id);
    if (!modEl) return;

    hideAllSections();
    modEl.style.display = 'block';
    const navItem = document.getElementById(`nav_item_${id}`);
    if (navItem) navItem.classList.add('active');

    setBreadcrumb(`${pillarNameOf(mObj.pillar)} › ${mObj.title}`);
    if (location.hash !== '#m-' + id) {
        try { location.hash = 'm-' + id; } catch (e) {}
    }
    // Remove home btn active state
    document.querySelectorAll('.nav-home-btn').forEach(b => b.classList.remove('active'));

    // ── Soft paywall: lock premium lessons for non-subscribers ──
    const unlocked = isModuleUnlocked(id);
    applyModuleLock(modEl, mObj, unlocked);

    if (unlocked) {
        // Track visit
        if (!userData.visited.includes(id)) {
            userData.visited.push(id);
            saveUserData();
            // Mark nav item complete (reveals the checkmark + green chip)
            if (navItem) navItem.classList.add('done');
        }
        trackEvent('module_view', { module_id: id });
        // Restore checklist state
        restoreChecklist(id);
    } else {
        trackEvent('paywall_view', { module_id: id });
    }

    // Scroll to top
    const sc = document.querySelector('.content-scrollable');
    if (sc) sc.scrollTop = 0;

    // On phones the sidebar overlays content — close it after navigating
    if (window.innerWidth <= 768) {
        const sb = document.getElementById('sidebar');
        if (sb) sb.classList.add('collapsed');
    }

    // Auto-open this module's pillar (accordion: collapses the others)
    openPillarExclusive(mObj.pillar);
}

function setBreadcrumb(text) {
    const el = document.getElementById('bc-current');
    if (el) el.textContent = text;
}

// ── PROGRESS ──────────────────────────────────────────────────
// Count only unique, REAL module ids — guards against duplicates or stale/junk
// entries in userData.visited that would otherwise push progress past 100%.
function visitedModuleCount() {
    const set = new Set(userData.visited || []);
    return MODULES_LIST.reduce((n, m) => n + (set.has(m.id) ? 1 : 0), 0);
}

function updateProgress() {
    const total = MODULES_LIST.length;
    const visited = visitedModuleCount();
    const pct = Math.min(100, Math.round((visited / total) * 100));
    const textEl = document.getElementById('progress-text');
    const barEl  = document.getElementById('progress-bar');
    if (textEl) textEl.textContent = `${pct}%`;
    if (barEl)  barEl.style.width  = `${pct}%`;
    updatePillarCounts();
    updateDashboardCertStatus();
    // Patch the journey in place — rebuilding 9 cards + 63 rows + SVG rings on
    // every checkbox tick is wasted layout work
    if (typeof updateJourneyProgress === 'function') updateJourneyProgress();
}

// ── DASHBOARD CERTIFICATION STATUS ───────────────────────────
const CERT_THRESHOLD_PCT = 80;

// The eligibility endpoint result barely changes — cache for 30s so hot paths
// (every checkbox/quiz/feedback save) don't each fire a network round-trip.
let _certEligCache = { ts: 0, data: null };

async function fetchCertEligibility(sess) {
    const now = Date.now();
    if (_certEligCache.data && (now - _certEligCache.ts) < 30000) return _certEligCache.data;
    const r = await authFetch(API_BASE + '/certificate/eligibility');
    if (!r.ok) return null;
    const data = await r.json();
    _certEligCache = { ts: now, data: data };
    return data;
}

async function updateDashboardCertStatus() {
    const card = document.getElementById('cert-status-card');
    if (!card) return;

    const sess = getSession();
    const visited = visitedModuleCount();
    const total = MODULES_LIST.length;
    const threshold = Math.max(1, Math.round(total * CERT_THRESHOLD_PCT / 100));

    const setText = (id, txt) => { const el = document.getElementById(id); if (el) el.textContent = txt; };
    const setWidth = (id, w) => { const el = document.getElementById(id); if (el) el.style.width = w; };

    if (!sess || !sess.token) {
        card.setAttribute('data-state', 'locked');
        setText('cert-status-icon', '🔒');
        setText('cert-status-eyebrow', 'CERTIFICATION');
        setText('cert-status-title', 'Sign in to track your progress');
        setText('cert-status-meta', 'Visit ' + CERT_THRESHOLD_PCT + '% of modules (' + threshold + '/' + total + ') to qualify for your SMEMinds Certificate of Completion.');
        setText('cert-status-percent', '—');
        setWidth('cert-status-fill', '0%');
        const btn = document.getElementById('cert-status-btn');
        if (btn) btn.textContent = 'Sign In';
        return;
    }

    // Try authoritative status from backend, fall back to local progress.
    let issued = null, eligible = visited >= threshold, serverThreshold = threshold;
    try {
        const data = await fetchCertEligibility(sess);
        if (data) {
            eligible = !!data.eligible;
            serverThreshold = data.threshold_modules || threshold;
            if (data.already_issued) {
                issued = { cert_id: data.cert_id, issued_at: data.issued_at };
            }
        }
    } catch (e) { /* offline — use local */ }

    if (issued) {
        card.setAttribute('data-state', 'issued');
        setText('cert-status-icon', '🏆');
        setText('cert-status-eyebrow', 'CERTIFIED');
        setText('cert-status-title', 'Congratulations! You\'re SMEMinds-certified.');
        const dt = issued.issued_at ? new Date(issued.issued_at * 1000).toLocaleDateString('en-IN', {year:'numeric',month:'short',day:'numeric'}) : '';
        setText('cert-status-meta', 'Issued ' + dt + ' · Click below to view, print, or share your certificate.');
        setText('cert-status-percent', issued.cert_id);
        setWidth('cert-status-fill', '100%');
        const btn = document.getElementById('cert-status-btn');
        if (btn) btn.textContent = 'View Certificate';
        return;
    }

    if (eligible) {
        card.setAttribute('data-state', 'eligible');
        setText('cert-status-icon', '✨');
        setText('cert-status-eyebrow', 'ELIGIBLE');
        setText('cert-status-title', 'You qualify for your certificate!');
        setText('cert-status-meta', 'You\'ve visited ' + visited + ' of ' + total + ' modules — well above the ' + serverThreshold + '-module threshold. Claim it now.');
        const pct = Math.min(100, Math.round((visited / total) * 100));
        setText('cert-status-percent', pct + '%');
        setWidth('cert-status-fill', '100%');
        const btn = document.getElementById('cert-status-btn');
        if (btn) btn.textContent = 'Claim Certificate';
        return;
    }

    // In progress
    card.setAttribute('data-state', 'progress');
    setText('cert-status-icon', '🎓');
    setText('cert-status-eyebrow', 'IN PROGRESS');
    const remaining = Math.max(0, serverThreshold - visited);
    setText('cert-status-title', remaining + ' module' + (remaining === 1 ? '' : 's') + ' away from your certificate');
    setText('cert-status-meta', 'Visit ' + visited + ' / ' + serverThreshold + ' qualifying modules (threshold = ' + CERT_THRESHOLD_PCT + '% of ' + total + '). Keep going!');
    const pct = Math.min(100, Math.round((visited / serverThreshold) * 100));
    setText('cert-status-percent', pct + '%');
    setWidth('cert-status-fill', pct + '%');
    const btn = document.getElementById('cert-status-btn');
    if (btn) btn.textContent = 'View Details';
}

function updatePillarCounts() {
    ['p1','p2','p3','p4','p5','p6','p7','p8','p9'].forEach(p => {
        const total = MODULES_LIST.filter(m => m.pillar === p).length;
        const done  = MODULES_LIST.filter(m => m.pillar === p && userData.visited.includes(m.id)).length;
        const el = document.getElementById(`count-${p}`);
        if (el) el.textContent = `${done}/${total}`;
    });
}

// ── SEARCH ────────────────────────────────────────────────────
let _searchPrevOpen = null;  // nav-open state before the search began

function searchContent() {
    const q = (document.getElementById('global-search')?.value || '').toLowerCase().trim();

    if (q && _searchPrevOpen === null) {
        _searchPrevOpen = {};
        document.querySelectorAll('.nav-list').forEach(ul => {
            _searchPrevOpen[ul.id] = ul.classList.contains('open');
        });
    }

    document.querySelectorAll('.nav-list li').forEach(li => {
        li.style.display = (!q || li.textContent.toLowerCase().includes(q)) ? 'block' : 'none';
    });

    if (q) {
        // Expand every pillar containing a match so results are visible
        document.querySelectorAll('.nav-list').forEach(ul => {
            const hasMatch = Array.from(ul.children).some(li => li.style.display !== 'none');
            ul.classList.toggle('open', hasMatch);
            const group = document.getElementById(ul.id.replace('nav-', 'group-'));
            if (group) group.classList.toggle('open', hasMatch);
        });
    } else if (_searchPrevOpen) {
        document.querySelectorAll('.nav-list').forEach(ul => {
            const wasOpen = !!_searchPrevOpen[ul.id];
            ul.classList.toggle('open', wasOpen);
            const group = document.getElementById(ul.id.replace('nav-', 'group-'));
            if (group) group.classList.toggle('open', wasOpen);
        });
        _searchPrevOpen = null;
    }
}

// ── MODALS ────────────────────────────────────────────────────
// ── TOOLS LIBRARY ────────────────────────────────────────────
function showToolsLibrary()  { const m = document.getElementById('tools-modal'); if (m) m.style.display = 'block'; }
function closeToolsLibrary() { const m = document.getElementById('tools-modal'); if (m) m.style.display = 'none'; }
window.addEventListener('click', function(e){
    if (e.target === document.getElementById('tools-modal')) closeToolsLibrary();
});

// ── CERTIFICATE ──────────────────────────────────────────────
const TOTAL_MODULES_FOR_CERT = MODULES_LIST.length; // 63 across 9 pillars

async function showCertificate() {
    const modal = document.getElementById('certificate-modal');
    if (!modal) return;
    modal.style.display = 'block';
    const sess = getSession();
    const elig = document.getElementById('cert-state-eligibility');
    const issued = document.getElementById('cert-state-issued');
    if (!sess || !sess.token) {
        // Not signed in — show prompt
        elig.style.display = 'block';
        issued.style.display = 'none';
        document.getElementById('cert-eligibility-msg').textContent = 'Please sign in to track progress and claim your certificate.';
        document.getElementById('cert-eligibility-msg').className = 'pending';
        document.getElementById('cert-claim-btn').disabled = true;
        renderLocalEligibility();
        return;
    }
    // Try backend first; if offline, fall back to local progress
    try {
        const data = await fetchCertEligibility(sess);
        if (!data) throw new Error('eligibility unavailable');
        if (data.already_issued) {
            // Fetch the full cert and render it
            const r2 = await authFetch(API_BASE + '/certificate/me');
            if (r2.ok) {
                const cert = await r2.json();
                renderIssuedCertificate(cert);
                return;
            }
        }
        renderEligibilityFromServer(data);
    } catch (e) {
        // Offline fallback: show local progress
        renderLocalEligibility();
        document.getElementById('cert-eligibility-msg').textContent = 'Backend unreachable — showing local progress. Sign in (online) to claim.';
        document.getElementById('cert-eligibility-msg').className = 'pending';
        document.getElementById('cert-claim-btn').disabled = true;
    }
}

function renderLocalEligibility() {
    const visited = visitedModuleCount();
    const quizzes = Object.keys(userData.quizScores || {}).length;
    const total = TOTAL_MODULES_FOR_CERT;
    const thresholdPct = 80;
    const threshold = Math.max(1, Math.round(total * thresholdPct / 100));
    fillEligibilityDisplay({
        modules_visited: visited, modules_total: total, quizzes_taken: quizzes,
        threshold_modules: threshold, threshold_pct: thresholdPct,
        eligible: visited >= threshold
    });
}

function renderEligibilityFromServer(data) {
    document.getElementById('cert-state-eligibility').style.display = 'block';
    document.getElementById('cert-state-issued').style.display = 'none';
    fillEligibilityDisplay(data);
    const msg = document.getElementById('cert-eligibility-msg');
    const btn = document.getElementById('cert-claim-btn');
    if (data.eligible) {
        msg.textContent = '✓ You are eligible! Click below to claim your certificate.';
        msg.className = 'ok';
        btn.disabled = false;
    } else {
        const remaining = data.threshold_modules - data.modules_visited;
        msg.textContent = `Visit ${remaining} more module${remaining===1?'':'s'} to qualify.`;
        msg.className = 'pending';
        btn.disabled = true;
    }
}

function fillEligibilityDisplay(d) {
    document.getElementById('cert-visited-count').textContent = d.modules_visited;
    document.getElementById('cert-total-count').textContent = d.modules_total;
    document.getElementById('cert-quiz-count').textContent = d.quizzes_taken;
    document.getElementById('cert-threshold-count').textContent = d.threshold_modules;
    document.getElementById('cert-threshold-pct').textContent = d.threshold_pct + '%';
    const pct = Math.min(100, Math.round((d.modules_visited / Math.max(1, d.threshold_modules)) * 100));
    document.getElementById('cert-progress-fill').style.width = pct + '%';
}

async function claimCertificate() {
    const sess = getSession();
    if (!sess || !sess.token) { alert('Please sign in first.'); return; }
    const btn = document.getElementById('cert-claim-btn');
    btn.disabled = true;
    const orig = btn.textContent;
    btn.textContent = 'Issuing…';
    try {
        const r = await authFetch(API_BASE + '/certificate/issue', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!r.ok) {
            const d = await r.json().catch(() => ({}));
            throw new Error(d.detail || ('HTTP ' + r.status));
        }
        const cert = await r.json();
        _certEligCache = { ts: 0, data: null };  // status changed — drop cache
        renderIssuedCertificate(cert);
    } catch (e) {
        alert('Could not issue certificate: ' + e.message);
        btn.disabled = false;
        btn.textContent = orig;
    }
}

let _issuedCert = null;

function renderIssuedCertificate(cert) {
    document.getElementById('cert-state-eligibility').style.display = 'none';
    document.getElementById('cert-state-issued').style.display = 'block';
    document.getElementById('cert-recipient-name').textContent = cert.name || '—';
    document.getElementById('cert-modules-count').textContent = cert.modules_total || TOTAL_MODULES_FOR_CERT;
    const date = cert.issued_at ? new Date(cert.issued_at * 1000) : new Date();
    document.getElementById('cert-date').textContent = date.toLocaleDateString('en-IN', { year:'numeric', month:'long', day:'numeric' });
    document.getElementById('cert-id-display').textContent = cert.cert_id || '—';
    document.getElementById('cert-verify-url').textContent = cert.verify_url || '';
    _issuedCert = Object.assign({}, cert, { _date: date });
    // Refresh dashboard card so the user sees the new "Certified" state immediately.
    updateDashboardCertStatus();
}

function closeCertificate() { document.getElementById('certificate-modal').style.display = 'none'; }

// ── CERTIFICATE SOCIAL SHARING ───────────────────────────────
const CERT_COURSE = 'Amazon India Account Management Playbook';
const CERT_ORG = 'SMEMinds LLP';
function certShareText() {
    return "I'm now certified in Amazon e-commerce fundamentals! 🎓 I completed the " + CERT_COURSE +
        " by " + CERT_ORG + " — mastering 9 growth pillars and 63 modules, from catalogue selection to brand protection. 🚀 #Amazon #Ecommerce #AmazonSeller #SMEMinds #Certification";
}
function certVerifyUrl() {
    return (_issuedCert && _issuedCert.verify_url) || '';
}

function shareLinkedIn() {
    if (!_issuedCert) return;
    const d = _issuedCert._date || new Date();
    const p = new URLSearchParams({
        startTask: 'CERTIFICATION_NAME',
        name: CERT_COURSE,
        organizationName: CERT_ORG,
        issueYear: String(d.getFullYear()),
        issueMonth: String(d.getMonth() + 1),
        certUrl: certVerifyUrl(),
        certId: _issuedCert.cert_id || ''
    });
    window.open('https://www.linkedin.com/profile/add?' + p.toString(), '_blank', 'noopener');
}
function shareFacebook() {
    const url = certVerifyUrl() || (typeof location !== 'undefined' ? location.href : '');
    window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url) +
        '&quote=' + encodeURIComponent(certShareText()), '_blank', 'noopener,width=660,height=580');
}
function shareInstagram() {
    // Instagram has no web share endpoint — hand the user a ready-to-post image.
    showToastMsg('📸 Downloading your certificate image — post it to Instagram!');
    downloadCertImage();
}
function copyCertLink() {
    const url = certVerifyUrl();
    if (!url) { showToastMsg('No verification link yet.'); return; }
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function(){ showToastMsg('🔗 Verification link copied!'); },
            function(){ showToastMsg(url); });
    } else { showToastMsg(url); }
}
function downloadCertImage() {
    certCardBlob().then(function(blob){
        if (!blob) return;
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'SMEMinds-Certificate-' + ((_issuedCert && _issuedCert.cert_id) || 'achievement') + '.png';
        document.body.appendChild(a); a.click(); a.remove();
        setTimeout(function(){ URL.revokeObjectURL(a.href); }, 1500);
        showToastMsg('⬇ Certificate image downloaded!');
    });
}

// Render the premium classic certificate to a high-res PNG (matches the on-screen design).
function certCardBlob() {
    return new Promise(function (resolve) {
        const W = 1600, H = 1260, cx = W / 2;
        const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
        const x = cv.getContext('2d');
        const c = _issuedCert || {};
        const IVORY = '#fffdf7', INK = '#16314f', GOLD = '#c8962f', GOLDD = '#9a6f1d',
              ORANGE = '#e0531f', MUT = '#6b7a90', BODY = '#3a4a5f';
        const serif = "Georgia, 'Times New Roman', serif";

        function rr(px, py, w, h, r) { x.beginPath(); x.moveTo(px + r, py); x.arcTo(px + w, py, px + w, py + h, r); x.arcTo(px + w, py + h, px, py + h, r); x.arcTo(px, py + h, px, py, r); x.arcTo(px, py, px + w, py, r); x.closePath(); }
        function wrapC(text, cy, maxW, lh) { const words = String(text).split(' '); let line = '', yy = cy; for (let i = 0; i < words.length; i++) { const t = line + words[i] + ' '; if (x.measureText(t).width > maxW && line) { x.fillText(line.trim(), cx, yy); line = words[i] + ' '; yy += lh; } else line = t; } x.fillText(line.trim(), cx, yy); return yy; }
        function spaced(px) { try { x.letterSpacing = (px || 0) + 'px'; } catch (e) {} }

        function diamondDivider(cy, half) {
            const g = x.createLinearGradient(cx - half, 0, cx, 0); g.addColorStop(0, 'rgba(200,150,47,0)'); g.addColorStop(1, GOLD);
            x.strokeStyle = g; x.lineWidth = 2; x.beginPath(); x.moveTo(cx - half, cy); x.lineTo(cx - 14, cy); x.stroke();
            const g2 = x.createLinearGradient(cx, 0, cx + half, 0); g2.addColorStop(0, GOLD); g2.addColorStop(1, 'rgba(200,150,47,0)');
            x.strokeStyle = g2; x.beginPath(); x.moveTo(cx + 14, cy); x.lineTo(cx + half, cy); x.stroke();
            x.fillStyle = GOLD; x.save(); x.translate(cx, cy); x.rotate(Math.PI / 4); x.fillRect(-6, -6, 12, 12); x.restore();
        }
        function cornerL(px, py, sx, sy, len) {
            x.strokeStyle = GOLD; x.lineWidth = 2.5; x.lineCap = 'butt';
            x.beginPath(); x.moveTo(px, py + sy * len); x.lineTo(px, py); x.lineTo(px + sx * len, py); x.stroke();
        }
        function arcText(str, ccx, ccy, r, centerAng, spread, flip) {
            const n = str.length, step = spread / n;
            x.textAlign = 'center'; x.textBaseline = 'middle';
            for (let i = 0; i < n; i++) {
                const ang = centerAng - spread / 2 + step * (i + 0.5);
                const px = ccx + Math.cos(ang) * r, py = ccy + Math.sin(ang) * r;
                x.save(); x.translate(px, py); x.rotate(ang + (flip ? -Math.PI / 2 : Math.PI / 2)); x.fillText(str[i], 0, 0); x.restore();
            }
            x.textBaseline = 'alphabetic';
        }
        function seal(sx, sy, r) {
            x.fillStyle = '#15365b'; x.beginPath(); x.moveTo(sx - 16, sy + r * .5); x.lineTo(sx - 30, sy + r * 1.55); x.lineTo(sx - 13, sy + r * 1.38); x.lineTo(sx - 3, sy + r * 1.55); x.lineTo(sx - 2, sy + r * .7); x.closePath(); x.fill();
            x.fillStyle = '#0e2a49'; x.beginPath(); x.moveTo(sx + 16, sy + r * .5); x.lineTo(sx + 30, sy + r * 1.55); x.lineTo(sx + 13, sy + r * 1.38); x.lineTo(sx + 3, sy + r * 1.55); x.lineTo(sx + 2, sy + r * .7); x.closePath(); x.fill();
            x.fillStyle = GOLD; const beads = 46, br = r + 13;
            for (let i = 0; i < beads; i++) { const a = i / beads * Math.PI * 2; x.beginPath(); x.arc(sx + Math.cos(a) * br, sy + Math.sin(a) * br, 2.3, 0, Math.PI * 2); x.fill(); }
            const gg = x.createLinearGradient(sx, sy - r, sx, sy + r); gg.addColorStop(0, '#f6da8b'); gg.addColorStop(.5, '#d7a838'); gg.addColorStop(1, '#a3741c');
            x.fillStyle = gg; x.beginPath(); x.arc(sx, sy, r, 0, Math.PI * 2); x.fill();
            x.strokeStyle = 'rgba(255,244,214,.6)'; x.lineWidth = 1.5; x.beginPath(); x.arc(sx, sy, r - 3, 0, Math.PI * 2); x.stroke();
            x.strokeStyle = 'rgba(124,90,22,.5)'; x.lineWidth = 1; x.beginPath(); x.arc(sx, sy, r - 16, 0, Math.PI * 2); x.stroke();
            x.fillStyle = '#5a4310'; x.font = '800 15px Outfit, sans-serif'; spaced(1.2);
            arcText('SMEMINDS · CERTIFIED', sx, sy, r - 10, -Math.PI / 2, Math.PI * 1.04, false);
            arcText('AMAZON INDIA', sx, sy, r - 10, Math.PI / 2, Math.PI * 0.52, true);
            spaced(0);
            x.strokeStyle = '#fff8e8'; x.lineWidth = 8; x.lineCap = 'round'; x.lineJoin = 'round';
            x.beginPath(); x.moveTo(sx - r * .32, sy + r * .03); x.lineTo(sx - r * .08, sy + r * .27); x.lineTo(sx + r * .34, sy - r * .28); x.stroke();
        }

        function draw(logo) {
            // ivory paper + faint guilloché
            x.fillStyle = IVORY; x.fillRect(0, 0, W, H);
            const glow = x.createRadialGradient(cx, -120, 40, cx, -120, 900); glow.addColorStop(0, 'rgba(200,150,47,.10)'); glow.addColorStop(1, 'rgba(200,150,47,0)');
            x.fillStyle = glow; x.fillRect(0, 0, W, H);
            x.save(); x.globalAlpha = .05; x.strokeStyle = GOLD; x.lineWidth = 1;
            for (let r = 40; r < 760; r += 18) { x.beginPath(); x.arc(cx, H * 0.42, r, 0, Math.PI * 2); x.stroke(); }
            x.restore();

            // double gold frame
            const m = 42;
            x.strokeStyle = GOLD; x.lineWidth = 3; rr(m, m, W - 2 * m, H - 2 * m, 9); x.stroke();
            x.strokeStyle = 'rgba(200,150,47,.55)'; x.lineWidth = 1.5; rr(m + 11, m + 11, W - 2 * (m + 11), H - 2 * (m + 11), 5); x.stroke();
            const cIn = 74, cLen = 46;
            cornerL(cIn, cIn, 1, 1, cLen); cornerL(W - cIn, cIn, -1, 1, cLen);
            cornerL(cIn, H - cIn, 1, -1, cLen); cornerL(W - cIn, H - cIn, -1, -1, cLen);

            x.textAlign = 'center';
            // logo
            if (logo) { const lh = 104, lw = lh * logo.width / logo.height; x.drawImage(logo, cx - lw / 2, 92, lw, lh); }
            // eyebrow
            x.fillStyle = GOLDD; x.font = '700 22px Outfit, sans-serif'; spaced(5); x.fillText('SMEMINDS LLP      ·      AMAZON INDIA', cx, 250); spaced(0);
            // title (serif): "Certificate " bold + "of Completion" italic
            const t1 = 'Certificate ', t2 = 'of Completion';
            x.font = '700 62px ' + serif; const w1 = x.measureText(t1).width;
            x.font = 'italic 400 62px ' + serif; const w2 = x.measureText(t2).width;
            const tStart = cx - (w1 + w2) / 2;
            x.textAlign = 'left'; x.fillStyle = INK;
            x.font = '700 62px ' + serif; x.fillText(t1, tStart, 340);
            x.font = 'italic 400 62px ' + serif; x.fillText(t2, tStart + w1, 340);
            x.textAlign = 'center';
            diamondDivider(382, 150);
            // presented
            x.fillStyle = MUT; x.font = 'italic 400 24px Inter, sans-serif'; x.fillText('This certificate is proudly awarded to', cx, 440);
            // name (serif, orange gradient)
            const ng = x.createLinearGradient(cx - 360, 0, cx + 360, 0); ng.addColorStop(0, '#ff7a45'); ng.addColorStop(.55, '#e0531f'); ng.addColorStop(1, '#c2410c');
            x.fillStyle = ng; x.font = '700 86px ' + serif; x.fillText(c.name || '—', cx, 540);
            // gold rule under name
            const gr = x.createLinearGradient(cx - 150, 0, cx + 150, 0); gr.addColorStop(0, 'rgba(200,150,47,0)'); gr.addColorStop(.5, GOLD); gr.addColorStop(1, 'rgba(200,150,47,0)');
            x.fillStyle = gr; x.fillRect(cx - 150, 568, 300, 2.5);
            // course
            x.fillStyle = MUT; x.font = 'italic 400 23px Inter, sans-serif'; x.fillText('for successfully completing the', cx, 622);
            x.fillStyle = INK; x.font = '800 36px Outfit, sans-serif'; x.fillText(CERT_COURSE, cx, 672);
            // description
            const mods = c.modules_total || 63;
            x.fillStyle = BODY; x.font = '400 23px Inter, sans-serif';
            wrapC('covering 9 strategic pillars and ' + mods + ' modules of professional Amazon seller training — from catalogue selection through brand protection.', 720, 1000, 34);

            // chips (centered group)
            const chips = ['9 Pillars', mods + ' Modules', 'Verified Credential'];
            x.font = '700 22px Outfit, sans-serif';
            const pad = 22, gap = 14, ch = 48, cw = chips.map(function (t) { return x.measureText(t).width + pad * 2; });
            let tot = cw.reduce(function (a, b) { return a + b; }, 0) + gap * (chips.length - 1), csx = cx - tot / 2, cy = 800;
            for (let i = 0; i < chips.length; i++) {
                rr(csx, cy, cw[i], ch, ch / 2); x.fillStyle = 'rgba(200,150,47,.08)'; x.fill();
                x.strokeStyle = 'rgba(200,150,47,.45)'; x.lineWidth = 1.5; rr(csx, cy, cw[i], ch, ch / 2); x.stroke();
                x.fillStyle = INK; x.textAlign = 'left'; x.textBaseline = 'middle'; x.fillText(chips[i], csx + pad, cy + ch / 2 + 1);
                x.textBaseline = 'alphabetic'; x.textAlign = 'center'; csx += cw[i] + gap;
            }

            // ── footer ──
            seal(cx, 1058, 80);
            const dstr = (c._date || new Date()).toLocaleDateString('en-IN', { year: 'numeric', month: 'long', day: 'numeric' });
            // left: signature
            x.textAlign = 'left'; x.strokeStyle = INK; x.lineWidth = 1.5; x.beginPath(); x.moveTo(120, 1070); x.lineTo(360, 1070); x.stroke();
            x.fillStyle = INK; x.font = '700 26px Outfit, sans-serif'; x.fillText('SMEMinds LLP', 120, 1106);
            x.fillStyle = MUT; x.font = '700 13px Outfit, sans-serif'; spaced(1.4); x.fillText('AUTHORISED SIGNATORY', 120, 1132); spaced(0);
            // right: issued / id
            x.textAlign = 'right'; const rx = W - 120;
            x.fillStyle = MUT; x.font = '700 13px Outfit, sans-serif'; spaced(1.4); x.fillText('ISSUED ON', rx, 1052); spaced(0);
            x.fillStyle = INK; x.font = '700 24px Outfit, sans-serif'; x.fillText(dstr, rx, 1082);
            x.fillStyle = MUT; x.font = '700 13px Outfit, sans-serif'; spaced(1.4); x.fillText('CREDENTIAL ID', rx, 1116); spaced(0);
            x.fillStyle = INK; x.font = '600 20px Consolas, monospace'; x.fillText(c.cert_id || '', rx, 1146);
            // verify (centered)
            x.textAlign = 'center'; x.fillStyle = MUT; x.font = '400 17px Consolas, monospace';
            x.fillText('Verify at  ' + (c.verify_url || ''), cx, 1205);

            cv.toBlob(function (b) { resolve(b); }, 'image/png');
        }

        function go() {
            if (typeof SMEMINDS_LOGO !== 'undefined' && SMEMINDS_LOGO) {
                const im = new Image();
                im.onload = function () { draw(im); };
                im.onerror = function () { draw(null); };
                im.src = SMEMINDS_LOGO;
            } else draw(null);
        }
        if (document.fonts && document.fonts.ready) document.fonts.ready.then(go).catch(go); else go();
    });
}

function printCertificate() {
    // The print CSS only shows #certificate-modal contents
    window.print();
}

// Clicks outside the cert modal close it
window.addEventListener('click', function(e){
    if (e.target === document.getElementById('certificate-modal')) closeCertificate();
});

function showBookmarks()      { document.getElementById('bookmarks-modal').style.display = 'block'; }
function closeBookmarks()     { document.getElementById('bookmarks-modal').style.display = 'none';  }
function closeGlobalFeedback(){ document.getElementById('global-feedback-modal').style.display = 'none'; }

function showGlobalFeedback() {
    document.getElementById('global-feedback-modal').style.display = 'block';

    const pillars = ['p1','p2','p3','p4','p5','p6','p7','p8','p9'];
    const pNames  = { p1:'Account Mgmt & Compliance', p2:'Selection', p3:'Efficiency', p4:'Traffic', p5:'Conversion', p6:'Speed', p7:'Tools', p8:'Brand Registry', p9:'Brand Protection' };
    const qCount  = Object.keys(userData.quizScores).length;
    let statsHtml = `<strong>Overall Progress:</strong> ${visitedModuleCount()} / ${MODULES_LIST.length} modules visited<br>`;
    pillars.forEach(p => {
        const total = MODULES_LIST.filter(m=>m.pillar===p).length;
        const done  = MODULES_LIST.filter(m=>m.pillar===p && userData.visited.includes(m.id)).length;
        statsHtml += `<strong>${pNames[p]}:</strong> ${done} / ${total} completed<br>`;
    });
    statsHtml += `<strong>Quizzes Completed:</strong> ${qCount} / ${MODULES_LIST.length}`;
    document.getElementById('global-progress-stats').innerHTML = statsHtml;

    let fbHtml = '';
    userData.feedback.forEach(f => {
        const stars = Math.max(0, Math.min(5, f.stars | 0));
        fbHtml += `<div style="padding:14px;border:1px solid var(--border);border-radius:8px;margin-bottom:10px;font-size:13px">
            <strong>Module ${escHtml(f.moduleId)}</strong> &nbsp;·&nbsp; ${'★'.repeat(stars)}${'☆'.repeat(5-stars)} &nbsp;·&nbsp; <em>${escHtml(f.role)||'—'}</em><br>
            <span style="color:var(--text-muted)">Helpful:</span> ${escHtml(f.helpful)||'—'}<br>
            <span style="color:var(--text-muted)">Improve:</span> ${escHtml(f.improve)||'—'}
        </div>`;
    });
    document.getElementById('global-feedback-list').innerHTML = fbHtml || '<p style="color:var(--text-muted)">No feedback submitted yet.</p>';
}

window.addEventListener('click', e => {
    if (e.target === document.getElementById('bookmarks-modal')) closeBookmarks();
    if (e.target === document.getElementById('global-feedback-modal')) closeGlobalFeedback();
});

// ── EXPORT FEEDBACK CSV ──────────────────────────────────────
function exportFeedback() {
    if (!userData.feedback.length) { alert('No feedback to export yet.'); return; }
    const rows = [['Module','Stars','Role','Helpful','Improve','Date']];
    userData.feedback.forEach(f => {
        rows.push([f.moduleId, f.stars, f.role||'', f.helpful||'', f.improve||'', f.date||'']);
    });
    // RFC-4180 quoting so commas, quotes and newlines in feedback round-trip
    const cell = v => '"' + String(v == null ? '' : v).replace(/"/g, '""') + '"';
    const csv = rows.map(r => r.map(cell).join(',')).join('\r\n');
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'SMEMinds_Playbook_Feedback.csv';
    a.click(); URL.revokeObjectURL(url);
}

// ── VIDEO PLAYER ─────────────────────────────────────────────
// Videos open on YouTube directly (embedding disabled by Amazon Seller University).
// No JS needed — cards are plain anchor tags.

// ── CHECKLIST ─────────────────────────────────────────────────
// Checkbox classes are dot-free (chk_1_1) — a dotted class like .chk_1.1 is an
// invalid CSS selector and would throw, losing every checklist save.
function updateChecklist(mid) {
    const chks = document.querySelectorAll(`.chk_${mid.replace(/\./g, '_')}`);
    userData.checklists[mid] = Array.from(chks).map(c => c.checked);
    saveUserData();
}

function restoreChecklist(mid) {
    if (!userData.checklists[mid]) return;
    const chks = document.querySelectorAll(`.chk_${mid.replace(/\./g, '_')}`);
    chks.forEach((c, i) => { c.checked = userData.checklists[mid][i] || false; });
}

// ── QUIZ ──────────────────────────────────────────────────────
function submitQuiz(mid) {
    const qContainer = document.getElementById(`quiz_${mid}`);
    if (!qContainer) return;
    const qs = qContainer.querySelectorAll('.quiz-q');
    const midCls = mid.replace(/\./g, '_');
    let score = 0;

    if (!qContainer.querySelector('input:checked')) {
        showToastMsg('Select at least one answer before submitting.');
        return;
    }

    qs.forEach((q, idx) => {
        const ans = q.getAttribute('data-ans');
        const selected = q.querySelector(`input[name='q_${midCls}_${idx}']:checked`);
        const exp = q.querySelector('.q-exp');
        if (!exp) return;

        if (selected) {
            // Both sides are option indexes — free text never decides grading
            const correct = selected.value === ans;
            if (correct) score++;
            exp.className = correct ? 'q-exp' : 'q-exp incorrect';
            const prefix = correct ? '<strong>✅ Correct!</strong> ' : '<strong>❌ Incorrect.</strong> ';
            exp.innerHTML = prefix + exp.innerHTML.replace(/<strong>.*?<\/strong>\s*/,'');
            exp.style.display = 'block';
        }
    });

    const resEl = document.getElementById(`quiz_res_${mid}`);
    if (resEl) {
        const pct = qs.length > 0 ? Math.round(score/qs.length*100) : 0;
        resEl.innerHTML = `${pct >= 80 ? '🎉' : pct >= 50 ? '👍' : '📚'} You scored <strong>${score} out of ${qs.length}</strong> (${pct}%)`;
    }

    // Keep the best score across attempts
    userData.quizScores[mid] = Math.max(score, userData.quizScores[mid] || 0);
    saveUserData();
}

// ── FEEDBACK ──────────────────────────────────────────────────
let currentStars = {};

function rateModule(mid, val) {
    currentStars[mid] = val;
    const container = document.getElementById(`stars_${mid}`);
    if (!container) return;
    container.querySelectorAll('span').forEach((s, i) => {
        s.classList.toggle('lit', i < val);
        s.style.color = i < val ? 'var(--accent)' : 'rgba(255,255,255,0.3)';
    });
}

function submitFeedback(mid) {
    const stars   = currentStars[mid] || 0;
    const helpful = document.getElementById(`fb_help_${mid}`)?.value || '';
    const improve = document.getElementById(`fb_imp_${mid}`)?.value  || '';
    const role    = document.getElementById(`fb_role_${mid}`)?.value || '';

    if (!stars) { alert('Please select a star rating first.'); return; }

    userData.feedback.push({ moduleId:mid, stars, helpful, improve, role, date: new Date().toISOString() });
    saveUserData();

    // Clear form
    const helpEl = document.getElementById(`fb_help_${mid}`);
    const impEl  = document.getElementById(`fb_imp_${mid}`);
    if (helpEl) helpEl.value = '';
    if (impEl)  impEl.value  = '';
    currentStars[mid] = 0;
    rateModule(mid, 0);

    showToastMsg('✅ Thank you! Feedback saved successfully.');
}

function showToastMsg(msg) {
    const t = document.getElementById('copy-toast');
    if (!t) return;
    const orig = t.textContent;
    t.textContent = msg;
    t.classList.add('show');
    setTimeout(() => { t.classList.remove('show'); t.textContent = orig; }, 3000);
}

// ── AUTH / SSO ────────────────────────────────────────────────
const AUTH_KEY = 'smeminds_auth_v1';

function getSession() {
    try { const s = localStorage.getItem(AUTH_KEY); return s ? JSON.parse(s) : null; } catch(e) { return null; }
}
function setSession(user) {
    localStorage.setItem(AUTH_KEY, JSON.stringify(user));
}
function clearSession() {
    localStorage.removeItem(AUTH_KEY);
}

function unlockApp(user) {
    const overlay = document.getElementById('login-overlay');
    const app = document.getElementById('main-app');
    if (overlay) overlay.style.display = 'none';
    if (app) app.style.display = 'flex';
    const nameEl = document.getElementById('user-name-el');
    const avatarEl = document.getElementById('user-avatar-el');
    if (nameEl) nameEl.textContent = user.name || user.email.split('@')[0];
    if (avatarEl) {
        if (user.picture) {
            avatarEl.innerHTML = '<img src="' + user.picture + '" alt="">';
        } else {
            const initials = (user.name || user.email).slice(0,2).toUpperCase();
            avatarEl.textContent = initials;
        }
    }
    // Entitlements: cached state applies instantly (works offline); the
    // plans → subscription chain then refreshes from the server in order.
    loadCachedSubscription();
    updatePlanBadge();
    refreshNavLocks();
    loadPlans().then(loadSubscription);
}

function handleLogout() {
    if (!confirm('Sign out of SMEMinds Playbook?')) return;
    clearSession();
    // Drop the local progress blob — the next sign-in must not inherit (and
    // permanently merge) this account's progress into another account.
    userData = { visited: [], checklists: {}, quizScores: {}, feedback: [] };
    try { localStorage.removeItem(USERDATA_KEY); } catch (e) {}
    SUBSCRIPTION = { plan: 'free', is_premium: false, paywall: SUBSCRIPTION.paywall || { free_modules: 3 }, plan_detail: null };
    updatePlanBadge();
    initNav();
    updateProgress();
    const overlay = document.getElementById('login-overlay');
    const app = document.getElementById('main-app');
    if (overlay) { overlay.style.display = ''; overlay.setAttribute('data-view', 'signin'); }
    if (app) app.style.display = 'none';
    authShow('signin');
}

// ── Auth view router + multi-step onboarding state ───────────
var SU = { name:'', email:'', pass:'', company:'', business_type:'', marketplace:'',
           gst:'', revenue_range:'', experience:'', plan:'free', cycle:'monthly' };

function authShow(view) {
    var overlay = document.getElementById('login-overlay');
    if (overlay) overlay.setAttribute('data-view', view);
    ['signin', 'signup', 'forgot', 'success'].forEach(function(v) {
        var el = document.getElementById('view-' + v);
        if (el) el.hidden = (v !== view);
    });
    if (view === 'signup') suGo(1);
    var f = document.querySelector('#view-' + view + ' input');
    if (f) setTimeout(function(){ try { f.focus(); } catch(e){} }, 60);
}
function authErr(id, msg) {
    var el = document.getElementById(id);
    if (!el) return;
    if (msg) { el.textContent = msg; el.classList.add('show'); }
    else { el.textContent = ''; el.classList.remove('show'); }
}
function cacheSub(sess, sub) { try { localStorage.setItem(subCacheKey(sess), JSON.stringify(sub)); } catch(e){} }

async function handleSignIn(e) {
    e.preventDefault();
    var email = document.getElementById('si-email').value.trim();
    var pass  = document.getElementById('si-pass').value;
    authErr('si-error', '');
    try {
        var r = await fetch(API_BASE + '/login', {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, password: pass })
        });
        if (!r.ok) {
            var d = await r.json().catch(function(){ return {}; });
            authErr('si-error', d.detail || 'Invalid email or password. New here? Create your account.');
            return;
        }
        var data = await r.json();
        var user = Object.assign({}, data.user, { token: data.token });
        setSession(user);
        if (data.subscription) cacheSub(user, data.subscription);
        claimLocalDataFor(user.email);
        unlockApp(user);
        await pullProgressFromServer();
        updateDashboardCertStatus();
    } catch (err) {
        authErr('si-error', 'Cannot reach server. Is the backend running on ' + API_BASE + '?');
    }
}

// Step 1 — create the account immediately (so "email exists" surfaces early)
async function suStep1() {
    var name  = document.getElementById('su-name').value.trim();
    var email = document.getElementById('su-email').value.trim();
    var pass  = document.getElementById('su-pass').value;
    authErr('su-error', '');
    if (!name) { authErr('su-error', 'Please enter your name.'); return; }
    if (!email || email.indexOf('@') < 0) { authErr('su-error', 'Please enter a valid email address.'); return; }
    if (pass.length < 8) { authErr('su-error', 'Password must be at least 8 characters.'); return; }
    SU.name = name; SU.email = email; SU.pass = pass;
    var btn = document.getElementById('su-btn-1');
    if (btn) { btn.disabled = true; btn.textContent = 'Creating…'; }
    try {
        var r = await fetch(API_BASE + '/register', {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, password: pass, name: name })
        });
        var d = await r.json().catch(function(){ return {}; });
        if (btn) { btn.disabled = false; btn.textContent = 'Continue'; }
        if (!r.ok) {
            authErr('su-error', d.detail || 'Could not create account.');
            if (r.status === 409) { authErr('su-error', 'An account with this email already exists. Try signing in instead.'); }
            return;
        }
        var user = Object.assign({}, d.user, { token: d.token });
        setSession(user);
        if (d.subscription) cacheSub(user, d.subscription);
        claimLocalDataFor(user.email);
        suGo(2);
    } catch (err) {
        if (btn) { btn.disabled = false; btn.textContent = 'Continue'; }
        authErr('su-error', 'Cannot reach server. Is the backend running on ' + API_BASE + '?');
    }
}

function suGo(step) {
    document.querySelectorAll('#view-signup .auth-step').forEach(function(s) {
        s.hidden = (parseInt(s.getAttribute('data-step'), 10) !== step);
    });
    document.querySelectorAll('#auth-steps .auth-dot').forEach(function(d) {
        var n = parseInt(d.getAttribute('data-s'), 10);
        d.classList.toggle('is-on', n === step);
        d.classList.toggle('is-done', n < step);
    });
    if (step === 4) renderSignupPlans();
    var f = document.querySelector('#view-signup .auth-step:not([hidden]) input, #view-signup .auth-step:not([hidden]) select');
    if (f) setTimeout(function(){ try { f.focus(); } catch(e){} }, 60);
}

async function patchProfile(fields) {
    try {
        var r = await authFetch(API_BASE + '/profile', {
            method: 'PATCH', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(fields)
        });
        return r.ok;
    } catch (e) { return false; }
}

async function suStep2() {
    SU.company = document.getElementById('su-company').value.trim();
    SU.business_type = document.getElementById('su-btype').value;
    SU.marketplace = document.getElementById('su-market').value;
    await patchProfile({ company: SU.company, business_type: SU.business_type,
                         marketplace: SU.marketplace, role: SU.business_type || undefined });
    var sess = getSession();
    if (sess && SU.business_type) { sess.role = SU.business_type; setSession(sess); }
    suGo(3);
}

async function suStep3() {
    SU.gst = document.getElementById('su-gst').value.trim();
    SU.revenue_range = document.getElementById('su-rev').value;
    SU.experience = document.getElementById('su-exp').value;
    await patchProfile({ gst: SU.gst, revenue_range: SU.revenue_range, experience: SU.experience });
    suGo(4);
}

function setCycle(c) {
    SU.cycle = (c === 'yearly') ? 'yearly' : 'monthly';
    var m = document.getElementById('cyc-monthly'), y = document.getElementById('cyc-yearly');
    if (m) m.classList.toggle('is-on', SU.cycle === 'monthly');
    if (y) y.classList.toggle('is-on', SU.cycle === 'yearly');
    renderSignupPlans();
}

async function renderSignupPlans() {
    var wrap = document.getElementById('su-plans');
    if (!wrap) return;
    if (!PLANS_CACHE.length) await loadPlans();
    if (!SU.plan) SU.plan = 'free';
    wrap.innerHTML = PLANS_CACHE.map(function(p) {
        var isFree = p.id === 'free';
        var price = SU.cycle === 'yearly' ? p.yearly : p.monthly;
        var amt = isFree ? 'Free' : '₹' + Number(price).toLocaleString('en-IN');
        var cyc = isFree ? 'forever' : (SU.cycle === 'yearly' ? '/yr' : '/mo');
        var sel = p.id === SU.plan ? ' is-sel' : '';
        return '<div class="auth-plan' + sel + '" onclick="selectPlan(\'' + escHtml(p.id) + '\')">' +
            '<span class="auth-plan-radio"></span>' +
            '<div class="auth-plan-info"><div class="auth-plan-name">' + escHtml(p.name) +
                (p.popular ? ' <span class="auth-plan-pop">Popular</span>' : '') + '</div>' +
            '<div class="auth-plan-desc">' + escHtml(p.tagline || '') + '</div></div>' +
            '<div class="auth-plan-price"><b>' + amt + '</b><span>' + cyc + '</span></div></div>';
    }).join('');
    var fin = document.getElementById('su-finish');
    if (fin) fin.textContent = (SU.plan === 'free') ? 'Start learning — Free' : 'Continue to payment';
}
function selectPlan(id) { SU.plan = id; renderSignupPlans(); }

async function suFinish() {
    authErr('su-plan-error', '');
    var sess = getSession();
    if (!sess || !sess.token) { authShow('signin'); return; }
    var fin = document.getElementById('su-finish');
    if (fin) fin.disabled = true;
    if (!SU.plan || SU.plan === 'free') {
        await patchProfile({ onboarded: '1' });
        await loadPlans(); await loadSubscription();
        if (fin) fin.disabled = false;
        showSuccess('free');
        return;
    }
    try {
        if (fin) fin.textContent = 'Starting checkout…';
        var r = await authFetch(API_BASE + '/billing/order', {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ plan: SU.plan, cycle: SU.cycle })
        });
        var order = await r.json().catch(function(){ return {}; });
        if (!r.ok) { authErr('su-plan-error', order.detail || 'Could not start checkout.'); if (fin) { fin.disabled = false; fin.textContent = 'Continue to payment'; } return; }
        if (order.mock) { await suActivate({ razorpay_order_id: order.order_id }); return; }
        var ready = await ensureRazorpay();
        if (!ready) { authErr('su-plan-error', 'Could not load the payment provider.'); if (fin) { fin.disabled = false; fin.textContent = 'Continue to payment'; } return; }
        var options = {
            key: order.key_id, amount: order.amount, currency: order.currency, name: 'SMEMinds Playbook',
            description: order.plan_name + ' plan (' + SU.cycle + ')', order_id: order.order_id,
            prefill: { email: sess.email || '', name: SU.name || '' }, theme: { color: '#ff6b35' },
            handler: function(resp) { suActivate({ razorpay_order_id: resp.razorpay_order_id, razorpay_payment_id: resp.razorpay_payment_id, razorpay_signature: resp.razorpay_signature }); }
        };
        var rzp = new Razorpay(options);
        rzp.on('payment.failed', function(){ authErr('su-plan-error', 'Payment failed. Please try again.'); if (fin) { fin.disabled = false; fin.textContent = 'Continue to payment'; } });
        rzp.open();
    } catch (e) {
        authErr('su-plan-error', 'Cannot reach server.'); if (fin) { fin.disabled = false; fin.textContent = 'Continue to payment'; }
    }
}

async function suActivate(payment) {
    var fin = document.getElementById('su-finish');
    try {
        var r = await authFetch(API_BASE + '/billing/verify', {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payment || {})
        });
        var data = await r.json().catch(function(){ return {}; });
        if (!r.ok) { authErr('su-plan-error', data.detail || 'Could not activate subscription.'); if (fin) { fin.disabled = false; fin.textContent = 'Continue to payment'; } return; }
        SUBSCRIPTION = Object.assign({}, SUBSCRIPTION, data.subscription, { plan_detail: data.plan_detail });
        var sess = getSession();
        if (sess) cacheSub(sess, Object.assign({}, data.subscription, { plan_detail: data.plan_detail }));
        await patchProfile({ onboarded: '1' });
        if (fin) fin.disabled = false;
        showSuccess(SU.plan, data.plan_detail);
    } catch (e) {
        authErr('su-plan-error', 'Activation failed. Please try again.'); if (fin) { fin.disabled = false; fin.textContent = 'Continue to payment'; }
    }
}

function showSuccess(plan, detail) {
    var el = document.getElementById('su-success-plan');
    if (el) {
        var name = (detail && detail.name) || (plan === 'free' ? 'Free' : plan);
        el.innerHTML = (plan === 'free')
            ? 'You\'re on the <b>Free</b> plan — your starter lessons are unlocked. Upgrade anytime for all 63 modules.'
            : 'You\'re now on <b>' + escHtml(name) + '</b> — all 63 modules, templates &amp; certifications unlocked. 🚀';
    }
    authShow('success');
}

function enterApp(where) {
    var sess = getSession();
    if (!sess) { authShow('signin'); return; }
    unlockApp(sess);
    pullProgressFromServer();
    updateDashboardCertStatus();
    if (where === 'modules') {
        setTimeout(function(){ var j = document.getElementById('journey'); if (j) j.scrollIntoView({ behavior: 'smooth' }); }, 200);
    }
}

// Social / OTP — present in the UI; need external provider credentials to function.
function authSocial(provider) {
    showToastMsg(provider + ' sign-in needs OAuth setup (client ID/secret). Add it in the backend to enable — use email for now.');
    authShow('signin');
    var el = document.getElementById('si-email'); if (el) el.focus();
}
function authOtp() {
    showToastMsg('Mobile OTP needs an SMS gateway (MSG91 / Twilio). Add credentials to enable — use email sign-in for now.');
}
async function handleForgot() {
    var email = document.getElementById('fp-email').value.trim();
    authErr('fp-error', '');
    var note = document.getElementById('fp-note');
    if (note) note.hidden = true;
    if (!email || email.indexOf('@') < 0) { authErr('fp-error', 'Please enter a valid email address.'); return; }
    try {
        var r = await fetch(API_BASE + '/forgot-password', {
            method: 'POST', headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email })
        });
        var d = await r.json().catch(function(){ return {}; });
        if (note) { note.hidden = false; note.textContent = d.message || 'If an account exists for that email, reset instructions were sent.'; }
    } catch (e) { authErr('fp-error', 'Cannot reach server. Is the backend running?'); }
}

// ── THEME TOGGLE ─────────────────────────────────────────────
function applyTheme(theme) {
    if (theme !== 'dark' && theme !== 'light') theme = 'light';
    document.documentElement.setAttribute('data-theme', theme);
    try { localStorage.setItem('smeminds_theme', theme); } catch (e) {}
}
function toggleTheme() {
    var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    applyTheme(cur === 'dark' ? 'light' : 'dark');
}
function initTheme() {
    var stored = null;
    try { stored = localStorage.getItem('smeminds_theme'); } catch (e) {}
    if (stored === 'dark' || stored === 'light') {
        applyTheme(stored);
    } else {
        // First visit — default to light (brand). Respect OS preference if user prefers dark.
        var prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
        applyTheme(prefersDark ? 'dark' : 'light');
    }
}
// Apply theme as early as possible to avoid FOUC
initTheme();

// ── GLOBAL SEARCH HELPERS ────────────────────────────────────
function focusGlobalSearch() {
    var input = document.getElementById('global-search');
    if (input) { input.focus(); input.select(); }
}
document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === 'k' || e.key === 'K')) {
        e.preventDefault();
        focusGlobalSearch();
    }
});

// ═══════════════════════════════════════════════════════════
// SUBSCRIPTION · SOFT PAYWALL
// ═══════════════════════════════════════════════════════════
function getFreeModuleIds() {
    var n = (SUBSCRIPTION.paywall && SUBSCRIPTION.paywall.free_modules) || 3;
    return MODULES_LIST.slice(0, n).map(function(m){ return m.id; });
}
function isModuleUnlocked(id) {
    if (SUBSCRIPTION.is_premium) return true;
    return getFreeModuleIds().indexOf(id) !== -1;
}

// Hide/reveal a module's body and inject the in-lesson paywall gate.
function applyModuleLock(modEl, mObj, unlocked) {
    var body = modEl.querySelector('.module-body');
    if (!body) return;
    var gate = body.querySelector('.paywall-gate');
    if (unlocked) {
        // Restore anything we hid
        body.querySelectorAll('[data-paywall-hidden]').forEach(function(el){
            el.style.display = ''; el.removeAttribute('data-paywall-hidden');
        });
        if (gate) gate.remove();
        return;
    }
    // Locked: keep only the overview (the free teaser), hide the rest
    Array.prototype.forEach.call(body.children, function(el){
        if (el.classList.contains('overview-content')) return;
        if (el.classList.contains('paywall-gate')) return;
        if (el.style.display !== 'none') {
            el.setAttribute('data-paywall-hidden', '1');
            el.style.display = 'none';
        }
    });
    if (!gate) {
        var freeN = (SUBSCRIPTION.paywall && SUBSCRIPTION.paywall.free_modules) || 3;
        gate = document.createElement('div');
        gate.className = 'paywall-gate';
        gate.innerHTML =
            '<div class="paywall-gate-lock">🔒</div>' +
            '<h3>' + mObj.id + ' — ' + mObj.title + '</h3>' +
            '<p>This is a premium lesson. Subscribe to unlock the full module — step-by-step SOPs, checklists, knowledge quiz and expert video walkthroughs.</p>' +
            '<ul class="paywall-gate-outcomes">' +
                '<li>Complete SOPs &amp; frameworks for ' + mObj.title + '</li>' +
                '<li>Actionable checklist you can apply today</li>' +
                '<li>Knowledge-check quiz &amp; Amazon video cards</li>' +
            '</ul>' +
            '<button class="btn btn-primary" onclick="openPaywall()">🔓 Unlock This Lesson</button>' +
            '<div class="paywall-gate-note">First ' + freeN + ' modules are free · Cancel anytime</div>';
        body.appendChild(gate);
    }
}

function updatePlanBadge() {
    var btn  = document.getElementById('upgrade-btn');
    var lbl  = document.getElementById('upgrade-btn-label');
    var pill = document.getElementById('plan-pill');
    var name = (SUBSCRIPTION.plan_detail && SUBSCRIPTION.plan_detail.name) ||
               (SUBSCRIPTION.plan === 'free' ? 'Free' : SUBSCRIPTION.plan);
    if (SUBSCRIPTION.is_premium) {
        if (btn) btn.classList.add('is-premium');
        if (lbl) lbl.textContent = 'Premium';
        if (pill) { pill.style.display = 'inline-flex'; pill.textContent = name; pill.classList.add('premium'); }
    } else {
        if (btn) btn.classList.remove('is-premium');
        if (lbl) lbl.textContent = 'Upgrade';
        if (pill) { pill.style.display = 'inline-flex'; pill.textContent = 'Free'; pill.classList.remove('premium'); }
    }
}

function refreshNavLocks() {
    var freeIds = getFreeModuleIds();
    MODULES_LIST.forEach(function(m){
        var li = document.getElementById('nav_item_' + m.id);
        if (!li) return;
        var locked = !(SUBSCRIPTION.is_premium || freeIds.indexOf(m.id) !== -1);
        li.classList.toggle('locked', locked);
        var lock = li.querySelector('.nav-lock');
        // The lock icon mirrors real gating — a previously-visited module that
        // is now locked still shows 🔒
        if (locked) {
            if (!lock) {
                lock = document.createElement('span');
                lock.className = 'nav-lock';
                lock.textContent = '🔒';
                li.appendChild(lock);
            }
        } else if (lock) {
            lock.remove();
        }
    });
}

async function loadPlans() {
    try {
        var r = await fetch(API_BASE + '/plans');
        if (!r.ok) return;
        var d = await r.json();
        PLANS_CACHE = d.plans || [];
        PAYMENTS_MOCK = !!d.mock_payments;
        if (d.paywall) {
            SUBSCRIPTION.paywall = d.paywall;
            refreshNavLocks();   // free_modules may have changed
        }
    } catch (e) { /* offline */ }
}

// Last-known entitlement per user, so a paying subscriber keeps premium access
// when the API is unreachable (offline single-file use-case).
function subCacheKey(sess) {
    return 'smeminds_sub_v1:' + ((sess && sess.email) || '').toLowerCase();
}
function loadCachedSubscription() {
    var sess = getSession();
    if (!sess) return;
    try {
        var s = localStorage.getItem(subCacheKey(sess));
        if (!s) return;
        var cached = JSON.parse(s);
        // Honour expiry offline — a lapsed plan must not stay premium forever
        if (cached.expires_at && cached.expires_at * 1000 < Date.now()) {
            cached.is_premium = false; cached.plan = 'free'; cached.status = 'expired';
        }
        SUBSCRIPTION = Object.assign({}, SUBSCRIPTION, cached);
    } catch (e) {}
}

async function loadSubscription() {
    var sess = getSession();
    if (!sess || !sess.token) { updatePlanBadge(); refreshNavLocks(); return; }
    try {
        var r = await authFetch(API_BASE + '/subscription');
        if (r.ok) {
            var data = await r.json();
            SUBSCRIPTION = Object.assign({}, SUBSCRIPTION, data);
            try { localStorage.setItem(subCacheKey(sess), JSON.stringify(data)); } catch (e) {}
        }
    } catch (e) { /* offline — cached entitlement (if any) stays in effect */ }
    updatePlanBadge();
    refreshNavLocks();
    if (typeof updateJourneyProgress === 'function') updateJourneyProgress();
}

// Razorpay checkout.js loads on demand — a render-blocking <script> in <head>
// would stall first paint and hang offline use.
var _rzpLoading = null;
function ensureRazorpay() {
    if (typeof Razorpay !== 'undefined') return Promise.resolve(true);
    if (_rzpLoading) return _rzpLoading;
    _rzpLoading = new Promise(function(resolve) {
        var s = document.createElement('script');
        s.src = 'https://checkout.razorpay.com/v1/checkout.js';
        s.onload = function(){ resolve(true); };
        s.onerror = function(){ _rzpLoading = null; resolve(false); };
        document.head.appendChild(s);
    });
    return _rzpLoading;
}

async function openPaywall() {
    var modal = document.getElementById('paywall-modal');
    if (!modal) return;
    if (!PLANS_CACHE.length) { await loadPlans(); }
    renderPlans();
    modal.style.display = 'block';
}
function closePaywall() {
    var m = document.getElementById('paywall-modal');
    if (m) m.style.display = 'none';
}

function setBillingCycle(c) {
    BILLING_CYCLE = c === 'yearly' ? 'yearly' : 'monthly';
    var bm = document.getElementById('bt-monthly');
    var by = document.getElementById('bt-yearly');
    if (bm) bm.classList.toggle('active', BILLING_CYCLE === 'monthly');
    if (by) by.classList.toggle('active', BILLING_CYCLE === 'yearly');
    renderPlans();
}

function renderPlans() {
    var wrap = document.getElementById('plan-cards');
    if (!wrap) return;
    var cur = SUBSCRIPTION.plan;
    var foot = document.getElementById('paywall-foot');
    if (foot) foot.textContent = PAYMENTS_MOCK
        ? 'Test mode — checkout is simulated, no real charge.'
        : 'Secure payment via Razorpay · UPI · Cards · Net Banking · EMI';
    wrap.innerHTML = PLANS_CACHE.map(function(p){
        var isFree = p.id === 'free';
        var isCurrent = p.id === cur;
        var price = BILLING_CYCLE === 'yearly' ? p.yearly : p.monthly;
        var amt = isFree ? 'Free' : '₹' + Number(price).toLocaleString('en-IN');
        var cyc = isFree ? 'forever' : (BILLING_CYCLE === 'yearly' ? '/year' : '/month');
        var cta;
        if (isCurrent)    cta = '<button class="plan-card-cta" disabled>Current</button>';
        else if (isFree)  cta = '<button class="plan-card-cta" disabled>Free</button>';
        else              cta = '<button class="plan-card-cta" onclick="subscribePlan(\'' + escHtml(p.id) + '\')">' + escHtml(p.cta || 'Choose') + '</button>';
        return '<div class="plan-card ' + (p.popular ? 'popular' : '') + ' ' + (isCurrent ? 'current' : '') + '">' +
            (p.popular ? '<span class="plan-card-pop">Most Popular</span>' : '') +
            '<div class="plan-card-info"><div class="plan-card-name">' + escHtml(p.name) + '</div>' +
            '<div class="plan-card-tag">' + escHtml(p.tagline || '') + '</div></div>' +
            '<div style="display:flex;align-items:center;gap:12px">' +
                '<div class="plan-card-price"><div class="plan-card-amt">' + amt + '</div>' +
                '<div class="plan-card-cyc">' + cyc + '</div></div>' + cta +
            '</div></div>';
    }).join('');
}

async function subscribePlan(planId) {
    var sess = getSession();
    if (!sess || !sess.token) { alert('Please sign in first.'); return; }
    var foot = document.getElementById('paywall-foot');
    if (foot) foot.textContent = 'Creating your secure order…';
    try {
        var r = await authFetch(API_BASE + '/billing/order', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ plan: planId, cycle: BILLING_CYCLE })
        });
        if (!r.ok) {
            var d = await r.json().catch(function(){ return {}; });
            if (foot) foot.textContent = d.detail || 'Could not start checkout.';
            return;
        }
        var order = await r.json();
        if (order.mock) {
            if (foot) foot.textContent = 'Processing test payment…';
            await activateSubscription({ razorpay_order_id: order.order_id });
            return;
        }
        var sdkReady = await ensureRazorpay();
        if (!sdkReady) {
            if (foot) foot.textContent = 'Could not load the payment provider. Check your connection and try again.';
            return;
        }
        var options = {
            key: order.key_id, amount: order.amount, currency: order.currency,
            name: 'SMEMinds Playbook',
            description: order.plan_name + ' plan (' + BILLING_CYCLE + ')',
            order_id: order.order_id,
            prefill: { email: sess.email || '', name: sess.name || '' },
            theme: { color: '#ff6b35' },
            handler: function(resp){
                activateSubscription({
                    razorpay_order_id: resp.razorpay_order_id,
                    razorpay_payment_id: resp.razorpay_payment_id,
                    razorpay_signature: resp.razorpay_signature
                });
            }
        };
        var rzp = new Razorpay(options);
        rzp.on('payment.failed', function(){ if (foot) foot.textContent = 'Payment failed. Please try again.'; });
        rzp.open();
    } catch (e) {
        if (foot) foot.textContent = 'Cannot reach server. Is the backend running on ' + API_BASE + '?';
    }
}

async function activateSubscription(payment) {
    var sess = getSession();
    var foot = document.getElementById('paywall-foot');
    try {
        // The server resolves plan/cycle/amount from its stored order record —
        // the client only relays Razorpay's confirmation fields.
        var r = await authFetch(API_BASE + '/billing/verify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payment || {})
        });
        if (!r.ok) {
            var d = await r.json().catch(function(){ return {}; });
            if (foot) foot.textContent = d.detail || 'Could not activate subscription.';
            return;
        }
        var data = await r.json();
        SUBSCRIPTION = Object.assign({}, SUBSCRIPTION, data.subscription, { plan_detail: data.plan_detail });
        try { if (sess) localStorage.setItem(subCacheKey(sess), JSON.stringify(Object.assign({}, data.subscription, { plan_detail: data.plan_detail }))); } catch (e) {}
        updatePlanBadge();
        refreshNavLocks();
        if (typeof updateJourneyProgress === 'function') updateJourneyProgress();
        closePaywall();
        showToastMsg('🎉 Welcome to ' + (data.plan_detail ? data.plan_detail.name : 'Premium') + '! All modules unlocked.');
        // Re-render the currently open module so its content reveals immediately
        var open = document.querySelector('.module-section[style*="block"]');
        if (open) { navToModule(open.id.replace('module_', '')); }
    } catch (e) {
        if (foot) foot.textContent = 'Activation failed. Please try again.';
    }
}

// ═══════════════════════════════════════════════════════════
// AMAZON GROWTH JOURNEY · curriculum render + interactions
// ═══════════════════════════════════════════════════════════
var PILLAR_META = [
    { p:'p1', num:'01', name:'Account Management', cat:'Amazon Foundation',          color:'#10b981', sops:22, hours:3, level:'Beginner',     desc:'Seller Central setup, account health, compliance, suspension appeals, tax &amp; fee optimisation.' },
    { p:'p2', num:'02', name:'Selection',          cat:'Catalogue Excellence',       color:'#ff6b35', sops:25, hours:4, level:'Beginner',     desc:'Product research, ASIN creation, variations, browse nodes, localisation &amp; bulk uploads.' },
    { p:'p3', num:'03', name:'Efficiency',         cat:'Listing Optimization Engine',color:'#6366f1', sops:20, hours:3, level:'Intermediate', desc:'SEO &amp; keyword strategy, image optimisation, A+ content, pricing &amp; listing quality.' },
    { p:'p4', num:'04', name:'Traffic',            cat:'Customer Acquisition Engine', color:'#3b82f6', sops:18, hours:4, level:'Intermediate', desc:'Sponsored Products / Brands / Display, DSP, external traffic, influencer &amp; organic SEO.' },
    { p:'p5', num:'05', name:'Conversion',         cat:'Revenue Growth Engine',      color:'#22c55e', sops:15, hours:3, level:'Intermediate', desc:'CRO, A/B testing, promotions, coupons, Subscribe &amp; Save, cross-sell &amp; upsell.' },
    { p:'p6', num:'06', name:'Speed',              cat:'Operations Excellence',      color:'#f59e0b', sops:20, hours:4, level:'Advanced',     desc:'FBA, inventory planning, forecasting, replenishment, Buy Box &amp; SLA monitoring.' },
    { p:'p7', num:'07', name:'Tools',              cat:'Seller Intelligence Stack',  color:'#8b5cf6', sops:24, hours:4, level:'Advanced',     desc:'Brand Analytics, Search Query Performance, Ad Console, Helium 10, Jungle Scout &amp; AI tools.' },
    { p:'p8', num:'08', name:'Brand Registry',     cat:'Brand Growth Framework',     color:'#ec4899', sops:18, hours:3, level:'Advanced',     desc:'Enrolment, Brand Store, A+ content, Sponsored Brands, Vine &amp; Brand Analytics.' },
    { p:'p9', num:'09', name:'Brand Protection',   cat:'Marketplace Defense System', color:'#ef4444', sops:22, hours:4, level:'Expert',       desc:'Trademark protection, Transparency, Project Zero, counterfeit &amp; hijacker enforcement.' }
];
var EXPANDED_PILLARS = {};

// Pull admin-editable pillar metadata from the backend (falls back to defaults)
async function loadPillars() {
    try {
        var r = await fetch(API_BASE + '/pillars');
        if (!r.ok) return;
        var d = await r.json();
        if (d && d.pillars && d.pillars.length) {
            PILLAR_META = d.pillars;
            renderJourney();
        }
    } catch (e) { /* offline — keep built-in defaults */ }
}

// Pull admin-editable site content (hero + journey heading + stat strip)
async function loadContent() {
    try {
        var r = await fetch(API_BASE + '/content');
        if (!r.ok) return;
        applyContent(await r.json());
    } catch (e) { /* offline — keep built-in copy */ }
}

function applyContent(c) {
    if (!c) return;
    var set = function(id, val){ var el = document.getElementById(id); if (el && val != null) el.textContent = val; };
    set('hero-eyebrow-text', c.hero_eyebrow);
    set('hero-title', c.hero_title);
    set('hero-accent', c.hero_accent);
    set('hero-subtitle', c.hero_subtitle);
    set('journey-eyebrow', c.journey_eyebrow);
    set('journey-title', c.journey_title);
    if (Array.isArray(c.stats) && c.stats.length) {
        var wrap = document.getElementById('curriculum-stats');
        if (wrap) {
            wrap.innerHTML = c.stats.map(function(s, i){
                var numeric = /^\d+$/.test(String(s.value));
                var accent = (i === c.stats.length - 1 && !numeric) ? ' cstat-accent' : '';
                var valHtml = numeric
                    ? '<span class="cstat-val" data-count="' + escHtml(s.value) + '"' + (s.suffix ? ' data-suffix="' + escHtml(s.suffix) + '"' : '') + '>0</span>'
                    : '<span class="cstat-val">' + escHtml(s.value || '') + escHtml(s.suffix || '') + '</span>';
                return '<div class="cstat' + accent + '">' + valHtml + '<span class="cstat-label">' + escHtml(s.label || '') + '</span></div>';
            }).join('');
            animateCounters();
        }
    }
}

var JP_ICON_BOOK  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>';
var JP_ICON_LIST  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>';
var JP_ICON_CLOCK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>';
var JP_ICON_AI    = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2M20 14h2M15 13v2M9 13v2"/></svg>';

function jpMetaItem(svg, val, label) {
    return '<span class="jp-meta-item">' + svg + '<strong>' + val + '</strong> <small>' + label + '</small></span>';
}

function pillarJourneyState(meta) {
    var mods = MODULES_LIST.filter(function(m){ return m.pillar === meta.p; });
    var total = mods.length;
    var done = mods.filter(function(m){ return userData.visited.indexOf(m.id) !== -1; }).length;
    var pct = total ? Math.round(done / total * 100) : 0;
    var anyUnlocked = mods.some(function(m){ return isModuleUnlocked(m.id); });
    var status, statusLabel;
    if (pct === 100)        { status = 'complete'; statusLabel = 'Completed'; }
    else if (!anyUnlocked)  { status = 'locked';   statusLabel = 'Locked'; }
    else if (done > 0)      { status = 'active';   statusLabel = 'In Progress'; }
    else                    { status = 'active';   statusLabel = 'Available'; }
    return { mods: mods, total: total, done: done, pct: pct, status: status, statusLabel: statusLabel };
}

// Cheap in-place refresh after a progress change: patches rings, bars and
// per-module ticks. Falls back to a full render when a pillar's status flips
// (locked/active/complete) since that changes structure, not just numbers.
function updateJourneyProgress() {
    var wrap = document.getElementById('journey');
    if (!wrap) return;
    if (!wrap.firstChild) { renderJourney(); return; }
    var R = 27, C = 2 * Math.PI * R;
    for (var i = 0; i < PILLAR_META.length; i++) {
        var meta = PILLAR_META[i];
        var step = document.getElementById('jp-step-' + meta.p);
        if (!step) { renderJourney(); return; }
        var st = pillarJourneyState(meta);
        if (step.getAttribute('data-status') !== st.status) { renderJourney(); return; }
        var ring = step.querySelector('.jp-ring .fill');
        if (ring) ring.setAttribute('stroke-dashoffset', (C * (1 - st.pct / 100)).toFixed(1));
        var fill = step.querySelector('.jp-prog-fill');
        if (fill) fill.style.width = st.pct + '%';
        var pctEl = step.querySelector('.jp-prog-pct');
        if (pctEl) pctEl.textContent = st.pct + '% · ' + st.done + '/' + st.total;
        step.querySelectorAll('.jp-mod').forEach(function(row){
            var midEl = row.querySelector('.jp-mod-id');
            if (!midEl) return;
            var mid = midEl.textContent;
            var d = userData.visited.indexOf(mid) !== -1;
            row.classList.toggle('done', d);
            var state = row.querySelector('.jp-mod-state');
            if (state) state.textContent = d ? '✓' : (isModuleUnlocked(mid) ? '' : '🔒');
        });
    }
}

function renderJourney() {
    var wrap = document.getElementById('journey');
    if (!wrap) return;
    var R = 27, C = 2 * Math.PI * R;
    wrap.innerHTML = PILLAR_META.map(function(meta){
        var st = pillarJourneyState(meta);
        var mods = st.mods, total = st.total, done = st.done, pct = st.pct;
        var status = st.status, statusLabel = st.statusLabel;
        var firstId = total ? mods[0].id : null;
        var offset = C * (1 - pct / 100);
        var node = status === 'complete'
            ? '<div class="jp-node-core"><span class="jp-check">✓</span></div>'
            : status === 'locked'
                ? '<div class="jp-node-core">🔒</div>'
                : '<div class="jp-node-core">' + meta.num + '</div>';
        var modList = mods.map(function(m){
            var d = userData.visited.indexOf(m.id) !== -1;
            var ul = isModuleUnlocked(m.id);
            var act = ul ? ("navToModule('" + m.id + "')") : "openPaywall()";
            return '<div class="jp-mod ' + (d ? 'done' : '') + '" onclick="' + act + '">' +
                '<span class="jp-mod-dot"></span><span class="jp-mod-id">' + m.id + '</span>' +
                '<span class="jp-mod-title">' + m.title + '</span>' +
                '<span class="jp-mod-state">' + (d ? '✓' : (ul ? '' : '🔒')) + '</span></div>';
        }).join('');
        var primary = status === 'locked'
            ? '<button class="jp-btn jp-btn-lock" onclick="event.stopPropagation();openPaywall()">🔓 Unlock Pillar</button>'
            : '<button class="jp-btn jp-btn-primary" onclick="event.stopPropagation();navToModule(\'' + firstId + '\')">' + (done > 0 ? 'Continue' : 'Start Learning') + '</button>';
        var expanded = EXPANDED_PILLARS[meta.p] ? ' expanded' : '';
        return '<div class="jp-step reveal is-' + status + expanded + '" id="jp-step-' + meta.p + '" data-status="' + status + '" style="--pc:' + meta.color + '">' +
            '<div class="jp-node">' +
                '<svg class="jp-ring" viewBox="0 0 72 72"><circle class="track" cx="36" cy="36" r="' + R + '"/>' +
                '<circle class="fill" cx="36" cy="36" r="' + R + '" stroke-dasharray="' + C.toFixed(1) + '" stroke-dashoffset="' + offset.toFixed(1) + '"/></svg>' +
                node +
            '</div>' +
            '<div class="jp-card">' +
                '<div class="jp-card-head">' +
                    '<div><div class="jp-cat">' + meta.cat + '</div><h3 class="jp-title">' + meta.num + ' · ' + meta.name + '</h3></div>' +
                    '<div class="jp-badges"><span class="jp-badge level">' + meta.level + '</span><span class="jp-badge status-' + status + '">' + statusLabel + '</span></div>' +
                '</div>' +
                '<p class="jp-desc">' + meta.desc + '</p>' +
                '<div class="jp-meta">' +
                    jpMetaItem(JP_ICON_BOOK, total, 'Modules') +
                    jpMetaItem(JP_ICON_LIST, meta.sops, 'SOPs') +
                    jpMetaItem(JP_ICON_CLOCK, meta.hours + 'h', 'Learn time') +
                '</div>' +
                '<div class="jp-prog"><div class="jp-prog-track"><div class="jp-prog-fill" style="width:' + pct + '%"></div></div>' +
                    '<span class="jp-prog-pct">' + pct + '% · ' + done + '/' + total + '</span></div>' +
                '<div class="jp-actions">' + primary +
                    '<button class="jp-btn jp-btn-ghost" onclick="event.stopPropagation();togglePillar(\'' + meta.p + '\')">Expand Curriculum</button>' +
                    '<button class="jp-btn jp-btn-icon" title="Ask SMEMinds AI" onclick="event.stopPropagation();askAIAbout(\'' + meta.p + '\')">' + JP_ICON_AI + '</button>' +
                '</div>' +
                '<div class="jp-modules">' + modList + '</div>' +
            '</div>' +
        '</div>';
    }).join('');
    observeReveals();
}

function togglePillar(p) {
    EXPANDED_PILLARS[p] = !EXPANDED_PILLARS[p];
    var step = document.getElementById('jp-step-' + p);
    if (step) step.classList.toggle('expanded', !!EXPANDED_PILLARS[p]);
}

// Animated KPI counters
function animateCounters() {
    var els = document.querySelectorAll('.cstat-val[data-count]');
    els.forEach(function(el){
        var target = parseInt(el.getAttribute('data-count'), 10) || 0;
        var suffix = el.getAttribute('data-suffix') || '';
        var start = null, dur = 1100;
        function step(ts){
            if (!start) start = ts;
            var prog = Math.min((ts - start) / dur, 1);
            var eased = 1 - Math.pow(1 - prog, 3);
            el.textContent = Math.round(target * eased) + suffix;
            if (prog < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
    });
}

// Scroll reveal
var _revealObserver = null;
function observeReveals() {
    var items = document.querySelectorAll('.reveal:not(.in)');
    if (!('IntersectionObserver' in window)) {
        items.forEach(function(el){ el.classList.add('in'); });
        return;
    }
    if (!_revealObserver) {
        _revealObserver = new IntersectionObserver(function(entries){
            entries.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('in'); _revealObserver.unobserve(e.target); } });
        }, { threshold: 0.12 });
    }
    items.forEach(function(el){ _revealObserver.observe(el); });
}

// ── AI LEARNING ASSISTANT ────────────────────────────────────
var AI_OPENED_ONCE = false;
var AI_GLOSSARY = {
    'acos':'ACoS = Ad Spend ÷ Ad Sales. The lower, the more efficient your ads. Deep-dive in Pillar 04 · Traffic.',
    'tacos':'TACoS = Ad Spend ÷ Total Sales — shows how reliant your revenue is on ads. See Pillar 04 · Traffic.',
    'buy box':'The Buy Box is the “Add to Cart” winner — driven by price, fulfilment, stock &amp; account health. See Pillar 06 · Speed.',
    'fba':'FBA (Fulfilment by Amazon) — Amazon stores, picks, packs &amp; ships your orders. Covered in Pillar 06 · Speed.',
    'fbm':'FBM (Fulfilled by Merchant) — you handle storage &amp; shipping. See Pillar 06 · Speed.',
    'a+':'A+ Content enriches listings with rich image/text modules to lift conversion. See Pillars 03 &amp; 08.',
    'brand registry':'Brand Registry unlocks brand-building &amp; protection tools. See Pillar 08.',
    'asin':'ASIN = Amazon Standard Identification Number — the unique product ID. See Pillar 02 · Selection.',
    'ppc':'PPC = Pay-Per-Click ads (Sponsored Products / Brands / Display). See Pillar 04 · Traffic.',
    'gst':'GST handling, invoicing &amp; TDS/TCS are covered in Pillar 01 · Account Management.',
    'suspension':'Suspension prevention &amp; the appeal (POA) framework live in Pillar 01 · Account Management.',
    'vine':'Amazon Vine gets early reviews from trusted reviewers. See Pillar 08 · Brand Registry.'
};

function toggleAI() {
    var panel = document.getElementById('ai-panel');
    if (!panel) return;
    var open = panel.classList.toggle('open');
    panel.setAttribute('aria-hidden', open ? 'false' : 'true');
    if (open && !AI_OPENED_ONCE) {
        AI_OPENED_ONCE = true;
        aiSeed();
    }
    if (open) { var i = document.getElementById('ai-input'); if (i) setTimeout(function(){ i.focus(); }, 60); }
}

function aiAddMsg(html, who) {
    var body = document.getElementById('ai-body');
    if (!body) return;
    who = who || 'bot';
    var row = document.createElement('div');
    row.className = 'ai-row ' + who;
    if (who === 'bot') {
        var av = document.createElement('img');
        av.className = 'ai-msg-avatar';
        av.alt = 'SMEMinds AI';
        if (typeof SMEMINDS_AI_ICON !== 'undefined' && SMEMINDS_AI_ICON) av.src = SMEMINDS_AI_ICON;
        row.appendChild(av);
    }
    var div = document.createElement('div');
    div.className = 'ai-msg ' + who;
    div.innerHTML = html;
    row.appendChild(div);
    body.appendChild(row);
    body.scrollTop = body.scrollHeight;
}

function aiSeed() {
    var name = (getSession() && (getSession().name || '')) || '';
    aiAddMsg('👋 Hi' + (name ? ' ' + name.split(' ')[0] : '') + '! I\'m your <strong>SMEMinds AI</strong> co-pilot. Ask me about any SOP, module, or Amazon term — or try:', 'bot');
    var chips = '<div class="ai-chips">' +
        '<span class="ai-chip" onclick="aiQuick(\'What should I learn next?\')">What next?</span>' +
        '<span class="ai-chip" onclick="aiQuick(\'How do I lower ACoS?\')">Lower ACoS</span>' +
        '<span class="ai-chip" onclick="aiQuick(\'Buy Box\')">Buy Box</span>' +
        '<span class="ai-chip" onclick="aiQuick(\'Brand Registry\')">Brand Registry</span>' +
    '</div>';
    aiAddMsg(chips, 'bot');
}

function aiQuick(q) {
    var i = document.getElementById('ai-input');
    if (i) i.value = q;
    askAI();
}

function askAIAbout(pillarId) {
    var meta = PILLAR_META.find(function(m){ return m.p === pillarId; });
    if (!meta) return;
    var panel = document.getElementById('ai-panel');
    if (panel && !panel.classList.contains('open')) toggleAI();
    if (!AI_OPENED_ONCE) { AI_OPENED_ONCE = true; aiSeed(); }
    aiAddMsg('Tell me about ' + meta.name, 'user');
    var mods = MODULES_LIST.filter(function(m){ return m.pillar === pillarId; });
    var links = aiModuleLinks(mods.slice(0, 6));
    aiAddMsg('<strong>' + meta.num + ' · ' + meta.name + '</strong> — ' + meta.cat + '.<br>' + meta.desc +
        '<br><br>' + mods.length + ' modules · ' + meta.sops + ' SOPs · ~' + meta.hours + 'h · ' + meta.level + '.<br>Jump in:' + links, 'bot');
}

function aiModuleLinks(mods) {
    return mods.map(function(m){
        var ul = isModuleUnlocked(m.id);
        var act = ul ? ("navToModule('" + m.id + "');toggleAI()") : "openPaywall()";
        return '<span class="ai-res-link" onclick="' + act + '">' + (ul ? '' : '🔒 ') + m.id + ' · ' + m.title + '</span>';
    }).join('');
}

function askAI() {
    var input = document.getElementById('ai-input');
    if (!input) return;
    var q = (input.value || '').trim();
    if (!q) return;
    aiAddMsg(q, 'user');
    input.value = '';
    setTimeout(function(){ aiAddMsg(aiAnswer(q), 'bot'); }, 250);
}

function aiAnswer(q) {
    var lower = q.toLowerCase();
    // 1) Recommend next
    if (/(next|recommend|what.*learn|start|where.*begin)/.test(lower)) {
        var next = MODULES_LIST.find(function(m){ return userData.visited.indexOf(m.id) === -1 && isModuleUnlocked(m.id); });
        if (next) return 'Based on your progress, start here:' + aiModuleLinks([next]);
        var locked = MODULES_LIST.find(function(m){ return !isModuleUnlocked(m.id); });
        if (locked) return 'You\'ve completed all your unlocked modules! 🎉 Unlock the full Playbook to keep going.<br><span class="ai-res-link" onclick="openPaywall()">⭐ View plans &amp; unlock everything</span>';
        return 'Amazing — you\'ve visited every module! 🏆 Head to the 🎓 Certificate to claim your credential.';
    }
    // 2) Glossary
    for (var key in AI_GLOSSARY) {
        if (lower.indexOf(key) !== -1) return AI_GLOSSARY[key];
    }
    // 3) Module search
    var terms = lower.split(/\s+/).filter(function(t){ return t.length > 2; });
    var matches = MODULES_LIST.filter(function(m){
        var t = m.title.toLowerCase();
        return terms.some(function(term){ return t.indexOf(term) !== -1; });
    }).slice(0, 6);
    if (matches.length) {
        return 'I found ' + matches.length + ' module' + (matches.length > 1 ? 's' : '') + ' that may help:' + aiModuleLinks(matches);
    }
    // 4) Fallback
    return 'I couldn\'t find an exact match. Try a topic like “PPC”, “Buy Box”, “FBA”, “Brand Registry”, or ask “what should I learn next?”. You can also <span class="ai-res-link" onclick="focusGlobalSearch();toggleAI()">search all modules ⌘K</span>.';
}

// ── BOOTSTRAP ────────────────────────────────────────────────
// DOMContentLoaded (not 'load') so startup doesn't wait on external fonts.
document.addEventListener('DOMContentLoaded', function() {
    applyBrandLogos(document);
    // Admin impersonation: open the playbook as a user via #impersonate=<jwt>
    var _imp = (location.hash || '').match(/impersonate=([^&]+)/);
    if (_imp) {
        var _tok = decodeURIComponent(_imp[1]);
        try { history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
        fetch(API_BASE + '/me', { headers: { Authorization: 'Bearer ' + _tok } })
            .then(function (r) { return r.ok ? r.json() : null; })
            .then(function (d) {
                if (d && d.user) {
                    var u = Object.assign({}, d.user, { token: _tok });
                    setSession(u); claimLocalDataFor(u.email);
                    unlockApp(u); pullProgressFromServer(); updateDashboardCertStatus();
                    showToastMsg('👀 Viewing as ' + (u.name || u.email) + ' (admin impersonation)');
                }
            }).catch(function () {});
    }
    var session = getSession();
    loadUserData();
    if (session) {
        // unlockApp loads cached entitlements + the plans → subscription chain
        unlockApp(session);
    } else {
        loadPlans().then(loadSubscription);
    }
    initNav();
    updateProgress();
    // Render the interactive Growth Journey + animate KPI counters
    renderJourney();
    animateCounters();
    observeReveals();
    // Background refresh from backend if signed in (non-blocking)
    if (session && session.token) { pullProgressFromServer(); }
    // Pull admin-editable pillars + site content (non-blocking)
    loadPillars();
    loadContent();
    // Fire-and-forget traffic tracking (anonymous if not signed in)
    trackAppOpen();
    // Open Pillar 1 nav by default
    var p1     = document.getElementById('nav-p1');
    var grp1   = document.getElementById('group-p1');
    if (p1)   p1.classList.add('open');
    if (grp1) grp1.classList.add('open');
    // Phones start with the off-canvas sidebar closed
    if (window.innerWidth <= 768) {
        var sb = document.getElementById('sidebar');
        if (sb) sb.classList.add('collapsed');
    }
    // Always land on the Dashboard. Clear any stale module hash left over from a
    // previous session so reopening never deep-jumps into a pillar (e.g. Brand Protection).
    try { if (location.hash && location.hash !== '#home') history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
    showDashboard();
    // Embed the medium overview player on the dashboard (paused poster, ready to play)
    mountOverviewPlayer();
});
