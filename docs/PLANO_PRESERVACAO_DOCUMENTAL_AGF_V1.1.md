# PLANO DE PRESERVAÇÃO DOCUMENTAL AGF — V1.1

**Projeto:** HAGF  
**Data:** 2026-11-06  
**Objetivo:** preservar automaticamente as fontes documentadas, com proveniência, integridade, versionamento e classificação de direitos de uso.

## 1. Diretriz obrigatória do projeto

**A documentação, captura, catalogação, validação, versionamento e geração de relatórios do HAGF devem ser automatizadas.** Não usar captura manual como procedimento operacional padrão.

A automação deve, contudo, respeitar os termos aplicáveis a cada origem. Automatizar não significa contornar restrições contratuais, autenticação, paywall, CAPTCHA ou controles técnicos.

## 2. Inventário atual

O manifesto `config/fontes_publicas.json` contém 23 fontes:

- 1 ficheiro com URL direto de download: `AGF_PRIVACY_PDF_2025`.
- 22 referências a páginas HTML ou índices públicos.

O PDF de Política de Privacidade 2025 já foi recuperado. SHA-256: `3eade497f8d95802deae454d921881465253c2f2c25039f649f65b0ce1b2d35c`. O binário não foi publicado no repositório público; existe no pacote local de recuperação e no artefacto da execução anterior.

## 3. Restrição que condiciona a automação

Os Termos de Uso do Site e os Termos do App identificados na diligência documental restringem scraping, mineração de dados, robôs, crawlers e extração automatizada sem autorização prévia.

Portanto, para as 22 páginas AGF ainda não preservadas, **não executar agora um crawler ou downloader automatizado sem base autorizativa**. A exigência de automação será atendida por uma destas vias:

1. API, feed, exportação ou mecanismo oficial de arquivo disponibilizado pela AGF;
2. autorização escrita da AGF para captura automatizada, com escopo, frequência, limites, formatos e finalidade definidos;
3. mecanismo automatizado expressamente permitido pelos termos aplicáveis, validado fonte a fonte.

Não substituir esse requisito por captura manual. Enquanto a via automatizada não estiver autorizada/disponível, registar a fonte como bloqueada para ingestão automatizada e manter a pendência explícita.

## 4. Arquitetura-alvo

```text
config/
  fontes_publicas.json
  politicas_origem.json
ingestao/
  adaptadores/
    direct_file/
    official_api/
    authorized_export/
  scheduler/
  validators/
arquivo/
  fontes/
    documentos/
    paginas/
  metadados/
  integridade/
    SHA256SUMS.txt
    inventario_preservacao.csv
research/
  execucoes/
```

Fluxo automatizado:

1. Ler o manifesto e validar a política da origem.
2. Selecionar apenas fontes com método de ingestão autorizado.
3. Obter o conteúdo sem autenticação indevida nem contorno de controles.
4. Guardar o original em arquivo local/privado.
5. Extrair metadados técnicos: URL, data/hora UTC, título, MIME, tamanho, status e versão.
6. Calcular SHA-256 e validar formato/assinatura.
7. Comparar com a versão anterior e identificar alterações.
8. Produzir relatório JSON/CSV e log de execução.
9. Atualizar o estado da fonte no manifesto.
10. Publicar no GitHub apenas metadados, hashes, relatórios e análises próprias, salvo autorização/licença para redistribuir o conteúdo integral.

## 5. Estados por fonte

- `PRESERVED`: cópia obtida por método autorizado, validada e com hash.
- `REFERENCE_ONLY`: apenas URL e metadados; ainda sem cópia.
- `BLOCKED_TERMS`: automação impedida pelas condições da origem.
- `AUTHORIZATION_REQUIRED`: depende de autorização ou mecanismo oficial.
- `UNAVAILABLE`: origem indisponível durante a execução.
- `VALIDATION_FAILED`: conteúdo obtido, mas falhou em formato, integridade ou leitura.
- `CHANGED`: hash diferente da última versão preservada; manter ambas as versões.

## 6. Critérios de conclusão

Uma fonte só recebe `PRESERVED` quando existir cópia local efetiva, URL de origem, timestamp, MIME/formato, tamanho, SHA-256, método autorizado e validação de leitura. A mera existência de URL ou metadados não conta como preservação.

## 7. Próximas tarefas técnicas

1. Manter o download direto já validado e testar o seu processo de integridade.
2. Criar esquema de política por origem e método de ingestão.
3. Identificar, no índice regulatório e nas páginas documentadas, quais itens possuem ficheiros diretos oficiais, sem descoberta automatizada proibida.
4. Solicitar à AGF uma via oficial de exportação/arquivo ou autorização específica para automatizar as 22 páginas.
5. Implementar adaptadores separados para ficheiro direto, API oficial e exportação autorizada.
6. Só depois ativar execução agendada para as fontes autorizadas.
7. Gerar relatório de cobertura: preservadas, alteradas, bloqueadas, indisponíveis e falhas.

## 8. Referências internas

- Manifesto: `config/fontes_publicas.json`
- Inventário: `research/INVENTARIO_FONTES_PUBLICAS_AGF_2026-11-06_V1.1.md`
- Operação do recuperador: `docs/OPERACAO_COLETA_PUBLICA_V1.0.md`
- Análise da Política de Privacidade: `research/ANALISE_POLITICA_PRIVACIDADE_AGF_2025_V1.0.md`
- Diligência cruzada: `research/DILIGENCIA_CRUZADA_TERMOS_PRIVACIDADE_AGF_V1.0.md`
