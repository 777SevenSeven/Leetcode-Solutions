import os
import json
import html
import re

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SOLUTIONS_JSON = os.path.join(REPO_DIR, 'metadata', 'solutions.json')
DOCS_DIR = os.path.join(REPO_DIR, 'docs')
SOLUTIONS_DIR = os.path.join(DOCS_DIR, 'solutions')

BASE_URL = "https://777sevenseven.github.io/Leetcode-Solutions"
GITHUB_REPO_URL = "https://github.com/777SevenSeven/Leetcode-Solutions"

DIFF_COLORS = {
    'Easy': '#00b8a3',
    'Medium': '#ffc01e',
    'Hard': '#ff375f'
}

def build_site():
    print("=" * 60)
    print("🌐 DISCOVERY ENGINEERING: BUILDING STATIC WEB PORTAL")
    print("=" * 60)

    if not os.path.exists(SOLUTIONS_JSON):
        print(f"Error: {SOLUTIONS_JSON} not found.")
        return

    with open(SOLUTIONS_JSON, 'r', encoding='utf-8') as f:
        solutions = json.load(f)

    os.makedirs(SOLUTIONS_DIR, exist_ok=True)

    # 1. Generate Individual Problem Pages
    sitemap_urls = [
        f"{BASE_URL}/"
    ]

    for s in solutions:
        pid = s['id']
        title = s['title']
        slug = s['slug']
        diff = s['difficulty']
        cat = s['category']
        time_c = s['time_complexity']
        space_c = s['space_complexity']
        approach = s['approach']
        orig_url = s['url']
        diff_color = DIFF_COLORS.get(diff, '#00b8a3')
        
        # Read solution code
        sol_file_rel = s['solution_path']
        sol_full_path = os.path.join(REPO_DIR, sol_file_rel)
        sql_code = ""
        if os.path.exists(sol_full_path):
            with open(sol_full_path, 'r', encoding='utf-8') as sf:
                sql_code = sf.read().strip()

        # Read problem statement from README.md
        readme_full_path = os.path.join(REPO_DIR, s['readme_path'])
        problem_statement_html = ""
        if os.path.exists(readme_full_path):
            with open(readme_full_path, 'r', encoding='utf-8') as rf:
                rm_text = rf.read()
                m = re.search(r'## Problem Statement\s*(.*?)\s*## Approach', rm_text, flags=re.DOTALL)
                if m:
                    raw_statement = m.group(1).strip()
                    # convert markdown blocks to html
                    raw_statement = html.escape(raw_statement)
                    # convert ```text to <pre>
                    raw_statement = re.sub(r'```text\n(.*?)\n```', r'<pre><code>\1</code></pre>', raw_statement, flags=re.DOTALL)
                    raw_statement = re.sub(r'`([^`]+)`', r'<code>\1</code>', raw_statement)
                    problem_statement_html = raw_statement.replace('\n', '<br>')
                    problem_statement_html = re.sub(r'(<br>\s*){2,}', '<br><br>', problem_statement_html)

        page_filename = f"{pid}-{slug}.html"
        page_url = f"{BASE_URL}/solutions/{page_filename}"
        sitemap_urls.append(page_url)

        github_raw_link = f"{GITHUB_REPO_URL}/blob/main/{sol_file_rel}"

        # JSON-LD Schema.org Structured Data
        schema_json = json.dumps({
            "@context": "https://schema.org",
            "@type": "TechArticle",
            "headline": f"LeetCode #{int(pid)} - {title} ({diff}) Solution & Explanation",
            "description": f"Optimized SQL solution and technical explanation for LeetCode problem {pid}: {title}. Includes asymptotic complexity analysis and clean query design.",
            "articleSection": cat,
            "keywords": f"LeetCode, SQL, MySQL, {cat}, {title}, Database, Algorithm",
            "author": {
                "@type": "Person",
                "name": "777SevenSeven"
            },
            "url": page_url
        }, indent=2, ensure_ascii=False)

        problem_page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LeetCode #{pid} - {html.escape(title)} | SQL Solution &amp; Analysis</title>
  <meta name="description" content="Detailed SQL query explanation and asymptotic complexity analysis for LeetCode #{pid}: {html.escape(title)} ({diff}).">
  <link rel="canonical" href="{page_url}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="LeetCode #{pid} - {html.escape(title)} ({diff})">
  <meta property="og:description" content="Technical approach, time and space complexity, and verified SQL solution.">
  <meta property="og:url" content="{page_url}">
  <meta property="og:type" content="article">
  
  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
{schema_json}
  </script>

  <style>
    :root {{
      --bg: #0f172a;
      --card-bg: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --code-bg: #090d16;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 2rem 1rem;
    }}
    .container {{ max-width: 860px; margin: 0 auto; }}
    .nav-back {{ margin-bottom: 1.5rem; }}
    .nav-back a {{ color: var(--primary); text-decoration: none; font-size: 0.95rem; }}
    .nav-back a:hover {{ text-decoration: underline; }}
    .header {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 2rem;
    }}
    .header h1 {{ font-size: 1.85rem; margin-bottom: 0.75rem; }}
    .tags {{ display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center; }}
    .badge {{
      display: inline-block;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
    }}
    .badge-diff {{ background: rgba(255,255,255,0.08); color: {diff_color}; border: 1px solid {diff_color}; }}
    .badge-cat {{ background: rgba(56, 189, 248, 0.1); color: var(--primary); border: 1px solid rgba(56, 189, 248, 0.3); }}
    .section {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
    }}
    .section h2 {{ font-size: 1.25rem; margin-bottom: 1rem; color: var(--primary); border-bottom: 1px solid var(--border); padding-bottom: 0.5rem; }}
    .metrics-table {{ width: 100%; border-collapse: collapse; margin-top: 0.5rem; }}
    .metrics-table th, .metrics-table td {{ text-align: left; padding: 0.6rem 0.8rem; border: 1px solid var(--border); font-size: 0.95rem; }}
    .metrics-table th {{ background: rgba(255,255,255,0.03); }}
    pre {{
      background: var(--code-bg);
      border: 1px solid var(--border);
      padding: 1.25rem;
      border-radius: 8px;
      overflow-x: auto;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.9rem;
      color: #e2e8f0;
    }}
    code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}
    .btn {{
      display: inline-block;
      padding: 0.5rem 1rem;
      background: #2563eb;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 500;
      margin-right: 0.75rem;
    }}
    .btn:hover {{ background: #1d4ed8; }}
    .btn-secondary {{ background: #334155; }}
    .btn-secondary:hover {{ background: #475569; }}
    .footer {{ text-align: center; margin-top: 3rem; color: var(--text-muted); font-size: 0.85rem; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="nav-back">
      <a href="../index.html">&larr; Back to Problem Catalog</a>
    </div>

    <div class="header">
      <h1>#{pid} - {html.escape(title)}</h1>
      <div class="tags">
        <span class="badge badge-diff">{diff}</span>
        <span class="badge badge-cat">{cat}</span>
        <span class="badge" style="background: rgba(34, 197, 94, 0.1); color: #22c55e; border: 1px solid #22c55e;">Status: Accepted</span>
      </div>
      <div style="margin-top: 1.25rem;">
        <a href="{orig_url}" target="_blank" rel="noopener noreferrer" class="btn">View on LeetCode &nearr;</a>
        <a href="{github_raw_link}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary">View Code on GitHub &nearr;</a>
      </div>
    </div>

    <div class="section">
      <h2>Problem Statement</h2>
      <div style="font-size: 0.95rem; color: #cbd5e1;">
        {problem_statement_html if problem_statement_html else f"<p>Visit the official problem page on <a href='{orig_url}' style='color: var(--primary);'>LeetCode</a>.</p>"}
      </div>
    </div>

    <div class="section">
      <h2>Approach &amp; Key Insights</h2>
      <p style="font-size: 0.95rem; color: #cbd5e1;">{html.escape(approach)}</p>
    </div>

    <div class="section">
      <h2>Complexity Analysis</h2>
      <table class="metrics-table">
        <thead>
          <tr>
            <th>Metric</th>
            <th>Complexity</th>
            <th>Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Time Complexity</strong></td>
            <td><code>{time_c}</code></td>
            <td>Execution runtime</td>
          </tr>
          <tr>
            <td><strong>Space Complexity</strong></td>
            <td><code>{space_c}</code></td>
            <td>Memory / Temporary buffer</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="section">
      <h2>Verified SQL Solution</h2>
      <pre><code>{html.escape(sql_code)}</code></pre>
    </div>

    <div class="footer">
      <p>LeetCode Solutions &amp; Competitive Programming Hub &bull; Maintained by 777SevenSeven</p>
    </div>
  </div>
</body>
</html>
"""
        with open(os.path.join(SOLUTIONS_DIR, page_filename), 'w', encoding='utf-8') as pf:
            pf.write(problem_page_html)

    # 2. Generate Home Index Page (Catalog with Live Filter & Search)
    solutions_json_for_js = json.dumps([{
        'id': s['id'],
        'title': s['title'],
        'slug': s['slug'],
        'difficulty': s['difficulty'],
        'category': s['category'],
        'time': s['time_complexity'],
        'space': s['space_complexity'],
        'page': f"solutions/{s['id']}-{s['slug']}.html",
        'code': s['solution_path'],
        'url': s['url']
    } for s in solutions], ensure_ascii=False)

    categories_list = sorted(list({s['category'] for s in solutions}))

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LeetCode Solutions &amp; Competitive Programming Hub | Discovery Portal</title>
  <meta name="description" content="Explore verified, thoroughly documented SQL and competitive programming solutions. Search by pattern, difficulty, or problem name.">
  <link rel="canonical" href="{BASE_URL}/">

  <!-- Open Graph -->
  <meta property="og:title" content="LeetCode Solutions &amp; Competitive Programming Hub">
  <meta property="og:description" content="Searchable catalog of verified solutions with asymptotic complexity analysis.">
  <meta property="og:url" content="{BASE_URL}/">
  <meta property="og:type" content="website">

  <style>
    :root {{
      --bg: #0f172a;
      --card-bg: #1e293b;
      --border: #334155;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      padding: 2.5rem 1rem;
    }}
    .container {{ max-width: 1040px; margin: 0 auto; }}
    .hero {{ text-align: center; margin-bottom: 2.5rem; }}
    .hero h1 {{ font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem; }}
    .hero p {{ color: var(--text-muted); font-size: 1.1rem; max-width: 600px; margin: 0 auto 1.5rem; }}
    .stats-row {{ display: flex; justify-content: center; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap; }}
    .stat-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      padding: 0.8rem 1.5rem;
      border-radius: 10px;
      text-align: center;
    }}
    .stat-num {{ font-size: 1.5rem; font-weight: 700; color: var(--primary); }}
    .stat-label {{ font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; }}
    
    .search-box {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
      margin-bottom: 2rem;
    }}
    .input-group {{
      display: flex;
      gap: 1rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }}
    input[type="text"] {{
      flex: 1;
      min-width: 250px;
      padding: 0.75rem 1rem;
      background: #090d16;
      border: 1px solid var(--border);
      border-radius: 8px;
      color: white;
      font-size: 0.95rem;
    }}
    input[type="text"]:focus {{ outline: none; border-color: var(--primary); }}
    
    .filters {{ display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center; }}
    .filter-btn {{
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border);
      color: var(--text-muted);
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      font-size: 0.85rem;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .filter-btn:hover, .filter-btn.active {{
      background: var(--primary);
      color: #0f172a;
      font-weight: 600;
      border-color: var(--primary);
    }}

    .catalog-table-wrap {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow-x: auto;
    }}
    table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; }}
    th, td {{ padding: 0.85rem 1rem; border-bottom: 1px solid var(--border); }}
    th {{ background: rgba(0,0,0,0.2); font-weight: 600; color: var(--text-muted); }}
    tr:hover td {{ background: rgba(255,255,255,0.02); }}
    .pill {{
      display: inline-block;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      font-size: 0.75rem;
      font-weight: 600;
    }}
    .pill-easy {{ background: rgba(0,184,163,0.15); color: #00b8a3; }}
    .pill-medium {{ background: rgba(255,192,30,0.15); color: #ffc01e; }}
    .pill-hard {{ background: rgba(255,55,95,0.15); color: #ff375f; }}
    a.prob-link {{ color: var(--text); text-decoration: none; font-weight: 500; }}
    a.prob-link:hover {{ color: var(--primary); text-decoration: underline; }}
    .action-link {{ color: var(--primary); text-decoration: none; font-size: 0.85rem; font-weight: 600; }}
    .action-link:hover {{ text-decoration: underline; }}
    .footer {{ text-align: center; margin-top: 3rem; color: var(--text-muted); font-size: 0.85rem; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="hero">
      <h1>⚡ LeetCode Solutions &amp; Engineering Hub</h1>
      <p>Systematically documented, tested, and indexed programming solutions featuring asymptotic analysis and query design patterns.</p>
      
      <div class="stats-row">
        <div class="stat-card">
          <div class="stat-num">{len(solutions)}</div>
          <div class="stat-label">Total Solved</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #00b8a3;">32</div>
          <div class="stat-label">Easy</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #ffc01e;">16</div>
          <div class="stat-label">Medium</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #ff375f;">1</div>
          <div class="stat-label">Hard</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" style="color: #22c55e;">100%</div>
          <div class="stat-label">SQL 50 Complete</div>
        </div>
      </div>
    </div>

    <div class="search-box">
      <div class="input-group">
        <input type="text" id="searchInput" placeholder="Search by problem name, #ID, or pattern (e.g. Join, Window, CTE)...">
      </div>
      <div class="filters" id="diffFilters">
        <span style="font-size: 0.85rem; color: var(--text-muted); margin-right: 0.25rem;">Difficulty:</span>
        <button class="filter-btn active" data-diff="ALL">All</button>
        <button class="filter-btn" data-diff="Easy">Easy</button>
        <button class="filter-btn" data-diff="Medium">Medium</button>
        <button class="filter-btn" data-diff="Hard">Hard</button>
      </div>
    </div>

    <div class="catalog-table-wrap">
      <table>
        <thead>
          <tr>
            <th style="width: 70px;">ID</th>
            <th>Problem Title</th>
            <th style="width: 100px;">Difficulty</th>
            <th>Topic / Category</th>
            <th style="width: 110px;">Time</th>
            <th style="width: 100px;">Action</th>
          </tr>
        </thead>
        <tbody id="catalogBody">
          <!-- Rendered via JavaScript -->
        </tbody>
      </table>
    </div>

    <div class="footer">
      <p>LeetCode Solutions &bull; Source code and documentation on <a href="{GITHUB_REPO_URL}" style="color: var(--primary);">GitHub</a> &bull; Maintained by 777SevenSeven</p>
    </div>
  </div>

  <script>
    const data = {solutions_json_for_js};
    let currentDiff = 'ALL';

    const searchInput = document.getElementById('searchInput');
    const catalogBody = document.getElementById('catalogBody');
    const diffButtons = document.querySelectorAll('#diffFilters .filter-btn');

    function render() {{
      const query = searchInput.value.toLowerCase().trim();
      const filtered = data.filter(item => {{
        const matchesDiff = currentDiff === 'ALL' || item.difficulty === currentDiff;
        const matchesQuery = !query || 
          item.id.includes(query) || 
          item.title.toLowerCase().includes(query) || 
          item.category.toLowerCase().includes(query) ||
          item.slug.toLowerCase().includes(query);
        return matchesDiff && matchesQuery;
      }});

      if (filtered.length === 0) {{
        catalogBody.innerHTML = '<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 2rem;">No matching problems found.</td></tr>';
        return;
      }}

      catalogBody.innerHTML = filtered.map(item => {{
        const pillClass = 'pill-' + item.difficulty.toLowerCase();
        return `
          <tr>
            <td><code>#${{item.id}}</code></td>
            <td><a class="prob-link" href="${{item.page}}">${{item.title}}</a></td>
            <td><span class="pill ${{pillClass}}">${{item.difficulty}}</span></td>
            <td>${{item.category}}</td>
            <td><code>${{item.time}}</code></td>
            <td><a class="action-link" href="${{item.page}}">Solution &rarr;</a></td>
          </tr>
        `;
      }}).join('');
    }}

    searchInput.addEventListener('input', render);

    diffButtons.forEach(btn => {{
      btn.addEventListener('click', () => {{
        diffButtons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentDiff = btn.getAttribute('data-diff');
        render();
      }});
    }});

    render();
  </script>
</body>
</html>
"""
    with open(os.path.join(DOCS_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)

    # 3. Generate sitemap.xml
    sitemap_items = []
    for u in sitemap_urls:
        sitemap_items.append(f"""  <url>
    <loc>{u}</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_items)}
</urlset>
"""
    with open(os.path.join(DOCS_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

    # 4. Generate robots.txt
    robots_txt = f"""# Robots.txt for LeetCode Solutions Portal
User-agent: *
Allow: /

# Explicit rules for AI Search engines
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(DOCS_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots_txt)

    print(f"Generated {len(solutions)} static solution pages in {SOLUTIONS_DIR}.")
    print(f"Generated index.html, sitemap.xml, and robots.txt in {DOCS_DIR}.")

if __name__ == '__main__':
    build_site()
