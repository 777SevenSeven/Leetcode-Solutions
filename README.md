<div align="center">

# ⚡ LeetCode Solutions & Competitive Programming Hub

Curated, tested, and systematically documented programming solutions with asymptotic complexity analysis and live discovery portal.

[![Problems Solved](https://img.shields.io/badge/Solved-49%20Problems-blue?style=for-the-badge&logo=leetcode)](https://github.com/777SevenSeven/Leetcode-Solutions)
[![Easy](https://img.shields.io/badge/Easy-32-brightgreen?style=for-the-badge)](https://github.com/777SevenSeven/Leetcode-Solutions)
[![Medium](https://img.shields.io/badge/Medium-16-yellow?style=for-the-badge)](https://github.com/777SevenSeven/Leetcode-Solutions)
[![Hard](https://img.shields.io/badge/Hard-1-red?style=for-the-badge)](https://github.com/777SevenSeven/Leetcode-Solutions)
[![SQL 50](https://img.shields.io/badge/SQL_50-100%25_Complete-success?style=for-the-badge)](./LeetCode/SQL/)
[![Web Portal](https://img.shields.io/badge/Live_Portal-GitHub_Pages-0ea5e9?style=for-the-badge&logo=googlechrome)](https://777sevenseven.github.io/Leetcode-Solutions/)

[🌐 Acessar Portal Web & Busca Interativa](https://777sevenseven.github.io/Leetcode-Solutions/) &bull; [📂 Catálogo LeetCode](./LeetCode/) &bull; [📑 Diretrizes de Contribuição](./CONTRIBUTING.md)

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
| **Select** | `5/5` | `██████████` 100% | ✅ Completed |
| **Basic Joins** | `9/9` | `██████████` 100% | ✅ Completed |
| **Basic Aggregate Functions** | `8/8` | `██████████` 100% | ✅ Completed |
| **Sorting and Grouping** | `6/6` | `██████████` 100% | ✅ Completed |
| **Advanced Select and Joins** | `7/7` | `██████████` 100% | ✅ Completed |
| **Subqueries** | `7/7` | `██████████` 100% | ✅ Completed |
| **Advanced String Functions / Regex / Clause** | `7/7` | `██████████` 100% | ✅ Completed |

---

## 📊 Métricas Consolidadas

<div align="center">

| Métrica | Valor | Percentual |
| :--- | :---: | :---: |
| **Total de Desafios Resolvidos** | **`49`** | `100%` |
| 🟢 **Dificuldade Fácil (Easy)** | `32` | `65.3%` |
| 🟡 **Dificuldade Média (Medium)** | `16` | `32.7%` |
| 🔴 **Dificuldade Difícil (Hard)** | `1` | `2.0%` |
| 🗄️ **Dialeto Relacional** | `MySQL 8.0` | `100%` |
| 🌐 **Páginas Estáticas Indexáveis** | `49` | `100%` |

</div>

---

## 📑 Catálogo de Soluções

A tabela abaixo reflete as soluções catalogadas em [`metadata/solutions.json`](./metadata/solutions.json). Cada solução possui seu próprio arquivo `.sql` e uma ficha técnica individual `README.md` com abordagem e análise assintótica.

| ID | Desafio | Dificuldade | Categoria | Tempo | Espaço | Código | Documentação |
| :-: | :--- | :-: | :--- | :-: | :-: | :-: | :-: |
| `0176` | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary) | `🟡 Medium` | Advanced String Functions / Regex / Clause | `O(N log N)` | `O(1)` | [`second-highest-salary.sql`](LeetCode/SQL/Medium/0176-second-highest-salary/0176-second-highest-salary.sql) | [`Docs`](LeetCode/SQL/Medium/0176-second-highest-salary/README.md) |
| `0180` | [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers) | `🟡 Medium` | Advanced Select and Joins | `O(N)` | `O(N)` | [`consecutive-numbers.sql`](LeetCode/SQL/Medium/0180-consecutive-numbers/0180-consecutive-numbers.sql) | [`Docs`](LeetCode/SQL/Medium/0180-consecutive-numbers/README.md) |
| `0185` | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries) | `🔴 Hard` | Subqueries | `O(N log N)` | `O(N)` | [`department-top-three-salaries.sql`](LeetCode/SQL/Hard/0185-department-top-three-salaries/0185-department-top-three-salaries.sql) | [`Docs`](LeetCode/SQL/Hard/0185-department-top-three-salaries/README.md) |
| `0196` | [Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails) | `🟢 Easy` | Advanced String Functions / Regex / Clause | `O(N^2)` | `O(1)` | [`delete-duplicate-emails.sql`](LeetCode/SQL/Easy/0196-delete-duplicate-emails/0196-delete-duplicate-emails.sql) | [`Docs`](LeetCode/SQL/Easy/0196-delete-duplicate-emails/README.md) |
| `0197` | [Rising Temperature](https://leetcode.com/problems/rising-temperature) | `🟢 Easy` | Basic Joins | `O(N log N)` | `O(N)` | [`rising-temperature.sql`](LeetCode/SQL/Easy/0197-rising-temperature/0197-rising-temperature.sql) | [`Docs`](LeetCode/SQL/Easy/0197-rising-temperature/README.md) |
| `0550` | [Game Play Analysis IV](https://leetcode.com/problems/game-play-analysis-iv) | `🟡 Medium` | Basic Aggregate Functions | `O(N log N)` | `O(N)` | [`game-play-analysis-iv.sql`](LeetCode/SQL/Medium/0550-game-play-analysis-iv/0550-game-play-analysis-iv.sql) | [`Docs`](LeetCode/SQL/Medium/0550-game-play-analysis-iv/README.md) |
| `0570` | [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports) | `🟡 Medium` | Basic Joins | `O(N)` | `O(N)` | [`managers-with-at-least-5-direct-reports.sql`](LeetCode/SQL/Medium/0570-managers-with-at-least-5-direct-reports/0570-managers-with-at-least-5-direct-reports.sql) | [`Docs`](LeetCode/SQL/Medium/0570-managers-with-at-least-5-direct-reports/README.md) |
| `0577` | [Employee Bonus](https://leetcode.com/problems/employee-bonus) | `🟢 Easy` | Basic Joins | `O(N + M)` | `O(N + M)` | [`employee-bonus.sql`](LeetCode/SQL/Easy/0577-employee-bonus/0577-employee-bonus.sql) | [`Docs`](LeetCode/SQL/Easy/0577-employee-bonus/README.md) |
| `0584` | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee) | `🟢 Easy` | Select | `O(N)` | `O(1)` | [`find-customer-referee.sql`](LeetCode/SQL/Easy/0584-find-customer-referee/0584-find-customer-referee.sql) | [`Docs`](LeetCode/SQL/Easy/0584-find-customer-referee/README.md) |
| `0585` | [Investments in 2016](https://leetcode.com/problems/investments-in-2016) | `🟡 Medium` | Subqueries | `O(N)` | `O(N)` | [`investments-in-2016.sql`](LeetCode/SQL/Medium/0585-investments-in-2016/0585-investments-in-2016.sql) | [`Docs`](LeetCode/SQL/Medium/0585-investments-in-2016/README.md) |
| `0595` | [Big Countries](https://leetcode.com/problems/big-countries) | `🟢 Easy` | Select | `O(N)` | `O(1)` | [`big-countries.sql`](LeetCode/SQL/Easy/0595-big-countries/0595-big-countries.sql) | [`Docs`](LeetCode/SQL/Easy/0595-big-countries/README.md) |
| `0596` | [Classes With at Least 5 Students](https://leetcode.com/problems/classes-with-at-least-5-students) | `🟢 Easy` | Sorting and Grouping | `O(N)` | `O(N)` | [`classes-with-at-least-5-students.sql`](LeetCode/SQL/Easy/0596-classes-with-at-least-5-students/0596-classes-with-at-least-5-students.sql) | [`Docs`](LeetCode/SQL/Easy/0596-classes-with-at-least-5-students/README.md) |
| `0602` | [Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends) | `🟡 Medium` | Subqueries | `O(N log N)` | `O(N)` | [`friend-requests-ii-who-has-the-most-friends.sql`](LeetCode/SQL/Medium/0602-friend-requests-ii-who-has-the-most-friends/0602-friend-requests-ii-who-has-the-most-friends.sql) | [`Docs`](LeetCode/SQL/Medium/0602-friend-requests-ii-who-has-the-most-friends/README.md) |
| `0610` | [Triangle Judgement](https://leetcode.com/problems/triangle-judgement) | `🟢 Easy` | Advanced Select and Joins | `O(N)` | `O(1)` | [`triangle-judgement.sql`](LeetCode/SQL/Easy/0610-triangle-judgement/0610-triangle-judgement.sql) | [`Docs`](LeetCode/SQL/Easy/0610-triangle-judgement/README.md) |
| `0619` | [Biggest Single Number](https://leetcode.com/problems/biggest-single-number) | `🟢 Easy` | Sorting and Grouping | `O(N)` | `O(N)` | [`biggest-single-number.sql`](LeetCode/SQL/Easy/0619-biggest-single-number/0619-biggest-single-number.sql) | [`Docs`](LeetCode/SQL/Easy/0619-biggest-single-number/README.md) |
| `0620` | [Not Boring Movies](https://leetcode.com/problems/not-boring-movies) | `🟢 Easy` | Basic Aggregate Functions | `O(N log N)` | `O(N)` | [`not-boring-movies.sql`](LeetCode/SQL/Easy/0620-not-boring-movies/0620-not-boring-movies.sql) | [`Docs`](LeetCode/SQL/Easy/0620-not-boring-movies/README.md) |
| `0626` | [Exchange Seats](https://leetcode.com/problems/exchange-seats) | `🟡 Medium` | Subqueries | `O(N)` | `O(1)` | [`exchange-seats.sql`](LeetCode/SQL/Medium/0626-exchange-seats/0626-exchange-seats.sql) | [`Docs`](LeetCode/SQL/Medium/0626-exchange-seats/README.md) |
| `1045` | [Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products) | `🟡 Medium` | Sorting and Grouping | `O(N)` | `O(N)` | [`customers-who-bought-all-products.sql`](LeetCode/SQL/Medium/1045-customers-who-bought-all-products/1045-customers-who-bought-all-products.sql) | [`Docs`](LeetCode/SQL/Medium/1045-customers-who-bought-all-products/README.md) |
| `1068` | [Product Sales Analysis I](https://leetcode.com/problems/product-sales-analysis-i) | `🟢 Easy` | Basic Joins | `O(N)` | `O(N)` | [`product-sales-analysis-i.sql`](LeetCode/SQL/Easy/1068-product-sales-analysis-i/1068-product-sales-analysis-i.sql) | [`Docs`](LeetCode/SQL/Easy/1068-product-sales-analysis-i/README.md) |
| `1070` | [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii) | `🟡 Medium` | Sorting and Grouping | `O(N log N)` | `O(N)` | [`product-sales-analysis-iii.sql`](LeetCode/SQL/Medium/1070-product-sales-analysis-iii/1070-product-sales-analysis-iii.sql) | [`Docs`](LeetCode/SQL/Medium/1070-product-sales-analysis-iii/README.md) |
| `1075` | [Project Employees I](https://leetcode.com/problems/project-employees-i) | `🟢 Easy` | Basic Aggregate Functions | `O(N)` | `O(N)` | [`project-employees-i.sql`](LeetCode/SQL/Easy/1075-project-employees-i/1075-project-employees-i.sql) | [`Docs`](LeetCode/SQL/Easy/1075-project-employees-i/README.md) |
| `1141` | [User Activity for the Past 30 Days I](https://leetcode.com/problems/user-activity-for-the-past-30-days-i) | `🟢 Easy` | Basic Aggregate Functions | `O(N)` | `O(N)` | [`user-activity-for-the-past-30-days-i.sql`](LeetCode/SQL/Easy/1141-user-activity-for-the-past-30-days-i/1141-user-activity-for-the-past-30-days-i.sql) | [`Docs`](LeetCode/SQL/Easy/1141-user-activity-for-the-past-30-days-i/README.md) |
| `1148` | [Article Views I](https://leetcode.com/problems/article-views-i) | `🟢 Easy` | Select | `O(N log N)` | `O(N)` | [`article-views-i.sql`](LeetCode/SQL/Easy/1148-article-views-i/1148-article-views-i.sql) | [`Docs`](LeetCode/SQL/Easy/1148-article-views-i/README.md) |
| `1164` | [Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date) | `🟡 Medium` | Advanced Select and Joins | `O(N log N)` | `O(N)` | [`product-price-at-a-given-date.sql`](LeetCode/SQL/Medium/1164-product-price-at-a-given-date/1164-product-price-at-a-given-date.sql) | [`Docs`](LeetCode/SQL/Medium/1164-product-price-at-a-given-date/README.md) |
| `1193` | [Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i) | `🟡 Medium` | Basic Aggregate Functions | `O(N)` | `O(N)` | [`monthly-transactions-i.sql`](LeetCode/SQL/Medium/1193-monthly-transactions-i/1193-monthly-transactions-i.sql) | [`Docs`](LeetCode/SQL/Medium/1193-monthly-transactions-i/README.md) |
| `1204` | [Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus) | `🟡 Medium` | Advanced Select and Joins | `O(N log N)` | `O(N)` | [`last-person-to-fit-in-the-bus.sql`](LeetCode/SQL/Medium/1204-last-person-to-fit-in-the-bus/1204-last-person-to-fit-in-the-bus.sql) | [`Docs`](LeetCode/SQL/Medium/1204-last-person-to-fit-in-the-bus/README.md) |
| `1211` | [Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage) | `🟢 Easy` | Basic Aggregate Functions | `O(N)` | `O(N)` | [`queries-quality-and-percentage.sql`](LeetCode/SQL/Easy/1211-queries-quality-and-percentage/1211-queries-quality-and-percentage.sql) | [`Docs`](LeetCode/SQL/Easy/1211-queries-quality-and-percentage/README.md) |
| `1251` | [Average Selling Price](https://leetcode.com/problems/average-selling-price) | `🟢 Easy` | Basic Aggregate Functions | `O(N)` | `O(N)` | [`average-selling-price.sql`](LeetCode/SQL/Easy/1251-average-selling-price/1251-average-selling-price.sql) | [`Docs`](LeetCode/SQL/Easy/1251-average-selling-price/README.md) |
| `1280` | [Students and Examinations](https://leetcode.com/problems/students-and-examinations) | `🟢 Easy` | Basic Joins | `O(S * B + E)` | `O(S * B)` | [`students-and-examinations.sql`](LeetCode/SQL/Easy/1280-students-and-examinations/1280-students-and-examinations.sql) | [`Docs`](LeetCode/SQL/Easy/1280-students-and-examinations/README.md) |
| `1321` | [Restaurant Growth](https://leetcode.com/problems/restaurant-growth) | `🟡 Medium` | Subqueries | `O(N log N)` | `O(N)` | [`restaurant-growth.sql`](LeetCode/SQL/Medium/1321-restaurant-growth/1321-restaurant-growth.sql) | [`Docs`](LeetCode/SQL/Medium/1321-restaurant-growth/README.md) |
| `1327` | [List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period) | `🟢 Easy` | Advanced String Functions / Regex / Clause | `O(N)` | `O(N)` | [`list-the-products-ordered-in-a-period.sql`](LeetCode/SQL/Easy/1327-list-the-products-ordered-in-a-period/1327-list-the-products-ordered-in-a-period.sql) | [`Docs`](LeetCode/SQL/Easy/1327-list-the-products-ordered-in-a-period/README.md) |
| `1341` | [Movie Rating](https://leetcode.com/problems/movie-rating) | `🟡 Medium` | Subqueries | `O(N log N)` | `O(N)` | [`movie-rating.sql`](LeetCode/SQL/Medium/1341-movie-rating/1341-movie-rating.sql) | [`Docs`](LeetCode/SQL/Medium/1341-movie-rating/README.md) |
| `1378` | [Replace Employee ID With The Unique Identifier](https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier) | `🟢 Easy` | Basic Joins | `O(N)` | `O(N)` | [`replace-employee-id-with-the-unique-identifier.sql`](LeetCode/SQL/Easy/1378-replace-employee-id-with-the-unique-identifier/1378-replace-employee-id-with-the-unique-identifier.sql) | [`Docs`](LeetCode/SQL/Easy/1378-replace-employee-id-with-the-unique-identifier/README.md) |
| `1484` | [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date) | `🟢 Easy` | Advanced String Functions / Regex / Clause | `O(N log N)` | `O(N)` | [`group-sold-products-by-the-date.sql`](LeetCode/SQL/Easy/1484-group-sold-products-by-the-date/1484-group-sold-products-by-the-date.sql) | [`Docs`](LeetCode/SQL/Easy/1484-group-sold-products-by-the-date/README.md) |
| `1517` | [Find Users With Valid E-Mails](https://leetcode.com/problems/find-users-with-valid-e-mails) | `🟢 Easy` | Advanced String Functions / Regex / Clause | `O(N)` | `O(1)` | [`find-users-with-valid-e-mails.sql`](LeetCode/SQL/Easy/1517-find-users-with-valid-e-mails/1517-find-users-with-valid-e-mails.sql) | [`Docs`](LeetCode/SQL/Easy/1517-find-users-with-valid-e-mails/README.md) |
| `1527` | [Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition) | `🟢 Easy` | Advanced String Functions / Regex / Clause | `O(N)` | `O(1)` | [`patients-with-a-condition.sql`](LeetCode/SQL/Easy/1527-patients-with-a-condition/1527-patients-with-a-condition.sql) | [`Docs`](LeetCode/SQL/Easy/1527-patients-with-a-condition/README.md) |
| `1581` | [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions) | `🟢 Easy` | Basic Joins | `O(N)` | `O(N)` | [`customer-who-visited-but-did-not-make-any-transactions.sql`](LeetCode/SQL/Easy/1581-customer-who-visited-but-did-not-make-any-transactions/1581-customer-who-visited-but-did-not-make-any-transactions.sql) | [`Docs`](LeetCode/SQL/Easy/1581-customer-who-visited-but-did-not-make-any-transactions/README.md) |
| `1633` | [Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest) | `🟢 Easy` | Basic Aggregate Functions | `O(N log N)` | `O(N)` | [`percentage-of-users-attended-a-contest.sql`](LeetCode/SQL/Easy/1633-percentage-of-users-attended-a-contest/1633-percentage-of-users-attended-a-contest.sql) | [`Docs`](LeetCode/SQL/Easy/1633-percentage-of-users-attended-a-contest/README.md) |
| `1661` | [Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine) | `🟢 Easy` | Basic Joins | `O(N)` | `O(N)` | [`average-time-of-process-per-machine.sql`](LeetCode/SQL/Easy/1661-average-time-of-process-per-machine/1661-average-time-of-process-per-machine.sql) | [`Docs`](LeetCode/SQL/Easy/1661-average-time-of-process-per-machine/README.md) |
| `1667` | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table) | `🟢 Easy` | Advanced String Functions / Regex / Clause | `O(N log N)` | `O(N)` | [`fix-names-in-a-table.sql`](LeetCode/SQL/Easy/1667-fix-names-in-a-table/1667-fix-names-in-a-table.sql) | [`Docs`](LeetCode/SQL/Easy/1667-fix-names-in-a-table/README.md) |
| `1683` | [Invalid Tweets](https://leetcode.com/problems/invalid-tweets) | `🟢 Easy` | Select | `O(N)` | `O(1)` | [`invalid-tweets.sql`](LeetCode/SQL/Easy/1683-invalid-tweets/1683-invalid-tweets.sql) | [`Docs`](LeetCode/SQL/Easy/1683-invalid-tweets/README.md) |
| `1729` | [Find Followers Count](https://leetcode.com/problems/find-followers-count) | `🟢 Easy` | Sorting and Grouping | `O(N log N)` | `O(N)` | [`find-followers-count.sql`](LeetCode/SQL/Easy/1729-find-followers-count/1729-find-followers-count.sql) | [`Docs`](LeetCode/SQL/Easy/1729-find-followers-count/README.md) |
| `1731` | [The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee) | `🟢 Easy` | Advanced Select and Joins | `O(N log N)` | `O(N)` | [`the-number-of-employees-which-report-to-each-employee.sql`](LeetCode/SQL/Easy/1731-the-number-of-employees-which-report-to-each-employee/1731-the-number-of-employees-which-report-to-each-employee.sql) | [`Docs`](LeetCode/SQL/Easy/1731-the-number-of-employees-which-report-to-each-employee/README.md) |
| `1757` | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products) | `🟢 Easy` | Select | `O(N)` | `O(1)` | [`recyclable-and-low-fat-products.sql`](LeetCode/SQL/Easy/1757-recyclable-and-low-fat-products/1757-recyclable-and-low-fat-products.sql) | [`Docs`](LeetCode/SQL/Easy/1757-recyclable-and-low-fat-products/README.md) |
| `1789` | [Primary Department for Each Employee](https://leetcode.com/problems/primary-department-for-each-employee) | `🟢 Easy` | Advanced Select and Joins | `O(N)` | `O(N)` | [`primary-department-for-each-employee.sql`](LeetCode/SQL/Easy/1789-primary-department-for-each-employee/1789-primary-department-for-each-employee.sql) | [`Docs`](LeetCode/SQL/Easy/1789-primary-department-for-each-employee/README.md) |
| `1907` | [Count Salary Categories](https://leetcode.com/problems/count-salary-categories) | `🟡 Medium` | Advanced Select and Joins | `O(N)` | `O(1)` | [`count-salary-categories.sql`](LeetCode/SQL/Medium/1907-count-salary-categories/1907-count-salary-categories.sql) | [`Docs`](LeetCode/SQL/Medium/1907-count-salary-categories/README.md) |
| `1934` | [Confirmation Rate](https://leetcode.com/problems/confirmation-rate) | `🟡 Medium` | Basic Joins | `O(N + M)` | `O(N)` | [`confirmation-rate.sql`](LeetCode/SQL/Medium/1934-confirmation-rate/1934-confirmation-rate.sql) | [`Docs`](LeetCode/SQL/Medium/1934-confirmation-rate/README.md) |
| `1978` | [Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company) | `🟢 Easy` | Subqueries | `O(N log N)` | `O(N)` | [`employees-whose-manager-left-the-company.sql`](LeetCode/SQL/Easy/1978-employees-whose-manager-left-the-company/1978-employees-whose-manager-left-the-company.sql) | [`Docs`](LeetCode/SQL/Easy/1978-employees-whose-manager-left-the-company/README.md) |
| `2356` | [Number of Unique Subjects Taught by Each Teacher](https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher) | `🟢 Easy` | Sorting and Grouping | `O(N)` | `O(N)` | [`number-of-unique-subjects-taught-by-each-teacher.sql`](LeetCode/SQL/Easy/2356-number-of-unique-subjects-taught-by-each-teacher/2356-number-of-unique-subjects-taught-by-each-teacher.sql) | [`Docs`](LeetCode/SQL/Easy/2356-number-of-unique-subjects-taught-by-each-teacher/README.md) |

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
