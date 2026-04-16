# ══════════════════════════════════════════════════════════════
# PILLAR 4 — CONVERSION  (5 Modules)
# ══════════════════════════════════════════════════════════════

pillar4_modules = [

{
    "id": "4.1",
    "number": "Module 4.1",
    "title": "Detail Page CRO",
    "difficulty": "Advanced",
    "time": "40 mins",
    "overview": """<p>Conversion Rate Optimisation (CRO) on your Amazon detail page can double your revenue without spending a rupee more on ads. This module covers above-the-fold audits, A/B testing with Manage Your Experiments, bullet point copywriting, Q&A management, Buy Box optimisation, and unit session percentage benchmarking.</p>""",
    "content": """
        <h3>1. Above-the-Fold Content Audit</h3>
        <div class='callout pro-tip'>
            <div><strong>Above-the-fold = what a customer sees before scrolling on mobile.</strong><br>
            Elements visible without scrolling on most Android/iPhone screens:<br>
            ✓ Main image (largest element — make it count)<br>
            ✓ Title (first 80 chars)<br>
            ✓ Price + any coupon/deal badge<br>
            ✓ Star rating + review count<br>
            ✓ Prime delivery badge<br>
            ✓ Add to Cart / Buy Now buttons<br><br>
            Audit monthly: Are all above-fold elements optimised?</div>
        </div>

        <h3>2. Split Testing via Manage Your Experiments (MYE)</h3>
        <table class='data-table'>
            <thead><tr><th>What to Test</th><th>Duration</th><th>Metric</th></tr></thead>
            <tbody>
                <tr><td>Main image</td><td>4–8 weeks</td><td>CTR (click-through rate)</td></tr>
                <tr><td>Title</td><td>4–8 weeks</td><td>Sales per session</td></tr>
                <tr><td>A+ Content</td><td>8–12 weeks</td><td>Conversion rate</td></tr>
                <tr><td>Bullet points</td><td>4–8 weeks</td><td>Conversion rate</td></tr>
            </tbody>
        </table>
        <p><strong>Path:</strong> SC → Growth → Manage Your Experiments → Create New Experiment</p>
        <div class='callout info'>
            <div><strong>MYE eligibility:</strong> Requires Brand Registry. ASIN must have sufficient traffic (typically 50+ sessions/week) for statistical significance.</div>
        </div>

        <h3>3. Benefit-First Bullet Point Copywriting</h3>
        <div class='callout success'>
            <div><strong>Conversion-optimised bullet formula:</strong><br>
            <code>BENEFIT (what it does FOR you) + FEATURE (how/what)</code><br><br>
            ✗ Bad: "Made of 304 stainless steel with double-wall vacuum insulation"<br>
            ✓ Good: "STAYS COLD 24 HOURS — double-wall vacuum insulation locks temperature, no condensation"</div>
        </div>

        <h3>4. Q&A (Answered Questions) Management</h3>
        <ul>
            <li>Seed 5–10 high-impact questions as a brand (use different accounts or ask team)</li>
            <li>Questions should cover top buyer objections: size/fit, compatibility, ingredients, warranty</li>
            <li>Monitor daily for new customer questions — respond within 24 hours</li>
            <li>Unanswered questions signal poor customer service to prospects</li>
        </ul>

        <h3>5. Buy Box Optimisation & CVR Benchmarking</h3>
        <p>Unit Session Percentage (USP) = Conversion Rate:<br>
        <strong>SC → Business Reports → Detail Page Sales → Unit Session Percentage</strong></p>
        <table class='data-table'>
            <thead><tr><th>Category</th><th>Average USP</th><th>Target</th></tr></thead>
            <tbody>
                <tr><td>Books</td><td>20–30%</td><td>&gt;25%</td></tr>
                <tr><td>Electronics</td><td>5–10%</td><td>&gt;8%</td></tr>
                <tr><td>Home &amp; Kitchen</td><td>8–15%</td><td>&gt;10%</td></tr>
                <tr><td>Apparel</td><td>5–10%</td><td>&gt;8%</td></tr>
                <tr><td>Beauty</td><td>10–20%</td><td>&gt;12%</td></tr>
            </tbody>
        </table>

        <h3>6. Price-to-Value Perception</h3>
        <div class='callout pro-tip'>
            <div><strong>Reference Price (Was price):</strong> Must reflect real historical selling price (Amazon verifies). A valid ₹999 → ₹599 strikethrough increases conversion by 10–20% by anchoring the perceived value.</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/manage-your-experiments' target='_blank'>Manage Your Experiments</a>
            <a class='pill' href='https://sellercentral.amazon.in/gp/site-metrics/report.html' target='_blank'>Business Reports (USP)</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Above-the-fold audit completed monthly on top 10 ASINs",
        "Manage Your Experiments running tests on main image and title",
        "All bullets rewritten in benefit-first format",
        "Q&A seeded with top 5–10 buyer objection questions",
        "Unit Session Percentage tracked weekly — above category benchmark",
        "Reference price (Was price) set on all ASINs with deal history"
    ],
    "quiz": [
        {
            "question": "What does Unit Session Percentage measure on Amazon?",
            "options": ["Ad conversion rate", "Organic conversion rate (orders per page visit)", "Return rate", "Buy Box win rate"],
            "answer": "Organic conversion rate (orders per page visit)",
            "explanation": "Unit Session Percentage = Total units ordered ÷ Total sessions. It's Amazon's measure of your listing's conversion rate — how many page visits become orders."
        },
        {
            "question": "What is the correct bullet point formula for maximum conversion?",
            "options": ["Feature → Benefit", "Specification → Compliance", "Benefit → Feature", "Price → Value"],
            "answer": "Benefit → Feature",
            "explanation": "Lead with the customer benefit (what it does FOR them), then back it with the feature (how). Benefit-first copywriting converts better because customers care about outcomes, not specifications."
        }
    ]
},

{
    "id": "4.2",
    "number": "Module 4.2",
    "title": "Promotions & Deals",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": """<p>Promotions are conversion accelerators — the right offer at the right time turns a browsing customer into a buyer. This module covers Subscribe &amp; Save, BOGOF, Amazon Pay promotions, EMI offers, and the path to Featured Merchant status.</p>""",
    "content": """
        <h3>1. Subscribe & Save — Recurring Revenue Engine</h3>
        <div class='callout pro-tip'>
            <div><strong>Subscribe &amp; Save (S&amp;S):</strong> Customers subscribe for regular deliveries in exchange for 5–15% discount.<br><br>
            Best for: FMCG, consumables, supplements, pet food, personal care<br>
            Enrolment: SC → Advertising → Subscribe &amp; Save → Enrol Products<br>
            Minimum discount: 5% (Amazon adds extra 10% if customer has 5+ active subscriptions)</div>
        </div>
        <p><strong>S&amp;S Strategy:</strong> Focus S&amp;S enrolment on your highest-margin consumables. S&amp;S customers have 3× higher lifetime value than one-time buyers.</p>

        <h3>2. BOGOF / Percentage-Off Promotions</h3>
        <table class='data-table'>
            <thead><tr><th>Promotion Type</th><th>Setup Path</th><th>Best For</th></tr></thead>
            <tbody>
                <tr><td>Buy One Get One Free</td><td>SC → Advertising → Promotions → Buy X Get Y</td><td>Clearing old stock, driving trial</td></tr>
                <tr><td>Percentage Off</td><td>SC → Advertising → Promotions → Percentage Off</td><td>Basket size increase, seasonal events</td></tr>
                <tr><td>Quantity Discount</td><td>SC → Advertising → Promotions → Tiered Pricing</td><td>B2B, multipacks</td></tr>
            </tbody>
        </table>

        <h3>3. Amazon Pay Cashback Promotions</h3>
        <ul>
            <li>Amazon Pay offers cashback on purchases made through Amazon Pay balance</li>
            <li>Sellers can co-fund cashback offers (visible to customer as "X% cashback with Amazon Pay")</li>
            <li>Funded jointly by Amazon and seller — contact your Amazon account manager</li>
            <li>Typical cashback: 5–20% on transactions ₹500+</li>
        </ul>

        <h3>4. No Cost EMI Strategy</h3>
        <div class='callout success'>
            <div><strong>No Cost EMI converts high-price hesitation into purchases.</strong><br>
            Products ₹3,000+: Enable No Cost EMI on major bank cards via SC → Manage Promotions → EMI<br>
            Amazon funds the interest cost — free for customers, no cost to seller for most card agreements.<br><br>
            Impact: 15–30% higher conversion on products ₹3K–₹50K price range.</div>
        </div>

        <h3>5. Featured Merchant Status</h3>
        <p>Featured Merchant (Sold by Amazon / Featured Offer) status requires:</p>
        <ul>
            <li>ODR &lt;1%, Cancellation Rate &lt;2.5%, LDR &lt;4%</li>
            <li>Account active for 90+ days</li>
            <li>Sufficient positive seller feedback</li>
            <li>FBA fulfilment (strongly preferred)</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/subscriptions' target='_blank'>Subscribe &amp; Save</a>
            <a class='pill' href='https://sellercentral.amazon.in/promotions' target='_blank'>Manage Promotions</a>
            <a class='pill' href='https://sellercentral.amazon.in/merchandising' target='_blank'>Deals &amp; Events</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Subscribe & Save enrolled for all eligible consumable ASINs",
        "No Cost EMI enabled on all ASINs ₹3,000+",
        "Promotional calendar set for BOGOF and % off events",
        "Amazon Pay cashback explored with account manager",
        "Featured Merchant status metrics monitored (ODR, LDR, Cancel Rate)"
    ],
    "quiz": [
        {
            "question": "What is the minimum S&S discount sellers must offer?",
            "options": ["2%", "5%", "10%", "15%"],
            "answer": "5%",
            "explanation": "Amazon requires a minimum 5% discount for Subscribe & Save enrolment. Amazon may add an additional 10% when customers have 5+ active subscriptions."
        },
        {
            "question": "At what price point does No Cost EMI have the most conversion impact?",
            "options": ["₹100–₹500", "₹500–₹1,000", "₹3,000–₹50,000", "₹1L+"],
            "answer": "₹3,000–₹50,000",
            "explanation": "No Cost EMI breaks the psychological barrier on higher-value purchases. Below ₹3K, customers rarely need EMI. Above ₹50K, other financial products take over."
        }
    ]
},

{
    "id": "4.3",
    "number": "Module 4.3",
    "title": "Social Proof",
    "difficulty": "Intermediate",
    "time": "30 mins",
    "overview": """<p>Social proof — star ratings, review count, and verified purchase rate — is the trust signal that converts a curious browser into a confident buyer. This module covers star rating targets, top review management, competitor benchmarking, and verified purchase rate tracking.</p>""",
    "content": """
        <h3>1. Star Rating Target: ≥4.0★</h3>
        <div class='callout pro-tip'>
            <div><strong>Star Rating Impact on Conversion:</strong><br>
            3.5★ → 4.0★: +25–40% conversion rate improvement<br>
            4.0★ → 4.5★: +10–15% improvement<br>
            4.5★ → 5.0★: Minimal additional impact (few products maintain 5★ at scale)<br><br>
            <strong>Target: ≥4.0★ minimum, 4.2–4.5★ optimal</strong></div>
        </div>

        <h3>2. Managing Top Reviews</h3>
        <ul>
            <li>Monitor your "Top Reviews" (sorted by Helpful votes) — these are what prospective buyers read first</li>
            <li>If a top review is negative: address the underlying issue → request customers mark accurate positive reviews as helpful</li>
            <li>Positive review content can be used (without names) in A+ Content and Brand Store — builds credibility</li>
            <li>Track in: SC → Performance → Voice of Customer → Review breakdown</li>
        </ul>

        <h3>3. Review Count Benchmarking vs Top 3 Competitors</h3>
        <table class='data-table'>
            <thead><tr><th>Your Review Count</th><th>vs Competitor</th><th>Competitive Position</th></tr></thead>
            <tbody>
                <tr><td>&lt;25% of #1 competitor</td><td>Significant gap</td><td>Aggressive review acquisition needed</td></tr>
                <tr><td>25–50%</td><td>Moderate gap</td><td>Vine + automation + deals</td></tr>
                <tr><td>50–100%</td><td>Competitive</td><td>Maintain velocity</td></tr>
                <tr><td>&gt;100%</td><td>Leader</td><td>Protect and grow lead</td></tr>
            </tbody>
        </table>

        <h3>4. Verified Purchase Review Rate</h3>
        <div class='callout success'>
            <div><strong>Verified Purchase (VP) reviews:</strong> Reviews from customers who actually purchased on Amazon. Amazon shows "Verified Purchase" badge prominently — these reviews are trusted far more by customers.<br><br>
            Target: &gt;80% of your reviews should be Verified Purchase.<br>
            Low VP rate is a red flag — can indicate review manipulation investigation.</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/voice-of-the-customer' target='_blank'>Voice of the Customer</a>
            <a class='pill' href='https://sellercentral.amazon.in/performance/feedback' target='_blank'>Feedback Manager</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Star rating ≥4.0 on all active ASINs",
        "Top reviews (by helpful votes) monitored and responded to",
        "Review count benchmarked vs top 3 competitors monthly",
        "Verified Purchase rate &gt;80% on all ASINs",
        "Voice of Customer report reviewed weekly"
    ],
    "quiz": [
        {
            "question": "What star rating threshold triggers the biggest conversion rate improvement?",
            "options": ["2.0 to 2.5", "3.5 to 4.0", "4.5 to 5.0", "1.0 to 2.0"],
            "answer": "3.5 to 4.0",
            "explanation": "Moving from 3.5★ to 4.0★ triggers a 25–40% conversion rate improvement — the biggest single star rating improvement for conversion. This is the critical threshold for customer trust."
        }
    ]
},

{
    "id": "4.4",
    "number": "Module 4.4",
    "title": "Post-Purchase",
    "difficulty": "Intermediate",
    "time": "30 mins",
    "overview": """<p>The post-purchase experience determines whether a customer returns and recommends you — or leaves a 1-star review and never comes back. This module covers packaging inserts, buyer-seller messaging, returns analysis, and PDR monitoring.</p>""",
    "content": """
        <h3>1. Packaging Insert Strategy</h3>
        <div class='callout pro-tip'>
            <div><strong>What's allowed on inserts:</strong><br>
            ✓ Warranty registration (your website, not incentivised)<br>
            ✓ Usage instructions / getting started guide<br>
            ✓ "Love it? Tell us" message (no review link with incentive)<br>
            ✓ Brand social handles<br>
            ✓ QR to brand experience page (how-to videos, FAQ)<br><br>
            ✗ NOT allowed: Offering discounts in exchange for reviews, directing only to leave positive reviews</div>
        </div>

        <h3>2. Buyer-Seller Messaging SOP</h3>
        <table class='data-table'>
            <thead><tr><th>Scenario</th><th>Response Time</th><th>Action</th></tr></thead>
            <tbody>
                <tr><td>Delivery question</td><td>24 hours</td><td>Check tracking, reassure</td></tr>
                <tr><td>Product issue / defect</td><td>24 hours</td><td>Replacement offer immediately</td></tr>
                <tr><td>Return request</td><td>24 hours</td><td>Approve and provide label</td></tr>
                <tr><td>Feature question</td><td>48 hours</td><td>Answer thoroughly, offer video link</td></tr>
            </tbody>
        </table>
        <p>Path: SC → Orders → Buyer-Seller Messages</p>

        <h3>3. Returns Rate Analysis & Root Cause</h3>
        <div class='callout success'>
            <div><strong>Return rate benchmarks (Amazon India):</strong><br>
            Electronics: 5–10% acceptable<br>
            Apparel: 15–25% acceptable (size/fit returns)<br>
            Home & Kitchen: 3–8% acceptable<br><br>
            Pull returns data: SC → Reports → Returns → Manage Returns</div>
        </div>
        <p>Top return reasons and fixes:</p>
        <ul>
            <li><strong>"Not as described"</strong> → Fix listing images/content</li>
            <li><strong>"Defective product"</strong> → QC improvement</li>
            <li><strong>"Size doesn't fit"</strong> → Add size chart, update dimensions in listing</li>
            <li><strong>"Arrived damaged"</strong> → Improve FBA packaging</li>
        </ul>

        <h3>4. Product Defect Rate (PDR) Monitoring</h3>
        <p>PDR is tracked via Voice of Customer: <strong>SC → Performance → Voice of the Customer</strong></p>
        <ul>
            <li>PDR includes: negative feedback, A-to-Z claims, and return rates combined</li>
            <li>Red ASIN (PDR &gt;10%): Investigate immediately</li>
            <li>Yellow ASIN (PDR 5–10%): Monitor closely</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/messaging/inbox' target='_blank'>Buyer-Seller Messages</a>
            <a class='pill' href='https://sellercentral.amazon.in/returns/list' target='_blank'>Manage Returns</a>
            <a class='pill' href='https://sellercentral.amazon.in/voice-of-the-customer' target='_blank'>Voice of the Customer</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [
        {"id": "GGLI_aIUO0M", "title": "Post-Purchase Excellence on Amazon India"}
    ],
    "checklist": [
        "Packaging inserts comply with Amazon ToS (no incentivised review requests)",
        "All buyer messages answered within 24 hours",
        "Returns rate tracked monthly per ASIN — action plans for outliers",
        "Top 3 return reasons identified per ASIN and fixes applied",
        "PDR (Voice of Customer) monitored weekly — no Red ASINs"
    ],
    "quiz": [
        {
            "question": "What is NOT allowed on packaging inserts on Amazon India?",
            "options": ["Brand social media handles", "Usage instructions", "QR code to how-to videos", "Discount offer in exchange for a positive review"],
            "answer": "Discount offer in exchange for a positive review",
            "explanation": "Offering any incentive (discount, free product, refund) in exchange for a review — positive or otherwise — is a violation of Amazon's Community Guidelines and can lead to account suspension."
        }
    ]
},

{
    "id": "4.5",
    "number": "Module 4.5",
    "title": "Cross-sell & Upsell",
    "difficulty": "Intermediate",
    "time": "30 mins",
    "overview": """<p>Increasing basket size through cross-selling and upselling is the highest-ROI conversion strategy — no extra traffic cost, pure revenue expansion. This module covers Frequently Bought Together analysis, Virtual Bundle testing, and Brand Store cross-sell pages.</p>""",
    "content": """
        <h3>1. Frequently Bought Together Analysis</h3>
        <div class='callout pro-tip'>
            <div><strong>FBT Analysis SOP:</strong><br>
            SC → Brand Analytics → Market Basket Analysis<br>
            This report shows what products customers buy alongside yours — your natural cross-sell partners.<br><br>
            Action: Create Virtual Bundles of the top 2–3 FBT combinations. Run Sponsored Display targeting buyers of FBT products.</div>
        </div>

        <h3>2. Virtual Bundle Conversion Testing</h3>
        <ul>
            <li>Create bundles from top Market Basket pairs: SC → Catalogue → Virtual Bundles</li>
            <li>Test bundle discount: 5%, 10%, 15% — measure conversion vs. individual ASIN purchase rate</li>
            <li>Promote bundles via Sponsored Products (bundle ASIN) and Brand Store</li>
            <li>Monitor: bundle conversion rate vs. standalone, average order value impact</li>
        </ul>
        <div class='callout success'>
            <div><strong>Virtual Bundle pricing rule:</strong> Bundle price must be lower than the sum of individual ASIN prices. Even a 5% bundle discount can increase basket size by 20–30%.</div>
        </div>

        <h3>3. Brand Store Cross-Sell Pages</h3>
        <table class='data-table'>
            <thead><tr><th>Page Type</th><th>Content</th><th>Goal</th></tr></thead>
            <tbody>
                <tr><td>Collection page</td><td>Full product range by category</td><td>Discovery, basket building</td></tr>
                <tr><td>Bundle/Kit page</td><td>Curated sets and kits</td><td>Higher AOV</td></tr>
                <tr><td>New arrivals</td><td>Latest ASINs</td><td>Repeat visit, new product trial</td></tr>
                <tr><td>Best sellers</td><td>Top-rated / most-sold ASINs</td><td>Social proof-driven upsell</td></tr>
            </tbody>
        </table>

        <h3>4. A+ Comparison Chart for Upsell</h3>
        <p>Use the A+ Comparison module to show premium tier products alongside your current ASIN. Customers viewing a mid-range ASIN should see the premium version with clear "why upgrade" messaging — drives 10–20% upsell rate to higher-margin products.</p>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='pill' href='https://sellercentral.amazon.in/brand-analytics/analytics/dashboard/marketBasket' target='_blank'>Market Basket Analysis</a>
            <a class='pill' href='https://sellercentral.amazon.in/virtual-bundles' target='_blank'>Virtual Bundles</a>
            <a class='pill' href='https://sellercentral.amazon.in/stores/manage' target='_blank'>Brand Store Manager</a>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Market Basket Analysis reviewed monthly for top 20 ASINs",
        "Virtual Bundles created for top 3 FBT combinations",
        "Bundle conversion rate monitored vs. standalone",
        "Brand Store cross-sell pages live (Collections, Bundles, Best Sellers)",
        "A+ Comparison chart updated to show upsell tier"
    ],
    "quiz": [
        {
            "question": "Which report shows what products customers buy alongside yours?",
            "options": ["Search Query Performance", "Market Basket Analysis", "Repeat Purchase Behaviour", "Demographics Report"],
            "answer": "Market Basket Analysis",
            "explanation": "Market Basket Analysis in Brand Analytics shows the top 3 products purchased in the same transaction as each of your ASINs — these are your highest-potential cross-sell and bundle partners."
        }
    ]
}

]
