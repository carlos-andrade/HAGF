# HAGF — Operação de recuperação de documentos públicos V1.0

**Estado:** coletor implementado; workflow limitado a validação manual, sem download automático  
**Escopo:** downloads pontuais de arquivos com URL direta, declarada e autorizada no manifesto.

## O que o script faz

- Lê `config/fontes_publicas.json`.
- Considera somente o campo `download_url`; o campo `url` é referência documental e nunca é requisitado pelo script.
- Exige HTTPS e host explicitamente permitido.
- Revalida o host após redirecionamentos.
- Limita o tamanho do arquivo.
- Bloqueia HTML, respostas vazias e tipos inesperados.
- Calcula SHA-256 e mantém relatório JSON de cada execução.
- Evita sobrescrever silenciosamente arquivos diferentes.

## O que o script NÃO faz

- Não rastreia páginas nem segue links encontrados em HTML.
- Não consulta sitemap ou robots.txt automaticamente.
- Não faz scraping de artigos ou páginas.
- Não acessa login, áreas pagas, comunidade ou APIs privadas.
- Não contorna CAPTCHA, paywall ou controles de acesso.
- Não coleta dados pessoais.

## Como executar

Validação sem rede e sem downloads:

```bash
python3 scripts/hagf_public_recovery.py
```

Download pontual de URL direta, após validação individual da fonte e revisão das condições aplicáveis:

```bash
python3 scripts/hagf_public_recovery.py --execute
```

**Atenção:** os Termos do Site AGF (dezembro/2025) vedam scraping, mineração de dados e uso de ferramentas automatizadas sem autorização expressa/prévia. Por governança, o workflow GitHub Actions foi limitado a testes e validação sem downloads. Não executar crawling, scraping ou downloads automatizados em lote nos domínios AGF. O modo `--execute` permanece para uso pontual e deliberado, após avaliação da fonte e das condições aplicáveis.

## Como adicionar uma fonte

Adicionar um objeto em `sources`, mantendo a referência pública em `url` e preenchendo `download_url` somente quando houver um link direto para um arquivo publicamente oferecido para download. A URL deve pertencer a um host da allowlist. Não inserir URLs de páginas HTML no campo de download.

## Interpretação da primeira execução

As fontes inicialmente cadastradas são referências institucionais e páginas HTML, não links diretos de arquivos. Portanto, o resultado esperado é `SKIPPED_NO_DIRECT_DOWNLOAD_URL`. Isso é intencional: não se deve rotular páginas HTML como documentos baixados.

## Próxima etapa

Alimentar o manifesto com URLs diretas de PDFs, planilhas ou outros arquivos que sejam efetivamente disponibilizados ao público para download. Cada novo link deve ser verificado individualmente antes de ser adicionado.
