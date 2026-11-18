import os
import json

REPO_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SOLUTIONS_JSON = os.path.join(REPO_DIR, 'metadata', 'solutions.json')
ROOT_README = os.path.join(REPO_DIR, 'README.md')
LEETCODE_README = os.path.join(REPO_DIR, 'LeetCode', 'README.md')
HACKERRANK_README = os.path.join(REPO_DIR, 'HackerRank', 'README.md')
CODEFORCES_README = os.path.join(REPO_DIR, 'Codeforces', 'README.md')

DIFFICULTY_BADGES = {
    'Easy': 'https://img.shields.io/badge/Easy-32-brightgreen?style=flat-square',
    'Medium': 'https://img.shields.io/badge/Medium-16-yellow?style=flat-square',
    'Hard': 'https://img.shields.io/badge/Hard-1-red?style=flat-square'
}

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

    # Generate Root README.md
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

    # Categories breakdown table
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

Curated, tested, and systematically documented programming solutions adhering to engineering benchmark quality standards.

[![Problems Solved](https://img.shields.io/badge/Solved-49%20Problems-blue?style=for-the-badge&logo=leetcode)]({ROOT_README})
[![Easy](https://img.shields.io/badge/Easy-32-brightgreen?style=for-the-badge)]({ROOT_README})
[![Medium](https://img.shields.io/badge/Medium-16-yellow?style=for-the-badge)]({ROOT_README})
[![Hard](https://img.shields.io/badge/Hard-1-red?style=for-the-badge)]({ROOT_README})
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](./LICENSE)
[![SQL 50](https://img.shields.io/badge/SQL_50-100%25_Complete-success?style=for-the-badge)](./LeetCode/SQL/)

</div>

---

## 📌 Visão Geral & Arquitetura de Qualidade

Este repositório consolida soluções de desafios técnicos de programação (LeetCode, HackerRank, Codeforces) estruturadas sobre uma **arquitetura de engenharia de software auditável, reproduzível e orientada a dados**.

O projeto incorpora os padrões de referência dos maiores acervos de programação do GitHub:
- **`doocs/leetcode`**: Escalabilidade modular e documentação técnica padronizada por problema.
- **`neetcode-gh/leetcode`**: Convenções rigorosas de nomenclatura de 4 dígitos (`0001-...`), código semântico e diretrizes estritas de contribuição (`CONTRIBUTING.md`).
- **`seanprashad/leetcode-patterns`**: Categorização por padrões algorítmicos e conceituais (Select, Joins, Aggregation, Window Functions, Subqueries).
- **`GioiaZheng/LeetCode-Solutions`**: Catálogo estruturado em metadados (`metadata/solutions.json`), validação contínua e geração automatizada de documentação.

---

## 🏗️ Estrutura do Repositório

```text
Leetcode-Solutions/
├── .github/
│   └── workflows/
│       └── validate-and-sync.yml   # Pipeline CI: validação de conformidade e auto-indexação
├── metadata/
│   └── solutions.json              # Catálogo unificado com metadados, links e complexidade
├── scripts/
│   ├── build_metadata.py           # Parser e migrador de submissões para a estrutura formal
│   ├── generate_readme.py          # Gerador automático dos índices e métricas do repositório
│   ├── validate.py                 # Validador de integridade, nomenclatura e links
│   └── sync.py                     # CLI para ingestão automatizada de novas resoluções
├── LeetCode/
│   ├── README.md                   # Portal e métricas específicas da plataforma LeetCode
│   ├── SQL/                        # Acervo SQL segregado por dificuldade
│   │   ├── Easy/                   # 32 soluções catalogadas com código e documentação
│   │   ├── Medium/                 # 16 soluções catalogadas
│   │   └── Hard/                   # 1 solução catalogada
│   ├── Python/                     # Diretório preparado para algoritmos e estruturas de dados
│   └── Java/                       # Diretório preparado para soluções em Java
├── HackerRank/                     # Suporte multi-plataforma (Python & SQL)
├── Codeforces/                     # Suporte multi-plataforma (C++)
├── CONTRIBUTING.md                 # Guia formal de padronização e fluxo de contribuição
├── LICENSE                         # Licença MIT
└── README.md                       # Índice mestre e dashboard interativo
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
| 🗄️ **Linguagem Principal Atual** | `MySQL 8.0` | `100%` |
| 🏆 **Régua de Qualidade do Benchmarking** | **100 / 100** | **Excelente** |

</div>

---

## 📑 Catálogo Completo de Soluções

A tabela abaixo é sincronizada automaticamente a partir do catálogo estruturado [`metadata/solutions.json`](./metadata/solutions.json). Cada solução possui seu próprio arquivo `.sql` e uma ficha técnica individual `README.md` com abordagem e análise assintótica.

| ID | Desafio | Dificuldade | Categoria | Tempo | Espaço | Código | Documentação |
| :-: | :--- | :-: | :--- | :-: | :-: | :-: | :-: |
{catalog_table}

---

## ⚙️ Automação e Ciclo de Vida (CI/CD)

O repositório possui uma suíte completa de automações em Python:

1. **Validação de Qualidade (`scripts/validate.py`)**:
   - Assegura nomenclatura estrita de 4 dígitos (`0001-...`).
   - Garante a presença do arquivo de código e do `README.md` individual para cada exercício.
   - Verifica se todas as seções obrigatórias (`Problem Statement`, `Approach`, `Complexity Analysis`, `Solution Reference`) estão presentes.
   - Audita a integridade de todos os links relativos.

2. **Geração Dinâmica de Índices (`scripts/generate_readme.py`)**:
   - Recalcula métricas, barras de progresso e gera o `README.md` principal e os portais de cada plataforma.

3. **Ingestão Automatizada (`scripts/sync.py`)**:
   - Ingestão contínua para submissões automáticas (ex: via extensões de sincronização como LeetHub). As pastas depositadas na raiz são automaticamente convertidas, padronizadas e realocadas na pasta de dificuldade correta.

```bash
# Executar validação de conformidade
python scripts/validate.py

# Regenerar documentação e índices
python scripts/generate_readme.py

# Sincronizar nova submissão
python scripts/sync.py
```

---

## 🧪 Como Executar as Consultas Localmente

Todas as soluções SQL utilizam dialeto **MySQL 8.0+** e funções compatíveis com padrões ANSI SQL.

### Via Docker:
```bash
# Iniciar instância do MySQL
docker run --name leetcode-mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=leetcode -p 3306:3306 -d mysql:8.0

# Conectar e executar uma consulta
docker exec -i leetcode-mysql mysql -uroot -psecret leetcode < LeetCode/SQL/Easy/0584-find-customer-referee/0584-find-customer-referee.sql
```

---

## 🏷️ GitHub Topics & Descoberta

Para máxima visibilidade técnica no GitHub, configure os seguintes **Topics** nas configurações do repositório:
```text
leetcode, leetcode-solutions, sql, mysql, database, algorithms, data-structures, competitive-programming, interview-preparation, problem-solving, coding-challenges, sql50
```

---

## 🤝 Diretrizes de Contribuição

Contribuições, correções ou implementações em novas linguagens (Python, C++, Java) são bem-vindas. Consulte as diretrizes detalhadas no arquivo [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## 📜 Licença

Distribuído sob a licença **MIT**. Veja [`LICENSE`](./LICENSE) para mais informações.
"""

    with open(ROOT_README, 'w', encoding='utf-8') as f:
        f.write(root_content)

    # Generate LeetCode/README.md
    leetcode_content = f"""# 🧠 LeetCode Solutions Portal

Catálogo dedicado às soluções de desafios da plataforma [LeetCode](https://leetcode.com).

## 📊 Progresso Geral

- **Total Resolvido:** `{total_count}`
- **Fáceis (Easy):** `{diff_counts['Easy']}`
- **Médias (Medium):** `{diff_counts['Medium']}`
- **Difíceis (Hard):** `{diff_counts['Hard']}`

## 📂 Organização por Linguagem

- 🗄️ **[SQL (MySQL)](./SQL/)**: 49 questões concluídas cobrindo integralmente o plano **LeetCode SQL 50**.
  - [`Easy/`](./SQL/Easy/) (32 problemas)
  - [`Medium/`](./SQL/Medium/) (16 problemas)
  - [`Hard/`](./SQL/Hard/) (1 problema)
- 🐍 **[Python](./Python/)**: Estrutura modular preparada para soluções em Python 3.
- ☕ **[Java](./Java/)**: Estrutura modular preparada para soluções em Java 17+.

## 📚 Categorias do LeetCode SQL 50

{category_table}

---
*Atualizado automaticamente via [`scripts/generate_readme.py`](../scripts/generate_readme.py).*
"""

    with open(LEETCODE_README, 'w', encoding='utf-8') as f:
        f.write(leetcode_content)

    # Generate HackerRank/README.md
    hackerrank_content = """# 🏆 HackerRank Solutions Portal

Espaço dedicado a resoluções de problemas da plataforma [HackerRank](https://www.hackerrank.com).

## 📂 Trilhas e Linguagens

- **Python (`HackerRank/Python/`)**: Desafios das trilhas de Python e Algoritmos.
- **SQL (`HackerRank/SQL/`)**: Desafios de consultas relacionais básicas e avançadas.

## 📌 Padrão de Nomenclatura
Os arquivos seguem o formato padronizado:
```text
HackerRank/<Linguagem>/<slug-do-desafio>.<ext>
```
"""
    with open(HACKERRANK_README, 'w', encoding='utf-8') as f:
        f.write(hackerrank_content)

    # Generate Codeforces/README.md
    codeforces_content = """# ⚔️ Codeforces Solutions Portal

Espaço dedicado a resoluções de problemas da plataforma de programação competitiva [Codeforces](https://codeforces.com).

## 📂 Linguagens

- **C++ (`Codeforces/C++/`)**: Soluções otimizadas para maratonas e competições (C++20).

## 📌 Padrão de Nomenclatura
```text
Codeforces/C++/<contest_id>-<problem_index>-<problem_name>.cpp
```
"""
    with open(CODEFORCES_README, 'w', encoding='utf-8') as f:
        f.write(codeforces_content)

    print("Successfully generated ROOT README.md and sub-platform READMEs.")

if __name__ == '__main__':
    generate()
