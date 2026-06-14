# ==============================================================
# PILLAR 3 — EFFICIENCY  (7 Modules)
# Auto-generated from the backend DB by _renumber.py.
# Edit modules in the admin panel (source of truth = smeminds.db).
# ==============================================================

pillar3_modules = [
  {
    "id": "3.1",
    "pillar": "p3",
    "number": "Module 3.1",
    "title": "Listing Quality",
    "difficulty": "Intermediate",
    "time": "40 mins",
    "overview": "<p>Listing quality is the single biggest lever for organic visibility on Amazon India. This module covers the Search Query Performance report, keyword mapping, title/bullet/description best practices, and the backend search terms strategy to achieve a listing completeness score above 90%.</p>",
    "content": "\n        <h3>1. Search Query Performance Report Analysis</h3>\n        <div class='callout pro-tip'>\n            <div><strong>SQP Report workflow (weekly):</strong><br>\n            SC → Brand Analytics → Search Query Performance<br>\n            Download for top 50 ASINs → filter by Impressions → identify queries where you have &gt;1% impression share but &lt;5% click share = optimisation opportunity.</div>\n        </div>\n\n        <h3>2. Keyword Tiering & Mapping</h3>\n        <table class='data-table'>\n            <thead><tr><th>Tier</th><th>Criteria</th><th>Placement</th></tr></thead>\n            <tbody>\n                <tr><td>Tier 1 (Primary)</td><td>Highest volume, exact match intent</td><td>Title (first 80 chars)</td></tr>\n                <tr><td>Tier 2 (Secondary)</td><td>High volume, broad relevance</td><td>Bullet points 1–2</td></tr>\n                <tr><td>Tier 3 (Long-tail)</td><td>Lower volume, high conversion</td><td>Backend search terms</td></tr>\n            </tbody>\n        </table>\n\n        <h3>3. Title Optimisation (150–200 Characters)</h3>\n        <div class='callout success'>\n            <div><strong>Title Formula:</strong><br>\n            <code>[Brand] + [Model] + [Primary Keyword] + [Key Feature] + [Size/Colour/Qty]</code><br>\n            Example: <em>Prestige IRIS 750W Mixer Grinder — 3 Stainless Steel Jars, Grey</em><br><br>\n            • Primary keyword in first 80 chars (mobile truncation point)<br>\n            • No ALL CAPS, no special characters, no promotional claims</div>\n        </div>\n\n        <h3>4. Bullet Points — 5 Bullets SOP</h3>\n        <ul>\n            <li><strong>Bullet 1:</strong> Hero benefit + top feature</li>\n            <li><strong>Bullet 2:</strong> Performance / technical specification</li>\n            <li><strong>Bullet 3:</strong> Materials / quality / certifications</li>\n            <li><strong>Bullet 4:</strong> Compatibility / use case</li>\n            <li><strong>Bullet 5:</strong> Brand guarantee or warranty</li>\n        </ul>\n\n        <h3>5. Backend Search Terms (250 Bytes)</h3>\n        <div class='callout info'>\n            <div>• Max 250 bytes (not characters — Hindi = 3 bytes/char)<br>\n            • Space-separated, no commas<br>\n            • No repeats from title/bullets<br>\n            • Include: synonyms, Hindi transliterations, common misspellings</div>\n        </div>\n\n        <h3>6. Listing Completeness Score (&gt;90%)</h3>\n        <p>Check at: <strong>SC → Inventory → Listing Quality Dashboard</strong><br>\n        Priority: images, A+ Content, product dimensions, material/fabric, target audience.</p>\n\n        <div class='bookmarks-inline'>\n            <strong>Key Links:</strong><br>\n            <a class='pill' href='https://sellercentral.amazon.in/brand-analytics' target='_blank'>SQP Report</a>\n            <a class='pill' href='https://sellercentral.amazon.in/listing/qualitydashboard' target='_blank'>Listing Quality Dashboard</a>\n        </div>\n    ",
    "process_flow": "",
    "tools": "",
    "videos": [
      {
        "id": "GGLI_aIUO0M",
        "title": "Writing High-Converting Amazon Listings"
      }
    ],
    "checklist": [
      "SQP report downloaded and analysed weekly for top 50 ASINs",
      "Keywords tiered (T1/T2/T3) and mapped to correct listing fields",
      "Title 150–200 chars with primary keyword in first 80 chars",
      "5 bullets written with benefit-first formula",
      "Backend search terms ≤250 bytes, no repeats from title",
      "Listing completeness score &gt;90% on all hero ASINs",
      "Zero suppressed listings"
    ],
    "quiz": [
      {
        "question": "Where should your highest-volume keyword appear in the listing?",
        "options": [
          "Backend search terms only",
          "Last bullet point",
          "First 80 characters of the title",
          "Product description"
        ],
        "answer": "First 80 characters of the title",
        "explanation": "The first 80 characters are shown on mobile and carry the most SEO weight with Amazon's A10 algorithm."
      },
      {
        "question": "What is the maximum size of backend search terms?",
        "options": [
          "250 characters",
          "500 bytes",
          "250 bytes",
          "1,000 characters"
        ],
        "answer": "250 bytes",
        "explanation": "Amazon measures backend search terms in bytes. Hindi/Devanagari characters consume 3 bytes each."
      }
    ]
  },
  {
    "id": "3.2",
    "pillar": "p3",
    "number": "Module 3.2",
    "title": "Image Optimisation",
    "difficulty": "Beginner",
    "time": "30 mins",
    "overview": "<p>Images are the #1 conversion lever on Amazon — 83% of customers say product images are the most influential purchase factor. This module covers main image compliance, the 6–9 slot strategy, video, and the mobile-first thumb test.</p>",
    "content": "\n        <h3>1. Main Image Requirements</h3>\n        <div class='callout pro-tip'>\n            <div>✓ Pure white background (RGB 255,255,255)<br>\n            ✓ Product ≥85% of frame<br>\n            ✓ Minimum 1,000px on longest side (2,000px recommended)<br>\n            ✓ No text, logos, watermarks, or props<br>\n            ✓ JPEG preferred</div>\n        </div>\n\n        <h3>2. 6–9 Image Slot Strategy</h3>\n        <table class='data-table'>\n            <thead><tr><th>Slot</th><th>Content</th><th>Purpose</th></tr></thead>\n            <tbody>\n                <tr><td>1 (Main)</td><td>White BG product</td><td>Compliance + CTR</td></tr>\n                <tr><td>2</td><td>Infographic — hero features</td><td>Quick education (mobile)</td></tr>\n                <tr><td>3</td><td>Lifestyle — in use</td><td>Emotional connection</td></tr>\n                <tr><td>4</td><td>Dimensions/scale</td><td>Reduce returns</td></tr>\n                <tr><td>5</td><td>Before/after or comparison</td><td>Demonstrate value</td></tr>\n                <tr><td>6</td><td>What's in the box</td><td>Set expectations</td></tr>\n                <tr><td>7</td><td>Certifications/badges</td><td>Trust building</td></tr>\n                <tr><td>8</td><td>360°/close-up detail</td><td>Premium feel</td></tr>\n                <tr><td>9 (Video)</td><td>30–90 sec demo</td><td>Highest CVR impact</td></tr>\n            </tbody>\n        </table>\n\n        <h3>3. The Thumb Test (Mobile-First)</h3>\n        <div class='callout success'>\n            <div><strong>67% of Amazon India traffic is mobile.</strong> Shrink your main image to thumbnail size (100×100px). Can you identify the product instantly? Does it stand out vs. competitors? If not — reshoot or reframe.</div>\n        </div>\n\n        <h3>4. Video Content Strategy</h3>\n        <ul>\n            <li>Duration: 30–90 sec (45–60 sec sweet spot)</li>\n            <li>Add subtitles — 60% watch with sound off</li>\n            <li>Structure: Problem → Solution → Product demo → CTA</li>\n            <li>Resolution: 1920×1080 min, MP4 format</li>\n        </ul>\n\n        <div class='bookmarks-inline'>\n            <strong>Key Links:</strong><br>\n            <a class='pill' href='https://sellercentral.amazon.in/gp/help/G1881' target='_blank'>Image Requirements Guide</a>\n            <a class='pill' href='https://sellercentral.amazon.in/catalog' target='_blank'>Manage Listings</a>\n        </div>\n    ",
    "process_flow": "",
    "tools": "",
    "videos": [
      {
        "id": "y4icIWo5ciY",
        "title": "Creating Converting Amazon Product Images"
      }
    ],
    "checklist": [
      "Main image: white BG, product ≥85% frame, ≥1000px",
      "All 6–9 slots filled with recommended content types",
      "Product demo video uploaded (30–90 sec, subtitled)",
      "Thumb test passed at thumbnail size",
      "Infographic text readable on mobile (min 30pt equivalent)",
      "All images JPEG, under 10MB"
    ],
    "quiz": [
      {
        "question": "What percentage of the frame must the product occupy in the main image?",
        "options": [
          "50%",
          "70%",
          "85%",
          "95%"
        ],
        "answer": "85%",
        "explanation": "Amazon requires the product to fill at least 85% of the image to maximise thumbnail visibility and click-through rate."
      },
      {
        "question": "What is the 'thumb test'?",
        "options": [
          "Check if image passes Amazon's AI",
          "Verify the image at thumbnail size for mobile clarity",
          "Test with 5 people before publishing",
          "Upload to a test ASIN first"
        ],
        "answer": "Verify the image at thumbnail size for mobile clarity",
        "explanation": "With 67% of Amazon India traffic from mobile, your main image must be identifiable and distinct even at 100×100px thumbnail size."
      }
    ]
  },
  {
    "id": "3.3",
    "pillar": "p3",
    "number": "Module 3.3",
    "title": "Pricing Strategy",
    "difficulty": "Advanced",
    "time": "40 mins",
    "overview": "<p>Pricing on Amazon India is a dynamic, real-time battleground. Win the Buy Box, protect margins, and grow revenue simultaneously using competitive analysis, automated repricing, deal calendars, price elasticity testing, and B2B pricing.</p>",
    "content": "\n        <h3>1. Buy Box Win Rate Monitoring</h3>\n        <div class='callout pro-tip'>\n            <div><strong>Buy Box Factors (by weight):</strong><br>\n            1. FBA fulfilment status<br>\n            2. Competitive landed price<br>\n            3. Seller metrics (ODR &lt;1%, LDR &lt;4%)<br>\n            4. Stock availability<br>\n            5. Seller feedback rating</div>\n        </div>\n        <p>Track at: <strong>SC → Business Reports → Detail Page Sales → Buy Box Percentage</strong><br>\n        Target: &gt;80% Buy Box win rate on all hero ASINs.</p>\n\n        <h3>2. Automated Repricing Rules</h3>\n        <table class='data-table'>\n            <thead><tr><th>Rule Type</th><th>Use Case</th><th>Must-Have Safeguard</th></tr></thead>\n            <tbody>\n                <tr><td>Beat competitor by X%</td><td>Stay below competition</td><td>Set minimum price floor</td></tr>\n                <tr><td>Featured Offer (Buy Box)</td><td>Match Buy Box price</td><td>Always pair with min price</td></tr>\n                <tr><td>Sales velocity</td><td>Raise price when selling fast</td><td>Monitor margin impact</td></tr>\n            </tbody>\n        </table>\n        <div class='callout warning'>\n            <div><strong>Always set a minimum price.</strong> Floor = Product Cost + FBA Fees + 15% minimum margin. Without it, rules race to zero.</div>\n        </div>\n\n        <h3>3. Deal & Coupon Calendar</h3>\n        <table class='data-table'>\n            <thead><tr><th>Type</th><th>Min Discount</th><th>Best Use</th></tr></thead>\n            <tbody>\n                <tr><td>Lightning Deal</td><td>≥15% off reference price</td><td>Fast velocity, new launches</td></tr>\n                <tr><td>7-Day Best Deal</td><td>≥10% (invite only)</td><td>Sustained volume boost</td></tr>\n                <tr><td>Coupon</td><td>Any ₹X or X%</td><td>Conversion boost, review seeding</td></tr>\n                <tr><td>Prime Exclusive Discount</td><td>≥10% for Prime members</td><td>Prime Day &amp; festive events</td></tr>\n            </tbody>\n        </table>\n\n        <h3>4. Price Elasticity Testing</h3>\n        <ol>\n            <li>Baseline: 2-week avg price, units/day, revenue/day</li>\n            <li>Test: ±10% price change</li>\n            <li>Measure 2 weeks: units and revenue change</li>\n            <li>PE = % change units ÷ % change price</li>\n            <li>PE &gt;1 (elastic): lower price. PE &lt;1 (inelastic): raise price.</li>\n        </ol>\n\n        <h3>5. B2B Pricing & Quantity Discounts</h3>\n        <div class='callout success'>\n            <div>30%+ of Amazon India GMV is B2B. Set Business Price without affecting retail Buy Box.<br>\n            <strong>SC → B2B → Manage Offers → Business Price &amp; Quantity Discounts</strong></div>\n        </div>\n\n        <div class='bookmarks-inline'>\n            <strong>Key Links:</strong><br>\n            <a class='pill' href='https://sellercentral.amazon.in/pricing/automation/rules' target='_blank'>Automate Pricing</a>\n            <a class='pill' href='https://sellercentral.amazon.in/merchandising/lightning-deals' target='_blank'>Lightning Deals</a>\n            <a class='pill' href='https://sellercentral.amazon.in/coupons' target='_blank'>Manage Coupons</a>\n            <a class='pill' href='https://sellercentral.amazon.in/business/pricing' target='_blank'>B2B Pricing</a>\n        </div>\n    ",
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
      "Buy Box win rate &gt;80% for all hero ASINs",
      "Automated repricing rules with min/max floors on all active ASINs",
      "Deal calendar planned 6 weeks ahead",
      "Coupons running on targeted ASINs",
      "B2B pricing enabled with quantity tiers",
      "Price elasticity tested on top 10 ASINs quarterly"
    ],
    "quiz": [
      {
        "question": "What is the #1 factor for winning the Buy Box on Amazon India?",
        "options": [
          "Lowest absolute price",
          "FBA fulfilment status",
          "Most reviews",
          "Oldest seller account"
        ],
        "answer": "FBA fulfilment status",
        "explanation": "FBA provides Amazon-controlled fast delivery and Prime eligibility — the highest-weighted Buy Box factor."
      },
      {
        "question": "Minimum discount required for a Lightning Deal submission?",
        "options": [
          "5%",
          "10%",
          "15%",
          "20%"
        ],
        "answer": "15%",
        "explanation": "Amazon India requires a minimum 15% off the reference price for Lightning Deal eligibility, plus ≥3★ and Prime eligibility."
      }
    ]
  },
  {
    "id": "3.4",
    "pillar": "p3",
    "number": "Module 3.4",
    "title": "Review & Rating",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": "<p>Reviews are the social proof engine of Amazon. A 4.2★/200-review product consistently outperforms a 5★/5-review product. This module covers velocity targets, Vine enrollment, negative review handling, policy compliance, and review request automation — all within Amazon's Terms of Service.</p>",
    "content": "\n        <h3>1. Review Velocity Targets</h3>\n        <table class='data-table'>\n            <thead><tr><th>Phase</th><th>Target</th><th>Priority Action</th></tr></thead>\n            <tbody>\n                <tr><td>Launch (0–30 days)</td><td>1 review / 10–20 orders</td><td>Vine + Request a Review</td></tr>\n                <tr><td>Growth (30–90 days)</td><td>5–10 reviews/month</td><td>Vine + automated requests</td></tr>\n                <tr><td>Mature (&gt;90 days)</td><td>Maintain ≥4.0★</td><td>Monitor &amp; respond</td></tr>\n            </tbody>\n        </table>\n        <div class='callout pro-tip'>\n            <div><strong>Benchmark rule:</strong> Target 50% of your top 3 competitors' review count to compete effectively on conversion.</div>\n        </div>\n\n        <h3>2. Vine Program</h3>\n        <ul>\n            <li>Eligibility: Brand Registry, &lt;30 reviews, FBA stock available</li>\n            <li>Cost: Free for ASINs with &lt;2 reviews (check current policy)</li>\n            <li>Path: SC → Advertising → Amazon Vine → Enrol product</li>\n            <li>Send 2–30 units; reviews appear in 4–8 weeks</li>\n        </ul>\n\n        <h3>3. Negative Review Response SOP</h3>\n        <div class='callout success'>\n            <div>1. Acknowledge the experience (don't argue)<br>\n            2. Apologise sincerely<br>\n            3. Offer resolution (replacement, refund)<br>\n            4. Move offline: \"Contact us at [support]\"<br>\n            5. Fix root cause<br><br>\n            Respond within 24 hours — prospective buyers read your responses.</div>\n        </div>\n\n        <h3>4. What's Allowed vs. Not Allowed</h3>\n        <div class='callout warning'>\n            <div><strong>NEVER do:</strong> incentivised reviews, family/friend reviews, review clubs, refunds for reviews.</div>\n        </div>\n        <div class='callout info'>\n            <div><strong>ALLOWED:</strong> Vine programme, \"Request a Review\" button in SC, neutral packaging inserts (\"Love it? Review us!\"), responding to existing reviews.</div>\n        </div>\n\n        <h3>5. Request a Review Automation</h3>\n        <p><strong>Manual:</strong> SC → Orders → Manage Orders → Request a Review (4–30 days post-delivery)</p>\n        <p><strong>Tools:</strong> FeedbackWhiz, Helium 10, Jungle Scout — automate within Amazon ToS windows.</p>\n\n        <div class='bookmarks-inline'>\n            <strong>Key Links:</strong><br>\n            <a class='pill' href='https://sellercentral.amazon.in/vine/dashboard' target='_blank'>Amazon Vine</a>\n            <a class='pill' href='https://sellercentral.amazon.in/orders-v3' target='_blank'>Manage Orders</a>\n            <a class='pill' href='https://sellercentral.amazon.in/performance/feedback' target='_blank'>Feedback Manager</a>\n        </div>\n    ",
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
      "Review velocity tracked monthly per ASIN",
      "Vine enrolled for all new launches (&lt;30 reviews)",
      "Automated 'Request a Review' active for all orders",
      "All negative reviews responded to within 24 hours",
      "Review manipulation checklist reviewed with team monthly",
      "Star rating ≥4.0 on all hero ASINs"
    ],
    "quiz": [
      {
        "question": "Which review acquisition method is compliant with Amazon ToS?",
        "options": [
          "Refund in exchange for a review",
          "Vine programme enrolment",
          "Review Facebook groups",
          "Email blast for 5-star reviews"
        ],
        "answer": "Vine programme enrolment",
        "explanation": "Amazon Vine is Amazon's own compliant review programme. All other methods mentioned are prohibited and risk account suspension."
      },
      {
        "question": "What review count benchmark should you aim for vs. top competitors?",
        "options": [
          "Equal to their count",
          "50% of their count",
          "Double their count",
          "10% of their count"
        ],
        "answer": "50% of their count",
        "explanation": "50% of the top competitor's review count provides enough social proof to compete effectively on conversion rate."
      }
    ]
  },
  {
    "id": "3.5",
    "pillar": "p3",
    "number": "Module 3.5",
    "title": "A+ & Brand Content",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": "<p>A+ Content transforms your product description area into a rich brand experience driving 3–10% higher conversion. This module covers Basic vs Premium A+ eligibility, module layout strategy, comparison charts for cross-selling, and Brand Story creation.</p>",
    "content": "\n        <h3>1. Basic vs Premium A+ Eligibility</h3>\n        <table class='data-table'>\n            <thead><tr><th>Feature</th><th>A+ Basic</th><th>Premium A+</th></tr></thead>\n            <tbody>\n                <tr><td>Requirement</td><td>Brand Registered</td><td>BR + Brand Story + ≥5 approved A+ pages</td></tr>\n                <tr><td>Interactive modules</td><td>No</td><td>Yes (hotspot, carousel, video)</td></tr>\n                <tr><td>CVR lift</td><td>3–5%</td><td>8–10%</td></tr>\n                <tr><td>Cost</td><td>Free</td><td>Free (earned)</td></tr>\n            </tbody>\n        </table>\n        <p>Check eligibility: <strong>SC → Advertising → A+ Content Manager</strong></p>\n\n        <h3>2. Recommended A+ Layout (7 modules)</h3>\n        <div class='callout pro-tip'>\n            <div>1. Hero banner — brand lifestyle<br>\n            2. 4-column feature icons — top 4 benefits<br>\n            3. Feature + image — deep dive on #1 feature<br>\n            4. Comparison chart — your product range<br>\n            5. Technical specs table<br>\n            6. Lifestyle + use case text<br>\n            7. Brand statement + logo</div>\n        </div>\n\n        <h3>3. Comparison Chart for Cross-Selling</h3>\n        <ul>\n            <li>Compare up to 6 of your own ASINs (not competitors)</li>\n            <li>Drives 5–15% uplift in multi-ASIN basket size</li>\n            <li>Use to upsell to premium tier or cross-sell complementary products</li>\n        </ul>\n\n        <h3>4. Brand Story</h3>\n        <div class='callout success'>\n            <div>Brand Story appears on every ASIN under your brand and unlocks Premium A+.<br>\n            Published once → applies to all ASINs automatically.<br><br>\n            <strong>Steps:</strong> SC → Advertising → A+ Content Manager → Brand Story → upload logo, heritage image, mission statement → Submit (7-day review)</div>\n        </div>\n\n        <div class='bookmarks-inline'>\n            <strong>Key Links:</strong><br>\n            <a class='pill' href='https://sellercentral.amazon.in/enhanced-content/marketing/dashboard' target='_blank'>A+ Content Manager</a>\n            <a class='pill' href='https://brandservices.amazon.in' target='_blank'>Brand Registry Portal</a>\n        </div>\n    ",
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
      "A+ Content live on all Brand Registered ASINs",
      "Brand Story published",
      "Premium A+ eligibility checked and unlocked",
      "7-module layout used on hero ASINs",
      "Comparison chart linking to product range",
      "A+ CVR performance reviewed monthly"
    ],
    "quiz": [
      {
        "question": "What is required to unlock Premium A+ Content?",
        "options": [
          "100+ reviews",
          "Brand Story + 5 approved A+ pages",
          "500+ monthly sales",
          "DSP advertising active"
        ],
        "answer": "Brand Story + 5 approved A+ pages",
        "explanation": "Premium A+ requires an approved Brand Story plus at least 5 approved A+ Basic pages published on your ASINs."
      },
      {
        "question": "Average CVR lift from A+ Content?",
        "options": [
          "0–1%",
          "1–2%",
          "3–10%",
          "15–20%"
        ],
        "answer": "3–10%",
        "explanation": "Amazon's data shows A+ Content drives 3–10% higher conversion rate. Premium A+ reaches the upper end."
      }
    ]
  },
  {
    "id": "3.6",
    "pillar": "p3",
    "number": "Module 3.6",
    "title": "Buy Box Strategy — Win, Maintain & Recover",
    "difficulty": "Advanced",
    "time": "35 mins",
    "overview": "<p>Over 80% of Amazon India orders are placed through the Buy Box. Lose it and sales can drop overnight — win it consistently and you own the category. This module breaks down the Buy Box algorithm, the 5 factors that control it, and the exact tactics to win and defend your position.</p>",
    "content": "\n        <h3>1. What Is the Buy Box?</h3>\n        <p>The Buy Box is the \"Add to Cart\" button on the product detail page. When a customer clicks Add to Cart, their order goes to the Buy Box winner — not necessarily the brand owner or lowest price.</p>\n        <div class='callout pro-tip'><div><strong>The 80% Rule:</strong> &gt;80% of Amazon India orders go through the Buy Box. Losing it even temporarily (during repricing delays, stockouts, or metric drops) can cause 50–80% sales decline in 24 hours.</div></div>\n\n        <h3>2. Buy Box Win Factors (Weighted)</h3>\n        <table class='data-table'>\n            <thead><tr><th>Factor</th><th>Weight</th><th>Action</th></tr></thead>\n            <tbody>\n                <tr><td>Price (Landed Price)</td><td>30–40%</td><td>Monitor competitors hourly; use dynamic pricing</td></tr>\n                <tr><td>Fulfillment Method</td><td>25–30%</td><td>FBA &gt; Easy Ship Prime &gt; FBM</td></tr>\n                <tr><td>Seller Metrics</td><td>15–20%</td><td>Feedback 4.5+, return rate &lt;2%, cancellation &lt;1.5%</td></tr>\n                <tr><td>In-Stock Status</td><td>10–15%</td><td>Never go OOS; maintain 30-day safety stock</td></tr>\n                <tr><td>Response Time + Compliance</td><td>5–10%</td><td>Respond to messages within 24 hrs; no policy violations</td></tr>\n            </tbody>\n        </table>\n\n        <h3>3. Step-by-Step: Winning the Buy Box</h3>\n        <ol>\n            <li>Ensure <strong>Professional Seller Plan</strong> (required for Buy Box eligibility)</li>\n            <li>Use <strong>FBA fulfillment</strong> (highest priority in algorithm)</li>\n            <li>Set competitive price — match or beat the current Buy Box price by ₹1–₹5</li>\n            <li>Maintain feedback rating <strong>4.5+</strong> (request reviews post-delivery)</li>\n            <li>Keep return rate &lt;2% and cancellation rate &lt;1.5%</li>\n            <li>Maintain inventory in stock (OOS = immediate Buy Box loss)</li>\n            <li>Respond to all customer messages within 24 hours</li>\n            <li>Monitor Buy Box % daily: Reports → Buy Box Percentage Detail</li>\n        </ol>\n\n        <h3>4. Monitoring Buy Box Ownership</h3>\n        <ol>\n            <li>Go to <strong>Reports → Buy Box Percentage Detail</strong></li>\n            <li>Check daily Buy Box share percentage per ASIN</li>\n            <li>Identify days when Buy Box was lost</li>\n            <li>Correlate with: price changes, stock levels, competitor activity, metric drops</li>\n        </ol>\n\n        <h3>5. Recovering Lost Buy Box</h3>\n        <ol>\n            <li>Check Account Health (Performance → Account Health) for violations</li>\n            <li>Check inventory status — ensure in stock</li>\n            <li>Review price vs. Buy Box competitor (may need adjustment)</li>\n            <li>Check feedback rating — ensure 4.5+</li>\n            <li>Check return and cancellation rates</li>\n            <li>If no issue found, raise Seller Support case</li>\n            <li>Monitor Buy Box % daily until recovered</li>\n        </ol>\n\n        <h3>6. Dynamic Pricing Rules</h3>\n        <table class='data-table'>\n            <thead><tr><th>Rule</th><th>Value</th></tr></thead>\n            <tbody>\n                <tr><td>Maximum price</td><td>Never exceed this (controls margin)</td></tr>\n                <tr><td>Minimum price</td><td>COGS + all fees + minimum 15% margin</td></tr>\n                <tr><td>Buy Box strategy</td><td>Undercut current Buy Box by ₹1–₹5</td></tr>\n                <tr><td>Repricing frequency</td><td>Hourly in competitive categories</td></tr>\n            </tbody>\n        </table>\n\n        <div class='bookmarks-inline'>\n            <strong>Key Links:</strong><br>\n            <a class='btn-sc' href='https://sellercentral.amazon.in/pricing/dashboard' target='_blank'>Manage Pricing</a>\n            <a class='btn-sc' href='https://sellercentral.amazon.in/performance/dashboard' target='_blank'>Account Health Dashboard</a>\n            <a class='pill-sc' href='https://sellercentral.amazon.in/gp/reports-manager/report.html/ref=xx_buybox_dnav_xx?ie=UTF8&reportType=GET_V2_SETTLEMENT_REPORT_DATA_PERFORMANCE' target='_blank'>Buy Box Report</a>\n        </div>\n\n        <div class='pain-point-section'>\n            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>\n            <div class='pain-point-body'>\n                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller goes OOS for 3 days — loses Buy Box to competitor. When restocked, competitor still holds Buy Box. Sales don't recover for 2–3 weeks.</p></div>\n                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Maintain minimum 30-day safety stock. Set Seller Central inventory alerts at 14 days of supply. On restock, run a 3-day Lightning Deal to rebuild sales velocity and reclaim Buy Box.</p></div>\n                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>FBA gives a significant Buy Box advantage over FBM even at a slightly higher price. In most categories, an FBA listing at ₹500 beats an FBM listing at ₹480. Switching to FBA often recovers lost Buy Box without any price change.</p></div>\n            </div>\n        </div>\n    ",
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
      "Enrolled in Professional Seller Plan (Buy Box eligibility requirement)",
      "Using FBA for all primary ASINs (highest Buy Box priority)",
      "Price set within ₹1–₹5 of current Buy Box price",
      "Feedback rating maintained at 4.5+ stars",
      "Return rate below 2% and cancellation rate below 1.5%",
      "Minimum 30-day safety stock maintained for top ASINs",
      "Reviewing Buy Box Percentage Detail report weekly"
    ],
    "quiz": [
      {
        "question": "What percentage of Amazon India orders typically go through the Buy Box?",
        "options": [
          "40%",
          "60%",
          "80%+",
          "95%+"
        ],
        "answer": "80%+",
        "explanation": "Over 80% of Amazon India orders are placed through the Buy Box (the Add to Cart button). Losing the Buy Box even temporarily causes 50–80% sales decline for most sellers."
      },
      {
        "question": "Which fulfillment method has the highest priority in Amazon's Buy Box algorithm?",
        "options": [
          "FBM with lowest price",
          "Easy Ship Standard",
          "FBA (Fulfillment by Amazon)",
          "Seller Flex"
        ],
        "answer": "FBA (Fulfillment by Amazon)",
        "explanation": "FBA is prioritized highest in the Buy Box algorithm, followed by Easy Ship Prime (Seller Fulfilled Prime), then standard Easy Ship, and finally FBM. FBA often wins the Buy Box even at a slightly higher price than FBM competitors."
      }
    ]
  },
  {
    "id": "3.7",
    "pillar": "p3",
    "number": "Module 3.7",
    "title": "Deals & Promotions Mastery",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": "<p>Deals are the fastest way to spike sales velocity, push organic rank, and acquire new-to-brand customers. This module covers the 4 deal types on Amazon India, eligibility requirements, profit-impact calculation, and a seasonal deal calendar so every promotion drives maximum ROI.</p>",
    "content": "\n        <h3>1. Four Deal Types on Amazon India</h3>\n        <table class='data-table'>\n            <thead><tr><th>Deal Type</th><th>Duration</th><th>Visibility</th><th>Best For</th></tr></thead>\n            <tbody>\n                <tr><td><strong>Lightning Deal</strong></td><td>6–24 hours</td><td>Today's Deals page + category</td><td>New product launches, sales velocity boost</td></tr>\n                <tr><td><strong>Best Deal</strong></td><td>7–14 days</td><td>Deals section + category listing</td><td>Sustained awareness, festival periods</td></tr>\n                <tr><td><strong>Deal of the Day</strong></td><td>24 hours</td><td>Homepage featured + email blasts</td><td>High-volume clearance, hero products</td></tr>\n                <tr><td><strong>Coupon</strong></td><td>Custom (up to 90 days)</td><td>Search results badge + detail page</td><td>Always-on conversion boost</td></tr>\n            </tbody>\n        </table>\n\n        <h3>2. Deal Eligibility Checklist (All Deal Types)</h3>\n        <ul>\n            <li>✅ Professional Seller Plan (mandatory)</li>\n            <li>✅ Buy Box winner for the ASIN</li>\n            <li>✅ Feedback rating: 4.5+ stars</li>\n            <li>✅ Account in good standing (no active violations)</li>\n            <li>✅ Product images meet Amazon requirements (1,000px+)</li>\n            <li>✅ Inventory in stock (sufficient quantity through deal period)</li>\n            <li>✅ Brand Size Chart approved (for apparel/footwear)</li>\n            <li>✅ Price higher than deal price before deal period (real discount)</li>\n        </ul>\n\n        <h3>3. Creating a Lightning Deal</h3>\n        <ol>\n            <li>Go to <strong>Advertising → Deals → Create Lightning Deal</strong></li>\n            <li>Select eligible ASIN</li>\n            <li>Set discount % or fixed amount</li>\n            <li>Choose start/end time (high-traffic: evenings 6–10PM, weekends)</li>\n            <li>Set max deal quantity (30–50% of weekly sales volume)</li>\n            <li>Submit 10+ days in advance (Amazon approval required)</li>\n            <li>Monitor performance real-time: sales volume + inventory remaining</li>\n        </ol>\n\n        <h3>4. Deal Profit Impact Calculation</h3>\n        <div class='callout pro-tip'><div><strong>Deal P&amp;L Formula:</strong><br>\n        Deal Profit = (Deal Price × Deal Units) − (COGS × Deal Units) − (All Fees × Deal Units)<br><br>\n        Example (₹500 product, 20% deal = ₹400):<br>\n        COGS: ₹200 | FBA Fee: ₹80 | Referral (10%): ₹40 | GST on fees: ₹21.60<br>\n        Deal Profit per unit: ₹400 − ₹200 − ₹80 − ₹40 − ₹21.60 = <strong>₹58.40 (14.6% margin)</strong><br>\n        Volume impact: Even at 14.6% margin, 3× volume may be more valuable than 25% margin at normal velocity — especially for ranking recovery or new product launch.</div></div>\n\n        <h3>5. No Cost EMI — Seller-Funded Financing</h3>\n        <div class='callout info'><div><strong>How No Cost EMI Works for Sellers:</strong> Customers pay no interest — but sellers absorb a cost equivalent to the bank interest rate. The cost is typically 1–2% of transaction value per month of EMI. For a 6-month EMI on a ₹3,000 item, seller absorbs ~₹180–₹360. Factor this into your deal price calculation for products eligible for EMI.</div></div>\n\n        <h3>6. SPC (Special Price Consideration) Strategy</h3>\n        <p>SPC (Smart Price Consideration) allows sellers to set temporarily reduced prices during high-visibility windows without going through the formal Deals approval process. Available via <strong>Advertising → Deals → SPC</strong> in select categories.</p>\n\n        <h3>7. Seasonal Deal Calendar</h3>\n        <table class='data-table'>\n            <thead><tr><th>Season</th><th>Months</th><th>Deal Strategy</th></tr></thead>\n            <tbody>\n                <tr><td>Republic Day Sale</td><td>Jan</td><td>Lightning Deals, stock up 6 weeks prior</td></tr>\n                <tr><td>Amazon Summer Sale</td><td>Apr–May</td><td>Summer-relevant SKUs, coupons</td></tr>\n                <tr><td>Prime Day India</td><td>Jul–Aug</td><td>10 weeks prior: deal submissions + inventory build</td></tr>\n                <tr><td>Great Indian Festival</td><td>Oct</td><td>12 weeks prior: all deal types, maximum inventory</td></tr>\n                <tr><td>Diwali Peak</td><td>Oct–Nov</td><td>Deals of the Day, gifting SKUs, bundles</td></tr>\n                <tr><td>Year-End Sale</td><td>Dec</td><td>Clearance + hero products for GOSF</td></tr>\n            </tbody>\n        </table>\n\n        <div class='bookmarks-inline'>\n            <strong>Key Links:</strong><br>\n            <a class='btn-sc' href='https://sellercentral.amazon.in/merchandising-new/' target='_blank'>Deals Dashboard</a>\n            <a class='btn-sc' href='https://sellercentral.amazon.in/coupons' target='_blank'>Coupons Manager</a>\n            <a class='pill-sc' href='https://sellercentral.amazon.in/gp/help/external/G202111490' target='_blank'>Lightning Deal Help</a>\n        </div>\n\n        <div class='pain-point-section'>\n            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>\n            <div class='pain-point-body'>\n                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller runs a 40% Lightning Deal without profit-impact calculation — sells 200 units at a loss, spends ad budget on a deal that destroys margin, and has no inventory left for the real festive peak.</p></div>\n                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Always run the Deal P&amp;L formula before submission. Minimum deal margin: 10% for deals with volume multiplier; 20%+ for standard deals. Set max deal quantity at 30–50% of weekly sales volume to protect inventory.</p></div>\n                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>The value of a Lightning Deal is not just the direct profit — it's the ranking boost from sales velocity spike. A deal that runs break-even can pay for itself 3× over through organic rank improvement in the 2 weeks after the deal ends.</p></div>\n            </div>\n        </div>\n    ",
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
      "Confirmed Buy Box ownership before submitting any deal",
      "Apparel/footwear size chart approved before deal submission",
      "Calculated deal profit impact (Deal P&L formula) before submission",
      "Set max deal quantity at 30–50% of weekly sales volume",
      "Submitted deal 10+ days in advance for approval",
      "Deal planned for high-traffic time slot (evenings, weekends)",
      "Seasonal deal calendar created with 12-week lead time for GIF/Prime Day"
    ],
    "quiz": [
      {
        "question": "For a Lightning Deal, how far in advance should a seller submit for Amazon approval?",
        "options": [
          "Same day",
          "3 days",
          "10+ days",
          "30 days"
        ],
        "answer": "10+ days",
        "explanation": "Amazon requires Lightning Deal submissions at least 10 days in advance for review and approval. For major events like GIF or Prime Day, Amazon often requires submissions 4–6 weeks in advance."
      },
      {
        "question": "An apparel seller's Lightning Deal was rejected even though they are the Buy Box winner. Most likely reason:",
        "options": [
          "Feedback rating below 4.8",
          "Brand Size Chart not approved",
          "Inventory too high",
          "Price too low"
        ],
        "answer": "Brand Size Chart not approved",
        "explanation": "Amazon requires an approved Brand Size Chart for all apparel and footwear deal submissions. Without it, Lightning Deals, Best Deals, and Deals of the Day are blocked regardless of other eligibility criteria."
      }
    ]
  }
]
