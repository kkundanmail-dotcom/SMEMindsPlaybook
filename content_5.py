# ══════════════════════════════════════════════════════════════
# PILLAR 5 — SPEED  (4 Modules)
# ══════════════════════════════════════════════════════════════

pillar5_modules = [

{
    "id": "5.1",
    "number": "Module 5.1",
    "title": "FBA Management",
    "difficulty": "Intermediate",
    "time": "45 mins",
    "overview": """<p>Fulfilled by Amazon (FBA) is the single most powerful operational decision an Amazon India seller can make — it unlocks Prime badge, Buy Box preference, and Amazon's world-class logistics. This module covers FBA enrollment, inbound shipment SOP, IPI monitoring, LTSF avoidance (charges apply from 180+ days), removal orders, and profitability calculation.</p>""",
    "content": """
        <h3>1. FBA Enrollment Eligibility & Fee Analysis</h3>
        <div class='callout pro-tip'>
            <div><strong>FBA Eligibility Check:</strong><br>
            ✓ ASIN not on FBA restricted list<br>
            ✓ Product weight + dimensions meet FBA limits<br>
            ✓ Product is non-hazmat (or enrolled in FBA Hazmat programme for eligible items)<br>
            ✓ Net profit after FBA fees is positive<br><br>
            <strong>Enroll here:</strong> <a class='btn-sc' href='https://sellercentral.amazon.in/fba/enrollment/index.html' target='_blank'>FBA Enrollment</a><br>
            <strong>FBA Training:</strong> <a class='btn-sc' href='https://sell.amazon.in/seller-university/fba' target='_blank'>FBA Seller University</a></div>
        </div>
        <table class='data-table'>
            <thead><tr><th>Fee Type</th><th>Basis</th><th>Rate (India)</th></tr></thead>
            <tbody>
                <tr><td>Referral fee</td><td>% of selling price (5–15% by category)</td><td>Varies — check SC Fee Schedule</td></tr>
                <tr><td>FBA fulfilment fee</td><td>Weight + size tier</td><td>Per ASIN via FBA Calculator</td></tr>
                <tr><td>Monthly storage fee</td><td>Volume × monthly rate</td><td>₹38/cubic foot (standard)</td></tr>
                <tr><td>LTSF (6–12 months)</td><td>Units stored 180–365 days</td><td>₹425/cubic foot/month</td></tr>
                <tr><td>LTSF (12+ months)</td><td>Units stored &gt;365 days</td><td>₹850/cubic foot/month</td></tr>
            </tbody>
        </table>

        <h3>2. FBA Inbound Shipment Creation SOP (Bulk Flat File Method)</h3>
        <ol>
            <li>SC → Inventory → Manage FBA Shipments → Upload Shipping Plan File</li>
            <li>Download the shipping plan template; fill product details; save as Tab-Delimited Text (.txt)</li>
            <li>Upload completed flat file — converts your SKUs to FNSKU format automatically</li>
            <li>Generate and print FNSKU labels: SC → Manage FBA Inventory → Print Item Labels</li>
            <li>Prepare MRP label per Legal Metrology Act (product name, quantity, MRP incl. taxes, manufacturer address, country of origin)</li>
            <li>Attach STN (Stock Transfer Note) / Tax Invoice with each shipment — FC will reject without it</li>
            <li>Book FC appointment via FCAS (FC Appointment System) before dispatching</li>
            <li>Track via: <a class='btn-sc' href='https://sellercentral.amazon.in/gp/fba/inbound-shipment-workflow/index.html' target='_blank'>Manage FBA Shipments</a></li>
            <li>Reconcile every shipment within 30 days of close — file discrepancy case within 9 months if units are missing</li>
        </ol>
        <div class='callout pro-tip'>
            <div><strong>Restock+ Programme:</strong> Follow Amazon's restock recommendations and ship within 14 days of recommended ship date (7 days for ATS shipments) to earn zero storage fees, guaranteed storage, and free removals via Seller Reward Credits.<br><br>
            Configure restock settings: Reorder Frequency (default 8 weeks), Supplier Lead Time, MOQ, and Coverage Period (recommend 4-week start).<br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/restockinventory/suggestions' target='_blank'>Restock Inventory Dashboard</a></div>
        </div>

        <h3>3. Inventory Performance Index (IPI)</h3>
        <div class='callout success'>
            <div><strong>IPI Score — Target &gt;400 (hard operational threshold):</strong><br>
            IPI is a composite score of: excess inventory ratio, stranded inventory %, FBA sell-through rate, and in-stock rate.<br><br>
            <strong>IPI &lt;400 → Amazon restricts your FBA storage limits</strong> — you cannot send new inventory until score improves. This is a critical constraint during peak seasons (GIF, Prime Day).<br><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/inventory-performance/dashboard' target='_blank'>IPI Dashboard</a></div>
        </div>
        <table class='data-table'>
            <thead><tr><th>IPI Driver</th><th>Threshold</th><th>Improvement Action</th></tr></thead>
            <tbody>
                <tr><td>Excess inventory</td><td>&gt;90 days cover</td><td>Create Lightning Deal or Coupon to sell down</td></tr>
                <tr><td>Stranded inventory</td><td>Any stranded units</td><td>Relist via SC → Fix Stranded Inventory</td></tr>
                <tr><td>Low sell-through rate</td><td>&lt;5% weekly</td><td>Increase PPC, improve listing, reduce price</td></tr>
                <tr><td>In-stock rate</td><td>&lt;80%</td><td>Improve restock forecasting; use Restock+ recommendations</td></tr>
            </tbody>
        </table>

        <h3>4. Long-Term Storage Fee (LTSF) Avoidance</h3>
        <div class='callout warning'>
            <div><strong>LTSF is charged on the last day of EVERY month</strong> (not just Feb/Aug anymore):<br>
            • 6–12 months: ₹425/cubic foot<br>
            • 12+ months: ₹850/cubic foot<br>
            • One unit of any ASIN is EXEMPT if at least one unit of that ASIN has been at the FC for &lt;6 months<br>
            • FIFO (First In, First Out) basis — oldest units charged first<br><br>
            <strong>Enable Automated Long-Term Storage Removals:</strong> Settings → Fulfilment by Amazon → Automated Long-Term Storage Removals → Enable<br><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/reportcentral/LTSF/1' target='_blank'>LTSF Report</a>
            &nbsp;<a class='btn-sc' href='https://sellercentral.amazon.in/inventoryplanning/manageinventoryhealth' target='_blank'>Manage Inventory Health</a></div>
        </div>
        <table class='data-table'>
            <thead><tr><th>LTSF Prevention Strategy</th><th>When to Use</th><th>Expected Outcome</th></tr></thead>
            <tbody>
                <tr><td>Lightning Deal / Coupon on aged stock</td><td>60–90 days before LTSF threshold</td><td>Fastest velocity boost — clear in 7–14 days</td></tr>
                <tr><td>Recommended Removal Report</td><td>Week 3 of each month</td><td>Pre-populated removal order for LTSF-eligible units</td></tr>
                <tr><td>FBA Removal Order</td><td>When LTSF &gt; removal fee + resell value</td><td>Recover 100% of stock to resell via other channel</td></tr>
                <tr><td>FBA Liquidations</td><td>Bulk aged stock with low unit value</td><td>Recover 5–40% of unit value; avoid LTSF entirely</td></tr>
                <tr><td>Automated LTSF Removal (enabled in settings)</td><td>Always-on safety net</td><td>Auto-removes inventory before LTSF triggers</td></tr>
            </tbody>
        </table>

        <h3>5. FBA Grade &amp; Resell / Liquidations</h3>
        <table class='data-table'>
            <thead><tr><th>Option</th><th>Recovery Rate</th><th>Best For</th></tr></thead>
            <tbody>
                <tr><td>Grade &amp; Resell</td><td>Customer prices (Amazon grades and relists)</td><td>Returned electronics, appliances</td></tr>
                <tr><td>FBA Liquidations</td><td>5–40% of unit value</td><td>Bulk excess clearance when LTSF imminent</td></tr>
                <tr><td>Removal Order (Return)</td><td>100% recovery — you resell via other channel</td><td>High-value products; resell offline</td></tr>
                <tr><td>Removal Order (Dispose)</td><td>Zero recovery — cheapest option</td><td>Damaged/expired low-value items</td></tr>
            </tbody>
        </table>

        <h3>6. FBA Reimbursements — Recovering Lost/Damaged Inventory</h3>
        <ul>
            <li>Amazon FCs occasionally receive fewer units than sent, or damage inventory in storage/transit</li>
            <li><strong>Window to file:</strong> Within 9 months of shipment creation — do not miss this deadline</li>
            <li><strong>Path:</strong> SC → Inventory → Shipments → Select shipment → Report Problem</li>
            <li><strong>Evidence needed:</strong> Supplier invoice, packing list with quantities, courier tracking</li>
            <li>Use the Inventory Reconciliation Report and Inventory Adjustments Report to identify all discrepancies</li>
            <li>Amazon reimburses at average selling price if discrepancy is confirmed as Amazon's fault</li>
            <li><strong>Best practice:</strong> Reconcile every shipment within 30 days of "shipment closed" status</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill-sc' href='https://sellercentral.amazon.in/fba/enrollment/index.html' target='_blank'>FBA Enrollment</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/inventory-performance/dashboard' target='_blank'>IPI Dashboard</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/reportcentral/LTSF/1' target='_blank'>LTSF Report</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/inventoryplanning/manageinventoryhealth' target='_blank'>Inventory Health</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/restockinventory/suggestions' target='_blank'>Restock Dashboard</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/inventory?viewId=STRANDED' target='_blank'>Stranded Inventory</a>
            <a class='pill-sc' href='https://sell.amazon.in/seller-university/fba' target='_blank'>FBA Training</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Sellers are shocked to find thousands of rupees deducted from their account as LTSF charges. "I had no idea my products had been sitting in the warehouse for so long — by the time I noticed, it was too late to remove them before the last day of the month."</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Enable Automated Long-Term Storage Removals in FBA Settings immediately. Then set a weekly calendar reminder to review the Inventory Age View for units approaching 180 days. Download the Recommended Removal Report in week 3 of each month and action every flagged ASIN — either run a Lightning Deal to sell through or create a removal order before the last day of the month.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>IPI score above 400 is not just a metric — it is your FBA storage access card. Sellers who maintain IPI &gt;550 consistently unlock expanded storage limits and are never storage-constrained during peak events like Prime Day and Great Indian Festival. Treat IPI like a weekly KPI: review excess inventory, clear stranded stock every Monday, and keep sell-through rate healthy year-round.</p></div>
            </div>
        </div>
    """,
    "process_flow": """
        <div class='svg-wrapper'>
            <svg viewBox="0 0 900 120" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
                <defs><marker id="arr_s1" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#1e3a5f"/></marker></defs>
                <text x="450" y="65" class="svg-watermark" transform="rotate(-12,450,65)">© SMEMinds | smeminds.com</text>
                <rect x="10"  y="35" width="120" height="50" rx="8" class="flow-step"/><text x="70"  y="62" class="flow-text">Enrol</text><text x="70"  y="76" class="flow-text">ASIN in FBA</text>
                <line x1="130" y1="60" x2="160" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_s1)"/>
                <rect x="160" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="220" y="62" class="flow-text">Create</text><text x="220" y="76" class="flow-text">Shipment</text>
                <line x1="280" y1="60" x2="310" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_s1)"/>
                <rect x="310" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="370" y="62" class="flow-text">Label &amp;</text><text x="370" y="76" class="flow-text">Pack + STN</text>
                <line x1="430" y1="60" x2="460" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_s1)"/>
                <rect x="460" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="520" y="62" class="flow-text">FC Check-in</text><text x="520" y="76" class="flow-text">Confirmed</text>
                <line x1="580" y1="60" x2="610" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_s1)"/>
                <rect x="610" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="670" y="62" class="flow-text">Monitor IPI</text><text x="670" y="76" class="flow-text">&amp; LTSF</text>
                <line x1="730" y1="60" x2="760" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_s1)"/>
                <rect x="760" y="35" width="120" height="50" rx="8" class="flow-step" style="fill:#ff6b35;"/><text x="820" y="62" class="flow-text" style="fill:#fff">Restock</text><text x="820" y="76" class="flow-text" style="fill:#fff">in Time</text>
            </svg>
        </div>
    """,
    "tools": "",
    "videos": [],
    "checklist": [
        "FBA fee calculated and margin positive for all FBA-enrolled ASINs",
        "Inbound shipment SOP documented and followed by operations team",
        "IPI score &gt;400 maintained",
        "Stranded inventory = 0 (weekly check)",
        "Aged inventory (&gt;150 days) actioned before LTSF charges",
        "Automated LTSF removal enabled in FBA Settings",
        "Every shipment reconciled within 30 days of close",
        "FBA Calculator run on every new ASIN before launch"
    ],
    "quiz": [
        {
            "question": "What happens if your IPI score falls below 400?",
            "options": [
                "Amazon removes your FBA privileges",
                "Amazon restricts your FBA storage limits",
                "FBA fees increase by 50%",
                "Your listings are suppressed"
            ],
            "answer": "Amazon restricts your FBA storage limits",
            "explanation": "An IPI score below 400 triggers Amazon to restrict your FBA storage limit, preventing you from sending new inventory — a critical constraint during peak sales periods."
        },
        {
            "question": "What is the fastest way to clear aged FBA inventory before long-term storage fees?",
            "options": [
                "Increase the selling price",
                "Create a Lightning Deal or Coupon on the aged ASIN",
                "File a removal order immediately",
                "Pause all advertising"
            ],
            "answer": "Create a Lightning Deal or Coupon on the aged ASIN",
            "explanation": "Lightning Deals and Coupons provide the fastest velocity boost to clear stock. FBA Removal is the backup if the deal doesn't move enough units in time."
        }
    ]
},

{
    "id": "5.2",
    "number": "Module 5.2",
    "title": "FBM & Easy Ship",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": """<p>Fulfilled by Merchant (FBM) and Amazon Easy Ship give sellers fulfilment flexibility, especially for heavy/bulky items or products requiring special handling. This module covers Easy Ship SLA compliance, Easy Ship Guaranteed Delivery (GD) and Seller Fulfilled Prime (SFP) eligibility, Seller Flex setup, and the critical performance metrics sellers must maintain to avoid account action.</p>""",
    "content": """
        <h3>1. Easy Ship Overview & Order Management</h3>
        <div class='callout pro-tip'>
            <div><strong>Amazon Easy Ship:</strong> Amazon's courier picks up from your doorstep and delivers to the customer. You pack and label — Amazon ships.<br><br>
            <strong>Benefits:</strong><br>
            • Amazon-badged logistics — customer trusts the delivery<br>
            • Trackable with Amazon tracking system<br>
            • No carrier negotiation needed<br>
            • Prime eligibility possible via Easy Ship Guaranteed Delivery → Seller Fulfilled Prime pathway<br><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/gp/ssof/shipping-queue.html' target='_blank'>Easy Ship Orders Queue</a></div>
        </div>

        <h3>2. Easy Ship Guaranteed Delivery (GD) Programme</h3>
        <div class='callout success'>
            <div><strong>GD Programme — Eligibility Requirements:</strong><br>
            ✓ Active Easy Ship seller with clean performance metrics<br>
            ✓ Your pick-up pin code covered under GD locations<br>
            ✓ Minimum 30 Easy Ship orders/month<br>
            ✓ Late Dispatch Rate ≤ 1.5%<br>
            ✓ Cancellation Rate ≤ 1.5%<br>
            ✓ Package limits: max 50cm × 35cm × 30cm, weight ≤ 9 kg<br><br>
            <strong>Only ONE pickup slot for GD orders: 1:00 PM – 4:00 PM daily</strong><br>
            Order cutoff: 12:00 PM same day. Schedule pickup by 12:45 PM.<br>
            Sundays are excluded from ESD (Estimated Ship Date) calculations.</div>
        </div>
        <table class='data-table'>
            <thead><tr><th>Order Time</th><th>Pickup Window</th><th>Action Required</th></tr></thead>
            <tbody>
                <tr><td>1DD / 2DD orders by 12:00 PM</td><td>1:00 PM – 4:00 PM same day</td><td>Schedule pickup by 12:45 PM; pack &amp; ready by 1 PM</td></tr>
                <tr><td>Standard Easy Ship orders</td><td>Multiple slots as per Amazon</td><td>Mark ready as per pickup slot confirmation</td></tr>
                <tr><td>After Saturday 12:00 PM</td><td>Monday (Sunday excluded)</td><td>ESD automatically set to Monday by Amazon</td></tr>
            </tbody>
        </table>

        <h3>3. Seller Fulfilled Prime (SFP / Easy Ship Prime)</h3>
        <div class='callout warning'>
            <div><strong>SFP Eligibility (Stricter than GD):</strong><br>
            • Must complete 30 days in GD Programme first with at least 1 GD order fulfilled<br>
            • LDR ≤ 1.0% and Cancellation Rate ≤ 1.0% for BOTH standard and GD orders<br>
            • Free shipping must be offered on all SKUs in the GD programme<br>
            • All orders must ship same-day or next-day<br><br>
            <strong>Prime badge benefit:</strong> Significantly boosts CTR, Buy Box win rate, and search ranking.<br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/seller-fulfilled-prime/registration/index.html' target='_blank'>Apply for Seller Fulfilled Prime</a></div>
        </div>

        <h3>4. Seller Flex — Your Own Warehouse as Prime FC</h3>
        <ul>
            <li><strong>What it is:</strong> Your warehouse operates as an Amazon-integrated Flex Site with Prime eligibility</li>
            <li><strong>IT requirements:</strong> Laptop (min 2 GB RAM), barcode scanner, Zebra label printer, dedicated broadband &gt;4 Mbps with backup link from different ISP</li>
            <li><strong>Performance thresholds (strict):</strong> Cancellation Rate &lt;0.05%, Late Shipment Rate &lt;0.05%, Late Handover &lt;0.05%</li>
            <li><strong>Order processing deadline:</strong> All orders must be processed before CPT (2 PM cutoff)</li>
            <li>Manage via: <a class='btn-sc' href='https://sellerflex.amazon.in' target='_blank'>Seller Flex Portal</a></li>
        </ul>

        <h3>5. FBM Performance Metrics — Account Health Thresholds</h3>
        <div class='callout warning'>
            <div><strong>Critical FBM Metrics:</strong><br>
            • <strong>Order Defect Rate (ODR):</strong> Target &lt;1% | Suspension: &gt;1%<br>
            • <strong>Late Dispatch Rate (LDR):</strong> Target &lt;4% | Alert: &gt;4% | Suspension: &gt;8%<br>
            • <strong>Pre-Fulfillment Cancellation Rate:</strong> Target &lt;2.5% | Suspension: &gt;5%<br>
            • <strong>Valid Tracking Rate (VTR):</strong> Target &gt;95% | Alert: &lt;90%<br>
            • <strong>Easy Ship GD Programme LDR:</strong> Target ≤ 1.5% (standard) / ≤ 1.0% (SFP)</div>
        </div>

        <h3>6. Self-Ship (MFN) Carrier Selection</h3>
        <ul>
            <li><strong>Tier-1 cities:</strong> Delhivery, Bluedart, DTDC — 1–2 day delivery</li>
            <li><strong>Tier-2/3 cities:</strong> India Post, Ekart — reliable but slower</li>
            <li><strong>Negotiation leverage:</strong> Volume commitments (500+ shipments/month) unlock 20–40% rate discounts</li>
            <li>Always use carriers that provide real-time tracking (impacts VTR metric)</li>
        </ul>

        <h3>7. Customer Return SOP for FBM</h3>
        <ol>
            <li>Receive return request in SC → Orders → Manage Returns</li>
            <li>Approve within 24 hours</li>
            <li>Issue pre-paid return label (Amazon Logistics or self-arranged)</li>
            <li>Process refund within 2 days of receiving returned item</li>
            <li>Inspect returned item — categorise as: Resellable / Damaged / Defective</li>
        </ol>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill-sc' href='https://sellercentral.amazon.in/gp/ssof/shipping-queue.html' target='_blank'>Easy Ship Orders</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/seller-fulfilled-prime/registration/index.html' target='_blank'>SFP Registration</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/account-health' target='_blank'>Account Health</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/returns/list' target='_blank'>Manage Returns</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Easy Ship sellers miss the GD programme pickup deadline — orders are not packed and marked ready by 12:45 PM, causing Late Dispatch Rate to spike above 1.5%, disqualifying them from the Guaranteed Delivery programme and losing the Prime badge eligibility pathway.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Set internal alerts at 11:30 AM to trigger order packing. Pre-pack all expected orders the previous evening for next-day delivery. For SKUs with stock shortages, opt them out of GD immediately via email to ez-guaranteed-delivery@amazon.com (include ASIN and SKU ID) to protect your LDR. Monitor LDR daily in Seller Central Account Health dashboard.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>The Easy Ship Prime pathway (GD Programme → SFP) is one of the most underutilised growth levers for FBM sellers in India. Sellers with Prime badge on Easy Ship listings typically see 20–35% higher conversion rates vs. non-Prime FBM. The 30-day qualification period is a short investment for a long-term competitive advantage — especially for heavy or bulky products that cannot go to FBA.</p></div>
            </div>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Easy Ship GD pickup scheduled daily — orders packed and ready by 12:45 PM",
        "Late Dispatch Rate &lt;1.5% for GD programme; &lt;4% for standard Easy Ship",
        "Cancellation Rate &lt;1.5% for GD; &lt;2.5% for standard FBM",
        "Valid Tracking Rate &gt;95%",
        "All FBM returns processed within 24 hours of request",
        "GD programme eligibility reviewed — SFP application submitted after 30 days qualifying",
        "ODR &lt;1% — checked weekly"
    ],
    "quiz": [
        {
            "question": "What is the maximum allowed Late Dispatch Rate before account suspension?",
            "options": ["2.5%", "4%", "8%", "10%"],
            "answer": "8%",
            "explanation": "Amazon alerts at &gt;4% LDR and can suspend the account at &gt;8% LDR. The target is &lt;4% consistently. Any single week above 8% puts the account at severe risk."
        },
        {
            "question": "What must you complete before applying for Seller Fulfilled Prime (Easy Ship Prime)?",
            "options": [
                "Send 100 Easy Ship orders in a week",
                "Complete 30 days in Easy Ship Guaranteed Delivery Programme with at least 1 GD order",
                "Enrol in FBA for at least 6 months",
                "Achieve ODR below 0.5%"
            ],
            "answer": "Complete 30 days in Easy Ship Guaranteed Delivery Programme with at least 1 GD order",
            "explanation": "SFP eligibility requires completing 30 days in the Easy Ship GD programme first. Only after this qualifying period can you apply for the Prime badge via the SFP registration page."
        }
    ]
},

{
    "id": "5.3",
    "number": "Module 5.3",
    "title": "Inventory Planning",
    "difficulty": "Advanced",
    "time": "40 mins",
    "overview": """<p>Running out of stock is the fastest way to lose BSR rank, organic keyword position, and Buy Box status — all at once. This module covers demand forecasting, the Reorder Point (ROP) formula, Out-of-Stock (OOS) rate measurement, OOS prevention using the STEP Dashboard, safety stock calculation, seasonal build-up, and working capital optimisation.</p>""",
    "content": """
        <h3>1. Out-of-Stock (OOS) Rate — Definition & Formula</h3>
        <div class='callout warning'>
            <div><strong>OOS Rate Formula:</strong><br>
            <code>OOS Rate = (OOS Customer Views ÷ Total Customer Views) × 100</code><br><br>
            <strong>Important:</strong> Only counts ASINs where you have won Buy Box ≥30% AND sold &gt;5 units in the last 15 days.<br><br>
            <strong>Example:</strong> 100 OOS views ÷ 1,000 total views = 10% OOS Rate<br><br>
            <strong>OOS Impact Cascade:</strong><br>
            • BSR rank drops within 24–48 hours of going OOS<br>
            • Organic keyword rank drops within 72 hours<br>
            • Buy Box is lost immediately<br>
            • Recovery takes 2–4 weeks after restocking<br><br>
            Monitor via: <a class='btn-sc' href='https://sellercentral.amazon.in/seller-performance/dashboard' target='_blank'>STEP Dashboard</a></div>
        </div>

        <h3>2. Reorder Point (ROP) Calculation</h3>
        <div class='callout pro-tip'>
            <div><strong>ROP Formula (from Amazon Inventory Guide):</strong><br>
            <code>ROP = (Average Daily Sales × Lead Time Days) + Safety Stock</code><br><br>
            <strong>Example:</strong> 20 units/day × 21 days lead time + 100 safety stock = <strong>520 units ROP</strong><br><br>
            When your FBA stock hits 520 units → trigger reorder immediately.<br><br>
            <strong>Days of Cover:</strong> <code>FBA Stock ÷ Avg Daily Sales</code><br>
            Example: 300 units ÷ 20/day = 15 days cover — dangerously low!</div>
        </div>
        <table class='data-table'>
            <thead><tr><th>Metric</th><th>Formula</th><th>Example</th></tr></thead>
            <tbody>
                <tr><td>Reorder Point (ROP)</td><td>(Avg Daily Sales × Lead Time) + Safety Stock</td><td>(20 × 21) + 100 = 520 units</td></tr>
                <tr><td>Safety Stock</td><td>(Max Daily Sales − Avg Daily Sales) × Max Lead Time</td><td>(30 − 20) × 30 = 300 units</td></tr>
                <tr><td>Days of Cover</td><td>FBA Stock ÷ Avg Daily Sales</td><td>300 ÷ 20 = 15 days (danger zone)</td></tr>
                <tr><td>Total Lead Time</td><td>Production + Transit + FC Receiving</td><td>2 + 3 + 1 week = 6 weeks typical</td></tr>
            </tbody>
        </table>

        <h3>3. OOS Prevention Protocol — Weekly Actions</h3>
        <table class='data-table'>
            <thead><tr><th>Day</th><th>Action</th><th>Tool/Report</th></tr></thead>
            <tbody>
                <tr><td>Monday</td><td>Review Inventory Health Report — check 'Weeks of Cover' for all ASINs</td><td>Inventory Health Report (SC → Reports → Fulfillment)</td></tr>
                <tr><td>Wednesday</td><td>Check inbound shipment status; reconcile closed shipments</td><td>Manage FBA Shipments + Received Inventory Report</td></tr>
                <tr><td>Friday</td><td>Review daily velocity; update demand forecasts; plan next replenishment</td><td>Daily Inventory History + Business Reports</td></tr>
                <tr><td>Monthly</td><td>Seasonal trend analysis; year-over-year comparison for GIF/Prime Day planning</td><td>Monthly Inventory History Report</td></tr>
            </tbody>
        </table>
        <div class='callout success'>
            <div><strong>Set Low Inventory Alerts:</strong><br>
            SC → Inventory → Manage FBA Inventory → Settings → Low Inventory Threshold<br>
            Set threshold at your ROP value — get email notification before stock hits danger zone.<br><br>
            <strong>STEP Dashboard OOS Metric:</strong> Check your OOS % weekly in the Supply Chain &amp; Fulfilment section to monitor improvement trend.<br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/seller-performance/dashboard' target='_blank'>STEP Dashboard</a>
            &nbsp;<a class='btn-sc' href='https://sellercentral.amazon.in/inventory' target='_blank'>Manage Inventory</a></div>
        </div>

        <h3>4. Safety Stock Formula</h3>
        <p><code>Safety Stock = (Max Daily Sales − Avg Daily Sales) × Max Lead Time</code></p>
        <p>For <strong>high-velocity ASINs:</strong> maintain 14–21 days safety stock in FBA at all times.<br>
        For <strong>festive season:</strong> stock at least 90 days of cover before any major sale event.</p>

        <h3>5. Seasonal Inventory Build-Up Calendar</h3>
        <table class='data-table'>
            <thead><tr><th>Event</th><th>Velocity Multiplier</th><th>Build-Up Starts</th><th>Action</th></tr></thead>
            <tbody>
                <tr><td>Great Indian Festival (Oct)</td><td>5–10× normal</td><td>August (12 weeks before)</td><td>Check last year's Daily Inventory History for velocity spike</td></tr>
                <tr><td>Prime Day (typically July)</td><td>3–5× normal</td><td>May (10 weeks before)</td><td>Deal submissions require stock confirmation 4 weeks prior</td></tr>
                <tr><td>Navratri/Diwali/Dussehra</td><td>2–3× normal</td><td>September (6 weeks before)</td><td>Build to 90 days of cover before event</td></tr>
            </tbody>
        </table>

        <h3>6. Working Capital &amp; Cash Flow Optimisation</h3>
        <div class='callout success'>
            <div><strong>Cash-to-Inventory Ratio Rules:</strong><br>
            • Keep 40–60 days of inventory in FBA (sweet spot)<br>
            • Below 30 days = OOS risk zone<br>
            • Above 90 days = capital trapped + LTSF risk zone<br><br>
            <strong>Disbursement alignment:</strong> Amazon pays every 14 days — plan inventory purchase orders against disbursement schedule to avoid cash gaps.<br><br>
            <strong>70/30 Rule for omnichannel sellers:</strong> 70% of stock committed to FBA, 30% for offline/other channels. Shift to 80/20 during peak Amazon seasons (Oct–Dec).</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill-sc' href='https://sellercentral.amazon.in/seller-performance/dashboard' target='_blank'>STEP Dashboard</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/inventory-planning/restock-inventory' target='_blank'>Restock Inventory</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/reportcentral/FORECAST/1' target='_blank'>Demand Forecast Report</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/inventory-performance/dashboard' target='_blank'>IPI Dashboard</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/inventory' target='_blank'>Manage Inventory</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>"During the Great Indian Festival, my bestselling product went out of stock. My ranking dropped from #5 to #50 in the category and it took 3 weeks to recover. I didn't have enough data to forecast demand properly — and I underestimated how long Amazon takes to receive and process my inbound shipment."</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Calculate your true total lead time: production time + transit to Amazon FC + FC receiving time (typically 3–6 weeks total). Use the ROP formula to set your reorder trigger. Download last year's Daily Inventory History report to identify your exact velocity spike during festive season. Start building GIF inventory in August — not September. Enable low inventory email alerts in Manage FBA Inventory settings at your ROP threshold.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>OOS rate is tracked on the STEP Dashboard and directly affects your seller tier and eligibility for Amazon promotions. Sellers who maintain OOS rate below 5% consistently are eligible for more deal slots and platform incentives. The best-performing Amazon India sellers treat their Weeks of Cover report like a financial dashboard — reviewed every Monday with a fixed reorder workflow that runs regardless of how busy the team is.</p></div>
            </div>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "12-week rolling demand forecast maintained for all hero ASINs",
        "Reorder point (ROP) calculated and low inventory alerts set in SC",
        "Safety stock = 14–21 days for high-velocity ASINs",
        "Days of Cover tracked weekly — no ASIN below 21 days cover",
        "Seasonal inventory build-up started at correct lead time (12 weeks for GIF)",
        "STEP Dashboard OOS rate checked weekly — target below 5%",
        "Working capital cycle aligned with Amazon 14-day disbursement schedule"
    ],
    "quiz": [
        {
            "question": "How quickly does BSR rank start dropping when an ASIN goes out of stock?",
            "options": ["Instantly when OOS", "Within 24–48 hours", "After 1 week", "Only after 30 days"],
            "answer": "Within 24–48 hours",
            "explanation": "Amazon's algorithm detects OOS and immediately reduces the ASIN's BSR contribution and search rank. Organic keyword positions drop within 72 hours, and recovery takes 2–4 weeks."
        },
        {
            "question": "Using the ROP formula, what is the Reorder Point for an ASIN with 20 units/day avg sales, 21-day lead time, and 100 units safety stock?",
            "options": ["420 units", "520 units", "300 units", "600 units"],
            "answer": "520 units",
            "explanation": "ROP = (20 units/day × 21 days) + 100 safety stock = 420 + 100 = 520 units. When FBA stock hits 520 units, trigger the reorder to ensure you never go OOS during lead time."
        }
    ]
},

{
    "id": "5.4",
    "number": "Module 5.4",
    "title": "Account Health & SLA",
    "difficulty": "Advanced",
    "time": "40 mins",
    "overview": """<p>Your Amazon account is a business-critical asset worth protecting above everything else. This module covers all key account health metrics, common listing upload error codes (8572, 8541, 8007, 8575), A-to-Z claim management, chargeback prevention, and writing a Plan of Action (POA) if the worst happens.</p>""",
    "content": """
        <h3>1. Order Defect Rate (ODR) — Most Critical Metric</h3>
        <div class='callout warning'>
            <div><strong>ODR Target: &lt;1% | Suspension Threshold: &gt;1%</strong><br><br>
            ODR = (Negative Seller Feedback + A-to-Z Claims Granted + Credit Card Chargebacks) ÷ Total Orders<br><br>
            Calculated over a 60-day rolling period on FBM orders.<br><br>
            Check: <a class='btn-sc' href='https://sellercentral.amazon.in/account-health' target='_blank'>Account Health Dashboard</a></div>
        </div>
        <table class='data-table'>
            <thead><tr><th>Metric</th><th>Target</th><th>Alert Level</th><th>Suspension Risk</th></tr></thead>
            <tbody>
                <tr><td>Order Defect Rate (ODR)</td><td>&lt;1%</td><td>&gt;0.75%</td><td>&gt;1%</td></tr>
                <tr><td>Late Dispatch Rate (LDR)</td><td>&lt;4%</td><td>&gt;4%</td><td>&gt;8%</td></tr>
                <tr><td>Pre-Fulfillment Cancel Rate</td><td>&lt;2.5%</td><td>&gt;2.5%</td><td>&gt;5%</td></tr>
                <tr><td>Valid Tracking Rate (VTR)</td><td>&gt;95%</td><td>&lt;95%</td><td>&lt;90%</td></tr>
            </tbody>
        </table>

        <h3>2. Common Flat File Upload Errors — Quick Reference</h3>
        <div class='callout pro-tip'>
            <div><strong>These errors appear in your Upload Status report after flat file uploads:</strong></div>
        </div>
        <table class='data-table'>
            <thead><tr><th>Error Code</th><th>Error Type</th><th>Primary Fix</th></tr></thead>
            <tbody>
                <tr><td><strong>8560</strong></td><td>Missing Standard Product ID / Mandatory Attributes</td><td>Add/correct EAN/UPC; use Mandatory-Data Macro Tool to find missing fields</td></tr>
                <tr><td><strong>8541</strong></td><td>SKU Data Mismatch with Amazon Catalog</td><td>Match your data exactly to the existing ASIN catalog entry; check part_number field</td></tr>
                <tr><td><strong>8007</strong></td><td>Parent SKU Not Found</td><td>Fix variation theme and parent-child data; ensure parent row has relationship_type = 'Parent'</td></tr>
                <tr><td><strong>8575</strong></td><td>Listing Creation Privilege Temporarily Removed</td><td>Contact Seller Support immediately; review ASIN Creation Policy</td></tr>
                <tr><td><strong>99003</strong></td><td>Missing Required Value for Variation Theme</td><td>Fill size_name and color_name for all child SKUs under SizeName-ColorName theme</td></tr>
                <tr><td><strong>20013</strong></td><td>Image File Size Exceeds Maximum</td><td>Resize at bulkresizephotos.com/en; keep below 10 MB; min 1000px longest side</td></tr>
                <tr><td><strong>90111</strong></td><td>Invalid Decimal Value in Field</td><td>Replace text values with numbers (e.g. '38' not 'Large'); check Valid Values tab</td></tr>
            </tbody>
        </table>
        <div class='callout success'>
            <div><strong>Flat File Best Practices (SMEMinds):</strong><br>
            • Always download the latest template from SC before uploading<br>
            • Fix errors in batch — never upload one SKU at a time<br>
            • Wait 15–30 minutes after correction before re-uploading<br>
            • Download the error report from Upload Status page immediately after upload<br>
            • Validate all EAN/UPC codes before entry</div>
        </div>

        <h3>3. A-to-Z Claim Management</h3>
        <div class='callout success'>
            <div><strong>A-to-Z Claim Prevention SOP:</strong><br>
            1. Reply to all buyer messages within 24 hours<br>
            2. Issue refunds proactively for missing/damaged orders before claim is filed<br>
            3. If claim is filed: respond within 72 hours with tracking + proof of delivery<br>
            4. Accepted claims count toward ODR — fight only with strong evidence (tracking, delivery confirmation, photos)</div>
        </div>

        <h3>4. Account Suspension Prevention Checklist</h3>
        <ul>
            <li>Monitor Account Health daily: <a class='btn-sc' href='https://sellercentral.amazon.in/account-health' target='_blank'>Account Health Dashboard</a></li>
            <li>All metrics in green — no yellow or red warnings</li>
            <li>No policy warnings or IP infringement notices</li>
            <li>All communication from Amazon responded to within 72 hours</li>
            <li>No listing policy violations (review manipulation, prohibited claims, false certifications)</li>
            <li>All required certifications (BIS, FSSAI, etc.) uploaded and current</li>
            <li>Monitor Performance Notifications: <a class='btn-sc' href='https://sellercentral.amazon.in/performance/notifications' target='_blank'>Performance Notifications</a></li>
        </ul>

        <h3>5. Plan of Action (POA) Writing SOP</h3>
        <div class='callout pro-tip'>
            <div><strong>POA Structure (3 required sections):</strong><br>
            <ol>
                <li><strong>Root Cause:</strong> What exactly caused the violation — be honest, specific, and factual. Never blame customers or Amazon.</li>
                <li><strong>Immediate Actions Taken:</strong> What you have already done to fix the problem (completed actions, not future promises).</li>
                <li><strong>Preventive Actions:</strong> Specific SOPs, processes, and systems you are implementing to ensure it never recurs — with timelines.</li>
            </ol>
            Keep POA to 1–2 pages maximum. Amazon reviewers read hundreds of POAs. Be specific and concrete — "I will try to improve" results in POA rejection. Show exact processes implemented.</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill-sc' href='https://sellercentral.amazon.in/account-health' target='_blank'>Account Health Dashboard</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/performance/notifications' target='_blank'>Performance Notifications</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/performance/feedback' target='_blank'>Feedback Manager</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Sellers receive an account suspension notice after a sudden spike in A-to-Z claims during festive season. Bulk orders from the same period have multiple "item not received" claims, pushing ODR above 1%. The seller does not have a POA ready and wastes 3–5 days trying to write one under pressure, extending the suspension period.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Maintain a POA template ready at all times with your business details, SOPs, and processes pre-filled. Check ODR daily during peak sales events — not weekly. When ODR exceeds 0.75% (the alert threshold), proactively contact buyers with tracking details and offer refunds before they escalate to A-to-Z claims. Use SC → Manage Orders to filter orders with no tracking scans older than 5 days and reach out immediately.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>Account health metrics and flat file error codes are two sides of the same operational discipline coin. Sellers who maintain spotless account health (ODR &lt;0.5%, LDR &lt;2%) AND upload error-free flat files consistently are the ones who scale fastest on Amazon India — because they spend zero time firefighting and 100% of their energy on growth activities like new product launches and advertising optimisation.</p></div>
            </div>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "ODR &lt;1% — checked daily",
        "VTR &gt;95% for FBM orders",
        "Cancellation Rate &lt;2.5%",
        "LDR &lt;4%",
        "All A-to-Z claims responded to within 72 hours",
        "Account Health dashboard checked daily — all metrics green",
        "POA template prepared and kept ready in case of notification",
        "Flat file uploads error-checked using Mandatory-Data Macro Tool before submission"
    ],
    "quiz": [
        {
            "question": "What three components make up the Order Defect Rate (ODR)?",
            "options": [
                "Returns + cancellations + chargebacks",
                "Negative feedback + A-to-Z claims + chargebacks",
                "Late shipments + OOS + returns",
                "Negative reviews + customer complaints + IPI"
            ],
            "answer": "Negative feedback + A-to-Z claims + chargebacks",
            "explanation": "ODR = (Negative Seller Feedback + A-to-Z Claims Granted + Credit Card Chargebacks) ÷ Total Orders in the period. All three components directly count against the 1% threshold."
        },
        {
            "question": "What is the most important element in a Plan of Action (POA)?",
            "options": [
                "A detailed history of your business",
                "Apologising to Amazon for the violation",
                "Specific root cause + concrete preventive actions",
                "List of all your products"
            ],
            "answer": "Specific root cause + concrete preventive actions",
            "explanation": "Amazon's review team looks for specificity — exact root cause, exact actions taken, exact processes implemented. Generic answers like 'we will improve' result in POA rejection."
        },
        {
            "question": "Which error code appears when your uploaded flat file SKU data conflicts with an existing ASIN in the Amazon catalog?",
            "options": ["Error 8007", "Error 8575", "Error 8541", "Error 99003"],
            "answer": "Error 8541",
            "explanation": "Error 8541 means the product ID (EAN/UPC) matches an existing ASIN in the catalog, but other data fields (like part_number) differ. Fix by matching your flat file data exactly to the existing catalog entry."
        }
    ]
}
,

# ─────────────────────────────────────────────────────────────
{
    "id": "5.5",
    "number": "Module 5.5",
    "title": "Easy Ship Prime & Guaranteed Delivery Programme",
    "difficulty": "Intermediate",
    "time": "30 mins",
    "overview": """<p>Easy Ship Prime (Seller Fulfilled Prime) gives you the Prime badge without moving inventory to Amazon FCs — but it demands near-perfect operational discipline. This module covers the GD Programme enrollment, daily dispatch SOP, SFP eligibility path, and performance thresholds that keep your Prime badge active.</p>""",
    "content": """
        <h3>1. Programme Hierarchy</h3>
        <table class='data-table'>
            <thead><tr><th>Programme</th><th>Delivery Promise</th><th>Prime Badge</th><th>Requirement</th></tr></thead>
            <tbody>
                <tr><td>Easy Ship Standard</td><td>3–5 days</td><td>❌</td><td>Basic Easy Ship</td></tr>
                <tr><td>Easy Ship GD (Fast Track)</td><td>1–2 days</td><td>❌</td><td>GD Programme enrollment</td></tr>
                <tr><td>Seller Fulfilled Prime (SFP)</td><td>1–2 days</td><td>✅ Prime</td><td>30 days in GD + metrics thresholds</td></tr>
            </tbody>
        </table>

        <h3>2. Enrolling in Easy Ship Guaranteed Delivery (GD)</h3>
        <ol>
            <li>Check eligibility: pin code coverage, seller account performance metrics</li>
            <li>Log in to Seller Central India</li>
            <li>Navigate to <strong>Shipping Settings → Easy Ship Settings</strong></li>
            <li>Enable Two-Day (2DD) and One-Day (1DD) Delivery options</li>
            <li>Settings activate within 3–4 hours</li>
            <li>Complete enrollment confirmation survey</li>
        </ol>

        <h3>3. Daily Operational Checklist (Non-Negotiable)</h3>
        <table class='data-table'>
            <thead><tr><th>Time</th><th>Action</th></tr></thead>
            <tbody>
                <tr><td><strong>By 12:00 PM</strong></td><td>Process all orders received — pick, pack, label</td></tr>
                <tr><td><strong>By 12:45 PM</strong></td><td>Schedule Easy Ship pickup</td></tr>
                <tr><td><strong>By 1:00 PM</strong></td><td>Orders ready for handover to logistics partner</td></tr>
                <tr><td>1:00–4:00 PM</td><td>LSP pickup window (only slot for GD)</td></tr>
                <tr><td>After Saturday 12 PM</td><td>ESD set to Monday (Sundays excluded)</td></tr>
            </tbody>
        </table>
        <div class='callout warning'><div><strong>Sunday Rule:</strong> Sundays are excluded from ESD (Expected Ship Date) calculations. Orders received after Saturday 12:00 PM have ESD set to Monday. Many sellers miss this and get Late Dispatch Rate violations over the weekend.</div></div>

        <h3>4. GD Performance Thresholds</h3>
        <table class='data-table'>
            <thead><tr><th>Metric</th><th>Easy Ship GD Threshold</th><th>SFP Threshold</th></tr></thead>
            <tbody>
                <tr><td>Late Dispatch Rate (LDR)</td><td>≤1.5%</td><td>≤1.0%</td></tr>
                <tr><td>Cancellation Rate</td><td>≤1.5%</td><td>≤1.0%</td></tr>
                <tr><td>Minimum Orders</td><td>≥30/month</td><td>—</td></tr>
                <tr><td>Free Shipping</td><td>Not required</td><td>Mandatory on all SFP SKUs</td></tr>
            </tbody>
        </table>

        <h3>5. Applying for Seller Fulfilled Prime (SFP)</h3>
        <ol>
            <li>Complete 30 days in GD Programme with ≥1 fulfilled GD order</li>
            <li>Ensure all metrics meet SFP thresholds (LDR ≤1.0%, cancellation ≤1.0%)</li>
            <li>Apply via <strong>sellercentral.amazon.in/seller-fulfilled-prime</strong></li>
            <li>Offer free shipping on all SFP SKUs (mandatory)</li>
            <li>Same-day/next-day shipping required for all SFP orders</li>
        </ol>

        <h3>6. Package Limits for GD Programme</h3>
        <ul>
            <li>Maximum Dimensions: 50 cm × 35 cm × 30 cm</li>
            <li>Maximum Weight: 9 kg</li>
            <li>Fulfillment Method: Amazon Easy Ship only</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/shipping-settings/easy-ship' target='_blank'>Easy Ship Settings</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/seller-fulfilled-prime' target='_blank'>Seller Fulfilled Prime</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/performance/dashboard' target='_blank'>Performance Dashboard</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller misses Saturday 12:00 PM cutoff — 15 orders dispatched Monday, all counted as Late. LDR spikes to 4%, triggering GD programme suspension. Prime badge lost for 30 days.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Set Saturday orders cut-off alert at 11:30 AM. Designate a dedicated GD processing station. Add buffer: process GD orders first before SFP or standard orders every day.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>SFP with Prime badge gives a Buy Box advantage comparable to FBA — without the complexity of inbounding to FCs. For sellers with consistent 200–500 orders/day warehouse operations, SFP often outperforms FBA on margin.</p></div>
            </div>
        </div>
    """,
    "checklist": [
        "Enabled Two-Day and One-Day delivery in Easy Ship Settings",
        "Daily: all orders processed and pickup scheduled by 12:45 PM",
        "Saturday: extra alert set for 11:30 AM to catch weekend orders",
        "LDR monitored daily in Performance Dashboard (target ≤1.5% for GD, ≤1.0% for SFP)",
        "Cancellation rate maintained below threshold (≤1.5% GD, ≤1.0% SFP)",
        "Free shipping enabled on all SFP SKUs (mandatory requirement)",
        "Package dimensions and weight within GD limits (50×35×30cm, ≤9kg)"
    ],
    "quiz": [
        {
            "question": "What is the Late Dispatch Rate (LDR) threshold for Easy Ship Guaranteed Delivery?",
            "options": ["≤5%", "≤3%", "≤1.5%", "≤0.5%"],
            "answer": "≤1.5%",
            "explanation": "Easy Ship GD Programme requires LDR ≤1.5% and Cancellation Rate ≤1.5%. Seller Fulfilled Prime (SFP) has stricter thresholds: LDR ≤1.0% and Cancellation Rate ≤1.0%."
        },
        {
            "question": "What happens to orders received on Saturday after 12:00 PM in the GD Programme?",
            "options": ["Must be dispatched same day", "ESD set to Sunday", "ESD set to Monday (Sundays excluded)", "Automatically cancelled"],
            "answer": "ESD set to Monday (Sundays excluded)",
            "explanation": "Sundays are excluded from GD calculations. Orders received after Saturday 12:00 PM have their Expected Ship Date (ESD) automatically set to Monday, not Sunday."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "5.6",
    "number": "Module 5.6",
    "title": "Seller Flex — Ship from Your Warehouse",
    "difficulty": "Advanced",
    "time": "45 mins",
    "overview": """<p>Seller Flex lets you ship Prime orders directly from your own warehouse using Amazon's carrier network — giving you Prime badge eligibility, inventory control, and lower storage costs versus FBA. This module covers Flex site setup, IT infrastructure, manpower planning, peak season preparation, and the return processing SOP.</p>""",
    "content": """
        <h3>1. What is Amazon Seller Flex?</h3>
        <p>Seller Flex is an Amazon program where your warehouse becomes a mini-fulfillment center. Amazon provides the carrier network; you provide the storage, packing, and handover operations. Eligible sellers can display the Prime badge on Flex-fulfilled orders.</p>
        <div class='callout success'><div><strong>Key Benefits:</strong> Prime badge without sending inventory to Amazon FCs | Inventory stays in your control | Lower storage costs vs. FBA | Pan-India delivery via Amazon logistics</div></div>

        <h3>2. IT Infrastructure Requirements</h3>
        <table class='data-table'>
            <thead><tr><th>Equipment</th><th>Minimum Specification</th></tr></thead>
            <tbody>
                <tr><td>Laptops / PCs</td><td>2 minimum | 2GB RAM | Windows 7+</td></tr>
                <tr><td>Barcode Scanners</td><td>USB or Bluetooth (1 per pack station)</td></tr>
                <tr><td>Shipping Label Printer</td><td>Zebra GX 430T recommended</td></tr>
                <tr><td>Gift Wrap Printer</td><td>Zebra GC 420T recommended</td></tr>
                <tr><td>Invoice Printer</td><td>PDF-enabled laser printer</td></tr>
                <tr><td>Internet (Primary)</td><td>&gt;4 Mbps fixed broadband</td></tr>
                <tr><td>Internet (Secondary)</td><td>&gt;4 Mbps (different ISP from primary)</td></tr>
                <tr><td>Power Backup</td><td>2+ hours UPS/DG/Inverter</td></tr>
            </tbody>
        </table>

        <h3>3. Manpower Planning by Volume</h3>
        <table class='data-table'>
            <thead><tr><th>Daily Volume</th><th>Shifts</th><th>Pack Stations</th><th>Staff Required</th></tr></thead>
            <tbody>
                <tr><td>Up to 500 units/day</td><td>1</td><td>1</td><td>3</td></tr>
                <tr><td>501–1,000 units/day</td><td>1</td><td>2</td><td>5</td></tr>
                <tr><td>1,001–1,500 units/day</td><td>1</td><td>3</td><td>6</td></tr>
                <tr><td>1,500+ units/day</td><td>2</td><td>4+</td><td>8+</td></tr>
            </tbody>
        </table>

        <h3>4. Performance Thresholds (Non-Negotiable)</h3>
        <table class='data-table'>
            <thead><tr><th>Metric</th><th>Threshold</th></tr></thead>
            <tbody>
                <tr><td>Cancellation Rate</td><td>&lt;0.05%</td></tr>
                <tr><td>Late Shipment Rate (ExSD Miss)</td><td>&lt;0.05%</td></tr>
                <tr><td>Late Handover to DA</td><td>&lt;0.05%</td></tr>
            </tbody>
        </table>
        <div class='callout warning'><div><strong>The Golden Rule of Seller Flex:</strong> Pack EVERY order before 2:00 PM (CPT — Carrier Pickup Time). Any order not ready at 2:00 PM will miss the pickup window and count as a late shipment. Three strikes on metrics = site suspension.</div></div>

        <h3>5. Peak Season Preparation Checklist (10 Steps)</h3>
        <ol>
            <li>Increase order processing capacity (add shifts, hire temp staff 4 weeks before)</li>
            <li>Monitor performance daily (cancellation rate + LSR)</li>
            <li>Monitor order backlog continuously (catch it before it becomes unmanageable)</li>
            <li>Avoid emergency holidays (apply 5 days in advance, ship pending orders first)</li>
            <li>Ensure ALL orders packed before 2:00 PM CPT (test with trial run pre-peak)</li>
            <li>Test power backup (UPS/DG) and secondary internet link</li>
            <li>Stock packaging materials 4 weeks early (boxes, polybags, labels, tape, gift wrap)</li>
            <li>Recalibrate all printers (test shipping label + invoice quality)</li>
            <li>Update contact details in User Management (add 2+ alternate contacts)</li>
            <li>Know your escalation path before peak starts</li>
        </ol>

        <h3>6. Returns Processing via CRET Portal</h3>
        <ol>
            <li>Access CRET Portal: eu-amazon-creturns.com/prepClassification/new</li>
            <li>Login: username = (sitecode)s001, password = (sitecode)s001@SITECODE</li>
            <li>Inspect returned units and classify:<br>
            Grade A = Like New | Grade B = Good | Grade C = Acceptable | Unsellable</li>
            <li>Update classification in CRET portal within specified timeline</li>
        </ol>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellerflex.amazon.in' target='_blank'>Seller Flex Portal</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/cu/contact-us' target='_blank'>Seller Support</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Power goes out during peak Diwali packing window — no backup power. Internet also down. 300 orders miss 2:00 PM CPT. LSR spikes to 12%. Seller Flex site suspended during peak season.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Test UPS/DG and secondary internet 4 weeks before every major sale event. Document backup procedure: if primary internet fails → switch to secondary within 5 mins. If power fails → UPS kicks in for 2+ hours.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>Seller Flex is most profitable for sellers with 500–2,000 orders/day who have stable warehouse operations. Below 200 orders/day, FBA is usually more cost-effective (lower overhead). Above 2,000/day, consider a dedicated 3PL partner to supplement Flex capacity.</p></div>
            </div>
        </div>
    """,
    "checklist": [
        "IT infrastructure set up: 2 laptops, barcode scanners, label printer, dual internet",
        "Power backup installed and tested (2+ hours minimum)",
        "Staff trained and assigned to roles (Site Manager, Pack Station, Inbound, Returns)",
        "Daily: all orders packed and ready before 2:00 PM CPT",
        "Peak season: temp staff hired 4 weeks before event",
        "Packaging materials stocked 4 weeks before peak",
        "CRET portal credentials confirmed and return processing workflow trained"
    ],
    "quiz": [
        {
            "question": "What is the CPT (Carrier Pickup Time) golden rule for Seller Flex?",
            "options": ["Pack all orders before 12:00 PM", "Pack all orders before 2:00 PM", "Ship all orders before 5:00 PM", "Pack 80% of orders before 2:00 PM"],
            "answer": "Pack all orders before 2:00 PM",
            "explanation": "The golden rule of Seller Flex: every order must be packed and ready before 2:00 PM (CPT — Carrier Pickup Time). Any order not ready at 2:00 PM misses the pickup window and counts as a late shipment."
        },
        {
            "question": "What is the Late Shipment Rate (LSR) threshold for Seller Flex?",
            "options": ["<5%", "<2%", "<0.5%", "<0.05%"],
            "answer": "<0.05%",
            "explanation": "Seller Flex performance thresholds are extremely strict: Cancellation Rate <0.05%, Late Shipment Rate <0.05%, and Late Handover to DA <0.05%. Three strikes on these metrics leads to site suspension."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "5.7",
    "number": "Module 5.7",
    "title": "IXD Programme — Pan-India Inventory Placement",
    "difficulty": "Advanced",
    "time": "35 mins",
    "overview": """<p>The IXD (Inventory Placement / Ship Cross Dock) Programme lets you send a single consolidated shipment to one Receive Centre and have Amazon distribute it across 13–14 fulfillment centers pan-India. This eliminates the cost and complexity of managing multiple FC shipments — but requires APoB registration in multiple states. This module covers eligibility, enrollment, network structure, and the Restock Inventory dashboard.</p>""",
    "content": """
        <h3>1. How IXD Works</h3>
        <p>Without IXD: You must create separate FBA shipments to each Amazon FC region → 5–6 shipments to cover India.<br>
        With IXD: You ship to your nearest <strong>Receive Centre (RC)</strong> once → Amazon distributes to 13–14 destination FCs automatically.</p>
        <div class='callout success'><div><strong>Key Benefits:</strong> Single shipment (vs. multiple regional shipments) | Lower freight cost (one logistics partner, one destination) | Pan-India coverage without multi-state logistics complexity | Amazon's IXD flat fee based on weight slab</div></div>

        <h3>2. IXD Eligibility Criteria</h3>
        <ul>
            <li>✅ GST registration in at least 3 states (with APoB — Additional Place of Business)</li>
            <li>✅ APoB registered in at least 1 IXD FC per state</li>
            <li>✅ Non-sort (oversize) ASINs &lt;20% of total inventory</li>
            <li>❌ Heavy &amp; Bulky items ineligible (LxBxH &gt; 29×23×18 inches)</li>
            <li>❌ Fragile or oversize items excluded</li>
            <li>✅ FSSAI license active across all FCs (for food sellers)</li>
        </ul>

        <h3>3. IXD Receive Centre Network</h3>
        <table class='data-table'>
            <thead><tr><th>Region</th><th>Receive Centre</th><th>Serves</th></tr></thead>
            <tbody>
                <tr><td>North (Delhi/NCR/Haryana)</td><td>DED3 / DEL8</td><td>North India FCs</td></tr>
                <tr><td>West (Gujarat/Maharashtra)</td><td>ISK3 / BOM6</td><td>West India FCs</td></tr>
                <tr><td>South (Karnataka/Telangana)</td><td>BLR4</td><td>South India FCs</td></tr>
            </tbody>
        </table>

        <h3>4. IXD Enrollment Process</h3>
        <ol>
            <li>Verify GST + APoB registration in minimum 3 states</li>
            <li>Verify APoB in at least 1 IXD FC per required state</li>
            <li>Check product catalog: non-sort ASINs &lt;20%</li>
            <li>Contact Amazon Seller Account Manager or raise a case in Seller Central</li>
            <li>Once approved, create a single shipment to your nearest Receive Centre</li>
            <li>Amazon distributes inventory to destination FCs automatically</li>
        </ol>

        <h3>5. Using the Restock Inventory (RIM) Dashboard</h3>
        <ol>
            <li>Go to <strong>Inventory → Inventory Planning → Restock Inventory</strong></li>
            <li>View per-FC quantity recommendations</li>
            <li>Filter by ASIN, FC, or days of supply</li>
            <li>Accept recommendation or customize quantity</li>
            <li>Create inbound shipment to nearest RC</li>
            <li>Track distribution status per destination FC</li>
        </ol>

        <h3>6. IXD Fees</h3>
        <p>IXD charges a flat shipping fee based on product weight slab (₹3–₹40 per unit typically). This fee applies only to outbound customer orders — not inter-FC transfers. No IXD fee for Seller Flex fulfillment.</p>

        <div class='callout info'><div><strong>APoB Registration Support:</strong> GetMyCA Consultants (mentioned in Amazon's own IXD guide) provides pan-India APoB registration services. Sellers without CA support should engage a chartered accountant in each state where FC registration is required.</div></div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/inventory-planning/restock-inventory' target='_blank'>Restock Inventory Dashboard</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/gp/ssof/shipping-queue.html' target='_blank'>Manage FBA Shipments</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller not enrolled in IXD manages 6 separate FC shipments — different freight partners, different STNs, different appointment slots, different reconciliations. Operational overhead consumes 3 staff days/week.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Enroll in IXD as soon as APoB registrations are in place. ROI: reducing 6 shipments to 1 cuts freight complexity by 80% and frees staff bandwidth for higher-value work. Engage a CA firm for pan-India APoB registration upfront.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>Use the RIM (Restock Inventory Management) dashboard to plan IXD quantities — it shows per-FC demand forecast so you know exactly how much Amazon will distribute to each region. Match your send quantity to RIM recommendations for optimal coverage.</p></div>
            </div>
        </div>
    """,
    "checklist": [
        "GST + APoB registration verified in minimum 3 states",
        "Non-sort ASINs confirmed below 20% of total inventory",
        "No Heavy & Bulky items in catalogue (ineligible for IXD)",
        "FSSAI license active across all FCs (food sellers only)",
        "IXD enrollment completed via Seller Account Manager or Support case",
        "Nearest Receive Centre identified and logistics partner confirmed",
        "RIM dashboard reviewed weekly for per-FC quantity recommendations"
    ],
    "quiz": [
        {
            "question": "How many states must a seller have APoB registration in to be eligible for IXD Programme?",
            "options": ["1 state", "2 states", "At least 3 states", "All 28 states"],
            "answer": "At least 3 states",
            "explanation": "IXD eligibility requires GST registration and APoB (Additional Place of Business) in at least 3 states, with APoB in at least 1 IXD FC per state. This enables Amazon to legally distribute inventory across state lines."
        },
        {
            "question": "What percentage of non-sort (oversize) ASINs is the maximum for IXD eligibility?",
            "options": ["5%", "10%", "20%", "35%"],
            "answer": "20%",
            "explanation": "For IXD eligibility, non-sort ASINs must be less than 20% of your total inventory. Heavy & Bulky items (LxBxH > 29×23×18 inches) are entirely ineligible for IXD."
        }
    ]
}

]
