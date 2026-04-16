# ══════════════════════════════════════════════════════════════
# PILLAR 3 — TRAFFIC  (5 Modules)
# ══════════════════════════════════════════════════════════════

pillar3_modules = [

# ─────────────────────────────────────────────────────────────
{
    "id": "3.1",
    "number": "Module 3.1",
    "title": "Sponsored Ads",
    "difficulty": "Advanced",
    "time": "50 mins",
    "overview": """<p>Amazon Advertising is the most efficient paid channel for driving qualified, purchase-intent traffic on Amazon India. This module covers every Sponsored Ad type — Products, Brands, Display, and Video — with campaign structure SOPs, bid strategy selection, keyword harvesting, negative management, and ACoS/TACoS optimisation frameworks based on SMEMinds' official Sponsored Ads Guide.</p>""",
    "content": """
        <h3>1. Sponsored Products — Auto Campaign Setup</h3>
        <div class='callout pro-tip'>
            <div><strong>Auto Campaign Launch SOP (SMEMinds Ads Guide):</strong><br>
            1. SC → Advertising → Campaign Manager → Create → Sponsored Products<br>
            2. Set targeting to <strong>Automatic</strong><br>
            3. Budget: Minimum <strong>₹150/day</strong> per campaign (SMEMinds recommended minimum to avoid budget exhaustion)<br>
            4. Launch budget for new ASINs: ₹500–₹1,000/day<br>
            5. Bid: Start at ₹20–₹40 (or at/slightly above Amazon's suggested bid)<br>
            6. <strong>Default bidding strategy: Dynamic Bids — Up and Down</strong> (recommended for all new campaigns)<br>
            7. Run for minimum 2 weeks before harvesting — Amazon's algorithm needs this data to optimise<br>
            8. Do NOT set an end date — or set it at least 60 days from launch<br>
            9. Turn on all 4 auto targeting groups: close match, loose match, substitutes, complements</div>
        </div>

        <h3>2. Sponsored Products — Manual Campaign Setup</h3>
        <table class='data-table'>
            <thead><tr><th>Match Type</th><th>Use</th><th>Bid Strategy</th></tr></thead>
            <tbody>
                <tr><td>Exact</td><td>Proven high-converting KWs from auto harvest (3+ orders)</td><td>Highest bid — target ACoS</td></tr>
                <tr><td>Phrase</td><td>Mid-funnel, research intent</td><td>Mid bid</td></tr>
                <tr><td>Broad</td><td>Discovery, new keyword mining</td><td>Lower bid, watch spend</td></tr>
            </tbody>
        </table>
        <div class='callout success'>
            <div><strong>Campaign Structure Best Practice:</strong><br>
            1 campaign = 1 ASIN or 1 product group<br>
            Separate campaigns per match type for budget control<br>
            Naming: [Brand]_[ASIN/Category]_[Exact/Phrase/Broad]_[Date]<br>
            Ensure at least 90% eligible ASIN coverage across campaigns for broader reach</div>
        </div>

        <h3>3. Bidding Strategy Selection — 3 Official Options</h3>
        <table class='data-table'>
            <thead><tr><th>Strategy</th><th>How It Works</th><th>When to Use</th></tr></thead>
            <tbody>
                <tr><td><strong>Dynamic Up &amp; Down</strong> ✅ Recommended</td><td>Amazon raises bids up to 100% for top-of-search, lowers for low-conversion spots</td><td>Default for all new campaigns &amp; fast-moving ASINs</td></tr>
                <tr><td>Dynamic Down Only</td><td>Amazon only reduces bids for low-conversion clicks — conservative</td><td>Mature campaigns with above-target ACoS needing protection</td></tr>
                <tr><td>Fixed Bids</td><td>Your exact bid every time — no algorithm adjustment</td><td>Niche exact-match campaigns with known conversion data</td></tr>
            </tbody>
        </table>
        <div class='callout info'>
            <div><strong>Placement Bid Adjustments:</strong> In addition to strategy, adjust bids by placement:<br>
            • <strong>Top of Search (First Page)</strong> — Premium placement, highest CPC, highest CVR<br>
            • <strong>Rest of Search</strong> — Middle/bottom of search results<br>
            • <strong>Product Pages</strong> — On competitor/complementary detail pages<br>
            Path: Advertising → Campaign Manager → Campaign Name → Campaign Settings → Adjust bids by placement</div>
        </div>

        <h3>4. ACoS Optimisation Framework — 3-Tier Action Map</h3>
        <table class='data-table'>
            <thead><tr><th>ACoS Status</th><th>Scenario</th><th>Recommended Actions</th></tr></thead>
            <tbody>
                <tr><td style="color:#16a34a;font-weight:bold;">&lt;25% — Scale Up</td><td>Efficient, profitable</td><td>Increase keyword bids by 30%; add more high-intent keywords; raise daily budget; increase Top-of-Search placement multiplier</td></tr>
                <tr><td style="color:#d97706;font-weight:bold;">25–35% — Monitor &amp; Tune</td><td>Near break-even</td><td>Review search term reports for irrelevant terms; convert broad-match to phrase/exact; test bid adjustments of ±10%; review placement multipliers</td></tr>
                <tr><td style="color:#dc2626;font-weight:bold;">&gt;35% — Reduce &amp; Restructure</td><td>Overspending</td><td>Add non-converting terms to Negative Keywords; pause high-spend non-converting ASINs; move paused ASINs to new focused campaign; reduce bids on high-ACoS keywords</td></tr>
            </tbody>
        </table>
        <div class='callout info'>
            <div><strong>Adding Negative Keywords:</strong><br>
            Advertising → Campaign Manager → (Campaign) → Negative Keywords → Add Negative Keywords<br>
            Add irrelevant or high-spend non-converting terms as Negative Exact or Negative Phrase</div>
        </div>

        <h3>5. Campaign Health — Additional Scenarios</h3>
        <table class='data-table'>
            <thead><tr><th>Scenario</th><th>Fix</th></tr></thead>
            <tbody>
                <tr><td>No Impressions</td><td>Raise bids ₹5+ above Amazon suggested bid; add broad-match keywords; create product targeting campaign on competitor ASINs</td></tr>
                <tr><td>Spend but No Sales</td><td>Replace under-performing ASINs with high-CVR ASINs; add non-converting terms as negatives; test new manual or auto campaign</td></tr>
                <tr><td>Budget Exhausted Daily</td><td>Increase daily budget by 20–30%; prioritise Fast-Moving ASINs (allocate 70% budget) vs Slow-Moving (30%)</td></tr>
                <tr><td>Paused Campaigns</td><td>Enable → verify stock → update bids to current suggested level → confirm ₹150+ daily budget → no end date set</td></tr>
            </tbody>
        </table>

        <h3>6. Keyword Harvesting SOP (Auto → Manual)</h3>
        <p><strong>Weekly SOP:</strong></p>
        <ol>
            <li>SC → Reports → Advertising Reports → Search Term Report</li>
            <li>Filter: ACoS &lt; target AND Orders ≥ 3 (minimum statistical confidence)</li>
            <li>Add qualifying terms as Exact or Phrase to manual campaign — bid 30% higher than auto bid</li>
            <li>Add low performers (clicks ≥ 10, 0 orders) as Negative Exact in auto campaign</li>
            <li>Review every alternate day for active optimisation — not just weekly</li>
        </ol>

        <h3>7. ACoS vs TACoS Framework</h3>
        <div class='callout info'>
            <div><strong>ACoS</strong> = Ad Spend ÷ Ad Revenue × 100<br>
            Target tiers: &lt;25% = scale up | 25–35% = monitor | &gt;35% = restructure<br><br>
            <strong>TACoS</strong> = Ad Spend ÷ Total Revenue × 100 (ad + organic combined)<br>
            Target: &lt;15% — declining TACoS proves organic revenue is growing faster than ad dependence<br><br>
            <strong>Budget split by ASIN type:</strong> Fast-Moving 70% (Auto + Manual + Product Targeting) | Slow-Moving 30% (Auto only)</div>
        </div>

        <h3>8. Sponsored Brands — Headline &amp; Video Ads</h3>
        <ul>
            <li><strong>Headline Ads:</strong> Top of search banner → 3 ASINs + logo + headline copy</li>
            <li><strong>Brand Store destination:</strong> Link to Brand Store for maximum browse experience</li>
            <li><strong>Sponsored Brands Video (SBV):</strong> Auto-play video in search results — highest CTR format</li>
            <li>Requires Brand Registry. Budget: ₹150/day minimum (same as SP minimum)</li>
        </ul>

        <h3>9. Sponsored Display — Retargeting &amp; Audience</h3>
        <table class='data-table'>
            <thead><tr><th>Targeting Type</th><th>Audience</th><th>Best Use Case</th></tr></thead>
            <tbody>
                <tr><td>Product targeting</td><td>Shoppers viewing specific ASINs</td><td>Competitor conquest, cross-sell</td></tr>
                <tr><td>Audience retargeting</td><td>Shoppers who viewed your ASIN but didn't buy</td><td>Re-engage warm audiences</td></tr>
                <tr><td>Category interest</td><td>Shoppers browsing your category</td><td>Top-of-funnel awareness</td></tr>
            </tbody>
        </table>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://advertising.amazon.in' target='_blank'>Amazon Advertising Console</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/advertising/dashboard' target='_blank'>Ads Dashboard</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/gc/advertising/sponsored-ads' target='_blank'>Campaign Manager</a>
            <a class='btn-sc' href='https://sell.amazon.in/seller-university' target='_blank'>Seller University</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Campaigns spend ₹20,000+/month but ACoS is stuck above 40% — budget draining into non-converting keywords with no clear action taken.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Apply the 3-tier ACoS framework immediately: campaigns &gt;35% ACoS → add high-spend non-converters as Negative Exact, pause non-converting ASINs, reduce bids by 20%. Set ₹150 minimum daily budget and switch to Dynamic Up &amp; Down bidding. Review Search Term Report every alternate day, not weekly.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>TACoS is the north star metric, not ACoS. If TACoS is declining while ACoS stays flat, ads are building organic rank — that's the compounding flywheel. Invest heavily in &lt;25% ACoS campaigns (scale 30% bid increases) while restructuring the high-ACoS ones. The auto→manual harvest cycle, done weekly, is what separates 15% TACoS accounts from 40% ones.</p></div>
            </div>
        </div>
    """,
    "process_flow": """
        <div class='svg-wrapper'>
            <svg viewBox="0 0 900 120" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
                <defs><marker id="arr_t1" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#1e3a5f"/></marker></defs>
                <text x="450" y="65" class="svg-watermark" transform="rotate(-12,450,65)">© SMEMinds | smeminds.com</text>
                <rect x="10"  y="35" width="120" height="50" rx="8" class="flow-step"/><text x="70"  y="62" class="flow-text">Auto</text><text x="70"  y="76" class="flow-text">Campaign</text>
                <line x1="130" y1="60" x2="160" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_t1)"/>
                <rect x="160" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="220" y="62" class="flow-text">2-Week</text><text x="220" y="76" class="flow-text">Run</text>
                <line x1="280" y1="60" x2="310" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_t1)"/>
                <rect x="310" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="370" y="62" class="flow-text">Harvest</text><text x="370" y="76" class="flow-text">Search Terms</text>
                <line x1="430" y1="60" x2="460" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_t1)"/>
                <rect x="460" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="520" y="62" class="flow-text">Manual</text><text x="520" y="76" class="flow-text">Exact/Phrase</text>
                <line x1="580" y1="60" x2="610" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_t1)"/>
                <rect x="610" y="35" width="120" height="50" rx="8" class="flow-step"/><text x="670" y="62" class="flow-text">Add</text><text x="670" y="76" class="flow-text">Negatives</text>
                <line x1="730" y1="60" x2="760" y2="60" stroke="#1e3a5f" stroke-width="2" marker-end="url(#arr_t1)"/>
                <rect x="760" y="35" width="120" height="50" rx="8" class="flow-step" style="fill:#ff6b35;"/><text x="820" y="62" class="flow-text" style="fill:#fff">Optimise</text><text x="820" y="76" class="flow-text" style="fill:#fff">Every 2 Days</text>
            </svg>
        </div>
    """,
    "tools": "",
    "videos": [],
    "checklist": [
        "Auto campaign live for every ASIN within 24 hours of launch — minimum ₹150/day budget",
        "Default bidding strategy set to Dynamic Bids — Up and Down",
        "Manual campaigns (Exact/Phrase/Broad) created after 2-week auto data",
        "Keyword harvest performed weekly — converting terms (3+ orders) moved to manual",
        "Negative keywords updated weekly from Search Term Report",
        "ACoS tier reviewed: &lt;25% = scale up 30% | 25–35% = tune | &gt;35% = restructure",
        "Sponsored Brands campaign live (if Brand Registered)",
        "Sponsored Display retargeting active on top 10 ASINs",
        "TACoS &lt;15% overall — tracked in Campaign Manager"
    ],
    "quiz": [
        {
            "question": "What is TACoS and why is it more important than ACoS for growth?",
            "options": [
                "Total ACoS = total ad spend ÷ total revenue; shows organic growth vs ad dependence",
                "Total ACoS = ad revenue ÷ total revenue; shows profit margin",
                "TACoS is the same as ACoS but calculated monthly",
                "TACoS measures click-through rate across all ad types"
            ],
            "answer": "Total ACoS = total ad spend ÷ total revenue; shows organic growth vs ad dependence",
            "explanation": "TACoS = Ad Spend ÷ (Ad Revenue + Organic Revenue). Declining TACoS means organic is growing — ads are building sustainable rank, not just buying sales."
        },
        {
            "question": "According to SMEMinds' Sponsored Ads Guide, what is the minimum daily budget per campaign to avoid budget exhaustion?",
            "options": ["₹50/day", "₹100/day", "₹150/day", "₹500/day"],
            "answer": "₹150/day",
            "explanation": "The SMEMinds Sponsored Ads Guide explicitly states: 'Set a minimum daily budget of ₹150 or above per campaign to avoid budget exhaustion.' This is the official recommended floor."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "3.2",
    "number": "Module 3.2",
    "title": "DSP & Display",
    "difficulty": "Expert",
    "time": "40 mins",
    "overview": """<p>Amazon DSP (Demand-Side Platform) extends your reach beyond Amazon's pages to 300M+ users across Amazon-owned and third-party properties. This module covers programmatic display strategy, audience segmentation, retargeting, lookalike audiences, and OTT/streaming TV for brand awareness — advanced tools for top-of-funnel growth.</p>""",
    "content": """
        <h3>1. Amazon DSP — Programmatic Display Strategy</h3>
        <div class='callout pro-tip'>
            <div><strong>DSP vs Sponsored Display:</strong><br>
            • <strong>Sponsored Display</strong> (self-serve): Product page and search, ASIN-level, accessible to all sellers<br>
            • <strong>Amazon DSP</strong> (managed/self-serve): Amazon + third-party sites, audience-level, minimum spend ~₹5L/month managed or via Amazon Advertising account for self-serve access</div>
        </div>
        <p>DSP is ideal for brands with ₹1Cr+ monthly GMV who want to build brand awareness beyond Amazon search.</p>

        <h3>2. Audience Segmentation</h3>
        <table class='data-table'>
            <thead><tr><th>Segment</th><th>Definition</th><th>Bid Premium</th></tr></thead>
            <tbody>
                <tr><td>Retargeting — ASIN Viewers</td><td>Viewed your ASIN, didn't purchase (last 30 days)</td><td>Highest — warmest audience</td></tr>
                <tr><td>Retargeting — Cart Abandoners</td><td>Added to cart, didn't complete purchase</td><td>Very high</td></tr>
                <tr><td>Lookalike — Customer Match</td><td>Similar to your existing customers</td><td>High</td></tr>
                <tr><td>In-Market Audience</td><td>Actively searching in your category</td><td>Medium-High</td></tr>
                <tr><td>Lifestyle Audience</td><td>Matches consumer lifestyle profile</td><td>Medium</td></tr>
            </tbody>
        </table>

        <h3>3. Retargeting Strategy</h3>
        <ol>
            <li><strong>ASIN Viewer Retargeting:</strong> Show ads to customers who viewed your ASIN in last 30 days on Amazon + partner sites</li>
            <li><strong>Cross-sell retargeting:</strong> Show your complementary ASIN to recent buyers of a related product</li>
            <li><strong>Reorder retargeting:</strong> Re-engage past buyers at predicted repurchase date (consumables)</li>
        </ol>

        <h3>4. Sponsored Display — Self-Serve Retargeting</h3>
        <p>For sellers not yet at DSP scale, Sponsored Display provides audience retargeting within Amazon. Key targeting options:</p>
        <ul>
            <li><strong>Views remarketing:</strong> Customers who viewed your ASIN in past 30 days</li>
            <li><strong>Purchases remarketing:</strong> Past buyers of your category (cross-sell opportunity)</li>
            <li><strong>Product targeting:</strong> Show ads on competitor ASINs to intercept their shoppers</li>
        </ul>
        <p>Path: <strong>SC → Advertising → Campaign Manager → Create → Sponsored Display</strong></p>

        <h3>5. OTT / Streaming TV Ads</h3>
        <ul>
            <li><strong>Placement:</strong> Amazon Prime Video (India), MX Player, Fire TV</li>
            <li><strong>Format:</strong> Non-skippable 15–30 sec video ads</li>
            <li><strong>Measurement:</strong> Branded search lift, new-to-brand orders</li>
            <li><strong>Investment level:</strong> ₹10L+ minimum campaign — best for established brands building national awareness</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://advertising.amazon.in/solutions/products/amazon-dsp' target='_blank'>Amazon DSP</a>
            <a class='btn-sc' href='https://advertising.amazon.in' target='_blank'>Amazon Advertising Console</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/advertising/dashboard' target='_blank'>Sponsored Display</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller spends entirely on Sponsored Products, ignoring display retargeting — losing 60–70% of warm ASIN viewers who leave without buying and never come back.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Activate Sponsored Display views remarketing on your top 20 ASINs immediately (no DSP account needed). Set up a 30-day ASIN viewer audience and target them with a 10–15% lower price or coupon message. This recaptures warm traffic at a fraction of the cost of acquiring cold traffic.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>DSP is not for most sellers — it's a brand-building tool for ₹1Cr+ GMV accounts. For mid-tier sellers, Sponsored Display retargeting delivers 80% of the value at 10% of the cost. Master Sponsored Display first, then graduate to DSP when your monthly ad budget consistently exceeds ₹3–5L and you need reach beyond Amazon.in.</p></div>
            </div>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Sponsored Display retargeting live on all top 20 ASINs",
        "Audience segments defined: viewer retargeting + cart abandoner",
        "DSP evaluated for brands at ₹1Cr+ monthly GMV",
        "New-to-Brand metrics tracked weekly from Sponsored Brands/Display",
        "OTT ads considered for brand-building campaigns"
    ],
    "quiz": [
        {
            "question": "Which audience segment has the highest purchase intent for retargeting?",
            "options": ["Lifestyle audience", "In-market audience", "Cart abandoners", "Lookalike audience"],
            "answer": "Cart abandoners",
            "explanation": "Cart abandoners have demonstrated the strongest purchase intent — they selected your product but didn't complete checkout. This is the warmest retargeting segment."
        },
        {
            "question": "What is the key difference between Sponsored Display and Amazon DSP?",
            "options": [
                "Sponsored Display uses video, DSP uses banners",
                "DSP reaches users on Amazon + third-party sites; Sponsored Display is Amazon pages only",
                "DSP is free, Sponsored Display is paid",
                "Sponsored Display requires Brand Registry, DSP does not"
            ],
            "answer": "DSP reaches users on Amazon + third-party sites; Sponsored Display is Amazon pages only",
            "explanation": "Amazon DSP is a programmatic platform reaching 300M+ users across Amazon.in and third-party publisher websites. Sponsored Display is primarily on Amazon product and search pages."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "3.3",
    "number": "Module 3.3",
    "title": "External Traffic",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": """<p>External traffic — from social media, influencers, Google Ads, and affiliate channels — can dramatically boost organic rank on Amazon. Amazon's A10 algorithm rewards external traffic with ranking boosts. This module covers the full external traffic playbook including Amazon Attribution tags, social strategy, influencer partnerships, and the Brand Referral Bonus programme.</p>""",
    "content": """
        <h3>1. Amazon Attribution — Track Everything</h3>
        <div class='callout pro-tip'>
            <div><strong>Amazon Attribution</strong> lets you measure how external traffic converts on Amazon.<br>
            Create attribution tags at: <strong>SC → Advertising → Amazon Attribution</strong><br><br>
            Create a unique tag for every channel: Facebook, Instagram, Google, Email, Influencer<br>
            This unlocks the Brand Referral Bonus for Brand Registered sellers: Amazon pays a ~10% bonus credit on first-time purchases driven by external traffic tagged with Attribution tags.</div>
        </div>

        <h3>2. Brand Referral Bonus — How It Works</h3>
        <div class='callout success'>
            <div><strong>Brand Referral Bonus (BRB):</strong><br>
            • Eligible: Brand Registered sellers with Amazon Attribution set up<br>
            • Benefit: ~10% bonus credit on referred sales (applied to future referral fees)<br>
            • How: Drive traffic via social/influencer/Google using Attribution-tagged URLs<br>
            • The bonus is automatically calculated and credited — no manual claim needed<br>
            • This effectively reduces your cost of external advertising by 10%</div>
        </div>

        <h3>3. Social Media → Amazon Strategy</h3>
        <table class='data-table'>
            <thead><tr><th>Platform</th><th>Content Type</th><th>Link Strategy</th></tr></thead>
            <tbody>
                <tr><td>Instagram Reels</td><td>30-sec product demos, unboxing</td><td>Bio link → landing page with Amazon button</td></tr>
                <tr><td>Facebook Ads</td><td>Carousel with product images &amp; USPs</td><td>Attribution-tagged Amazon product URL</td></tr>
                <tr><td>YouTube</td><td>Review-style or how-to videos</td><td>Description link with attribution tag</td></tr>
                <tr><td>WhatsApp / Meta</td><td>Direct message deals to opted-in subscribers</td><td>Attribution-tagged URL</td></tr>
            </tbody>
        </table>

        <h3>4. Influencer &amp; Affiliate Marketing</h3>
        <ul>
            <li><strong>Amazon Influencer Programme:</strong> Indian creators with storefronts on Amazon — they earn commission on sales</li>
            <li><strong>Amazon Associates:</strong> Affiliate publishers earn 1–10% commission by driving traffic to Amazon</li>
            <li><strong>Micro-influencers (10K–100K followers):</strong> Often 3–5× higher engagement than macro — ideal for niche products</li>
            <li><strong>Selection criteria:</strong> Category fit, India audience, ≥3% engagement rate, authentic reviews track record</li>
        </ul>
        <div class='callout info'>
            <div><strong>Influencer collaboration model:</strong><br>
            1. Send product free for review (no guaranteed positive review agreed — Amazon ToS compliance)<br>
            2. Provide attribution-tagged Amazon link<br>
            3. Offer 5–10% affiliate commission on verifiable sales via Amazon Associates</div>
        </div>

        <h3>5. Google Shopping / Search Ads to Amazon</h3>
        <p>While sending Google traffic to Amazon is not always the most capital-efficient strategy, it can boost organic ranking during launch. Use sparingly:</p>
        <ul>
            <li>Create a Google Shopping campaign targeting brand + category keywords</li>
            <li>Destination: Your Amazon product page with attribution tag</li>
            <li>Monitor: attribution-tagged conversion rate in Amazon Attribution dashboard</li>
            <li>Best used during launch phase to accelerate BSR improvement</li>
        </ul>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/attribution/overview' target='_blank'>Amazon Attribution</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/gp/cobrandingpage/marketing-communications' target='_blank'>Brand Referral Bonus</a>
            <a class='btn-sc' href='https://affiliate-program.amazon.in' target='_blank'>Amazon Associates India</a>
            <a class='btn-sc' href='https://sell.amazon.in/seller-university' target='_blank'>Seller University</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller runs Instagram and influencer campaigns driving traffic to Amazon but has no way to measure which channel or influencer actually converted — marketing spend feels like a black box.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Set up Amazon Attribution immediately (SC → Advertising → Amazon Attribution). Create a unique tracking tag for each channel and each influencer. This gives you exact conversion data per source. Simultaneously enrol in Brand Referral Bonus to recover ~10% of referred sales as a fee credit — it monetises your external marketing investment.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>External traffic is an organic rank multiplier, not just a sales channel. Amazon's algorithm interprets traffic arriving from outside Amazon.in as a strong quality signal — rewarding the listing with improved organic placement. A well-executed external traffic campaign during launch can cut your time to Page 1 organic rank by 30–50%, reducing the total Sponsored Ads spend needed.</p></div>
            </div>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Amazon Attribution account set up and tags created for every channel",
        "Brand Referral Bonus programme enrolled",
        "Attribution-tagged URLs used in all external campaigns",
        "Social media content calendar includes Amazon product links",
        "At least 3 influencer partnerships active per quarter",
        "External traffic conversion rate tracked in Attribution dashboard weekly"
    ],
    "quiz": [
        {
            "question": "What financial benefit does the Brand Referral Bonus provide?",
            "options": [
                "10% discount on FBA fees",
                "~10% bonus credit on first-time purchases driven by external traffic",
                "Free Lightning Deal submission",
                "10% discount on Sponsored Ads"
            ],
            "answer": "~10% bonus credit on first-time purchases driven by external traffic",
            "explanation": "Amazon's Brand Referral Bonus pays Brand Registered sellers a ~10% bonus credit on sales generated through external traffic tagged with Amazon Attribution tags. This credit offsets future referral fees."
        },
        {
            "question": "Why does Amazon's A10 algorithm reward external traffic?",
            "options": [
                "External traffic has lower ad costs",
                "Amazon charges a higher referral fee for external sales",
                "External traffic demonstrates demand beyond Amazon, boosting organic rank",
                "It increases Amazon's marketplace market share"
            ],
            "answer": "External traffic demonstrates demand beyond Amazon, boosting organic rank",
            "explanation": "Amazon rewards external traffic because it shows the product has genuine demand across channels. This signals quality and relevance, which improves organic search ranking."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "3.4",
    "number": "Module 3.4",
    "title": "Organic SEO",
    "difficulty": "Intermediate",
    "time": "40 mins",
    "overview": """<p>Organic rank on Amazon is the most profitable traffic you can get — zero marginal cost, high conversion intent. This module covers search term rank tracking, BSR monitoring, CTR optimisation, the Search Query Performance deep dive, and the full purchase rate funnel analysis from impressions to orders.</p>""",
    "content": """
        <h3>1. Search Term Rank Tracking</h3>
        <div class='callout pro-tip'>
            <div><strong>Rank Tiers to Track (Weekly):</strong><br>
            • <strong>Top 3 position:</strong> The "cash" zone — captures 50%+ of clicks for that keyword<br>
            • <strong>Top 10:</strong> First page visibility — captures 80%+ of all clicks<br>
            • <strong>Page 1:</strong> Any position on page 1 — minimum viable organic presence<br><br>
            Tools: Helium 10 Keyword Tracker, DataHawk, SellerApp Rank Tracker</div>
        </div>

        <h3>2. BSR (Best Seller Rank) Tracking</h3>
        <table class='data-table'>
            <thead><tr><th>BSR Level</th><th>What It Means</th><th>Action</th></tr></thead>
            <tbody>
                <tr><td>BSR &lt;10</td><td>Top 10 in category — bestseller badge</td><td>Maintain stock, protect with ads</td></tr>
                <tr><td>BSR 10–100</td><td>Strong performer, significant volume</td><td>Protect rank with competitive pricing</td></tr>
                <tr><td>BSR 100–500</td><td>Good mid-tier product</td><td>Increase ads, improve CVR</td></tr>
                <tr><td>BSR 500–5,000</td><td>Moderate performer</td><td>Content optimisation, deals</td></tr>
                <tr><td>BSR &gt;5,000</td><td>Low visibility</td><td>Evaluate for exit or major overhaul</td></tr>
            </tbody>
        </table>
        <p>Track daily BSR in: <strong>SC → Business Reports → Sales Dashboard</strong></p>

        <h3>3. CTR Optimisation</h3>
        <p>Low CTR = customers see your listing but don't click. Fix levers:</p>
        <ul>
            <li><strong>Main image:</strong> Run A/B test via Manage Your Experiments</li>
            <li><strong>Title:</strong> Front-load highest-volume keyword, make benefit clear in first 80 characters</li>
            <li><strong>Price:</strong> If BSR is declining but no price change — competitors have undercut you</li>
            <li><strong>Badges:</strong> "#1 Best Seller", "Amazon's Choice", "Climate Pledge Friendly" all increase CTR</li>
            <li><strong>Star rating:</strong> &gt;4.0★ significantly improves CTR vs. below 4.0★</li>
            <li><strong>Coupons:</strong> Green coupon badge in search results increases CTR by 15–25%</li>
        </ul>

        <h3>4. Search Query Performance Report — Deep Dive</h3>
        <p>The SQP report is the most powerful organic SEO tool in Seller Central (Brand Registered sellers only):</p>
        <ol>
            <li>SC → Brand Analytics → Search Query Performance</li>
            <li>Filter by ASIN → Sort by Impressions descending</li>
            <li><strong>High impressions, low click share</strong> = title or main image not compelling → optimise above-the-fold</li>
            <li><strong>High click share, low conversion</strong> = price or content issue → audit detail page</li>
            <li><strong>Low impressions</strong> = keyword not in listing → add to title or backend search terms</li>
        </ol>

        <h3>5. Purchase Rate Funnel Analysis</h3>
        <div class='callout success'>
            <div><strong>The 3-Step Funnel:</strong><br>
            Impressions → <strong>CTR</strong> → Clicks → <strong>CVR</strong> → Orders<br><br>
            • CTR benchmark (Amazon India): 0.3–0.5% in search results<br>
            • CVR benchmark: 8–15% depending on category<br>
            • Identify the weakest step and fix it first before increasing ad spend</div>
        </div>

        <h3>6. Campaign Manager — ACoS-Organic Connection</h3>
        <div class='callout info'>
            <div><strong>Organic Rank + Paid Rank = Total Visibility:</strong><br>
            Sponsored Ads that generate sales signal to Amazon that your ASIN converts for that keyword → improving organic rank over time. This is why TACoS (not just ACoS) is the right metric — organic growth is the compounding return on ad investment. Target ACoS below your category benchmark during GIS events (typically 10–15% for peak events).</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/brand-analytics/analytics/dashboard/searchQueryPerformance' target='_blank'>SQP Report</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/gp/site-metrics/report.html' target='_blank'>Business Reports</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/listing-quality-dashboard' target='_blank'>Listing Quality Dashboard</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller has decent sales but is invisible in organic search — 95% of revenue comes from paid ads. Turning off ads drops sales to near zero, creating total ad dependency and unsustainable margins.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Run the SQP report (SC → Brand Analytics → Search Query Performance) to identify keywords where you have high impressions but low click share — these are the keywords where better title/image content will unlock organic clicks. Also run Sponsored Ads for these same keywords to signal conversion relevance to Amazon's algorithm, driving organic rank improvement in parallel.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>Organic rank is earned through conversion signals, not just keyword stuffing. Amazon rewards ASINs that convert — so the fastest path to organic rank is: (1) optimise your listing for conversion, (2) drive targeted paid traffic to prove conversion, (3) harvest organic rank over 4–8 weeks. A listing with 12% CVR beats a listing with 5% CVR on the same keyword every time.</p></div>
            </div>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Top 20 keywords tracked weekly (Top 3 / Top 10 / Page 1 positions)",
        "BSR tracked daily for all hero ASINs",
        "CTR tracked in Business Reports — benchmark ≥0.3%",
        "SQP report reviewed weekly — action items created for underperformers",
        "Funnel analysis (Impressions → CTR → CVR → Orders) done monthly per ASIN",
        "Listing Quality Dashboard reviewed — all suppressions resolved"
    ],
    "quiz": [
        {
            "question": "In the Search Query Performance report, high impressions but low click share indicates what problem?",
            "options": [
                "Keyword not in listing",
                "Title or main image not compelling enough",
                "Price too high",
                "Out of stock"
            ],
            "answer": "Title or main image not compelling enough",
            "explanation": "High impressions means you're appearing in search. Low click share means customers see your listing but choose competitors — the fix is title or main image optimisation."
        },
        {
            "question": "What CTR benchmark should Amazon India listings aim for?",
            "options": ["0.01–0.05%", "0.3–0.5%", "2–5%", "10–15%"],
            "answer": "0.3–0.5%",
            "explanation": "Average CTR for Amazon India search results is 0.3–0.5%. Consistently below 0.3% signals a title, image, or pricing issue."
        }
    ]
},

# ─────────────────────────────────────────────────────────────
{
    "id": "3.5",
    "number": "Module 3.5",
    "title": "Deals & Events",
    "difficulty": "Intermediate",
    "time": "35 mins",
    "overview": """<p>Amazon India's deal events — Great Indian Festival, Prime Day, Diwali, and Lightning Deals — are traffic multipliers delivering 5–10× normal daily sales. This module covers the complete deal planning calendar, STEP program fee tiers, SSLD submission process, eligibility requirements, and GIS preparation with 90+ day lead times.</p>""",
    "content": """
        <h3>1. Great Indian Sale — 90+ Day Preparation Mandate</h3>
        <div class='callout pro-tip'>
            <div><strong>GIS 2024 Key Dates (SMEMinds GIS Guide):</strong><br>
            ▸ Great Indian Festival (Diwali) — October 2024 (Prime members get 24-hr early access)<br>
            ▸ <strong>FC Inventory Cutoff: Send shipments to all 6 clusters before 10th September</strong><br>
            ▸ Flex / APOB Registration Deadline: 31st August<br>
            ▸ Coupon &amp; Deal Submission Deadline: Before 31st December (BAU rounds)<br><br>
            <strong>Rule: Start GIS preparation 90+ days in advance. Sellers who prepare last-minute consistently underperform.</strong></div>
        </div>

        <h3>2. GIS Preparation Timeline</h3>
        <table class='data-table'>
            <thead><tr><th>Week</th><th>Action</th></tr></thead>
            <tbody>
                <tr><td>-12 weeks (90 days)</td><td>Identify hero ASINs; start inventory build; resolve all ASIN suppressions</td></tr>
                <tr><td>-10 weeks</td><td>Submit Lightning Deal &amp; Best Deal applications via SSLD portal</td></tr>
                <tr><td>-8 weeks</td><td>FBA shipment creation across all 6 clusters; festive packaging if applicable; complete APOB/VPPOB</td></tr>
                <tr><td>-6 weeks</td><td>Festive A+ Content &amp; Brand Store GIS page published; coupons activated on Band A-B-C ASINs</td></tr>
                <tr><td>-4 weeks</td><td>Increase Sponsored Ads budgets 3–5×; add festive keywords; set up Prime Exclusive Discounts</td></tr>
                <tr><td>-2 weeks</td><td>Confirm all deals approved; all 6 clusters stocked; No Cost EMI enabled on ₹3K+ ASINs</td></tr>
                <tr><td>Event week</td><td>Monitor hourly; adjust bids (increase 20–40% on top keywords); target ACoS 10–15%</td></tr>
                <tr><td>+1 week</td><td>Return management; review collection; account health check; post-event keyword harvest</td></tr>
            </tbody>
        </table>

        <h3>3. Lightning Deal — Eligibility &amp; Submission</h3>
        <div class='callout info'>
            <div><strong>Lightning Deal Eligibility Requirements (SMEMinds Deals Guide):</strong><br>
            ✓ Professional Seller account<br>
            ✓ Minimum 5 seller feedback ratings per month<br>
            ✓ Overall seller rating ≥ 3.5 stars<br>
            ✓ Product rating ≥ 3 stars (if 5+ customer ratings exist)<br>
            ✓ Product in New Condition<br>
            ✓ Prime-eligible (FBA or Seller Fulfilled Prime)<br>
            ✓ All variations included (≥50% for apparel/shoes)<br>
            ✓ Enrolled in Amazon STEP program (determines fee tier)</div>
        </div>
        <p><strong>Submission Path:</strong></p>
        <ol>
            <li>SC → Advertising → Deals → (SSLD Portal: <code>sellercentral.amazon.in/merchandising-new</code>)</li>
            <li>Browse 'Eligible ASINs' section — only Amazon-recommended fast-moving ASINs appear here</li>
            <li>Click Edit → Set Schedule, Maximum Deal Price, Minimum Deal Quantity → Submit</li>
            <li>Submit at least 2 weeks before desired event window — Amazon doesn't guarantee slot</li>
        </ol>

        <h3>4. Lightning Deal Fee Structure — STEP Program Tiers</h3>
        <table class='data-table'>
            <thead><tr><th>STEP Level</th><th>Fee per Amazon-Recommended Lightning Deal</th></tr></thead>
            <tbody>
                <tr><td><strong>Premium</strong></td><td>₹222 per deal (best rate)</td></tr>
                <tr><td><strong>Advanced</strong></td><td>₹222 per deal (same as Premium)</td></tr>
                <tr><td>Standard</td><td>₹249 per deal</td></tr>
                <tr><td>Basic</td><td>₹277 per deal</td></tr>
            </tbody>
        </table>
        <div class='callout success'>
            <div><strong>SMEMinds Pro Tip:</strong> Always submit Lightning Deals on Fast Moving ASINs (your top recommended products). Premium and Advanced STEP sellers save ₹27–₹55 per deal vs Basic. For heavy deal users running 10+ deals/month, STEP level directly impacts deal costs.</div>
        </div>

        <h3>5. Self-Service Lightning Deals (SSLD)</h3>
        <ul>
            <li>SSLD allows sellers to configure and submit Lightning Deals <strong>directly without category manager approval</strong></li>
            <li>Path: SC → Advertising → Deals OR directly: <code>sellercentral.amazon.in/merchandising-new</code></li>
            <li>View 'Deal Bank' for pre-approved slots and available deal windows</li>
            <li>Duration: 4–12 hours (Amazon assigns slot)</li>
        </ul>

        <h3>6. Deal Types Comparison</h3>
        <table class='data-table'>
            <thead><tr><th>Deal Type</th><th>Duration</th><th>Minimum Discount</th><th>Best For</th></tr></thead>
            <tbody>
                <tr><td>Lightning Deal (LD)</td><td>4–12 hours</td><td>15–20% off reference price</td><td>Burst velocity, BSR boost, deals page traffic (10× during GIS)</td></tr>
                <tr><td>Best Deal (BD)</td><td>1–2 weeks</td><td>10%+ off reference price</td><td>Sustained velocity, keyword rank improvement</td></tr>
                <tr><td>Prime Exclusive Discount (PED)</td><td>Event window</td><td>Category-specific</td><td>Prime members only — very high conversion during GIS</td></tr>
                <tr><td>Coupon</td><td>Seller-defined (continuous)</td><td>5%+ (15%+ for max CTR)</td><td>Continuous search CTR lift (green badge — +15–25% CTR)</td></tr>
            </tbody>
        </table>

        <h3>7. GIS Advertising Strategy</h3>
        <div class='callout info'>
            <div><strong>GIS Ad Budget Rules:</strong><br>
            • Increase bids by 20–40% on top-performing keywords 1 week before sale<br>
            • GIS ad spend is 3–5× more competitive than BAU periods<br>
            • Target ACoS: 10–15% for GIS events (more aggressive than BAU 25–35% threshold)<br>
            • Pause low-performing ASINs from campaigns to preserve budget for high-velocity products<br>
            • Set hourly budget caps to avoid over-spending in peak morning hours</div>
        </div>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/merchandising-new' target='_blank'>Lightning Deals (SSLD)</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/prime-exclusive-discounts' target='_blank'>Prime Exclusive Discounts</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/coupons' target='_blank'>Manage Coupons</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/promotions' target='_blank'>Manage Promotions</a>
            <a class='btn-sc' href='https://sellercentral.amazon.in/advertising/dashboard' target='_blank'>Campaign Manager</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller tries to submit Lightning Deals 1–2 weeks before GIF/Prime Day and discovers their ASIN is not in the Eligible ASINs section — missing the biggest sales window of the year entirely.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Solution</div><p>Apply the 90-day GIS preparation rule. Check Eligible ASINs in the SSLD portal (sellercentral.amazon.in/merchandising-new) at 10 weeks out. If ASINs are missing: verify 3+ star rating, Prime eligibility (FBA/SFP), and that the account has 5+ monthly feedback ratings and 3.5+ seller rating. Resolve eligibility gaps immediately — don't wait. Prioritise Fast-Moving ASINs for deal submissions.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Strategic Insight</div><p>The STEP program is not just a badge — it's a direct cost reduction on deal fees. Premium/Advanced STEP sellers pay ₹222 vs ₹277 for Basic. If you run 20 deals/month, that's ₹1,100/month saved. More importantly, high STEP levels signal account health and often unlock better deal slot access. Treat STEP level improvement as a quarterly goal alongside your sales targets.</p></div>
            </div>
        </div>
    """,
    "process_flow": "",
    "tools": "",
    "videos": [],
    "checklist": [
        "Event calendar built for full year (GIF, Prime Day, Diwali, GOSF, Republic Day)",
        "GIS preparation started 90+ days before event",
        "FBA inventory shipped to all 6 clusters before FC cutoff (10th September for GIF)",
        "APOB/VPPOB cluster registration completed by 31st August deadline",
        "Lightning Deal submissions via SSLD completed 10 weeks before event",
        "STEP program level checked — target Premium/Advanced for ₹222 deal fee",
        "Sponsored Ads budgets pre-set to 3–5× normal for event week",
        "Prime Exclusive Discounts configured for GIS event window",
        "Coupons running on Band A-B-C ASINs for continuous CTR lift"
    ],
    "quiz": [
        {
            "question": "How many weeks in advance should GIS preparation start according to SMEMinds' GIS Guide?",
            "options": ["2 weeks", "4 weeks", "8 weeks", "12 weeks (90+ days)"],
            "answer": "12 weeks (90+ days)",
            "explanation": "SMEMinds' GIS Guide states: 'Sellers who prepare 90+ days in advance consistently outperform those who react last-minute.' The FC inventory cutoff for GIF is 10th September — meaning shipments must leave your warehouse 12 weeks before the October event."
        },
        {
            "question": "What is the Lightning Deal fee for Premium and Advanced STEP sellers on Amazon India?",
            "options": ["₹100 per deal", "₹222 per deal", "₹249 per deal", "₹500 per deal"],
            "answer": "₹222 per deal",
            "explanation": "Per the SMEMinds Deals Guide fee structure: Premium and Advanced STEP sellers both pay ₹222 per Amazon-recommended Lightning Deal — the lowest available rate. Standard STEP pays ₹249 and Basic pays ₹277."
        }
    ]
}
,

# ─────────────────────────────────────────────────────────────
{
    "id": "3.6",
    "number": "Module 3.6",
    "title": "Sponsored Ads Deep-Dive — PPC Campaign Planning",
    "difficulty": "Advanced",
    "time": "50 mins",
    "overview": """<p>Amazon Sponsored Ads are the most direct lever for sales velocity — but poorly structured campaigns can burn through budget with zero returns. This module covers the complete campaign architecture, from Automatic discovery campaigns to Manual keyword campaigns with bid optimization, ACoS management, and seasonal scaling strategy used by top-performing Amazon India sellers.</p>""",
    "content": """
        <h3>1. The Three Ad Types</h3>
        <table class='data-table'>
            <thead><tr><th>Ad Type</th><th>Eligibility</th><th>Placement</th><th>Best For</th></tr></thead>
            <tbody>
                <tr><td><strong>Sponsored Products (SP)</strong></td><td>All professional sellers</td><td>Search results + detail pages</td><td>Individual ASIN visibility + sales</td></tr>
                <tr><td><strong>Sponsored Brands (SB)</strong></td><td>Brand Registry required</td><td>Top of search (banner)</td><td>Brand awareness + new customer acquisition</td></tr>
                <tr><td><strong>Sponsored Display (SD)</strong></td><td>Brand Registry required</td><td>Competitor PDPs + off-Amazon</td><td>Retargeting + conquesting</td></tr>
            </tbody>
        </table>

        <h3>2. Campaign Architecture — The Auto-to-Manual Flow</h3>
        <div class='callout pro-tip'><div><strong>The 4-Week Launch Protocol:</strong><br>
        Week 1–2: Run Automatic campaign (budget ₹500–₹1,000/day). Let Amazon discover converting search terms.<br>
        Week 3: Download Search Term Report → identify terms with &gt;5 clicks and 1+ orders (high-intent).<br>
        Week 4: Create Manual campaign with top-performing keywords. Add converting terms as Exact match. Add non-converting terms as Negative matches in Auto campaign.<br>
        Ongoing: Scale Manual budget on profitable keywords; reduce Auto budget as Manual scales.</div></div>

        <h3>3. Setting Up Sponsored Products Campaign</h3>
        <ol>
            <li>Go to <strong>Advertising → Advertising Console → Create Campaign → Sponsored Products</strong></li>
            <li>Name campaign: "SP – [Product] – [Auto/Manual] – [Priority]"</li>
            <li>For <strong>Automatic:</strong><br>
            Select ASIN | Set daily budget ₹500–₹1,000 | Set default bid ₹5–₹10 | Launch</li>
            <li>For <strong>Manual (after Auto data collection):</strong><br>
            Create ad groups | Add keywords + bid per keyword | Set match types (Exact, Phrase, Broad) | Launch</li>
        </ol>

        <h3>4. The ACoS Framework</h3>
        <p><strong>ACoS</strong> = (Ad Spend ÷ Ad Revenue) × 100</p>
        <table class='data-table'>
            <thead><tr><th>ACoS Range</th><th>Status</th><th>Action</th></tr></thead>
            <tbody>
                <tr><td>&lt;15%</td><td>Excellent</td><td>Scale budget aggressively</td></tr>
                <tr><td>15–25%</td><td>Good</td><td>Maintain; optimize bids</td></tr>
                <tr><td>25–35%</td><td>Acceptable</td><td>Review keywords; pause low-converters</td></tr>
                <tr><td>&gt;35%</td><td>Concerning</td><td>Pause or reduce bids immediately</td></tr>
                <tr><td>&gt;50%</td><td>Loss-making</td><td>Pause campaign; restructure</td></tr>
            </tbody>
        </table>
        <div class='callout info'><div><strong>Rule of Thumb:</strong> Target ACoS below your net margin %. If your margin is 30%, keep ACoS below 25–28% to remain profitable after ads.</div></div>

        <h3>5. Match Types — When to Use Each</h3>
        <table class='data-table'>
            <thead><tr><th>Match Type</th><th>How It Works</th><th>Use For</th></tr></thead>
            <tbody>
                <tr><td>Broad</td><td>Amazon shows ad for related terms (includes synonyms)</td><td>Discovery; finding new keywords</td></tr>
                <tr><td>Phrase</td><td>Ad shows when search contains your keyword phrase</td><td>Balance of reach + control</td></tr>
                <tr><td>Exact</td><td>Ad shows only for exact keyword or close variants</td><td>Best-performing, proven keywords</td></tr>
                <tr><td>Negative Exact</td><td>Blocks specific irrelevant search terms</td><td>Cost control; remove wasted spend</td></tr>
            </tbody>
        </table>

        <h3>6. Bid Optimization Weekly Workflow</h3>
        <ol>
            <li>Pull Search Term Report from Advertising Console (weekly)</li>
            <li>Identify high ACoS keywords (&gt;35%) → lower bid by 15–20% or add to Negative list</li>
            <li>Identify low ACoS + high-impression keywords → raise bid by 10–15% to capture more volume</li>
            <li>Move top-performing broad/phrase terms to Exact match campaigns</li>
            <li>Add completely irrelevant terms to Negative Exact list in Auto campaign</li>
        </ol>

        <h3>7. Seasonal Budget Scaling</h3>
        <table class='data-table'>
            <thead><tr><th>Season</th><th>Budget Adjustment</th></tr></thead>
            <tbody>
                <tr><td>Low Season (Jun–Aug)</td><td>Reduce by 20–30%; focus on high-intent, low-competition keywords</td></tr>
                <tr><td>Pre-Festive (Aug–Sep)</td><td>Increase by 30–50%; add seasonal keywords</td></tr>
                <tr><td>Festive Season (Oct–Nov)</td><td>Increase by 50–100%; expand match types; run SB banners</td></tr>
                <tr><td>Peak (Diwali, Prime Day)</td><td>Maximum budget; aggressive bid on all profitable keywords</td></tr>
            </tbody>
        </table>

        <div class='bookmarks-inline'>
            <strong>Key Links:</strong><br>
            <a class='btn-sc' href='https://sellercentral.amazon.in/advertising/dashboard' target='_blank'>Advertising Console</a>
            <a class='btn-sc' href='https://advertising.amazon.in' target='_blank'>Amazon Ads India</a>
            <a class='pill-sc' href='https://sellercentral.amazon.in/gp/help/external/G200663330' target='_blank'>Search Term Report Help</a>
        </div>

        <div class='pain-point-section'>
            <div class='pain-point-header'><span>⚠️</span><h4>Seller Pain Points &amp; Strategic Solutions</h4></div>
            <div class='pain-point-body'>
                <div class='pp-card pp-pain'><div class='pp-card-label'>😤 Pain Point</div><p>Seller runs Auto campaign for 3 months without downloading Search Term Report — spending ₹50,000/month on keywords that have never converted. ACoS: 68%. No campaign ever switches to Manual.</p></div>
                <div class='pp-card pp-solution'><div class='pp-card-label'>✅ Strategic Solution</div><p>Download Search Term Report weekly. Rule: Any keyword with &gt;20 clicks and 0 orders → Negative Exact. Any keyword with ≥3 orders in 14 days → move to Exact match Manual campaign and scale budget.</p></div>
                <div class='pp-card pp-insight'><div class='pp-card-label'>💡 Pro Insight</div><p>During festive season, CPCs (cost per click) spike 2–3× as competitors flood the auction. Solution: Pre-build your converting Exact match keyword list 4 weeks before the event so you're not bidding on unknown terms at premium prices.</p></div>
            </div>
        </div>
    """,
    "checklist": [
        "Started with Automatic campaign for discovery (2 weeks minimum)",
        "Downloaded Search Term Report and identified high-intent keywords",
        "Created Manual campaign with Exact match for top-converting keywords",
        "Set ACoS target below net margin percentage",
        "Added irrelevant terms as Negative Exact in Auto campaign",
        "Campaign naming convention applied: SP – [Product] – [Auto/Manual]",
        "Seasonal budget scaling calendar set up with reminders"
    ],
    "quiz": [
        {
            "question": "ACoS stands for and is calculated as:",
            "options": ["Average Cost of Sales: COGS / Revenue × 100", "Advertising Cost of Sales: Ad Spend / Ad Revenue × 100", "Amazon Cost of Service: Total Fees / Revenue × 100", "Average Conversion on Sales: Orders / Clicks × 100"],
            "answer": "Advertising Cost of Sales: Ad Spend / Ad Revenue × 100",
            "explanation": "ACoS = (Advertising Spend / Advertising Revenue) × 100. If you spent ₹10,000 in ads and generated ₹50,000 in ad-attributed sales, ACoS = 20%. Your target should be below your net margin %."
        },
        {
            "question": "What is the recommended first step when launching PPC for a new product on Amazon India?",
            "options": ["Start with Manual Exact match campaign", "Start with Sponsored Brands campaign", "Start with Automatic campaign for 2 weeks to discover converting search terms", "Start with Sponsored Display campaign"],
            "answer": "Start with Automatic campaign for 2 weeks to discover converting search terms",
            "explanation": "The Auto-to-Manual flow starts with an Automatic campaign to let Amazon discover which search terms convert. After 2 weeks, download the Search Term Report, identify converting keywords, and create Manual campaigns targeting those exact terms."
        }
    ]
}

]
