# HAGF — Operação de recuperação e preservação documental V1.1

**Estado:** coletor de ficheiros diretos e ledger automatizado implementados; GitHub Actions #10 concluído com sucesso em 06/11/2026.  
**Escopo:** downloads explicitamente configurados e autorizados, inventário automatizado, metadados, integridade e relatórios.

## Componentes

### 1. Recuperador de ficheiros diretos

`scripts/hagf_public_recovery.py`

- Lê `config/fontes_publicas.json`.
- Considera somente o campo `download_url`; o campo `url` é referência documental e nunca é requisitado.
- Exige HTTPS e host explicitamente permitido.
- Revalida o host após redirecionamentos.
- Limita o tamanho do ficheiro.
- Bloqueia HTML, respostas vazias e tipos inesperados.
- Calcula SHA-256 e mantém relatório JSON.
- Evita sobrescrever silenciosamente ficheiros diferentes.

O modo `--execute` só pode ser utilizado para fontes e métodos cuja automação esteja permitida. A existência de URL direto, isoladamente, não substitui a avaliação das condições aplicáveis.

### 2. Ledger de preservação

`scripts/hagf_preservation_ledger.py`

- Lê todas as fontes do manifesto.
- Verifica artefactos locais declarados por `archive_path`.
- Calcula tamanho e SHA-256 dos ficheiros locais.
- Classifica fontes sem cópia ou sem adaptador autorizado.
- Gera relatórios JSON e CSV em `research/execucoes/`.
- Não faz requisições HTTP e não captura páginas.

### 3. Testes

`tests/test_hagf_public_recovery.py` e `tests/test_hagf_preservation_ledger.py`.

## Execução local

```bash
python3 -m py_compile scripts/hagf_public_recovery.py scripts/hagf_preservation_ledger.py
python3 -m unittest discover -s tests -v
python3 scripts/hagf_preservation_ledger.py
python3 scripts/hagf_public_recovery.py
```

Para download direto, usar `--execute` somente após verificar a política da fonte e a autorização do método.

## Workflow GitHub Actions

O workflow `.github/workflows/hagf-public-recovery.yml`:
1. compila os dois scripts;
2. executa todos os testes;
3. gera o ledger JSON/CSV;
4. executa o recuperador em dry-run;
5. publica os relatórios como artefacto por 90 dias.

O workflow é iniciado por alterações relevantes em main e também por `workflow_dispatch`. A execução #10 concluiu com sucesso: compilação, 11 testes, ledger JSON/CSV e dry-run do recuperador. [Consultar execução #10](https://github.com/carlos-andrade/HAGF/actions/runs/42257952950).

## Restrições da origem AGF

Os Termos de Uso do Site e do App identificados na diligência restringem scraping, mineração de dados e ferramentas automatizadas sem autorização prévia. Portanto:

- não rastrear páginas nem descobrir links por crawling;
- não fazer scraping de artigos ou páginas;
- não aceder a login, áreas pagas, comunidade ou APIs privadas;
- não contornar CAPTCHA, paywall ou controles de acesso;
- não recolher dados pessoais;
- não assumir que página pública equivale a autorização para extração automatizada.

A ingestão automatizada das referências HTML depende de API/exportação oficial ou autorização específica que cubra o método pretendido. Enquanto isso, o ledger regista a pendência automaticamente.

## Estados do ledger

- `PRESERVED`: ficheiro local existe e foi validado com tamanho e SHA-256.
- `RECOVERED_PRIOR_RUN_NOT_MATERIALIZED`: há URL direta e registo de recuperação anterior, mas o binário não está no workspace atual.
- `AUTHORIZATION_REQUIRED`: referência HTML sem adaptador autorizado.
- `BLOCKED_PATH_TRAVERSAL`: caminho declarado resolve fora da raiz do repositório.

## Artefactos

O workflow publica JSON e CSV como artefacto do GitHub Actions com retenção de 90 dias. O repositório mantém código, documentação, metadados e análises; ficheiros integrais de terceiros não são publicados sem base de redistribuição.
