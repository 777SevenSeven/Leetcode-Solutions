import os
import json

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SOLUTIONS_JSON = os.path.join(REPO_DIR, 'metadata', 'solutions.json')
ROOT_README = os.path.join(REPO_DIR, 'README.md')
LEETCODE_README = os.path.join(REPO_DIR, 'LeetCode', 'README.md')
HACKERRANK_README = os.path.join(REPO_DIR, 'HackerRank', 'README.md')
CODEFORCES_README = os.path.join(REPO_DIR, 'Codeforces', 'README.md')

PORTAL_URL = "https://777sevenseven.github.io/Leetcode-Solutions/"
REPO_URL = "https://github.com/777SevenSeven/Leetcode-Solutions"

DIFFICULTY_PILLS = {
    'Easy': '`🟢 Easy`',
    'Medium': '`🟡 Medium`',
    'Hard': '`🔴 Hard`'
}

def generate():
    if not os.path.exists(SOLUTIONS_JSON):
        print(f"Error: {SOLUTIONS_JSON} not found. Run build_metadata.py first.")
        return

    with open(SOLUTIONS_JSON, 'r', encoding='utf-8') as f:
        solutions = json.load(f)

    total_count = len(solutions)
    diff_counts = {'Easy': 0, 'Medium': 0, 'Hard': 0}
    category_counts = {}

    for s in solutions:
        d = s['difficulty']
        diff_counts[d] = diff_counts.get(d, 0) + 1
        cat = s['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1

    catalog_rows = []
    for s in solutions:
        id_str = s['id']
        title_str = s['title']
        diff_pill = DIFFICULTY_PILLS.get(s['difficulty'], s['difficulty'])
        cat = s['category']
        time_c = s['time_complexity']
        space_c = s['space_complexity']
        sol_link = f"[`{s['slug']}.sql`]({s['solution_path']})"
        readme_link = f"[`Docs`]({s['readme_path']})"
        lc_link = f"[{title_str}]({s['url']})"

        catalog_rows.append(
            f"| `{id_str}` | {lc_link} | {diff_pill} | {cat} | `{time_c}` | `{space_c}` | {sol_link} | {readme_link} |"
        )

    catalog_table = "\n".join(catalog_rows)

    category_rows = []
    sql50_total_per_cat = {
        'Select': 5,
        'Basic Joins': 9,
        'Basic Aggregate Functions': 8,
        'Sorting and Grouping': 6,
        'Advanced Select and Joins': 7,
        'Subqueries': 7,
        'Advanced String Functions / Regex / Clause': 7
    }

    for cat_name, target in sql50_total_per_cat.items():
        completed = category_counts.get(cat_name, 0)
        pct = int((completed / target) * 100) if target > 0 else 100
        bar = "█" * (pct // 10) + "░" * (10 - (pct // 10))
        status = "✅ Completed" if completed >= target else f"{completed}/{target}"
        category_rows.append(f"| **{cat_name}** | `{completed}/{target}` | `{bar}` {pct}% | {status} |")

    category_table = "\n".join(category_rows)

    root_content = f"""<div align="center">

# ⚡ LeetCode Solutions & Competitive Programming Hub

Curated, tested, and systematically documented programming solutions with asymptotic complexity analysis and live discovery portal.

[![Problems Solved](https://img.shields.io/badge/Solved-49%20Problems-blue?style=for-the-badge&logo=leetcode)]({REPO_URL})
[![Easy](https://img.shields.io/badge/Easy-32-brightgreen?style=for-the-badge)]({REPO_URL})
[![Medium](https://img.shields.io/badge/Medium-16-yellow?style=for-the-badge)]({REPO_URL})
[![Hard](https://img.shields.io/badge/Hard-1-red?style=for-the-badge)]({REPO_URL})
[![SQL 50](https://img.shields.io/badge/SQL_50-100%25_Complete-success?style=for-the-badge)](./LeetCode/SQL/)
[![Web Portal](https://img.shields.io/badge/Live_Portal-GitHub_Pages-0ea5e9?style=for-the-badge&logo=googlechrome)]({PORTAL_URL})

[🌐 Acessar Portal Web & Busca Interativa]({PORTAL_URL}) &bull; [📂 Catálogo LeetCode](./LeetCode/) &bull; [📑 Diretrizes de Contribuição](./CONTRIBUTING.md)

</div>

---

## 📌 Visão Geral & Discovery Engineering

Este repositório consolida soluções de desafios técnicos de programação (LeetCode, HackerRank, Codeforces) estruturadas sob uma arquitetura de engenharia de software auditável, modular e com foco em **descoberta e indexação técnica**:

- **Interface de Descoberta Web (GitHub Pages)**: Portal estático independente com pesquisa em tempo real por padrões relacionais, dificuldade e identificadores.
- **Indexação Técnica & SEO**: Cada problema possui sua própria página estática indexável (`docs/solutions/`), equipada com metadados estruturados Schema.org / JSON-LD, sitemap XML e permissões explícitas para crawlers de busca e agentes de IA (`OAI-SearchBot`, Googlebot, Bingbot).
- **Padronização e Rastreabilidade**: Convenção de 4 dígitos (`0000-slug`), separação dos códigos-fonte e fichas técnicas individuais com análise assintótica de tempo e espaço ($O$).
- **Catálogo Estruturado em Metadados**: Base única em [`metadata/solutions.json`](./metadata/solutions.json) utilizada para alimentar documentação, scripts e a interface web.

---

## 🏗️ Estrutura do Repositório

```text
Leetcode-Solutions/
├── docs/                           # Portal Web estático (GitHub Pages)
│   ├── index.html                  # Interface de exploração e busca por filtros
│   ├── solutions/                  # Páginas estáticas individuais de cada exercício
│   ├── sitemap.xml                 # Mapeamento para motores de busca
│   └── robots.txt                  # Diretrizes para indexadores e agentes de IA
├── metadata/
│   └── solutions.json              # Catálogo centralizado em formato JSON
├── scripts/
│   ├── generate_site.py            # Compilador do portal web estático
│   ├── generate_readme.py          # Gerador automático dos índices e métricas
│   ├── validate.py                 # Validador de integridade, nomenclatura e links
│   └── sync.py                     # Sincronizador e ingestor de novas submissões
├── LeetCode/
│   ├── README.md                   # Portal específico da plataforma LeetCode
│   ├── SQL/                        # Acervo SQL segregado por dificuldade
│   │   ├── Easy/                   # 32 soluções catalogadas
│   │   ├── Medium/                 # 16 soluções catalogadas
│   │   └── Hard/                   # 1 solução catalogada
│   ├── Python/                     # Diretório preparado para algoritmos e estruturas de dados
│   └── Java/                       # Diretório preparado para soluções em Java
├── HackerRank/                     # Suporte multi-plataforma (Python & SQL)
├── Codeforces/                     # Suporte multi-plataforma (C++)
├── CONTRIBUTING.md                 # Guia de padronização e fluxo de contribuição
├── LICENSE                         # Licença MIT
└── README.md                       # Índice principal e dashboard
```

---

## 🎯 Progresso: LeetCode SQL 50 Study Plan

O plano de estudos **LeetCode SQL 50** está **concluído**, cobrindo todas as competências fundamentais de engenharia de dados e modelagem relacional:

| Categoria SQL | Soluções Concluídas | Progresso Visual | Status |
| :--- | :---: | :---: | :---: |
{category_table}

---

## 📊 Métricas Consolidadas

<div align="center">

| Métrica | Valor | Percentual |
| :--- | :---: | :---: |
| **Total de Desafios Resolvidos** | **`{total_count}`** | `100%` |
| 🟢 **Dificuldade Fácil (Easy)** | `{diff_counts['Easy']}` | `{(diff_counts['Easy']/total_count*100):.1f}%` |
| 🟡 **Dificuldade Média (Medium)** | `{diff_counts['Medium']}` | `{(diff_counts['Medium']/total_count*100):.1f}%` |
| 🔴 **Dificuldade Difícil (Hard)** | `{diff_counts['Hard']}` | `{(diff_counts['Hard']/total_count*100):.1f}%` |
| 🗄️ **Dialeto Relacional** | `MySQL 8.0` | `100%` |
| 🌐 **Páginas Estáticas Indexáveis** | `{total_count}` | `100%` |

</div>

---

## 📑 Catálogo de Soluções

A tabela abaixo reflete as soluções catalogadas em [`metadata/solutions.json`](./metadata/solutions.json). Cada solução possui seu próprio arquivo `.sql` e uma ficha técnica individual `README.md` com abordagem e análise assintótica.

| ID | Desafio | Dificuldade | Categoria | Tempo | Espaço | Código | Documentação |
| :-: | :--- | :-: | :--- | :-: | :-: | :-: | :-: |
{catalog_table}

---

## ⚙️ Manutenção e Scripts Utilitários

O repositório conta com scripts em Python para manutenção contínua:

```bash
# Validar conformidade estrutural, links e metadados
python scripts/validate.py

# Regenerar documentação Markdown do README
python scripts/generate_readme.py

# Recompilar portal estático (HTML, sitemap e robots)
python scripts/generate_site.py

# Ingerir novas submissões
python scripts/sync.py
```

---

## 🧪 Como Executar as Consultas Localmente

Todas as soluções utilizam **MySQL 8.0+** e são compatíveis com padrões ANSI SQL.

### Exemplo com Docker:
```bash
# Iniciar instância do MySQL
docker run --name leetcode-mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=leetcode -p 3306:3306 -d mysql:8.0

# Executar uma consulta
docker exec -i leetcode-mysql mysql -uroot -psecret leetcode < LeetCode/SQL/Easy/0584-find-customer-referee/0584-find-customer-referee.sql
```

---

## 🏷️ GitHub Topics & Descoberta

Topics configurados para o repositório:
```text
leetcode, leetcode-solutions, sql, mysql, database, algorithms, data-structures, competitive-programming, interview-preparation, problem-solving, coding-challenges, sql50
```

---

## 🤝 Diretrizes de Contribuição

Consulte [`CONTRIBUTING.md`](./CONTRIBUTING.md) para regras de nomenclatura, formatação de soluções e checklist para envio de pull requests.

---

## 📜 Licença

Distribuído sob a licença **MIT**. Veja [`LICENSE`](./LICENSE) para mais informações.
"""

    with open(ROOT_README, 'w', encoding='utf-8') as f:
        f.write(root_content)

    print("Successfully regenerated ROOT README.md with clean links.")

if __name__ == '__main__':
    generate()
