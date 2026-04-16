# ══════════════════════════════════════════════════════════════
# PILLAR 6 — TOOLS  (5 Modules)
# ══════════════════════════════════════════════════════════════

pillar6_modules = [

{
    "id": "6.1",
    "number": "Module 6.1",
    "title": "Seller Central",
    "difficulty": "Beginner",
    "time": "35 mins",
    "overview": """<p>Seller Central is your Amazon command centre. This module covers the essential setup — user permissions, the reports you must pull weekly, Business Reports setup, inventory reporting automation, payment reconciliation, and FBA discrepancy resolution — giving your team a structured operating rhythm.</p>""",
    "content": """
        <h3>1. Seller Central Dashboard Setup & User Permissions</h3>
        <div class='callout pro-tip'>
            <div><strong>User Permissions by Role (SC → Settings → User Permissions):</strong><br>
            • <strong>Account Manager:</strong> Full access except banking<br>
            • <strong>Catalogue Manager:</strong> Inventory + listings only<br>
            • <strong>Finance:</strong> Reports + payments view only<br>
            • <strong>PPC Manager:</strong> Advertising console only<br>
            • <strong>CS Team:</strong> Orders + messaging only<br><br>
            Use principle of least privilege — give each user only what they need.</div>
        </div>

        <h3>2. Core Reports Library — What to Pull & When</h3>
        <table class='data-table'>
            <thead><tr><th>Report</th><th>Frequency</th><th>Path in SC</th></tr></thead>
            <tbody>
                <tr><td>Business Reports (Detail Page)</td><td>Daily</td><td>Reports → Business Reports → By ASIN</td></tr>
                <tr><td>Search Term Report (PPC)</td><td>Weekly</td><td>Advertising → Reports → Search Term</td></tr>
                <tr><td>Search Query Performance</td><td>Weekly</td><td>Brand Analytics → SQP</td></tr>
                <tr><td>Inventory Ledger Report</td><td>Monthly</td><td>Reports → Fulfilment → Inventory Ledger</td></tr>
                <tr><td>Transaction View</td><td>Weekly</td><td>Reports → Payments → Transaction View</td></tr>
                <tr><td>A-to-Z Claims</td><td>Daily</td><td>Performance → A-to-Z Guarantee Claims</td></tr>
            </tbody>
        </table>

        <h3>3. Business Reports Setup</h3>
        <ul>
            <li><strong>Detail Page Sales and Traffic:</strong> Sessions, pageviews, Buy Box %, Unit Session %</li>
            <li><strong>Sales and Traffic by ASIN:</strong> Revenue per ASIN, sessions, conversion</li>
            <li><strong>Brand Analytics Reports:</strong> Search Query Performance, Market Basket, Demographics</li>
        </ul>
        <p>Pro tip: Download weekly to Excel and build a running tracker to see trends. Trends matter more than any single data point.</p>

        <h3>4. Payment & Disbursement Reconciliation</h3>
        <div class='callout success'>
            <div><strong>Weekly reconciliation SOP:</strong><br>
            SC → Reports → Payments → Transaction View<br>
            1. Export all transactions for the period<br>
            2. Cross-check total sales vs. total disbursed<br>
            3. Flag: unexpected fee charges, missing reimbursements, damaged inventory claims<br>
            4. File SC case for any discrepancy &gt;₹500</div>
        </div>

        <h3>5. FBA Shipment Discrepancy Resolution</h3>
        <ul>
            <li>Amazon FCs occasionally receive fewer units than sent (discrepancy)</li>
            <li>Window to file: within 9 months of shipment creation</li>
            <li>Path: SC → Inventory → Shipments → Select shipment → Report Problem</li>
            <li>Evidence needed: Supplier invoice, packing list with quantities</li>
            <li>Amazon reimburses at average selling price if discrepancy confirmed</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/gp/account-manager/home.html' target='_blank'>User Permissions</a>
            <a class='pill' href='https://sellercentral.amazon.in/gp/site-metrics/report.html' target='_blank'>Business Reports</a>
            <a class='pill' href='https://sellercentral.amazon.in/reportcentral' target='_blank'>Reports Library</a>
            <a class='pill' href='https://sellercentral.amazon.in/payments/summary/ref=xx_payments_dnav_xx' target='_blank'>Payments</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [
        {"id": "GGLI_aIUO0M", "title": "Amazon Seller Central — Complete Navigation Guide"},
        {"id": "y4icIWo5ciY", "title": "Essential Amazon Reports Every Seller Must Track"}
    ],
    "checklist": [
        "User permissions set correctly for all team members",
        "Weekly reports calendar established and followed by team",
        "Business Reports dashboard bookmarked and checked daily",
        "Payment reconciliation completed weekly",
        "FBA shipment discrepancies reviewed and filed within 9 months",
        "Transaction View exported and reconciled monthly"
    ],
    "quiz": [
        {
            "question": "What is the deadline to file an FBA shipment discrepancy claim?",
            "options": ["30 days", "90 days", "9 months", "12 months"],
            "answer": "9 months",
            "explanation": "Amazon allows up to 9 months from shipment creation to file a discrepancy claim. After this window, the claim is not eligible for investigation or reimbursement."
        }
    ]
},

{
    "id": "6.2",
    "number": "Module 6.2",
    "title": "Brand Analytics",
    "difficulty": "Advanced",
    "time": "40 mins",
    "overview": """<p>Brand Analytics is Amazon's most powerful data intelligence tool — available exclusively to Brand Registered sellers. This module covers all five Brand Analytics reports: Search Query Performance, Market Basket, Repeat Purchase Behaviour, Demographics, and Item Comparison — and how to turn each into action.</p>""",
    "content": """
        <h3>1. Search Query Performance (SQP) Report</h3>
        <div class='callout pro-tip'>
            <div><strong>SQP shows you:</strong><br>
            • Total search volume for any query<br>
            • Your ASIN's Impression Share, Click Share, and Conversion Share vs. top 3 results<br><br>
            <strong>Use it to:</strong><br>
            1. Identify keywords where you get impressions but lose clicks → fix title/image<br>
            2. Find keywords where competitors dominate → increase bid on SP<br>
            3. Discover new high-volume keywords to add to listings</div>
        </div>

        <h3>2. Market Basket Analysis</h3>
        <p>Shows top 3 products purchased alongside each of your ASINs in the same transaction.</p>
        <p><strong>Actions:</strong></p>
        <ul>
            <li>Create Virtual Bundles from top FBT pairs</li>
            <li>Target FBT products with Sponsored Display</li>
            <li>Add cross-sell module to A+ Content showing FBT products</li>
        </ul>

        <h3>3. Repeat Purchase Behaviour Report</h3>
        <p>Shows what percentage of your customers are repeat buyers and their purchase frequency.</p>
        <div class='callout success'>
            <div><strong>Repeat Purchase Actions:</strong><br>
            High repeat rate ASIN: Enrol in Subscribe &amp; Save → lock in recurring revenue<br>
            Low repeat rate: Investigate — poor product experience? Better alternatives available?</div>
        </div>

        <h3>4. Demographics Report</h3>
        <p>Shows your customer profile: age range, household income, education, gender, marital status, geography.</p>
        <p>Use to:</p>
        <ul>
            <li>Refine DSP and Sponsored Display audience targeting</li>
            <li>Inform product development (what income/age bracket buys you?)</li>
            <li>Tailor creative (lifestyle images, tone of voice) to actual buyer profile</li>
        </ul>

        <h3>5. Item Comparison & Alternate Purchase Report</h3>
        <p>Shows which products customers view when they view yours — and what they ultimately buy instead.</p>
        <div class='callout info'>
            <div><strong>Two use cases:</strong><br>
            1. <strong>Item Comparison:</strong> What customers view alongside your ASIN = competitor map<br>
            2. <strong>Alternate Purchase:</strong> What they buy instead = your actual competition for conversion<br><br>
            Target alternate purchase ASINs with Sponsored Display product targeting.</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/brand-analytics' target='_blank'>Brand Analytics Dashboard</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "SQP report reviewed weekly for top 50 ASINs",
        "Market Basket pairs identified and actioned (bundles + SD targeting)",
        "Repeat Purchase rate tracked monthly — S&S enrolment for high-repeat ASINs",
        "Demographics report used to inform A+ Content creative and DSP targeting",
        "Alternate Purchase report reviewed monthly — top competitors targeted via SD"
    ],
    "quiz": [
        {
            "question": "What does the Alternate Purchase report show you?",
            "options": [
                "What customers buy alongside your product",
                "What customers ultimately buy instead of your product",
                "Your top performing keywords",
                "Your customer's geographic location"
            ],
            "answer": "What customers ultimately buy instead of your product",
            "explanation": "The Alternate Purchase report shows the products customers buy when they view your ASIN but don't purchase. These are your direct conversion competitors — ideal targets for Sponsored Display product targeting."
        }
    ]
},

{
    "id": "6.3",
    "number": "Module 6.3",
    "title": "Advertising Console",
    "difficulty": "Advanced",
    "time": "40 mins",
    "overview": """<p>The Amazon Advertising Console is your central hub for all paid media on Amazon India. This module covers campaign structure best practices, naming conventions, bulk operations, Amazon Attribution setup, and integration with third-party tools — everything needed to run a professional advertising operation at scale.</p>""",
    "content": """
        <h3>1. Campaign Structure & Naming Convention</h3>
        <div class='callout pro-tip'>
            <div><strong>Campaign Naming Convention:</strong><br>
            <code>[Brand]_[Ad Type]_[ASIN/Category]_[Match Type]_[Objective]_[YYYYMM]</code><br><br>
            Examples:<br>
            • SMEMinds_SP_B09XYZ_Exact_Harvest_202601<br>
            • SMEMinds_SB_Kitchen_Brand_Awareness_202601<br>
            • SMEMinds_SD_Retarget_ASIN_Viewers_202601</div>
        </div>
        <table class='data-table'>
            <thead><tr><th>Ad Type</th><th>Abbreviation</th><th>Best Structure</th></tr></thead>
            <tbody>
                <tr><td>Sponsored Products</td><td>SP</td><td>1 ASIN per ad group, separate match types</td></tr>
                <tr><td>Sponsored Brands</td><td>SB</td><td>1 campaign per brand story / collection</td></tr>
                <tr><td>Sponsored Display</td><td>SD</td><td>1 targeting type per campaign</td></tr>
                <tr><td>Sponsored Brands Video</td><td>SBV</td><td>1 video per campaign, test thumbnails</td></tr>
            </tbody>
        </table>

        <h3>2. Bulk Operations</h3>
        <p>Bulk operations allow editing thousands of bids, budgets, and keywords at once:</p>
        <ol>
            <li>Advertising Console → Bulk Operations → Download report</li>
            <li>Edit in Excel: bid adjustments, pause/enable, budget changes</li>
            <li>Upload modified file</li>
            <li>Changes apply within 1–4 hours</li>
        </ol>
        <p>Use for: weekly bid optimisation across 100+ keywords, event budget increases, new negative keyword additions at scale.</p>

        <h3>3. Amazon Attribution Dashboard</h3>
        <p>Track how external traffic converts on Amazon:</p>
        <ul>
            <li>SC → Advertising → Amazon Attribution → Create tag → Copy URL</li>
            <li>Use unique tag per channel (Meta, Google, Email, Influencer)</li>
            <li>Dashboard shows: Clicks, DPV (Detail Page Views), Add-to-Carts, Purchases, Revenue</li>
            <li>Unlocks Brand Referral Bonus (~10% credit on external-driven new customer purchases)</li>
        </ul>

        <h3>4. 3P PPC Tools Integration</h3>
        <div class='callout info'>
            <div><strong>When to consider 3P tools:</strong><br>
            &gt;50 campaigns or &gt;1,000 keywords → manual optimisation becomes inefficient<br><br>
            <strong>Options:</strong><br>
            • <strong>SellerApp:</strong> India-focused, SC integration, ACOS optimisation<br>
            • <strong>Helium 10 Adtomic:</strong> Keyword bid automation, dayparting<br>
            • <strong>Pacvue / Perpetua:</strong> Enterprise-grade, algorithmic bidding<br>
            • <strong>Scale Insights:</strong> Automated rules with granular controls</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://advertising.amazon.in' target='_blank'>Amazon Advertising Console</a>
            <a class='pill' href='https://sellercentral.amazon.in/attribution/overview' target='_blank'>Amazon Attribution</a>
            <a class='pill' href='https://advertising.amazon.in/tools/bulk-operations' target='_blank'>Bulk Operations</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "All campaigns follow consistent naming convention",
        "Campaigns structured: 1 ASIN or 1 targeting type per ad group",
        "Bulk operations used weekly for bid optimisation",
        "Amazon Attribution tags live for all external channels",
        "Brand Referral Bonus enrolled",
        "3P advertising tool evaluated if managing &gt;50 campaigns"
    ],
    "quiz": [
        {
            "question": "What is the recommended campaign structure for Sponsored Products?",
            "options": [
                "All ASINs in one campaign",
                "1 ASIN per ad group, separate campaigns per match type",
                "All match types in one ad group",
                "1 brand per campaign"
            ],
            "answer": "1 ASIN per ad group, separate campaigns per match type",
            "explanation": "This structure gives granular budget control and performance visibility per ASIN, and separates exact/phrase/broad match types to allow different bid strategies."
        }
    ]
},

{
    "id": "6.4",
    "number": "Module 6.4",
    "title": "3P Tools",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": """<p>Third-party tools extend Amazon's native capabilities in keyword research, competitor intelligence, inventory management, and review management. This module covers the key tools used by top Amazon India sellers and when to invest in each.</p>""",
    "content": """
        <h3>1. Keyword Research Tools</h3>
        <table class='data-table'>
            <thead><tr><th>Tool</th><th>Best For</th><th>India-Specific?</th></tr></thead>
            <tbody>
                <tr><td>Helium 10 Cerebro</td><td>Reverse ASIN lookup — find competitor keywords</td><td>Partial (India data improving)</td></tr>
                <tr><td>DataHawk</td><td>India-specific keyword rank tracking</td><td>Yes — India focused</td></tr>
                <tr><td>SellerApp</td><td>India keyword research + BSR tracking</td><td>Yes — India built</td></tr>
                <tr><td>Jungle Scout</td><td>Product/keyword opportunity research</td><td>Limited India data</td></tr>
            </tbody>
        </table>
        <div class='callout pro-tip'>
            <div><strong>For Amazon India specifically,</strong> DataHawk and SellerApp have the best local data quality. Helium 10 is excellent for global benchmarking but India search volume data is less reliable than US data.</div>
        </div>

        <h3>2. Competitor Intelligence Tools</h3>
        <ul>
            <li><strong>Keepa (India):</strong> Price history, BSR history, review history over time — essential for competitive analysis</li>
            <li><strong>Jungle Scout Cobalt:</strong> Market share, competitive landscape, new product launches</li>
            <li><strong>SellerApp Competitor Intelligence:</strong> India-specific competitor ASIN tracking</li>
        </ul>
        <p>Use Keepa weekly to monitor: competitor pricing strategies, inventory gaps (when a competitor goes OOS = opportunity to increase ad bids).</p>

        <h3>3. Inventory Management Tools</h3>
        <table class='data-table'>
            <thead><tr><th>Tool</th><th>Use Case</th></tr></thead>
            <tbody>
                <tr><td>Unicommerce</td><td>India's leading OMS — multi-channel inventory sync for omnichannel sellers</td></tr>
                <tr><td>Linnworks</td><td>Multi-warehouse, multi-channel inventory for scaling brands</td></tr>
                <tr><td>Browntape</td><td>India-focused multi-channel order &amp; inventory management</td></tr>
            </tbody>
        </table>

        <h3>4. Review Management Tools</h3>
        <ul>
            <li><strong>FeedbackWhiz:</strong> Automated review request sequences (compliant with Amazon ToS), negative review alerts</li>
            <li><strong>Jungle Scout Alerts:</strong> Real-time review monitoring across all ASINs</li>
            <li><strong>SellerApp Review Automation:</strong> India-optimised review request timing</li>
        </ul>

        <h3>5. PPC Automation Platforms</h3>
        <div class='callout info'>
            <div><strong>For brands with 50+ campaigns:</strong><br>
            • <strong>Pacvue:</strong> Enterprise, dayparting, portfolio bidding<br>
            • <strong>Perpetua:</strong> AI-driven bid optimisation, stream-optimised<br>
            • <strong>Scale Insights:</strong> Rule-based automation with granular control<br>
            • <strong>SellerApp Ads:</strong> India-native, most cost-effective for local brands</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://www.helium10.com' target='_blank'>Helium 10</a>
            <a class='pill' href='https://www.datahawk.co' target='_blank'>DataHawk</a>
            <a class='pill' href='https://www.sellerapp.com' target='_blank'>SellerApp</a>
            <a class='pill' href='https://www.keepa.com' target='_blank'>Keepa</a>
            <a class='pill' href='https://www.unicommerce.com' target='_blank'>Unicommerce</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Keyword research tool selected and integrated into weekly workflow",
        "Competitor ASINs tracked in Keepa for price/BSR history",
        "Inventory management tool implemented if selling on 2+ channels",
        "Review automation tool set up (FeedbackWhiz or SellerApp)",
        "PPC automation evaluated if managing &gt;50 campaigns"
    ],
    "quiz": [
        {
            "question": "Which tool provides the most accurate Amazon India keyword and BSR data?",
            "options": ["Helium 10", "Jungle Scout", "DataHawk / SellerApp (India-focused)", "Google Keyword Planner"],
            "answer": "DataHawk / SellerApp (India-focused)",
            "explanation": "DataHawk and SellerApp are built with Amazon India as a primary market. They have local data crawlers that provide more accurate India-specific keyword volume and BSR data than US-first tools."
        }
    ]
},

{
    "id": "6.5",
    "number": "Module 6.5",
    "title": "Manage Your Experiments",
    "difficulty": "Advanced",
    "time": "30 mins",
    "overview": """<p>Manage Your Experiments (MYE) is Amazon's native A/B testing tool for Brand Registered sellers. Split traffic between two versions of your title, main image, or A+ Content — and let data decide which converts better. This module covers MYE setup, test design, results interpretation, and rollout.</p>""",
    "content": """
        <h3>1. MYE Eligibility Requirements</h3>
        <div class='callout pro-tip'>
            <div><strong>Eligibility checklist:</strong><br>
            ✓ Brand Registry enrolled and approved<br>
            ✓ ASIN has sufficient traffic (Amazon typically requires 30+ sessions/week)<br>
            ✓ You are the brand owner (not a reseller) on the ASIN<br>
            ✓ A+ Content published on the ASIN (for A+ testing)<br><br>
            Path: SC → Growth → Manage Your Experiments</div>
        </div>

        <h3>2. What You Can Test</h3>
        <table class='data-table'>
            <thead><tr><th>Experiment Type</th><th>Elements</th><th>Primary Metric</th></tr></thead>
            <tbody>
                <tr><td>Product Title</td><td>Title text (both versions must be policy-compliant)</td><td>Sales / session</td></tr>
                <tr><td>Main Image</td><td>Two different main images</td><td>Click-through rate</td></tr>
                <tr><td>A+ Content</td><td>Two different A+ modules/layouts</td><td>Conversion rate</td></tr>
                <tr><td>Bullet Points</td><td>Different benefit ordering</td><td>Conversion rate</td></tr>
            </tbody>
        </table>

        <h3>3. Test Design Best Practices</h3>
        <ul>
            <li><strong>One variable at a time:</strong> Don't change title AND image in the same experiment</li>
            <li><strong>Hypothesis-driven:</strong> Define expected outcome before launching ("We expect Version B to increase CVR by 5% because benefit-first bullets")</li>
            <li><strong>Minimum duration:</strong> 4 weeks (Amazon recommends 4–8 weeks for significance)</li>
            <li><strong>Don't run during deals:</strong> Promotions skew conversion data</li>
        </ul>

        <h3>4. Interpreting & Rolling Out Results</h3>
        <div class='callout success'>
            <div><strong>MYE Results Reading:</strong><br>
            • <strong>Statistically significant winner:</strong> Roll out immediately to 100% of traffic<br>
            • <strong>Inconclusive result:</strong> Extend test duration or redesign more differentiated versions<br>
            • <strong>Surprising loser:</strong> Investigate — could be device-type split (mobile vs desktop)</div>
        </div>
        <p>Keep a test log: what was tested, hypothesis, result, action taken. Over 12 months, this compound learning is a competitive moat.</p>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/manage-your-experiments' target='_blank'>Manage Your Experiments</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "MYE eligibility confirmed — Brand Registry active",
        "At least 1 active experiment running on top 5 ASINs at all times",
        "Tests run for minimum 4 weeks (no deals during test period)",
        "One variable changed per experiment",
        "Test log maintained with hypothesis, result, and rollout action",
        "Winners rolled out to 100% within 1 week of significance"
    ],
    "quiz": [
        {
            "question": "What is the minimum recommended duration for a Manage Your Experiments test?",
            "options": ["1 week", "2 weeks", "4 weeks", "8 weeks"],
            "answer": "4 weeks",
            "explanation": "Amazon recommends 4–8 weeks minimum for statistical significance. Tests shorter than 4 weeks may not have enough traffic to produce reliable results, especially for lower-volume ASINs."
        }
    ]
}
,

# ─────────────────────────────────────────────────────────────
{
    "id": "6.6",
    "number": "Module 6.6",
    "title": "Kitna Milega — Profitability Calculator & Margin Mastery",
    "difficulty": "Intermediate",
    "time": "45 mins",
    "overview": """<p>"Kitna Milega" literally means "How much will I get?" — and it is Amazon India's official FBA Revenue Calculator. This module goes beyond the tool: it teaches the complete Amazon profitability framework, all 6 fee components, the impact of the March 2026 Zero Referral Fee expansion, and how to engineer your pricing strategy for maximum margin across every product category.</p>""",
    "content": """
        <h3>1. The Kitna Milega Tool</h3>
        <p>Amazon India's FBA Revenue Calculator (nicknamed "Kitna Milega" — Hindi for "How much will I get?") is the official seller tool for comparing FBA vs. FBM profitability side-by-side. Access it at <strong>sellercentral.amazon.in/fba/profitabilitycalculator</strong>.</p>
        <div class='callout pro-tip'><div><strong>What the Calculator Does:</strong><br>
        ✅ Compares FBA vs. FBM (self-ship) side-by-side<br>
        ✅ Auto-calculates all Amazon fees (referral, weight handling, fulfillment)<br>
        ✅ Shows your net revenue per order<br>
        ✅ Helps decide whether to switch from FBM to FBA for each product<br>
        ⚠️ Does NOT include COGS, advertising costs, or storage fees — you must add those manually.</div></div>

        <h3>2. The 6 Fee Components Every Seller Must Know</h3>
        <table class='data-table'>
            <thead><tr><th>#</th><th>Fee</th><th>Rate / Basis</th><th>Tip</th></tr></thead>
            <tbody>
                <tr><td>1</td><td><strong>Referral Fee</strong></td><td>0–24% of selling price (category-dependent)</td><td>ZERO for ≤₹1,000 in 1,800+ categories (Mar 2026)</td></tr>
                <tr><td>2</td><td><strong>Closing Fee</strong></td><td>₹5–₹6 flat per order</td><td>Applies to all orders regardless of fulfillment method</td></tr>
                <tr><td>3</td><td><strong>Weight Handling Fee</strong></td><td>₹73–₹200+ based on weight slab</td><td>FBA only; check chargeable weight (actual vs. volumetric)</td></tr>
                <tr><td>4</td><td><strong>Monthly Storage Fee</strong></td><td>₹50/cu.ft/month (Nov 2025+)</td><td>Higher during Oct–Dec peak season</td></tr>
                <tr><td>5</td><td><strong>Aged Inventory Surcharge</strong></td><td>Monthly billing from 271+ days</td><td>Set removal alerts at 250 days</td></tr>
                <tr><td>6</td><td><strong>GST on Fees</strong></td><td>18% applied to all fees (1–5 above)</td><td>Multiply every fee by 1.18 for true cost</td></tr>
            </tbody>
        </table>

        <h3>3. The SMEMinds Profitability Formula</h3>
        <div class='callout success'><div><strong>Net Profit per Unit = </strong><br>
        Selling Price<br>
        − Referral Fee × 1.18 (if applicable)<br>
        − Closing Fee × 1.18<br>
        − Weight Handling Fee × 1.18 (FBA only)<br>
        − Monthly Storage Cost allocation<br>
        − Cost of Goods Sold (COGS)<br>
        − Advertising Cost (ACoS allocation)<br>
        − Returns Provision (category return rate × average return cost)<br>
        <strong>= Net Profit (₹) | Net Margin (%)</strong></div></div>

        <h3>4. Three Scenarios — Worked Examples</h3>
        <table class='data-table'>
            <thead><tr><th>Scenario</th><th>Selling Price</th><th>Category</th><th>COGS</th><th>Weight</th><th>Net Profit</th><th>Margin</th></tr></thead>
            <tbody>
                <tr><td><strong>Budget Hero</strong></td><td>₹599</td><td>Apparel (≤₹1k → 0% ref)</td><td>₹180</td><td>300g (₹73)</td><td>₹326</td><td>54.4%</td></tr>
                <tr><td><strong>Mid-Range</strong></td><td>₹1,499</td><td>Fashion (10% ref)</td><td>₹450</td><td>600g (₹98)</td><td>₹703</td><td>46.9%</td></tr>
                <tr><td><strong>Premium</strong></td><td>₹3,999</td><td>Electronics (8% ref)</td><td>₹1,800</td><td>1.2kg (₹131)</td><td>₹1,560</td><td>39.0%</td></tr>
            </tbody>
        </table>
        <p style="font-size:12px;color:var(--text-muted)">*All examples include 18% GST on fees. Storage and advertising costs not included — add ~₹30–₹80 per unit for complete picture.</p>

        <h3>5. Price Point Engineering — The ₹1,000 Threshold Strategy</h3>
        <div class='callout pro-tip'><div><strong>The Zero Fee Sweet Spot (Mar 2026+):</strong><br>
        Products priced ≤₹1,000 now attract ZERO referral fees in 1,800+ categories.<br><br>
        <strong>Example: Apparel product</strong><br>
        At ₹999: Referral Fee = ₹0 → Net higher by ₹70–₹140 vs. pricing at ₹1,099<br>
        At ₹1,099: Referral Fee = 7–10% = ₹77–₹110 → Margin drops 7–10%<br><br>
        <strong>Action:</strong> Model your price elasticity. If demand doesn't meaningfully increase at ₹999 vs. ₹1,099, price at ₹999 and pocket the referral fee saving.</div></div>

        <h3>6. Chargeable Weight — The Hidden Fee Multiplier</h3>
        <p>Amazon uses the <strong>higher</strong> of actual weight vs. volumetric weight for FBA fee calculation.</p>
        <p><strong>Volumetric Weight Formula:</strong> (Length × Breadth × Height in cm) ÷ 5,000 = Volumetric Weight in kg</p>
        <div class='callout warning'><div><strong>Example:</strong> A product weighs 400g but is in a large box (40×30×15cm).<br>
        Volumetric weight = (40×30×15) ÷ 5,000 = 3.6 kg → Amazon charges 3.6 kg slab (₹200+ fee, not ₹73).<br>
        <strong>Fix:</strong> Reduce packaging size. Right-size your boxes — packaging that's too large costs you ₹127+ extra per unit in weight handling alone.</div></div>

        <h3>7. FBA vs FBM Decision Framework</h3>
        <table class='data-table'>
            <thead><tr><th>Factor</th><th>Use FBA</th><th>Use FBM</th></tr></thead>
            <tbody>
                <tr><td>Order volume</td><td>&gt;50 orders/day</td><td>&lt;20 orders/day</td></tr>
                <tr><td>Product weight</td><td>&lt;2 kg (low weight handling fee)</td><td>&gt;5 kg (high weight fee erodes margin)</td></tr>
                <tr><td>Inventory turnover</td><td>Fast-moving (&lt;60 days)</td><td>Slow-moving (storage fees mount for FBA)</td></tr>
                <tr><td>Buy Box priority</td><td>FBA wins Buy Box more easily</td><td>FBM needs compensating low price</td></tr>
                <tr><td>Peak season</td><td>FBA handles scale automatically</td><td>FBM requires operational capacity surge</td></tr>
            </tbody>
        </table>

        <div class='bookmarks-inline'>
            <strong>Tools &amp; Resources:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/fba/profitabilitycalculator/index?lang=en_IN' target='_blank'>Kitna Milega — Official Calculator</a>
            <a class='btn-sc' href='https://sell.amazon.in/fees-and-pricing' target='_blank'>Amazon India Fee Schedule</a>
            <a class='pill-sc' href='https://www.aboutamazon.in/news/small-business/amazon-seller-fee-reduction-zero-referral-march-2026' target='_blank'>Zero Fee Announcement</a>
            <a class='pill' href='https://rekonsile.com/amazon-india-fee-revision-september-2025-complete-guide' target='_blank'>Sep 2025 Fee Revision Guide</a>
            <a class='pill' href='https://rekonsile.com/amazon-india-shipping-fees-2025-complete-guide-of-fba-fbm-and-weight-handling-charges' target='_blank'>Shipping Fees Complete Guide 2025</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller sells 1,000 units/month at ₹1,049 price point — paying 10% referral fee (₹1,04,900/month in fees alone). Post-March 2026, moving to ₹999 price point eliminates referral fee entirely, saving ₹99,000/month — more than their marketing budget.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Audit every ASIN priced ₹1,001–₹1,500. For each one: model impact of pricing at ₹999 vs. current price. Factor in demand elasticity and margin impact. Most fashion/lifestyle products should move to ≤₹1,000 pricing.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>The "hidden" fee killer is oversized packaging. A seller shipping a 500g product in a large box pays ₹200+ weight handling instead of ₹73 — an extra ₹127 per unit × 1,000 units/month = ₹1,27,000 wasted. Right-size your packaging before scaling.</p></div>
            </div>
        </div>
    """,
    "checklist": [
        "Ran Kitna Milega calculator for every active ASIN",
        "All 6 fee components included in profitability model (not just referral fee)",
        "Audited all ASINs priced ₹1,001–₹1,500 for ₹999 pricing opportunity",
        "Calculated chargeable weight (actual vs. volumetric) for all FBA products",
        "Right-sized packaging for top 10 ASINs by volume",
        "Set storage removal alerts at 250-day mark for all FBA inventory",
        "Built Google Sheet P&L model including advertising cost and returns provision"
    ],
    "quiz": [
        {
            "question": "'Kitna Milega' translates to and is officially used for:",
            "options": ["'Best Price' — Amazon's dynamic pricing tool", "'How much will I get?' — Amazon India's FBA Revenue Calculator", "'Guaranteed Delivery' — Amazon India's shipping SLA tool", "'Smart Pricing' — Amazon's automated repricing system"],
            "answer": "'How much will I get?' — Amazon India's FBA Revenue Calculator",
            "explanation": "'Kitna Milega' means 'How much will I get?' in Hindi and is the colloquial name for Amazon India's official FBA Revenue Calculator. It compares FBA vs. FBM profitability side-by-side and calculates all Amazon deductions automatically."
        },
        {
            "question": "A product has actual weight 400g but box dimensions of 40×30×15cm. What chargeable weight does Amazon use?",
            "options": ["400g (actual weight)", "3.6 kg (volumetric weight — higher)", "1 kg (rounded up)", "500g (standard slab)"],
            "answer": "3.6 kg (volumetric weight — higher)",
            "explanation": "Volumetric weight = (40×30×15) ÷ 5,000 = 3.6 kg. Amazon uses the HIGHER of actual vs. volumetric weight. Since 3.6 kg > 400g, you pay the 3.6 kg fee slab — costing ₹200+ vs. ₹73 for the 0–500g slab. Right-sizing the box saves ₹127+ per unit."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "6.7",
    "number": "Module 6.7",
    "title": "Subscribe & Save, MOQ & AUR Strategy",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": """<p>Three underutilised Amazon India tools — Subscribe &amp; Save, Minimum Order Quantity (MOQ), and Average Unit Revenue (AUR) optimisation — can dramatically improve your revenue quality without increasing ad spend. This module covers all three with implementation SOPs and the strategic context for when each works best.</p>""",
    "content": """
        <h3>1. Subscribe &amp; Save — Recurring Revenue on Amazon India</h3>
        <p>Subscribe &amp; Save (SNS) lets customers subscribe to regular deliveries (monthly, bi-monthly, etc.) at a discounted price. Sellers fund the discount; Amazon manages the recurring order logistics.</p>

        <h3>2. SNS Eligibility &amp; Setup</h3>
        <ul>
            <li>Available for: FMCG, grocery, personal care, health supplements, pet food, household products</li>
            <li>Requires: FBA fulfillment (SNS not available for FBM)</li>
            <li>Requires: Professional Seller Plan + consistent inventory availability</li>
            <li>Typical seller discount: 5–10% (Amazon may add additional platform discount)</li>
        </ul>
        <ol>
            <li>Go to <strong>Advertising → Subscribe &amp; Save</strong> in Seller Central</li>
            <li>Select eligible ASINs to enroll</li>
            <li>Set your seller discount % (minimum 0%, typically 5%)</li>
            <li>Maintain consistent inventory (SNS requires &gt;30 days stock at all times)</li>
            <li>Monitor SNS subscriber count and revenue in SNS dashboard</li>
        </ol>

        <h3>3. SNS Business Value</h3>
        <table class='data-table'>
            <thead><tr><th>Metric</th><th>Without SNS</th><th>With SNS</th></tr></thead>
            <tbody>
                <tr><td>Revenue predictability</td><td>Variable month-to-month</td><td>Recurring base revenue locked in</td></tr>
                <tr><td>Customer acquisition cost</td><td>Full ad spend per order</td><td>Zero ad cost on renewals</td></tr>
                <tr><td>Inventory planning</td><td>Demand forecasting required</td><td>Predictable demand from subscribers</td></tr>
                <tr><td>Customer LTV</td><td>Single purchase</td><td>12–24 month subscriber lifecycle</td></tr>
            </tbody>
        </table>

        <h3>4. Minimum Order Quantity (MOQ) Strategy</h3>
        <p>MOQ allows B2B sellers to set minimum quantities that business buyers must purchase. This is particularly powerful for bulk consumables, packaging materials, and commodity products.</p>
        <ul>
            <li>Navigate to <strong>Inventory → Business Settings → MOQ Settings</strong></li>
            <li>Set MOQ per ASIN (e.g., minimum 5 units per order for a 10-pack tissue)</li>
            <li>MOQ applies only to B2B buyers — consumer orders are unaffected</li>
            <li>Combine with B2B bulk pricing tiers for maximum impact</li>
        </ul>

        <h3>5. Average Unit Revenue (AUR) Optimisation</h3>
        <p>AUR = Total Revenue ÷ Total Units Sold. Increasing AUR without proportional increase in costs is the fastest path to margin improvement.</p>
        <div class='callout success'><div><strong>5 Ways to Increase AUR:</strong><br>
        1. <strong>Bundle creation:</strong> 2-pack or 3-pack at premium price vs. singles<br>
        2. <strong>Premium variant introduction:</strong> Add a "Pro" version at 30–50% premium<br>
        3. <strong>Price architecture:</strong> Remove your lowest-priced variant, push customers to mid/high<br>
        4. <strong>Cross-sell via Virtual Bundles:</strong> Pair complementary products<br>
        5. <strong>Upsell via A+ content:</strong> Compare table showing premium option benefits</div></div>

        <h3>6. AUR Tracker — Weekly Review</h3>
        <ol>
            <li>Go to <strong>Reports → Sales → Sales by ASIN</strong></li>
            <li>Export weekly sales data (units + revenue)</li>
            <li>Calculate AUR per ASIN: Revenue ÷ Units</li>
            <li>Identify ASINs with declining AUR (price erosion signal)</li>
            <li>Identify ASINs where bundle/premium variant could increase AUR</li>
            <li>Set AUR target per category: target 10% improvement per quarter</li>
        </ol>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/sns/manage' target='_blank'>Subscribe &amp; Save Dashboard</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/business/reports' target='_blank'>B2B Reports</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/gp/help/external/G201664430' target='_blank'>SNS Help Guide</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller in personal care category spends ₹80,000/month on PPC to acquire buyers — but has zero Subscribe &amp; Save enrollment, so every customer is a one-time acquisition with full ad cost attached.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Enroll all FMCG/consumable ASINs in SNS immediately. Even 200 SNS subscribers × ₹500 AOV = ₹1,00,000 in monthly recurring revenue with zero incremental ad cost. One-time customer acquisition pays for itself on repeat orders.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>AUR optimisation is more powerful than volume growth. Increasing AUR from ₹450 to ₹550 (+22%) on 1,000 units/month = ₹1,00,000 extra monthly revenue with identical operations, ad spend, and FBA costs.</p></div>
            </div>
        </div>
    """,
    "checklist": [
        "Enrolled all eligible FMCG/consumable ASINs in Subscribe & Save",
        "Maintained 30+ days FBA inventory for all SNS-enrolled ASINs",
        "Set SNS discount at 5–7% (competitive but margin-safe)",
        "B2B MOQ set for bulk-eligible ASINs",
        "AUR tracking added to weekly review (Revenue ÷ Units by ASIN)",
        "Bundle creation roadmap drafted for top 5 ASINs by volume",
        "A+ content comparison table created showing premium variant benefits"
    ],
    "quiz": [
        {
            "question": "Subscribe & Save on Amazon India is available for which fulfillment method?",
            "options": ["FBM only", "FBA only", "Both FBA and FBM", "Easy Ship only"],
            "answer": "FBA only",
            "explanation": "Subscribe & Save requires FBA fulfillment. FBM sellers cannot enroll in SNS. Products must be eligible for FBA and maintain consistent inventory availability for recurring subscription deliveries."
        },
        {
            "question": "A seller has ₹10 lakh monthly revenue selling 2,000 units. AUR = ₹500. To improve AUR to ₹600 without volume change, monthly revenue becomes:",
            "options": ["₹10 lakh (unchanged)", "₹11 lakh", "₹12 lakh", "₹14 lakh"],
            "answer": "₹12 lakh",
            "explanation": "AUR improvement to ₹600 on 2,000 units = ₹12,00,000 monthly revenue — a 20% revenue increase with zero additional units, ads, or operational changes. This is the power of AUR optimisation."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "6.8",
    "number": "Module 6.8",
    "title": "LTSF & Inventory Age Management",
    "difficulty": "Intermediate",
    "time": "30 mins",
    "overview": """<p>Long-Term Storage Fees (now called Aged Inventory Surcharges) switched to monthly billing in 2025 — meaning slow-moving inventory silently drains profitability every single month. This module covers the current surcharge structure, how to read your Inventory Age View, the removal order SOP, and how to keep your IPI score healthy.</p>""",
    "content": """
        <h3>1. The 2025 Billing Change — Monthly AIS</h3>
        <div class='callout warning'><div><strong>Important Change:</strong> From 2025, Amazon shifted from twice-yearly LTSF billing (February &amp; August) to <strong>monthly Aged Inventory Surcharge (AIS)</strong>. Inventory aged 271+ days now incurs ongoing monthly charges — not a once-yearly penalty. This makes early action critical.</div></div>

        <h3>2. Current Aged Inventory Surcharge Structure</h3>
        <table class='data-table'>
            <thead><tr><th>Inventory Age</th><th>AIS Rate</th><th>Action</th></tr></thead>
            <tbody>
                <tr><td>0–270 days</td><td>No surcharge</td><td>Monitor sell-through rate</td></tr>
                <tr><td>271–365 days</td><td>Surcharge applies monthly</td><td>Run promotions, reduce price</td></tr>
                <tr><td>365+ days</td><td>₹15.65/cu.ft or ₹15/unit (whichever higher)</td><td>Create removal order immediately</td></tr>
            </tbody>
        </table>

        <h3>3. Inventory Age View — How to Read It</h3>
        <ol>
            <li>Go to <strong>Inventory → Inventory Planning → Inventory Age</strong></li>
            <li>View age breakdown per ASIN: 0–90 | 91–180 | 181–270 | 271–365 | 365+ days</li>
            <li>Filter by "271+ days" to see all at-risk inventory</li>
            <li>Sort by "Estimated Storage Fee" to prioritize by cost impact</li>
            <li>Set a weekly calendar alert to review this report every Monday</li>
        </ol>

        <h3>4. Removing Aged Inventory (SOP)</h3>
        <ol>
            <li>Go to <strong>Inventory → Manage FBA Inventory → Create Removal Order</strong></li>
            <li>Select ASINs aged 250+ days (act before 271 to avoid first surcharge)</li>
            <li>Choose removal method: Return to Address OR Dispose</li>
            <li>For returnable products: return to warehouse and attempt liquidation on other channels</li>
            <li>For unsellable/damaged: dispose at Amazon's facility (lower cost than return)</li>
            <li>Removal SLA: 14–21 days processing</li>
        </ol>

        <h3>5. IPI Score — Inventory Performance Index</h3>
        <table class='data-table'>
            <thead><tr><th>IPI Score</th><th>Status</th><th>Impact</th></tr></thead>
            <tbody>
                <tr><td>550+</td><td>Excellent</td><td>Unlimited FBA storage</td></tr>
                <tr><td>400–549</td><td>Good</td><td>Standard storage limits</td></tr>
                <tr><td>350–399</td><td>At Risk</td><td>Reduced storage limits</td></tr>
                <tr><td>Below 350</td><td>Critical</td><td>Severe storage restrictions</td></tr>
            </tbody>
        </table>

        <h3>6. IPI Improvement Actions</h3>
        <ul>
            <li>✅ Maintain sell-through rate &gt;2 units/week per ASIN</li>
            <li>✅ Keep in-stock rate &gt;98% for top-selling ASINs</li>
            <li>✅ Keep excess inventory &lt;10% of total stock</li>
            <li>✅ Reduce unfulfillable units (create removal orders for damaged stock)</li>
            <li>✅ Use Sponsored Products to accelerate sell-through on aging ASINs</li>
            <li>✅ Use coupons (5–10% off) to move inventory before the 271-day mark</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/inventory-planning/inventory-age' target='_blank'>Inventory Age View</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/inventory-planning/stranded-inventory' target='_blank'>Inventory Health Dashboard</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/gp/help/external/200725880' target='_blank'>Aged Inventory Surcharge Help</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller sends 1,000 units of a slow-moving product to FBA. After 12 months, ₹15/unit × 1,000 units = ₹15,000/month in AIS charges — on top of ₹50/cu.ft monthly storage. Total cost: ₹25,000+/month for inventory that sells at 5 units/month.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Set a "250-day alert" calendar for every FBA ASIN. At 250 days, run a 15% coupon and Sponsored Products boost for 30 days. At 270 days, if still aging, create removal order. Never let inventory hit 365 days — the surcharge at that point exceeds the product value for many SKUs.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>The IPI score is a leading indicator of hidden costs. An IPI below 400 means Amazon is signaling you have too much slow-moving stock. Fix it proactively — removal orders + sell-through campaigns — before Amazon imposes storage limits that prevent you from sending new inventory during peak season.</p></div>
            </div>
        </div>
    """,
    "checklist": [
        "Inventory Age View reviewed weekly (filter: 271+ days)",
        "Removal orders created for all inventory aged 250+ days",
        "IPI score monitored monthly (target 550+)",
        "Sell-through rate above 2 units/week for all FBA ASINs",
        "In-stock rate above 98% for top-selling products",
        "Excess inventory below 10% of total FBA stock",
        "Coupon or Lightning Deal planned for ASINs approaching 270 days"
    ],
    "quiz": [
        {
            "question": "When did Amazon India switch from twice-yearly LTSF billing to monthly Aged Inventory Surcharge?",
            "options": ["2022", "2023", "2024", "2025"],
            "answer": "2025",
            "explanation": "In 2025, Amazon shifted from twice-yearly LTSF billing (February & August) to monthly Aged Inventory Surcharge (AIS). Inventory aged 271+ days now incurs ongoing monthly charges, making early action critical."
        },
        {
            "question": "At what inventory age should sellers proactively create removal orders to avoid the first AIS charge?",
            "options": ["180 days", "200 days", "250 days", "300 days"],
            "answer": "250 days",
            "explanation": "AIS charges begin at 271 days. Creating a removal order at 250 days gives 14–21 days processing time, ensuring inventory is removed before the first monthly surcharge kicks in at 271 days."
        }
    ]
}

]
