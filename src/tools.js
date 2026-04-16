// ═══════════════════════════════════════════════════
// SMEMINDS PLAYBOOK — ALL INTERACTIVE TOOLS
// ═══════════════════════════════════════════════════

// ── TOOL 1: Fee Calculator ──────────────────────────
function calcFeeTool() {
    const price = parseFloat(document.getElementById('t1_price').value) || 0;
    const cat = parseFloat(document.getElementById('t1_cat').value) || 0.10;
    const ftype = document.getElementById('t1_type').value;
    const weight = parseFloat(document.getElementById('t1_weight').value) || 0;

    const refFee = Math.max(price * cat, 10);
    const closingFee = (ftype === 'self') ? 17 : (ftype === 'easy' ? 17 : 0);
    let fulfillFee = 0;
    const wSlabs = Math.ceil(weight / 500);

    if (ftype === 'fba') {
        const packFee = 20;
        const wFee = weight <= 500 ? 30 : weight <= 1000 ? 40 : weight <= 2000 ? 65 : 65 + (Math.ceil((weight - 2000) / 500) * 25);
        fulfillFee = packFee + wFee;
    } else if (ftype === 'easy') {
        fulfillFee = weight <= 500 ? 35 : weight <= 1000 ? 50 : weight <= 2000 ? 70 : 70 + (Math.ceil((weight - 2000) / 500) * 20);
    }

    const totalFee = refFee + closingFee + fulfillFee;
    const net = price - totalFee;
    const margin = price > 0 ? ((net / price) * 100).toFixed(1) : 0;
    const netColor = net > 0 ? 'var(--success)' : 'var(--danger, #e74c3c)';

    const el = document.getElementById('t1_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div class="res-row"><span>Referral Fee (${(cat*100).toFixed(1)}%):</span><span>₹${refFee.toFixed(2)}</span></div>
        <div class="res-row"><span>Closing Fee:</span><span>₹${closingFee.toFixed(2)}</span></div>
        <div class="res-row"><span>Fulfilment / Weight Fee:</span><span>₹${fulfillFee.toFixed(2)}</span></div>
        <div class="res-row" style="color:var(--warning);font-weight:700"><span>Total Amazon Fees:</span><span>₹${totalFee.toFixed(2)}</span></div>
        <div class="res-row" style="color:${netColor};font-weight:800;font-size:1.1em"><span>Net Proceeds:</span><span>₹${net.toFixed(2)} (${margin}% margin)</span></div>
        <div style="margin-top:12px;font-size:12px;color:var(--text-muted)">⚠️ Sample calculation only. Verify with official Amazon Fee Calculator.</div>`;
}

// ── TOOL 2: ACOS / TACOS Calculator ─────────────────
function calcAcosTool() {
    const spend = parseFloat(document.getElementById('t2_spend').value) || 0;
    const adRev = parseFloat(document.getElementById('t2_adrev').value) || 0;
    const totalRev = parseFloat(document.getElementById('t2_totalrev').value) || 0;
    const margin = parseFloat(document.getElementById('t2_margin').value) || 40;

    const acos = adRev > 0 ? (spend / adRev * 100) : 0;
    const tacos = totalRev > 0 ? (spend / totalRev * 100) : 0;
    const beAcos = margin;
    const roas = spend > 0 ? (adRev / spend).toFixed(2) : 0;

    let recColor = 'var(--success)', rec = '🚀 Scale Hard — ACOS is excellent';
    if (acos > beAcos) { recColor = 'var(--danger,#e74c3c)'; rec = '⚠️ Reduce Spend / Optimise — ACOS above break-even'; }
    else if (acos > beAcos * 0.75) { recColor = 'var(--warning)'; rec = '⚡ Maintain & Optimise — getting close to break-even'; }

    const el = document.getElementById('t2_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div class="res-row"><span>ACOS:</span><span style="font-weight:700">${acos.toFixed(1)}%</span></div>
        <div class="res-row"><span>TACOS:</span><span style="font-weight:700">${tacos.toFixed(1)}%</span></div>
        <div class="res-row"><span>Break-Even ACOS:</span><span>${beAcos.toFixed(1)}%</span></div>
        <div class="res-row"><span>ROAS:</span><span>${roas}×</span></div>
        <div class="res-row" style="color:${recColor};font-weight:700"><span>Recommendation:</span><span>${rec}</span></div>`;
}

// ── TOOL 3: Buy Box Probability ──────────────────────
function calcBuyBox() {
    const ful = parseInt(document.getElementById('bb_ful').value) || 2;
    const priceDiff = parseFloat(document.getElementById('bb_price').value) || 0;
    const rating = parseFloat(document.getElementById('bb_rating').value) || 4;
    const odr = parseFloat(document.getElementById('bb_odr').value) || 1;

    let score = 0;
    score += ful === 4 ? 40 : ful === 3 ? 30 : ful === 2 ? 20 : 10;
    score += priceDiff <= 0 ? 25 : priceDiff <= 3 ? 15 : priceDiff <= 5 ? 8 : 0;
    score += rating >= 4.5 ? 15 : rating >= 4.0 ? 10 : rating >= 3.5 ? 5 : 0;
    score += odr < 0.5 ? 10 : odr < 1 ? 7 : odr < 2 ? 3 : 0;
    const pct = Math.min(score, 98);

    let label = '🔴 Low — significant changes needed';
    let color = 'var(--danger,#e74c3c)';
    if (pct >= 80) { label = '🟢 High — strong Buy Box candidate'; color = 'var(--success)'; }
    else if (pct >= 55) { label = '🟡 Medium — improvements will help'; color = 'var(--warning)'; }

    const el = document.getElementById('bb_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div class="res-row"><span>Buy Box Win Probability:</span><span style="font-size:1.5em;font-weight:800;color:${color}">${pct}%</span></div>
        <div class="res-row" style="color:${color};font-weight:600"><span>Assessment:</span><span>${label}</span></div>
        <div style="margin-top:12px;font-size:13px;color:var(--text-muted)">Tip: Switch to FBA + match lowest price for maximum probability.</div>
        <div class="score-bar-wrap"><div class="score-bar" style="width:${pct}%;background:${color}"></div></div>`;
}

// ── TOOL 4: Pricing Simulator ────────────────────────
function calcPricing() {
    const mrp = parseFloat(document.getElementById('ps_mrp').value) || 0;
    const cogs = parseFloat(document.getElementById('ps_cogs').value) || 0;
    const feeRate = (parseFloat(document.getElementById('ps_fee').value) || 10) / 100;
    const targetMargin = (parseFloat(document.getElementById('ps_margin').value) || 20) / 100;

    const minSP = cogs / (1 - feeRate - targetMargin);
    const discount = mrp > 0 ? ((mrp - minSP) / mrp * 100) : 0;
    const actualMargin = minSP > 0 ? ((minSP - cogs - minSP * feeRate) / minSP * 100) : 0;
    const strikePct = mrp > 0 && minSP > 0 ? ((mrp - minSP) / mrp * 100).toFixed(0) : 0;

    const recommended = Math.ceil(minSP / 10) * 10 - 1;

    const el = document.getElementById('ps_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div class="res-row"><span>Minimum Selling Price (floor):</span><span style="font-weight:700">₹${minSP.toFixed(0)}</span></div>
        <div class="res-row"><span>Recommended Price (psychological):</span><span style="font-weight:700;color:var(--accent)">₹${recommended}</span></div>
        <div class="res-row"><span>Discount % shown to customer:</span><span style="color:var(--success);font-weight:700">${strikePct}% off</span></div>
        <div class="res-row"><span>Net Margin at Recommended Price:</span><span>${actualMargin.toFixed(1)}%</span></div>
        <div style="margin-top:12px;padding:12px;background:var(--accent-light);border-radius:8px;font-size:13px">
            💡 <strong>What the customer sees:</strong> <del>₹${mrp}</del> → <strong>₹${recommended}</strong> (${strikePct}% off)</div>`;
}

// ── TOOL 5: Error Code Lookup ────────────────────────
const ERROR_DB = {
    '8572': { title: 'GS1 UPC/Barcode Brand Mismatch', fix: 'The brand name registered with GS1 doesn\'t match your listing. Fix: Apply for GTIN Exemption via Seller Central → Catalogue → GTIN Exemption, OR update brand name to exactly match GS1 record.' },
    '8541': { title: 'Listing Data Conflict', fix: 'Another seller\'s data conflicts with your listing update. Fix: Use "Suggest an Update" on the ASIN detail page, or open a Seller Support case with your evidence.' },
    '8006': { title: 'Invalid Browse Node', fix: 'The browse node ID is deprecated or doesn\'t exist. Fix: Use the Product Classifier Tool in Seller Central to find the correct active node for your product type.' },
    '5461': { title: 'Missing Mandatory Attribute', fix: 'A required column in your flat file is empty. Fix: Download the error report → identify which column is missing → fill it → re-upload only the affected rows.' },
    '8565': { title: 'Blocked / Restricted ASIN', fix: 'This product requires category approval in your account. Fix: Apply for Category Approval via Seller Central → Performance → Selling Applications.' },
    '8200': { title: 'GTIN Validation Failed', fix: 'Barcode is not registered in GS1 database. Fix: Register your barcode with GS1 India (gs1india.org) OR apply for a GTIN Exemption if you are the brand manufacturer.' },
    '8558': { title: 'Main Image Rejected', fix: 'Main image does not meet requirements. Fix: Ensure background is pure white (RGB 255,255,255), resolution ≥1000×1000px, product fills 85%+ of frame, no text/logos/watermarks.' },
    '99010': { title: 'Listing Suppressed — Condition Restriction', fix: 'Product description violates condition guidelines. Fix: Review category-specific condition requirements; ensure condition description matches actual product condition exactly.' },
    '8026': { title: 'Restricted Product', fix: 'Product is in a restricted category. Fix: Check Amazon\'s Restricted Products policy. Apply for selling approval or remove the listing if product is prohibited.' },
    'image': { title: 'Image-Related Errors', fix: 'Check: (1) Main image background = pure white RGB 255,255,255. (2) Resolution ≥1000×1000px. (3) No text, logos, or watermarks on MAIN. (4) Product fills 85%+ of frame. (5) File size < 10MB.' },
    'barcode': { title: 'Barcode / GTIN Errors', fix: 'Common fixes: (1) Apply for GTIN Exemption if you are the brand manufacturer. (2) Register barcode with GS1 India. (3) Ensure brand name in listing exactly matches GS1 record (error 8572).' },
    'node': { title: 'Browse Node Errors', fix: 'Use the Product Classifier Tool or Browse Tree Guide (BTG) to find the correct node. Always use the deepest/most specific leaf node. Never assign a parent category node.' },
    'suppressed': { title: 'Listing Suppression', fix: 'Check Listing Quality Report. Common causes: (1) Missing/non-compliant main image. (2) Missing mandatory attributes. (3) Restricted content in title/bullets. Fix each flag shown in the report.' }
};

function lookupError() {
    const q = document.getElementById('err_input').value.trim().toLowerCase();
    const el = document.getElementById('err_res');
    if (!q) { el.innerHTML = '<p style="color:var(--text-muted)">Type an error code or keyword above.</p>'; return; }

    let found = null;
    for (const [key, val] of Object.entries(ERROR_DB)) {
        if (q === key || q.includes(key) || key.includes(q)) { found = val; break; }
    }

    if (found) {
        el.innerHTML = `<div style="margin-bottom:8px"><strong style="color:var(--primary)">${found.title}</strong></div><p style="font-size:14px;color:var(--text-dark)">${found.fix}</p>`;
    } else {
        el.innerHTML = `<p style="color:var(--text-muted)">No match found for "<strong>${q}</strong>". Try searching: 8572, 8541, 8006, 5461, 8565, 8200, 8558, image, barcode, node, suppressed.</p>`;
    }
}

// ── TOOL 6: OOS / Reorder Point ─────────────────────
function calcOOS() {
    const velocity = parseFloat(document.getElementById('oos_velocity').value) || 0;
    const lead = parseFloat(document.getElementById('oos_lead').value) || 0;
    const buffer = parseFloat(document.getElementById('oos_buffer').value) || 7;
    const current = parseFloat(document.getElementById('oos_stock').value) || 0;

    const reorderPt = Math.ceil(velocity * lead);
    const safetyStock = Math.ceil(velocity * buffer);
    const maxStock = reorderPt + safetyStock + Math.ceil(velocity * 30);
    const daysRemaining = velocity > 0 ? Math.floor(current / velocity) : 999;
    const orderNow = current <= reorderPt;

    let riskColor = 'var(--success)', riskLabel = '🟢 Low Risk — stock levels healthy';
    if (orderNow && daysRemaining < lead) { riskColor = 'var(--danger,#e74c3c)'; riskLabel = '🔴 CRITICAL — OOS imminent, order immediately!'; }
    else if (orderNow) { riskColor = 'var(--warning)'; riskLabel = '🟡 Medium Risk — reorder point reached, place order now'; }

    const el = document.getElementById('oos_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div class="res-row"><span>Reorder Point:</span><span style="font-weight:700">${reorderPt} units</span></div>
        <div class="res-row"><span>Safety Stock:</span><span>${safetyStock} units</span></div>
        <div class="res-row"><span>Days of Cover (current stock):</span><span style="font-weight:700">${daysRemaining} days</span></div>
        <div class="res-row"><span>Recommended Max Stock:</span><span>${maxStock} units</span></div>
        <div class="res-row" style="color:${riskColor};font-weight:700"><span>Risk Status:</span><span>${riskLabel}</span></div>`;
}

// ── TOOL 7: Deal ROI Calculator ──────────────────────
function calcDealRoi() {
    const regular = parseFloat(document.getElementById('deal_regular').value) || 0;
    const deal = parseFloat(document.getElementById('deal_price').value) || 0;
    const units = parseFloat(document.getElementById('deal_units').value) || 0;
    const fee = parseFloat(document.getElementById('deal_fee').value) || 0;
    const cogs = parseFloat(document.getElementById('deal_cogs').value) || 0;

    const revenue = deal * units;
    const totalCogs = cogs * units;
    const grossProfit = revenue - totalCogs - fee;
    const roi = fee + totalCogs > 0 ? ((grossProfit / (fee + totalCogs)) * 100) : 0;
    const discountPct = regular > 0 ? ((regular - deal) / regular * 100).toFixed(1) : 0;
    const breakEvenUnits = deal > cogs ? Math.ceil(fee / (deal - cogs)) : 'N/A';
    const goNogo = grossProfit > 0 ? '🟢 GO — Deal is profitable' : '🔴 NO-GO — Deal loses money at this price/volume';

    const el = document.getElementById('deal_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div class="res-row"><span>Deal Discount:</span><span>${discountPct}% off</span></div>
        <div class="res-row"><span>Deal Revenue:</span><span>₹${revenue.toLocaleString('en-IN')}</span></div>
        <div class="res-row"><span>Total COGS:</span><span>₹${totalCogs.toLocaleString('en-IN')}</span></div>
        <div class="res-row"><span>Deal Fee:</span><span>₹${fee.toLocaleString('en-IN')}</span></div>
        <div class="res-row" style="font-weight:700"><span>Gross Profit:</span><span style="color:${grossProfit>0?'var(--success)':'var(--danger,#e74c3c)'}">₹${grossProfit.toLocaleString('en-IN')}</span></div>
        <div class="res-row"><span>Break-Even Units:</span><span>${breakEvenUnits}</span></div>
        <div class="res-row" style="font-weight:700"><span>Decision:</span><span>${goNogo}</span></div>`;
}

// ── TOOL 8: ASIN Health Score ────────────────────────
function calcAsinHealth() {
    const titleLen = parseInt(document.getElementById('ah_title').value) || 0;
    const bullets = parseInt(document.getElementById('ah_bullets').value) || 0;
    const images = parseInt(document.getElementById('ah_images').value) || 0;
    const aplus = parseInt(document.getElementById('ah_aplus').value) || 0;
    const terms = parseInt(document.getElementById('ah_terms').value) || 0;
    const video = parseInt(document.getElementById('ah_video').value) || 0;

    let score = 0;
    const issues = [];
    const tips = [];

    // Title
    if (titleLen >= 50 && titleLen <= 100) { score += 20; }
    else if (titleLen >= 30 && titleLen < 50) { score += 10; issues.push('Title is too short (under 50 chars)'); }
    else if (titleLen > 100) { score += 10; issues.push('Title is too long (over 100 chars)'); }
    else { issues.push('Title is critically short — add brand, model, key features'); }

    // Bullets
    if (bullets >= 5) { score += 20; }
    else if (bullets >= 3) { score += 12; tips.push('Add more bullets — aim for 5 (max impact)'); }
    else { score += 5; issues.push('Fewer than 3 bullets — add bullet points immediately'); }

    // Images
    if (images >= 7) { score += 20; }
    else if (images >= 4) { score += 12; tips.push('Add more images — fill all 9 slots for best results'); }
    else { score += 5; issues.push('Too few images — minimum 3–5 required'); }

    // A+
    if (aplus) { score += 20; }
    else { score += 5; issues.push('No A+ Content — add it for 3–10% conversion lift'); }

    // Search Terms
    if (terms) { score += 10; }
    else { issues.push('Search Terms field empty — fill it with relevant keywords'); }

    // Video
    if (video) { score += 10; }
    else { tips.push('Add a product video — increases conversion by up to 9%'); }

    const grade = score >= 90 ? 'A' : score >= 75 ? 'B' : score >= 60 ? 'C' : score >= 45 ? 'D' : 'F';
    const color = score >= 75 ? 'var(--success)' : score >= 50 ? 'var(--warning)' : 'var(--danger,#e74c3c)';

    const el = document.getElementById('ah_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div style="text-align:center;margin-bottom:16px">
            <div style="font-size:3rem;font-weight:800;color:${color}">${score}/100</div>
            <div style="font-size:1.5rem;font-weight:700;color:${color}">Grade: ${grade}</div>
        </div>
        ${issues.length ? `<div style="margin-bottom:12px"><strong style="color:var(--danger,#e74c3c)">Issues to Fix:</strong><ul style="margin-top:8px">${issues.map(i=>`<li style="color:#c0392b;font-size:13px;margin-bottom:4px">❌ ${i}</li>`).join('')}</ul></div>` : ''}
        ${tips.length ? `<div><strong style="color:var(--warning)">Improvements:</strong><ul style="margin-top:8px">${tips.map(t=>`<li style="color:var(--warning);font-size:13px;margin-bottom:4px">💡 ${t}</li>`).join('')}</ul></div>` : ''}
        ${score >= 90 ? '<div style="color:var(--success);font-weight:700;margin-top:8px">🌟 Excellent! This listing is fully optimised.</div>' : ''}`;
}

// ── TOOL 9: Image Compliance Checker ────────────────
function checkImageCompliance() {
    const w = parseInt(document.getElementById('img_w').value) || 0;
    const h = parseInt(document.getElementById('img_h').value) || 0;
    const type = document.getElementById('img_type').value;
    const bg = parseInt(document.getElementById('img_bg').value);

    const checks = [];
    let pass = true;

    if (Math.max(w, h) >= 2000) checks.push({ ok: true, msg: 'Resolution ≥2000px — Zoom feature active ✓' });
    else if (Math.max(w, h) >= 1000) checks.push({ ok: true, msg: 'Resolution ≥1000px — minimum requirement met ✓' });
    else { checks.push({ ok: false, msg: `Resolution ${Math.max(w,h)}px — FAIL: minimum 1000px required` }); pass = false; }

    if (type === 'main') {
        if (bg === 1) checks.push({ ok: true, msg: 'Background is pure white ✓' });
        else { checks.push({ ok: false, msg: 'FAIL: MAIN image must have pure white (RGB 255,255,255) background' }); pass = false; }
    } else {
        checks.push({ ok: true, msg: 'Additional image — no background restriction ✓' });
    }

    const el = document.getElementById('img_res');
    el.style.display = 'block';
    el.innerHTML = `
        <div style="margin-bottom:12px;font-weight:700;font-size:1.1em;color:${pass?'var(--success)':'var(--danger,#e74c3c)'}">
            ${pass ? '✅ COMPLIANT — Image meets Amazon requirements' : '❌ NON-COMPLIANT — Fix required before uploading'}</div>
        ${checks.map(c => `<div style="padding:6px 0;border-bottom:1px solid var(--border);font-size:13px;color:${c.ok?'var(--success)':'var(--danger,#e74c3c)'}">
            ${c.ok?'✅':'❌'} ${c.msg}</div>`).join('')}`;
}

// ── TOOL: Title Counter ──────────────────────────────
function checkTitle() {
    const val = document.getElementById('tcc_input').value;
    const len = val.length;
    let color = 'var(--success)', msg = 'Perfect length ✓';
    if (len < 30) { color = 'var(--danger,#e74c3c)'; msg = 'Too short — add brand name, model, key features'; }
    else if (len < 50) { color = 'var(--warning)'; msg = 'A bit short — try to reach 50–100 characters'; }
    else if (len > 100 && len <= 150) { color = 'var(--warning)'; msg = 'Getting long — Amazon recommends under 100 chars'; }
    else if (len > 150) { color = 'var(--danger,#e74c3c)'; msg = 'Too long — risk of truncation and suppression'; }

    const hasAllCaps = /\b[A-Z]{4,}\b/.test(val);
    const hasClaims = /(best|#1|world'?s|greatest|cheapest|amazing)/i.test(val);
    const warnings = [];
    if (hasAllCaps) warnings.push('⚠️ Contains ALL CAPS words — not allowed in titles');
    if (hasClaims) warnings.push('⚠️ Contains subjective claims (Best, #1, etc.) — not allowed');

    const el = document.getElementById('tcc_res');
    el.innerHTML = `
        <div style="font-size:2em;font-weight:800;color:${color}">${len} chars</div>
        <div style="color:${color};font-weight:600;margin-bottom:8px">${msg}</div>
        <div style="background:var(--border);border-radius:8px;height:8px;overflow:hidden">
            <div style="height:100%;width:${Math.min(len,150)/150*100}%;background:${color};transition:width 0.3s"></div>
        </div>
        <div style="display:flex;justify-content:space-between;font-size:11px;color:var(--text-muted);margin-top:4px"><span>0</span><span>50 (min)</span><span>100 (ideal max)</span><span>150</span></div>
        ${warnings.length ? `<div style="margin-top:12px">${warnings.map(w=>`<div style="color:var(--warning);font-size:13px;padding:4px 0">${w}</div>`).join('')}</div>` : ''}`;
}

// ── Accordion Toggle ─────────────────────────────────
function toggleAcc(el) {
    const body = el.nextElementSibling;
    const isOpen = body.style.display === 'block';
    body.style.display = isOpen ? 'none' : 'block';
    el.innerHTML = el.innerHTML.replace(isOpen ? '▲' : '▼', isOpen ? '▼' : '▲');
}
