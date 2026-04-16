import os
import base64

BASE = os.path.dirname(os.path.abspath(__file__))

def read_file(filepath):
    if not os.path.exists(filepath): return ""
    with open(filepath, 'r', encoding='utf-8') as f: return f.read()

def get_logo_b64():
    # Priority order: official K: drive > cached b64 > Desktop fallback
    official_jpg = r'K:\Official\4. SME-Minds.com\Marketing\Logo\Final Logos\SMEMinds Logo.jpeg'
    logo_path    = os.path.join(BASE, 'src', 'logo_b64.txt')
    desktop_jpg  = r'C:\Users\kunda\OneDrive\Desktop\SMEMinds Logo.jpeg'

    for src in [official_jpg, desktop_jpg]:
        if os.path.exists(src):
            with open(src, 'rb') as f:
                data = base64.b64encode(f.read()).decode('utf-8')
            # Cache to logo_b64.txt for offline builds
            with open(logo_path, 'w') as f:
                f.write(data)
            print(f"  Logo loaded from: {src}")
            return f"data:image/jpeg;base64,{data}"

    if os.path.exists(logo_path):
        with open(logo_path, 'r') as f:
            data = f.read().strip()
        print("  Logo loaded from cache (logo_b64.txt)")
        return f"data:image/jpeg;base64,{data}"

    return ""  # fallback: no logo

def generate_modules():
    try:
        from content_1 import pillar1_modules
        from content_2 import pillar2_modules
        from content_3 import pillar3_modules
        from content_4 import pillar4_modules
        from content_5 import pillar5_modules
        from content_6 import pillar6_modules
        from content_7 import pillar7_modules
        from content_8 import pillar8_modules
    except Exception as e:
        print(f"Error importing content: {e}")
        return f"<div>Error loading content: {e}</div>"

    all_modules = (pillar1_modules + pillar2_modules + pillar3_modules +
                   pillar4_modules + pillar5_modules + pillar6_modules +
                   pillar7_modules + pillar8_modules)
    html = ""

    for m in all_modules:
        # Difficulty badge class
        diff_lower = m.get('difficulty','').lower()
        diff_class = 'badge-beginner' if diff_lower=='beginner' else \
                     'badge-intermediate' if diff_lower=='intermediate' else \
                     'badge-advanced' if diff_lower=='advanced' else 'badge-expert'

        # Tools section
        tools_html = m.get('tools','')

        # Videos section — YouTube card links (no embed = no Error 153)
        # Amazon Seller University videos have embedding disabled by channel owner.
        video_html = ""
        videos = m.get('videos', [])
        if videos:
            cards = ""
            for v in videos:
                vid_id  = v["id"]
                vid_title = v["title"]
                cards += (
                    "<a class='yt-card' href='https://www.youtube.com/watch?v=" + vid_id + "' target='_blank' rel='noopener'>"
                    "<div class='yt-card-thumb'>"
                    "<img src='https://img.youtube.com/vi/" + vid_id + "/mqdefault.jpg' "
                    "alt='" + vid_title + "' loading='lazy' "
                    "onerror=\"this.parentElement.style.background='#1e3a5f'\">"
                    "<div class='yt-card-play'>"
                    "<svg viewBox='0 0 68 48' xmlns='http://www.w3.org/2000/svg' width='44' height='31'>"
                    "<path d='M66.5 7.7c-.8-2.9-3-5.2-5.9-6C55.8 0 34 0 34 0S12.2 0 7.4 1.7c-2.9.8-5.1 3.1-5.9 6C0 12.5 0 24 0 24s0 11.5 1.5 16.3c.8 2.9 3 5.2 5.9 6C12.2 48 34 48 34 48s21.8 0 26.6-1.7c2.9-.8 5.1-3.1 5.9-6C68 35.5 68 24 68 24s0-11.5-1.5-16.3z' fill='#ff0000' fill-opacity='0.9'/>"
                    "<path d='M45 24 27 14v20' fill='#fff'/>"
                    "</svg>"
                    "</div>"
                    "</div>"
                    "<div class='yt-card-info'>"
                    "<span class='yt-card-label'>Amazon Seller University</span>"
                    "<p class='yt-card-title'>" + vid_title + "</p>"
                    "<span class='yt-card-cta'>Watch on YouTube &nbsp;↗</span>"
                    "</div>"
                    "</a>"
                )
            video_html = (
                "<div class='video-container'>"
                "<h4>Related Videos</h4>"
                "<div class='yt-cards'>" + cards + "</div>"
                "</div>"
            )

        # Checklist
        checklist_html = ""
        checklist = m.get('checklist', [])
        mid = m['id']
        if checklist:
            items = ""
            for c in checklist:
                items += "<li><label><input type='checkbox' class='chk_" + mid + "' onchange='updateChecklist(\"" + mid + "\")'> " + c + "</label></li>"
            checklist_html = "<div class='checklist-container'><h4>Module Checklist</h4><ul>" + items + "</ul></div>"

        # Quiz
        quiz_html = ""
        quiz = m.get('quiz', [])
        if quiz:
            q_items = ""
            for i, q in enumerate(quiz):
                opts = ""
                for opt in q['options']:
                    opts += "<label><input type='radio' name='q_" + mid + "_" + str(i) + "' value='" + opt + "'> " + opt + "</label>"
                q_items += "<div class='quiz-q' data-ans='" + q["answer"] + "'><p><strong>Q" + str(i+1) + ":</strong> " + q["question"] + "</p>" + opts + "<div class='q-exp' style='display:none'>" + q.get("explanation","") + "</div></div>"
            quiz_html = "<div class='quiz-container' id='quiz_" + mid + "'><h4>Module Quiz</h4>" + q_items + "<button class='btn btn-primary' onclick='submitQuiz(\"" + mid + "\")'>Submit Quiz</button><div class='quiz-result' id='quiz_res_" + mid + "'></div></div>"

        # Feedback
        feedback_html = f"""
        <div class='feedback-container'>
            <h4>📊 Rate This Module</h4>
            <p style='color:var(--text-muted);font-size:13px;margin-bottom:4px'>How useful was this module?</p>
            <div class='star-rating' id='stars_{m["id"]}'>
                <span onclick='rateModule("{m["id"]}",1)'>★</span>
                <span onclick='rateModule("{m["id"]}",2)'>★</span>
                <span onclick='rateModule("{m["id"]}",3)'>★</span>
                <span onclick='rateModule("{m["id"]}",4)'>★</span>
                <span onclick='rateModule("{m["id"]}",5)'>★</span>
            </div>
            <textarea id='fb_help_{m["id"]}' placeholder='What did you find most helpful?' style='user-select:text'></textarea>
            <textarea id='fb_imp_{m["id"]}'  placeholder='What could be improved?' style='user-select:text'></textarea>
            <select id='fb_role_{m["id"]}'>
                <option value=''>Select your role...</option>
                <option value='New Seller'>New Seller</option>
                <option value='Experienced Seller'>Experienced Seller</option>
                <option value='Account Manager'>Account Manager</option>
                <option value='Consultant'>Consultant</option>
                <option value='Other'>Other</option>
            </select>
            <br><br>
            <button class='btn btn-accent' onclick='submitFeedback("{m["id"]}")'>Submit Feedback</button>
        </div>"""

        # Process flow
        process_flow = m.get('process_flow','')

        # Build module HTML
        module_html = f"""
        <div class='module-section' id='module_{m["id"]}'>
            <div class='module-header'>
                <div class='module-header-top'>
                    <div>
                        <h2>{m["number"]} — {m["title"]}</h2>
                        <div class='module-meta'>
                            <span class='badge badge-diff {diff_class}'>{m.get("difficulty","")}</span>
                            <span class='badge badge-time'>⏱ {m.get("time","")}</span>
                        </div>
                    </div>
                    <div class='module-logo-block'>
                        <img src='{{ LOGO_B64 }}' alt='SMEMinds' class='module-logo-img' onerror="this.style.display='none'">
                    </div>
                </div>
            </div>
            <div class='module-body'>
                <div class='overview-content'>{m.get("overview","")}</div>
                <div class='module-content'>{m.get("content","")}</div>
                {process_flow}
                {tools_html}
                {video_html}
                {checklist_html}
                {quiz_html}
                {feedback_html}
            </div>
        </div>"""
        html += module_html

    return html

def build():
    print("Building SMEMinds Playbook...")

    template  = read_file(os.path.join(BASE, 'src', 'template.html'))
    css       = read_file(os.path.join(BASE, 'src', 'style.css'))
    js        = read_file(os.path.join(BASE, 'src', 'app.js'))
    tools_js  = read_file(os.path.join(BASE, 'src', 'tools.js'))
    tools_html= read_file(os.path.join(BASE, 'src', 'tools.html'))

    logo_b64  = get_logo_b64()
    modules_html = generate_modules()

    final_html = template
    final_html = final_html.replace('{{ CSS }}', css)
    final_html = final_html.replace('{{ JS }}', js + "\n\n" + tools_js)
    final_html = final_html.replace('{{ TOOLS }}', tools_html)
    final_html = final_html.replace('{{ MODULES }}', modules_html)
    final_html = final_html.replace('{{ LOGO_B64 }}', logo_b64)

    out_path = os.path.join(BASE, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"[OK] Successfully built: index.html ({size_kb:.0f} KB)")

if __name__ == "__main__":
    build()
