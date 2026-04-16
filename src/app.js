// ═══════════════════════════════════════════════════════════
// SMEMINDS AMAZON ACCOUNT MANAGEMENT PLAYBOOK — CORE APP
// ═══════════════════════════════════════════════════════════

// ── COPY PROTECTION ─────────────────────────────────────────
document.addEventListener('contextmenu', e => e.preventDefault());
document.addEventListener('keydown', e => {
    if (e.key === 'F12' ||
        (e.ctrlKey && ['u','U','c','C','a','A','s','S','p','P'].includes(e.key)) ||
        (e.metaKey && ['u','c','a','s'].includes(e.key))) {
        e.preventDefault(); showToast();
    }
});
document.addEventListener('copy', e => { e.preventDefault(); showToast(); });
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        const ov = document.getElementById('screen-overlay');
        if (ov) ov.style.display = 'flex';
    } else {
        const ov = document.getElementById('screen-overlay');
        if (ov) ov.style.display = 'none';
    }
});

function showToast() {
    const t = document.getElementById('copy-toast');
    if (!t) return;
    t.classList.add('show');
    setTimeout(() => t.classList.remove('show'), 3000);
}

// ── MODULE REGISTRY ──────────────────────────────────────────
const MODULES_LIST = [
    // P1 — Selection (8 modules)
    { id:'1.1', title:'Catalogue Strategy',         pillar:'p1' },
    { id:'1.2', title:'Catalogue Building',         pillar:'p1' },
    { id:'1.3', title:'Catalogue Health',           pillar:'p1' },
    { id:'1.4', title:'Localisation',               pillar:'p1' },
    { id:'1.5', title:'Fee Schedule & Cost Mastery',pillar:'p1' },
    { id:'1.6', title:'Flat File Bulk Management',  pillar:'p1' },
    { id:'1.7', title:'FBA Shipment Creation',      pillar:'p1' },
    { id:'1.8', title:'Variations & Size Charts',   pillar:'p1' },
    // P2 — Efficiency (7 modules)
    { id:'2.1', title:'Listing Quality',            pillar:'p2' },
    { id:'2.2', title:'Image Optimisation',         pillar:'p2' },
    { id:'2.3', title:'Pricing Strategy',           pillar:'p2' },
    { id:'2.4', title:'Review & Rating',            pillar:'p2' },
    { id:'2.5', title:'A+ & Brand Content',         pillar:'p2' },
    { id:'2.6', title:'Buy Box Strategy',           pillar:'p2' },
    { id:'2.7', title:'Deals & Promotions',         pillar:'p2' },
    // P3 — Traffic (6 modules)
    { id:'3.1', title:'Sponsored Ads',              pillar:'p3' },
    { id:'3.2', title:'DSP & Display',              pillar:'p3' },
    { id:'3.3', title:'External Traffic',           pillar:'p3' },
    { id:'3.4', title:'Organic SEO',                pillar:'p3' },
    { id:'3.5', title:'Deals & Events',             pillar:'p3' },
    { id:'3.6', title:'Sponsored Ads Deep-Dive',    pillar:'p3' },
    // P4 — Conversion (5 modules)
    { id:'4.1', title:'Detail Page CRO',            pillar:'p4' },
    { id:'4.2', title:'Promotions & Deals',         pillar:'p4' },
    { id:'4.3', title:'Social Proof',               pillar:'p4' },
    { id:'4.4', title:'Post-Purchase',              pillar:'p4' },
    { id:'4.5', title:'Cross-sell & Upsell',        pillar:'p4' },
    // P5 — Speed (7 modules)
    { id:'5.1', title:'FBA Management',             pillar:'p5' },
    { id:'5.2', title:'FBM & Easy Ship',            pillar:'p5' },
    { id:'5.3', title:'Inventory Planning',         pillar:'p5' },
    { id:'5.4', title:'Account Health & SLA',       pillar:'p5' },
    { id:'5.5', title:'Easy Ship Prime & GD',       pillar:'p5' },
    { id:'5.6', title:'Seller Flex',                pillar:'p5' },
    { id:'5.7', title:'IXD Programme',              pillar:'p5' },
    // P6 — Tools (8 modules)
    { id:'6.1', title:'Seller Central',             pillar:'p6' },
    { id:'6.2', title:'Brand Analytics',            pillar:'p6' },
    { id:'6.3', title:'Advertising Console',        pillar:'p6' },
    { id:'6.4', title:'3P Tools',                   pillar:'p6' },
    { id:'6.5', title:'Manage Your Experiments',    pillar:'p6' },
    { id:'6.6', title:'Kitna Milega — Profitability',pillar:'p6' },
    { id:'6.7', title:'Subscribe & Save + MOQ + AUR',pillar:'p6' },
    { id:'6.8', title:'LTSF & Inventory Age',       pillar:'p6' },
    // P7 — Brand Registry (6 modules)
    { id:'7.1', title:'BR Enrolment',               pillar:'p7' },
    { id:'7.2', title:'Brand Store',                pillar:'p7' },
    { id:'7.3', title:'A+ Content (BR)',             pillar:'p7' },
    { id:'7.4', title:'Sponsored Brands',           pillar:'p7' },
    { id:'7.5', title:'MYE via Brand Registry',     pillar:'p7' },
    { id:'7.6', title:'Vine Programme',             pillar:'p7' },
    // P8 — Brand Protection (8 modules)
    { id:'8.1', title:'IP & Trademark',             pillar:'p8' },
    { id:'8.2', title:'Transparency Programme',     pillar:'p8' },
    { id:'8.3', title:'Project Zero',               pillar:'p8' },
    { id:'8.4', title:'Listing Hijacking',          pillar:'p8' },
    { id:'8.5', title:'Review Manipulation',        pillar:'p8' },
    { id:'8.6', title:'Account Safety',             pillar:'p8' },
    { id:'8.7', title:'Amazon B2B',                 pillar:'p8' },
    { id:'8.8', title:'GIS & Sale Planning',        pillar:'p8' }
];

// ── STATE ─────────────────────────────────────────────────────
let userData = { visited: [], checklists: {}, quizScores: {}, feedback: [] };

function loadUserData() {
    try { const s = localStorage.getItem('smeminds_playbook_v2'); if (s) userData = JSON.parse(s); } catch(e) {}
}
function saveUserData() {
    try { localStorage.setItem('smeminds_playbook_v2', JSON.stringify(userData)); } catch(e) {}
    updateProgress();
}

// ── NAV INIT ──────────────────────────────────────────────────
function initNav() {
    ['p1','p2','p3','p4','p5','p6','p7','p8'].forEach(p => {
        const ul = document.getElementById(`nav-${p}`);
        if (!ul) return;
        ul.innerHTML = '';
        MODULES_LIST.filter(m => m.pillar === p).forEach(m => {
            const li = document.createElement('li');
            li.id = `nav_item_${m.id}`;
            const visited = userData.visited.includes(m.id);
            li.textContent = `${m.id} — ${m.title}${visited?' ✓':''}`;
            li.onclick = () => navToModule(m.id);
            ul.appendChild(li);
        });
    });
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const main    = document.getElementById('main-content');
    if (!sidebar) return;
    sidebar.classList.toggle('collapsed');
    const collapsed = sidebar.classList.contains('collapsed');
    if (main) main.style.marginLeft = collapsed ? '0' : '';
}

function toggleNav(listId, groupId) {
    const list  = document.getElementById(listId);
    const group = document.getElementById(groupId);
    if (list)  list.classList.toggle('open');
    if (group) group.classList.toggle('open');
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
    setBreadcrumb('Dashboard');
    // Highlight home nav btn
    document.querySelectorAll('.nav-home-btn').forEach(b => b.classList.add('active'));
}

function navToModule(id) {
    hideAllSections();
    const modEl = document.getElementById(`module_${id}`);
    if (!modEl) return;

    modEl.style.display = 'block';
    const navItem = document.getElementById(`nav_item_${id}`);
    if (navItem) navItem.classList.add('active');

    const mObj = MODULES_LIST.find(m => m.id === id);
    if (!mObj) return;

    const pillarNames = { p1:'Selection', p2:'Efficiency', p3:'Traffic', p4:'Conversion', p5:'Speed', p6:'Tools', p7:'Brand Registry', p8:'Brand Protection' };
    setBreadcrumb(`${pillarNames[mObj.pillar]} › ${mObj.title}`);
    // Remove home btn active state
    document.querySelectorAll('.nav-home-btn').forEach(b => b.classList.remove('active'));

    // Track visit
    if (!userData.visited.includes(id)) {
        userData.visited.push(id);
        saveUserData();
        // Update nav item to show check
        if (navItem) navItem.textContent = `${id} — ${mObj.title} ✓`;
    }

    // Restore checklist state
    restoreChecklist(id);

    // Scroll to top
    const sc = document.querySelector('.content-scrollable');
    if (sc) sc.scrollTop = 0;

    // Auto-open the pillar nav
    const pillarNav = document.getElementById(`nav-${mObj.pillar}`);
    const pillarGroup = document.getElementById(`group-${mObj.pillar}`);
    if (pillarNav  && !pillarNav.classList.contains('open'))  pillarNav.classList.add('open');
    if (pillarGroup && !pillarGroup.classList.contains('open')) pillarGroup.classList.add('open');
}

function setBreadcrumb(text) {
    const el = document.getElementById('bc-current');
    if (el) el.textContent = text;
}

// ── PROGRESS ──────────────────────────────────────────────────
function updateProgress() {
    const total = MODULES_LIST.length;
    const visited = userData.visited.length;
    const pct = Math.round((visited / total) * 100);
    const textEl = document.getElementById('progress-text');
    const barEl  = document.getElementById('progress-bar');
    if (textEl) textEl.textContent = `${pct}%`;
    if (barEl)  barEl.style.width  = `${pct}%`;
    updatePillarCounts();
}

function updatePillarCounts() {
    ['p1','p2','p3','p4','p5','p6','p7','p8'].forEach(p => {
        const total = MODULES_LIST.filter(m => m.pillar === p).length;
        const done  = MODULES_LIST.filter(m => m.pillar === p && userData.visited.includes(m.id)).length;
        const el = document.getElementById(`count-${p}`);
        if (el) el.textContent = `${done}/${total}`;
    });
}

// ── SEARCH ────────────────────────────────────────────────────
function searchContent() {
    const q = (document.getElementById('global-search')?.value || '').toLowerCase().trim();
    document.querySelectorAll('.nav-list li').forEach(li => {
        if (!q || li.textContent.toLowerCase().includes(q)) {
            li.style.display = 'block';
            li.parentElement.classList.add('active');
        } else {
            li.style.display = 'none';
        }
    });
}

// ── MODALS ────────────────────────────────────────────────────
function showBookmarks()      { document.getElementById('bookmarks-modal').style.display = 'block'; }
function closeBookmarks()     { document.getElementById('bookmarks-modal').style.display = 'none';  }
function closeGlobalFeedback(){ document.getElementById('global-feedback-modal').style.display = 'none'; }

function showGlobalFeedback() {
    document.getElementById('global-feedback-modal').style.display = 'block';

    const pillars = ['p1','p2','p3','p4','p5','p6','p7','p8'];
    const pNames  = { p1:'Selection', p2:'Efficiency', p3:'Traffic', p4:'Conversion', p5:'Speed', p6:'Tools', p7:'Brand Registry', p8:'Brand Protection' };
    const qCount  = Object.keys(userData.quizScores).length;
    let statsHtml = `<strong>Overall Progress:</strong> ${userData.visited.length} / 40 modules visited<br>`;
    pillars.forEach(p => {
        const total = MODULES_LIST.filter(m=>m.pillar===p).length;
        const done  = MODULES_LIST.filter(m=>m.pillar===p && userData.visited.includes(m.id)).length;
        statsHtml += `<strong>${pNames[p]}:</strong> ${done} / ${total} completed<br>`;
    });
    statsHtml += `<strong>Quizzes Completed:</strong> ${qCount} / 40`;
    document.getElementById('global-progress-stats').innerHTML = statsHtml;

    let fbHtml = '';
    userData.feedback.forEach(f => {
        fbHtml += `<div style="padding:14px;border:1px solid var(--border);border-radius:8px;margin-bottom:10px;font-size:13px">
            <strong>Module ${f.moduleId}</strong> &nbsp;·&nbsp; ${'★'.repeat(f.stars)}${'☆'.repeat(5-f.stars)} &nbsp;·&nbsp; <em>${f.role||'—'}</em><br>
            <span style="color:var(--text-muted)">Helpful:</span> ${f.helpful||'—'}<br>
            <span style="color:var(--text-muted)">Improve:</span> ${f.improve||'—'}
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
        rows.push([f.moduleId, f.stars, f.role||'', (f.helpful||'').replace(/,/g,' '), (f.improve||'').replace(/,/g,' '), f.date||'']);
    });
    const csv = rows.map(r => r.join(',')).join('\n');
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
function updateChecklist(mid) {
    const chks = document.querySelectorAll(`.chk_${mid}`);
    userData.checklists[mid] = Array.from(chks).map(c => c.checked);
    saveUserData();
}

function restoreChecklist(mid) {
    if (!userData.checklists[mid]) return;
    const chks = document.querySelectorAll(`.chk_${mid}`);
    chks.forEach((c, i) => { c.checked = userData.checklists[mid][i] || false; });
}

// ── QUIZ ──────────────────────────────────────────────────────
function submitQuiz(mid) {
    const qContainer = document.getElementById(`quiz_${mid}`);
    if (!qContainer) return;
    const qs = qContainer.querySelectorAll('.quiz-q');
    let score = 0;

    qs.forEach((q, idx) => {
        const ans = q.getAttribute('data-ans');
        const selected = q.querySelector(`input[name='q_${mid}_${idx}']:checked`);
        const exp = q.querySelector('.q-exp');
        if (!exp) return;

        if (selected) {
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

    userData.quizScores[mid] = score;
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
const ACCOUNTS_KEY = 'smeminds_accounts_v1';

function getSession() {
    try { const s = localStorage.getItem(AUTH_KEY); return s ? JSON.parse(s) : null; } catch(e) { return null; }
}
function setSession(user) {
    localStorage.setItem(AUTH_KEY, JSON.stringify(user));
}
function clearSession() {
    localStorage.removeItem(AUTH_KEY);
}
function getAccounts() {
    try { const s = localStorage.getItem(ACCOUNTS_KEY); return s ? JSON.parse(s) : []; } catch(e) { return []; }
}
function saveAccount(email, passHash, name, role) {
    const accs = getAccounts();
    accs.push({ email: email.toLowerCase(), passHash, name, role });
    localStorage.setItem(ACCOUNTS_KEY, JSON.stringify(accs));
}
function findAccount(email) {
    return getAccounts().find(a => a.email === email.toLowerCase());
}
// Simple hash (not cryptographic — client-side only)
function simpleHash(str) {
    let h = 0;
    for (let i = 0; i < str.length; i++) { h = ((h << 5) - h + str.charCodeAt(i)) | 0; }
    return h.toString(16);
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
}

function handleLogout() {
    if (!confirm('Sign out of SMEMinds Playbook?')) return;
    clearSession();
    const overlay = document.getElementById('login-overlay');
    const app = document.getElementById('main-app');
    if (overlay) overlay.style.display = 'flex';
    if (app) app.style.display = 'none';
}

function switchAuthTab(tab) {
    const signInForm = document.getElementById('form-signin');
    const signUpForm = document.getElementById('form-signup');
    const tabSI = document.getElementById('tab-signin');
    const tabSU = document.getElementById('tab-signup');
    if (tab === 'signin') {
        if (signInForm) signInForm.style.display = 'block';
        if (signUpForm) signUpForm.style.display = 'none';
        if (tabSI) { tabSI.style.background = 'var(--accent)'; tabSI.style.color = '#fff'; }
        if (tabSU) { tabSU.style.background = 'transparent'; tabSU.style.color = 'var(--text-muted)'; }
    } else {
        if (signInForm) signInForm.style.display = 'none';
        if (signUpForm) signUpForm.style.display = 'block';
        if (tabSI) { tabSI.style.background = 'transparent'; tabSI.style.color = 'var(--text-muted)'; }
        if (tabSU) { tabSU.style.background = 'var(--accent)'; tabSU.style.color = '#fff'; }
    }
}

function handleEmailSignIn(e) {
    e.preventDefault();
    const email = document.getElementById('si-email').value.trim();
    const pass  = document.getElementById('si-pass').value;
    const errEl = document.getElementById('si-error');
    const acc = findAccount(email);
    if (!acc || acc.passHash !== simpleHash(pass)) {
        errEl.textContent = 'Invalid email or password. New here? Sign up above.';
        errEl.style.display = 'block';
        return;
    }
    errEl.style.display = 'none';
    const user = { email: acc.email, name: acc.name, role: acc.role };
    setSession(user);
    unlockApp(user);
}

function handleEmailSignUp(e) {
    e.preventDefault();
    const name  = document.getElementById('su-name').value.trim();
    const email = document.getElementById('su-email').value.trim();
    const pass  = document.getElementById('su-pass').value;
    const role  = document.getElementById('su-role').value;
    const errEl = document.getElementById('su-error');
    const okEl  = document.getElementById('su-success');
    if (findAccount(email)) {
        errEl.textContent = 'An account with this email already exists. Please sign in.';
        errEl.style.display = 'block'; okEl.style.display = 'none'; return;
    }
    errEl.style.display = 'none';
    saveAccount(email, simpleHash(pass), name, role);
    okEl.textContent = 'Account created! Signing you in...';
    okEl.style.display = 'block';
    setTimeout(function() {
        var user = { email: email.toLowerCase(), name: name, role: role };
        setSession(user);
        unlockApp(user);
    }, 800);
}

function triggerGoogleLogin() {
    var email = prompt('Enter your Google email address:');
    if (email && email.includes('@')) {
        var name = email.split('@')[0];
        var user = { email: email.toLowerCase(), name: name, picture: '' };
        if (!findAccount(email)) { saveAccount(email, simpleHash('google_sso'), name, ''); }
        setSession(user);
        unlockApp(user);
    }
}

// ── BOOTSTRAP ────────────────────────────────────────────────
window.addEventListener('load', function() {
    var session = getSession();
    if (session) {
        unlockApp(session);
    }
    loadUserData();
    initNav();
    updateProgress();
    // Open Pillar 1 nav by default
    var p1     = document.getElementById('nav-p1');
    var grp1   = document.getElementById('group-p1');
    if (p1)   p1.classList.add('open');
    if (grp1) grp1.classList.add('open');
    // Mark home btn active
    document.querySelectorAll('.nav-home-btn').forEach(b => b.classList.add('active'));
});
