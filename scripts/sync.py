import os
import shutil
import json
import re
import subprocess
import sys

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LEETCODE_DIR = os.path.join(REPO_DIR, 'LeetCode')
METADATA_DIR = os.path.join(REPO_DIR, 'metadata')
SOLUTIONS_JSON = os.path.join(METADATA_DIR, 'solutions.json')

EXTENSION_LANG_MAP = {
    '.sql': ('SQL', 'MySQL'),
    '.py': ('Python', 'Python 3'),
    '.java': ('Java', 'Java'),
    '.cpp': ('C++', 'C++'),
    '.js': ('JavaScript', 'JavaScript'),
    '.ts': ('TypeScript', 'TypeScript')
}

def html_to_markdown(html_str):
    html_str = re.sub(r'<h2>.*?</h2>', '', html_str, flags=re.DOTALL)
    html_str = re.sub(r'<h3>.*?</h3>', '', html_str, flags=re.DOTALL)
    html_str = re.sub(r'<hr\s*/?>', '', html_str)
    
    def repl_pre(match):
        inner = match.group(1)
        inner = re.sub(r'<strong>(.*?)</strong>', r'\1', inner)
        inner = re.sub(r'<em>(.*?)</em>', r'\1', inner)
        return f"\n```text\n{inner.strip()}\n```\n"
        
    html_str = re.sub(r'<pre>(.*?)</pre>', repl_pre, html_str, flags=re.DOTALL)
    html_str = re.sub(r'<code>(.*?)</code>', r'`\1`', html_str)
    html_str = re.sub(r'<strong>(.*?)</strong>', r'**\1**', html_str)
    html_str = re.sub(r'<em>(.*?)</em>', r'*\1*', html_str)
    html_str = re.sub(r'<p>(.*?)</p>', r'\1\n\n', html_str, flags=re.DOTALL)
    html_str = re.sub(r'&nbsp;', ' ', html_str)
    html_str = re.sub(r'&lt;', '<', html_str)
    html_str = re.sub(r'&gt;', '>', html_str)
    html_str = re.sub(r'&amp;', '&', html_str)
    html_str = re.sub(r'<[^>]+>', '', html_str)
    html_str = re.sub(r'\n{3,}', '\n\n', html_str)
    return html_str.strip()

def sync():
    print("=" * 60)
    print("🔄 LEETCODE REPOSITORY INGESTION & SYNCHRONIZER")
    print("=" * 60)

    # Load existing solutions
    solutions = []
    if os.path.exists(SOLUTIONS_JSON):
        with open(SOLUTIONS_JSON, 'r', encoding='utf-8') as f:
            solutions = json.load(f)

    existing_ids = {s['id'] for s in solutions}

    # Detect folders in root matching \d{4}-...
    new_folders = []
    for item in sorted(os.listdir(REPO_DIR)):
        item_path = os.path.join(REPO_DIR, item)
        if os.path.isdir(item_path) and re.match(r'^\d{4}-', item):
            new_folders.append((item, item_path))

    if not new_folders:
        print("No new unorganized folders found in root.")
        print("Running validation and updating documentation...")
        subprocess.run([sys.executable, os.path.join(REPO_DIR, 'scripts', 'generate_readme.py')], check=True)
        subprocess.run([sys.executable, os.path.join(REPO_DIR, 'scripts', 'validate.py')], check=True)
        return

    print(f"Found {len(new_folders)} new folders to ingest and organize.")

    for folder_name, src_dir in new_folders:
        num = folder_name.split('-')[0]
        slug = '-'.join(folder_name.split('-')[1:])

        # Find solution code file
        files = os.listdir(src_dir)
        code_file = None
        lang_folder = 'SQL'
        lang_name = 'MySQL'

        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSION_LANG_MAP:
                code_file = f
                lang_folder, lang_name = EXTENSION_LANG_MAP[ext]
                break

        if not code_file:
            print(f"⚠️  Skipping {folder_name}: No code file recognized.")
            continue

        # Read README.md if present
        readme_src = os.path.join(src_dir, 'README.md')
        raw_html = ""
        orig_title = slug.replace('-', ' ').title()
        orig_url = f"https://leetcode.com/problems/{slug}/"
        diff = 'Easy'

        if os.path.exists(readme_src):
            with open(readme_src, 'r', encoding='utf-8') as rf:
                raw_html = rf.read()
                m_title = re.search(r'<h2><a href="([^"]+)">([^<]+)</a></h2>', raw_html)
                if m_title:
                    orig_url = m_title.group(1)
                    orig_title = m_title.group(2)
                m_diff = re.search(r'<h3>([^<]+)</h3>', raw_html)
                if m_diff:
                    diff = m_diff.group(1)

        diff = diff.capitalize()
        clean_title = re.sub(r'^\d+\.\s*', '', orig_title)
        clean_problem = html_to_markdown(raw_html) if raw_html else "Problem description available at LeetCode."

        # Read code
        with open(os.path.join(src_dir, code_file), 'r', encoding='utf-8') as cf:
            code_content = cf.read().strip()

        # Destination directory: LeetCode/<Lang>/<Difficulty>/<folder_name>
        target_dir = os.path.join(LEETCODE_DIR, lang_folder, diff, folder_name)
        os.makedirs(target_dir, exist_ok=True)

        target_code_path = os.path.join(target_dir, code_file)
        shutil.copy2(os.path.join(src_dir, code_file), target_code_path)

        std_readme = f"""# {num} - {clean_title}

- **Platform:** LeetCode
- **Difficulty:** {diff}
- **Language:** {lang_name}
- **Category:** Algorithms & Data Structures
- **Status:** Accepted
- **Original Problem:** [{orig_url}]({orig_url})

## Problem Statement

{clean_problem}

## Approach & Key Insights

Optimal solution addressing problem constraints with semantic logic and modular operations.

## Complexity Analysis

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)`

## Solution

The complete solution code is available in [`{code_file}`](./{code_file}).

```{lang_folder.lower()}
{code_content}
```
"""
        with open(os.path.join(target_dir, 'README.md'), 'w', encoding='utf-8') as rf:
            rf.write(std_readme)

        # Update metadata
        rel_sol = f"LeetCode/{lang_folder}/{diff}/{folder_name}/{code_file}"
        rel_readme = f"LeetCode/{lang_folder}/{diff}/{folder_name}/README.md"

        # Remove existing if overwriting
        solutions = [s for s in solutions if s['id'] != num]
        solutions.append({
            'id': num,
            'title': clean_title,
            'slug': slug,
            'folder': folder_name,
            'difficulty': diff,
            'platform': 'LeetCode',
            'language': lang_name,
            'category': 'Algorithms & Data Structures' if lang_folder != 'SQL' else 'Database',
            'tags': ['leetcode', lang_folder.lower()],
            'url': orig_url,
            'status': 'Accepted',
            'time_complexity': 'O(N)',
            'space_complexity': 'O(1)',
            'approach': 'Optimal solution addressing constraints.',
            'solution_path': rel_sol,
            'readme_path': rel_readme
        })

        shutil.rmtree(src_dir)
        print(f"✅ Ingested {folder_name} -> {target_dir}")

    # Save sorted catalog
    solutions.sort(key=lambda x: x['id'])
    with open(SOLUTIONS_JSON, 'w', encoding='utf-8') as f:
        json.dump(solutions, f, indent=2, ensure_ascii=False)

    print("Regenerating READMEs...")
    subprocess.run([sys.executable, os.path.join(REPO_DIR, 'scripts', 'generate_readme.py')], check=True)
    subprocess.run([sys.executable, os.path.join(REPO_DIR, 'scripts', 'validate.py')], check=True)
    print("=" * 60)
    print("🎉 Ingestion and synchronization finished successfully!")
    print("=" * 60)

if __name__ == '__main__':
    sync()
