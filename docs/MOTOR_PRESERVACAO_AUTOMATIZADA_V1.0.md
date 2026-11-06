# HAGF — Motor de preservação automatizada V1.0

## Objetivo

Gerar automaticamente um ledger de preservação para todas as fontes do manifesto, com estado individual, caminho do artefacto, tamanho, SHA-256, método de captura e timestamp UTC.

## Componentes

- `scripts/hagf_preservation_ledger.py`: lê o manifesto e verifica os artefactos locais declarados por `archive_path`; gera JSON e CSV.
- `tests/test_hagf_preservation_ledger.py`: testa classificação, integridade, contagem e bloqueio de path traversal.
- `.github/workflows/hagf-public-recovery.yml`: compila, executa testes, gera ledger e relatório dry-run do recuperador; publica os relatórios como artefacto GitHub Actions.

## Execução local

```bash
python3 -m py_compile scripts/hagf_preservation_ledger.py scripts/hagf_public_recovery.py
python3 -m unittest discover -s tests -v
python3 scripts/hagf_preservation_ledger.py
python3 scripts/hagf_public_recovery.py
```

O ledger produz dois ficheiros em `research/execucoes/`:
- `HAGF_PRESERVATION_LEDGER_<timestamp>.json`
- `HAGF_PRESERVATION_LEDGER_<timestamp>.csv`

## Estados

- `PRESERVED`: ficheiro local existe, é legível e tem tamanho e SHA-256 calculados.
- `RECOVERED_PRIOR_RUN_NOT_MATERIALIZED`: existe URL direta e há registo de recuperação anterior, mas o ficheiro não está no workspace atual; não declarar cópia local.
- `AUTHORIZATION_REQUIRED`: referência HTML sem adaptador autorizado configurado.
- `BLOCKED_PATH_TRAVERSAL`: caminho declarado resolve fora da raiz do repositório.

## Limites intencionais

O ledger não faz requisições HTTP, scraping, crawling, descoberta de links nem captura de páginas. O seu papel é inventariar e verificar automaticamente o estado dos ficheiros existentes.

A ingestão de páginas AGF permanece desativada até existir API/exportação oficial ou autorização específica que cubra o método automatizado. Não habilitar um adaptador apenas porque a página é publicamente acessível.

## Artefactos e retenção

O workflow publica JSON e CSV como artefacto do GitHub Actions com retenção de 90 dias. O repositório mantém código e documentação; os binários de terceiros não são automaticamente commitados nem redistribuídos.

## Critério de aceite

A implementação é aceite quando:
1. todos os testes passam;
2. o ledger contém todas as fontes do manifesto;
3. cada fonte possui estado explícito;
4. cada ficheiro local declarado recebe tamanho e SHA-256;
5. nenhuma referência HTML é requisitada pelo ledger;
6. o relatório JSON e CSV são publicados como artefacto.
