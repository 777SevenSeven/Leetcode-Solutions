# Diretrizes de Contribuição (Contributing Guide)

Agradecemos o interesse em contribuir com este acervo! Para manter a excelência técnica, rastreabilidade e consistência, este repositório segue regras estritas inspiradas nos padrões dos projetos `neetcode-gh/leetcode` e `doocs/leetcode`.

---

## 📋 Regras Obrigatórias para Submissões

Toda contribuição ou adição de solução deve atender aos seguintes critérios:

1. **Submissão Aceita (Accepted)**:
   - Apenas submissões testadas e com veredito `Accepted` na plataforma de origem (LeetCode, HackerRank ou Codeforces) são aceitas.

2. **Convenção de Nomenclatura (4 Dígitos)**:
   - O diretório e o arquivo devem iniciar com o número do problema formatado em 4 dígitos com preenchimento de zeros à esquerda:
     - Formato: `<0000>-<slug-da-questao>`
     - Exemplo: `0176-second-highest-salary`
     - Arquivo de código: `0176-second-highest-salary.sql` (ou `.py`, `.java`, `.cpp`).

3. **Estrutura de Diretórios**:
   - Cada solução deve ser alocada dentro de sua respectiva plataforma, linguagem e nível de dificuldade:
     ```text
     LeetCode/<Linguagem>/<Dificuldade>/<0000>-<slug>/
     ├── README.md
     └── <0000>-<slug>.<ext>
     ```
   - Níveis de dificuldade válidos: `Easy`, `Medium`, `Hard`.

4. **Documentação Individual Obrigatória (`README.md`)**:
   - Cada pasta de problema deve conter um arquivo `README.md` estruturado com o template padrão:
     - Cabeçalho de metadados: Platform, Difficulty, Language, Category, Status, Original Problem URL.
     - `## Problem Statement`: Enunciado ou resumo limpo em Markdown.
     - `## Approach & Key Insights`: Racional da abordagem algorítmica/relacional.
     - `## Complexity Analysis`: Análise explícita de complexidade de tempo (`Time Complexity`) e espaço (`Space Complexity`).
     - `## Solution`: Referência direta ao arquivo de código.

5. **Múltiplas Soluções / Abordagens**:
   - Múltiplas soluções para o mesmo exercício são aceitas **apenas** quando diferirem significativamente em paradigma, estratégia algorítmica ou complexidade assintótica (ex: Força Bruta vs Tabela Hash vs Dois Ponteiros).

6. **Código Limpo e Semântico**:
   - Utilize nomes de variáveis claros, aliases expressivos em consultas SQL, boas práticas de indentação e sem comentários redundantes.

---

## 🛠️ Passo a Passo para Contribuir

### 1. Criar uma Branch
```bash
git checkout -b feat/add-0001-two-sum
```

### 2. Adicionar o Problema
Você pode adicionar os arquivos diretamente na estrutura `LeetCode/<Linguagem>/<Dificuldade>/...` ou utilizar a automação de ingestão:
```bash
# Sincroniza e auto-organiza novas pastas
python scripts/sync.py
```

### 3. Auditar a Qualidade Localmente
Antes de abrir o Pull Request, execute a suíte de auditoria:
```bash
# Validar conformidade estrutural
python scripts/validate.py

# Regenerar documentação e índices
python scripts/generate_readme.py
```

O script deve reportar:
```text
✅ ALL AUDIT CHECKS PASSED SUCCESSFULLY!
TOTAL QUALITY SCORE: 100 / 100
```

### 4. Padrão de Mensagens de Commit (Conventional Commits)
Utilize mensagens semânticas no formato:
- `feat(leetcode): add 0001-two-sum (python)`
- `docs(sql): improve explanation for 0185-department-top-three-salaries`
- `fix(catalog): update complexity in solutions.json`

---

## 🚀 Integração Contínua (CI)

Todo Pull Request disparará automaticamente a pipeline do GitHub Actions para validar:
- Formatação de nomes e diretórios.
- Existência da ficha técnica e do código correspondente.
- Conformidade do catálogo `metadata/solutions.json`.
- Integridade de todos os links.
