import os
import shutil
import json
import re

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LEETCODE_DIR = os.path.join(REPO_DIR, 'LeetCode')
SQL_DIR = os.path.join(LEETCODE_DIR, 'SQL')
METADATA_DIR = os.path.join(REPO_DIR, 'metadata')
SOLUTIONS_JSON = os.path.join(METADATA_DIR, 'solutions.json')

# SQL 50 Categorization and metadata mappings
PROBLEM_DATA = {
    '1757': {
        'category': 'Select',
        'tags': ['select', 'conditional-filtering', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Filter records where both `low_fats` and `recyclable` are flagged as "Y" using a direct WHERE clause condition.'
    },
    '0584': {
        'category': 'Select',
        'tags': ['select', 'null-handling', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Query customer names handling three-valued logic (NULL) by explicitly checking `referee_id != 2 OR referee_id IS NULL`.'
    },
    '0595': {
        'category': 'Select',
        'tags': ['select', 'filtering', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Filter countries satisfying either area threshold (>= 3,000,000 sq km) or population threshold (>= 25,000,000).'
    },
    '1148': {
        'category': 'Select',
        'tags': ['select', 'distinct', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Filter records where `author_id = viewer_id`, eliminating duplicate authors with `DISTINCT` and sorting ascending by author ID.'
    },
    '1683': {
        'category': 'Select',
        'tags': ['select', 'string-length', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Use MySQL `CHAR_LENGTH(content) > 15` rather than `LENGTH()` to correctly measure multi-byte character counts.'
    },
    '1378': {
        'category': 'Basic Joins',
        'tags': ['joins', 'left-join', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Perform a `LEFT JOIN` between `Employees` and `EmployeeUNI` on `id` to retain all employee records even when no unique identifier exists (yielding NULL).'
    },
    '1068': {
        'category': 'Basic Joins',
        'tags': ['joins', 'inner-join', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Join `Sales` and `Product` tables on `product_id` to project each sale alongside its human-readable product name, sale year, and unit price.'
    },
    '1581': {
        'category': 'Basic Joins',
        'tags': ['joins', 'left-join', 'null-filtering', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Identify visits without transactions via a `LEFT JOIN` on `visit_id` where `Transactions.transaction_id IS NULL`, grouping by `customer_id` with `COUNT(*)`.'
    },
    '0197': {
        'category': 'Basic Joins',
        'tags': ['joins', 'self-join', 'date-functions', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Self-join the `Weather` table where `DATEDIFF(w1.recordDate, w2.recordDate) = 1` and test `w1.temperature > w2.temperature` to identify rising temperature days.'
    },
    '1661': {
        'category': 'Basic Joins',
        'tags': ['joins', 'self-join', 'aggregation', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Self-join the table matching identical `machine_id` and `process_id` between start and end events, computing average processing time with `ROUND(AVG(a2.timestamp - a1.timestamp), 3)`.'
    },
    '0577': {
        'category': 'Basic Joins',
        'tags': ['joins', 'left-join', 'null-handling', 'sql-50'],
        'time': 'O(N + M)',
        'space': 'O(N + M)',
        'approach': 'Perform a `LEFT JOIN` on `empId` and check `b.bonus < 1000 OR b.bonus IS NULL` to ensure employees without bonus entries are properly included.'
    },
    '1280': {
        'category': 'Basic Joins',
        'tags': ['joins', 'cross-join', 'left-join', 'group-by', 'sql-50'],
        'time': 'O(S * B + E)',
        'space': 'O(S * B)',
        'approach': 'Generate all student-subject combinations via `CROSS JOIN`, then `LEFT JOIN` with `Examinations` and count matched records with `COUNT(e.subject_name)`.'
    },
    '0570': {
        'category': 'Basic Joins',
        'tags': ['joins', 'group-by', 'having', 'self-join', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Group direct reports by `managerId` with `HAVING COUNT(*) >= 5`, then join with `Employee` to retrieve the manager names.'
    },
    '1934': {
        'category': 'Basic Joins',
        'tags': ['joins', 'left-join', 'conditional-aggregation', 'sql-50'],
        'time': 'O(N + M)',
        'space': 'O(N)',
        'approach': 'Compute confirmation rate with `LEFT JOIN` on `user_id` and `ROUND(IFNULL(AVG(c.action = "confirmed"), 0), 2)` grouped by `Signups.user_id`.'
    },
    '0620': {
        'category': 'Basic Aggregate Functions',
        'tags': ['filtering', 'modulus', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Select odd-numbered IDs using `id % 2 = 1` with `description != "boring"`, ordering the output by rating in descending order.'
    },
    '1251': {
        'category': 'Basic Aggregate Functions',
        'tags': ['aggregation', 'left-join', 'weighted-average', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Left join prices and unit sales within effective date ranges (`purchase_date BETWEEN start_date AND end_date`), computing weighted average with `IFNULL(ROUND(SUM(price * units) / SUM(units), 2), 0)`.'
    },
    '1075': {
        'category': 'Basic Aggregate Functions',
        'tags': ['aggregation', 'inner-join', 'rounding', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Join `Project` with `Employee` on `employee_id`, group by `project_id`, and calculate average experience rounded to two decimals: `ROUND(AVG(experience_years), 2)`.'
    },
    '1633': {
        'category': 'Basic Aggregate Functions',
        'tags': ['aggregation', 'subquery', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Group by `contest_id` and compute registration percentage against total registered users dynamically fetched from `(SELECT COUNT(*) FROM Users)`.'
    },
    '1211': {
        'category': 'Basic Aggregate Functions',
        'tags': ['aggregation', 'conditional-sum', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Group by `query_name` and compute average quality `ROUND(AVG(rating / position), 2)` and poor query percentage `ROUND(AVG(rating < 3) * 100, 2)`.'
    },
    '1193': {
        'category': 'Basic Aggregate Functions',
        'tags': ['aggregation', 'date-formatting', 'conditional-sum', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Extract year-month via `DATE_FORMAT(trans_date, "%Y-%m")` and aggregate total and approved transactions and amounts per month and country.'
    },
    '1141': {
        'category': 'Basic Aggregate Functions',
        'tags': ['aggregation', 'distinct', 'date-range', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Filter activity within the 30-day window ending on 2019-07-27, grouping by `activity_date` with `COUNT(DISTINCT user_id)`.'
    },
    '0550': {
        'category': 'Basic Aggregate Functions',
        'tags': ['aggregation', 'subquery', 'date-arithmetic', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Determine each player\'s initial login date using a subquery with `MIN(event_date)`, then measure consecutive day logins with `DATEDIFF(event_date, first_login) = 1`.'
    },
    '2356': {
        'category': 'Sorting and Grouping',
        'tags': ['group-by', 'count-distinct', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Group records by `teacher_id` and count distinct subjects taught per teacher using `COUNT(DISTINCT subject_id)`.'
    },
    '1070': {
        'category': 'Sorting and Grouping',
        'tags': ['subqueries', 'group-by', 'min', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Filter sales where `(product_id, year)` matches the first year each product was sold using a tuple `IN` subquery with `GROUP BY product_id`.'
    },
    '0596': {
        'category': 'Sorting and Grouping',
        'tags': ['group-by', 'having', 'count', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Group by `class` and filter for classes with five or more registered students using `HAVING COUNT(student) >= 5`.'
    },
    '1729': {
        'category': 'Sorting and Grouping',
        'tags': ['group-by', 'count', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Group by `user_id`, tally followers with `COUNT(follower_id)`, and sort the results by `user_id ASC`.'
    },
    '0619': {
        'category': 'Sorting and Grouping',
        'tags': ['subquery', 'group-by', 'having', 'max', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Use a subquery grouping by `num` with `HAVING COUNT(*) = 1` to isolate unique numbers, then wrap with `SELECT MAX(num)`.'
    },
    '1045': {
        'category': 'Sorting and Grouping',
        'tags': ['group-by', 'having', 'count-distinct', 'subquery', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Group purchases by `customer_id` and filter with `HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)`.'
    },
    '1731': {
        'category': 'Advanced Select and Joins',
        'tags': ['joins', 'self-join', 'aggregation', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Self-join `Employees` where manager ID equals employee ID, grouping by manager with `COUNT(reports.employee_id)` and `ROUND(AVG(reports.age))`.'
    },
    '1789': {
        'category': 'Advanced Select and Joins',
        'tags': ['subquery', 'union', 'or-filtering', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Retrieve records where `primary_flag = "Y"` or employee belongs to only a single department (`HAVING COUNT(*) = 1`).'
    },
    '0610': {
        'category': 'Advanced Select and Joins',
        'tags': ['conditional-logic', 'case-when', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Evaluate triangle inequality theorem via `CASE WHEN x + y > z AND x + z > y AND y + z > x THEN "Yes" ELSE "No" END`.'
    },
    '0180': {
        'category': 'Advanced Select and Joins',
        'tags': ['joins', 'self-join', 'consecutive-values', 'window-functions', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Join three consecutive rows (`l1.id = l2.id - 1 AND l2.id = l3.id - 1`) verifying `l1.num = l2.num AND l2.num = l3.num` with `DISTINCT`.'
    },
    '1164': {
        'category': 'Advanced Select and Joins',
        'tags': ['subqueries', 'union-all', 'window-functions', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Union products with price updates on/before target date (picking the latest change via subquery) with products updated only after that date (assigned default price 10).'
    },
    '1204': {
        'category': 'Advanced Select and Joins',
        'tags': ['window-functions', 'running-total', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Compute cumulative weight with `SUM(weight) OVER (ORDER BY turn)` in a CTE or subquery, filter `<= 1000`, and take the last person (`ORDER BY turn DESC LIMIT 1`).'
    },
    '1907': {
        'category': 'Advanced Select and Joins',
        'tags': ['union-all', 'case-when', 'aggregation', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Construct fixed category rows ("Low Salary", "Average Salary", "High Salary") via `UNION ALL` to guarantee all categories appear even with zero counts.'
    },
    '1978': {
        'category': 'Subqueries',
        'tags': ['subqueries', 'not-in', 'filtering', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Filter low-salary employees (< $30,000) whose `manager_id` is NOT NULL and `NOT IN (SELECT employee_id FROM Employees)`.'
    },
    '0626': {
        'category': 'Subqueries',
        'tags': ['case-when', 'modulus', 'subquery', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Swap adjacent seat IDs using conditional `CASE WHEN` logic: odd IDs increase by 1 (except the final seat if total count is odd), while even IDs decrease by 1.'
    },
    '1341': {
        'category': 'Subqueries',
        'tags': ['subqueries', 'union-all', 'window-functions', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Combine two independent subqueries via `UNION ALL`: the user with the most movie ratings and the highest average rated movie in February 2020.'
    },
    '1321': {
        'category': 'Subqueries',
        'tags': ['window-functions', 'moving-average', 'rolling-window', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Group daily total amounts, then calculate 7-day rolling sum and moving average using `SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)`.'
    },
    '0602': {
        'category': 'Subqueries',
        'tags': ['subqueries', 'union-all', 'group-by', 'sorting', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Combine `requester_id` and `accepter_id` using `UNION ALL`, group by ID, order by total count descending, and extract the top friend using `LIMIT 1`.'
    },
    '0585': {
        'category': 'Subqueries',
        'tags': ['subqueries', 'tuple-filtering', 'in-clause', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Sum `tiv_2016` where `tiv_2015 IN (SELECT tiv_2015 GROUP BY HAVING COUNT(*) > 1)` and `(lat, lon) IN (SELECT lat, lon GROUP BY HAVING COUNT(*) = 1)`.'
    },
    '0185': {
        'category': 'Subqueries',
        'tags': ['subqueries', 'dense-rank', 'window-functions', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Assign partitioned salary rankings with `DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC)` and filter rankings `<= 3`.'
    },
    '1667': {
        'category': 'Advanced String Functions / Regex / Clause',
        'tags': ['string-functions', 'concat', 'upper', 'lower', 'substring', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Capitalize names using `CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2)))` and sort by `user_id`.'
    },
    '1527': {
        'category': 'Advanced String Functions / Regex / Clause',
        'tags': ['string-matching', 'like', 'pattern-matching', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Search conditions containing type 1 diabetes codes using `conditions LIKE "DIAB1%" OR conditions LIKE "% DIAB1%"`.'
    },
    '0196': {
        'category': 'Advanced String Functions / Regex / Clause',
        'tags': ['delete', 'self-join', 'duplicate-removal', 'sql-50'],
        'time': 'O(N^2)',
        'space': 'O(1)',
        'approach': 'Delete duplicate emails using a self-join `DELETE p1 FROM Person p1, Person p2 WHERE p1.email = p2.email AND p1.id > p2.id`.'
    },
    '0176': {
        'category': 'Advanced String Functions / Regex / Clause',
        'tags': ['subqueries', 'distinct', 'limit-offset', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(1)',
        'approach': 'Query distinct salaries ordered descending with `LIMIT 1 OFFSET 1` wrapped in an outer scalar `SELECT (...) AS SecondHighestSalary` to return NULL if non-existent.'
    },
    '1484': {
        'category': 'Advanced String Functions / Regex / Clause',
        'tags': ['group-by', 'group-concat', 'distinct', 'sql-50'],
        'time': 'O(N log N)',
        'space': 'O(N)',
        'approach': 'Aggregate daily sales with `COUNT(DISTINCT product)` and concatenate unique product names alphabetically using `GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ",")`.'
    },
    '1327': {
        'category': 'Advanced String Functions / Regex / Clause',
        'tags': ['joins', 'date-filtering', 'having', 'aggregation', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(N)',
        'approach': 'Join `Products` and `Orders`, filter `order_date BETWEEN "2020-02-01" AND "2020-02-29"`, group by product, and filter `HAVING SUM(unit) >= 100`.'
    },
    '1517': {
        'category': 'Advanced String Functions / Regex / Clause',
        'tags': ['regex', 'regular-expression', 'pattern-validation', 'sql-50'],
        'time': 'O(N)',
        'space': 'O(1)',
        'approach': 'Validate email syntax via regular expression `mail REGEXP "^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$"`.'
    }
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

def build():
    stats_path = os.path.join(REPO_DIR, 'stats.json')
    stats = {}
    if os.path.exists(stats_path):
        with open(stats_path, 'r', encoding='utf-8') as f:
            stats = json.load(f)

    shas = stats.get('leetcode', {}).get('shas', {})
    
    # Ensure directories exist
    os.makedirs(METADATA_DIR, exist_ok=True)
    for diff in ['Easy', 'Medium', 'Hard']:
        os.makedirs(os.path.join(SQL_DIR, diff), exist_ok=True)
        os.makedirs(os.path.join(LEETCODE_DIR, 'Python', diff), exist_ok=True)
        os.makedirs(os.path.join(LEETCODE_DIR, 'Java', diff), exist_ok=True)
    
    for placeholder_dir in [
        os.path.join(REPO_DIR, 'HackerRank', 'Python'),
        os.path.join(REPO_DIR, 'HackerRank', 'SQL'),
        os.path.join(REPO_DIR, 'Codeforces', 'C++')
    ]:
        os.makedirs(placeholder_dir, exist_ok=True)
        gitkeep = os.path.join(placeholder_dir, '.gitkeep')
        if not os.path.exists(gitkeep):
            with open(gitkeep, 'w', encoding='utf-8') as f:
                f.write('')

    solutions_catalog = []
    
    # Find all problem folders in root or existing LeetCode/SQL
    items_to_process = []
    for item in sorted(os.listdir(REPO_DIR)):
        item_path = os.path.join(REPO_DIR, item)
        if os.path.isdir(item_path) and re.match(r'^\d{4}-', item):
            items_to_process.append((item, item_path))
            
    print(f"Found {len(items_to_process)} raw problem folders at root.")
    
    for folder_name, src_dir in items_to_process:
        num = folder_name.split('-')[0]
        slug = '-'.join(folder_name.split('-')[1:])
        
        # Read existing README.md
        orig_readme = os.path.join(src_dir, 'README.md')
        raw_html = ""
        orig_title = ""
        orig_url = f"https://leetcode.com/problems/{slug}/"
        diff = shas.get(folder_name, {}).get('difficulty', '')
        
        if os.path.exists(orig_readme):
            with open(orig_readme, 'r', encoding='utf-8') as f:
                raw_html = f.read()
                m_title = re.search(r'<h2><a href="([^"]+)">([^<]+)</a></h2>', raw_html)
                if m_title:
                    orig_url = m_title.group(1)
                    orig_title = m_title.group(2)
                m_diff = re.search(r'<h3>([^<]+)</h3>', raw_html)
                if m_diff:
                    diff = m_diff.group(1)
                    
        if not diff:
            diff = 'Easy'
        difficulty = diff.capitalize()
        
        # Clean title: e.g. "176. Second Highest Salary" -> "Second Highest Salary"
        clean_title = re.sub(r'^\d+\.\s*', '', orig_title) if orig_title else slug.replace('-', ' ').title()
        
        # Meta info
        meta = PROBLEM_DATA.get(num, {
            'category': 'Database',
            'tags': ['sql', 'database'],
            'time': 'O(N)',
            'space': 'O(1)',
            'approach': 'Standard SQL relational query utilizing conditional filtering and aggregate grouping.'
        })
        
        # Find SQL file
        sql_files = [f for f in os.listdir(src_dir) if f.endswith('.sql')]
        sql_filename = sql_files[0] if sql_files else f"{folder_name}.sql"
        sql_src_path = os.path.join(src_dir, sql_filename)
        sql_code = ""
        if os.path.exists(sql_src_path):
            with open(sql_src_path, 'r', encoding='utf-8') as sf:
                sql_code = sf.read().strip()
                
        # Format markdown problem description
        clean_problem_statement = html_to_markdown(raw_html)
        
        # Build standardized README.md content according to Benchmarking standard
        std_readme = f"""# {num} - {clean_title}

- **Platform:** LeetCode
- **Difficulty:** {difficulty}
- **Language:** MySQL (SQL)
- **Category:** {meta['category']}
- **Status:** Accepted
- **Original Problem:** [{orig_url}]({orig_url})

## Problem Statement

{clean_problem_statement}

## Approach & Key Insights

{meta['approach']}

## Complexity Analysis

- **Time Complexity:** `{meta['time']}`
- **Space Complexity:** `{meta['space']}`

## Solution

The complete SQL query solution is available in [`{sql_filename}`](./{sql_filename}).

```sql
{sql_code}
```
"""
        # Target directory: LeetCode/SQL/<Difficulty>/<folder_name>
        target_dir = os.path.join(SQL_DIR, difficulty, folder_name)
        os.makedirs(target_dir, exist_ok=True)
        
        # Write new standardized README.md
        with open(os.path.join(target_dir, 'README.md'), 'w', encoding='utf-8') as rf:
            rf.write(std_readme)
            
        # Copy SQL solution file
        if os.path.exists(sql_src_path):
            shutil.copy2(sql_src_path, os.path.join(target_dir, sql_filename))
            
        # Catalog record
        rel_solution_path = f"LeetCode/SQL/{difficulty}/{folder_name}/{sql_filename}"
        rel_readme_path = f"LeetCode/SQL/{difficulty}/{folder_name}/README.md"
        
        solutions_catalog.append({
            'id': num,
            'title': clean_title,
            'slug': slug,
            'folder': folder_name,
            'difficulty': difficulty,
            'platform': 'LeetCode',
            'language': 'MySQL',
            'category': meta['category'],
            'tags': meta['tags'],
            'url': orig_url,
            'status': 'Accepted',
            'time_complexity': meta['time'],
            'space_complexity': meta['space'],
            'approach': meta['approach'],
            'solution_path': rel_solution_path,
            'readme_path': rel_readme_path
        })
        
        # Clean up old source directory at root
        shutil.rmtree(src_dir)
        
    # Sort solutions by ID
    solutions_catalog.sort(key=lambda x: x['id'])
    
    with open(SOLUTIONS_JSON, 'w', encoding='utf-8') as f:
        json.dump(solutions_catalog, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully processed and organized {len(solutions_catalog)} problems.")
    print(f"Catalog saved to {SOLUTIONS_JSON}")

if __name__ == '__main__':
    build()
