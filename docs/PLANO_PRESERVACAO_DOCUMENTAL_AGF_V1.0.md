# PLANO DE PRESERVAÇÃO DOCUMENTAL AGF — V1.0

**Projeto:** HAGF  
**Data:** 2026-11-06  
**Objetivo:** preservar as fontes públicas já registadas no manifesto, com proveniência, integridade e classificação de direitos de uso.

## 1. Situação inicial verificada

O manifesto `config/fontes_publicas.json` contém 23 fontes:

- 1 ficheiro com URL direto de download: `AGF_PRIVACY_PDF_2025`.
- 22 referências a páginas HTML ou índices públicos.

O PDF de Política de Privacidade 2025 já foi recuperado numa execução anterior. O ficheiro original foi preservado no pacote local `AGF_RECOVERY_2026-11-06.zip`; o binário não foi publicado no repositório público. SHA-256 registado: `3eade497f8d95802deae454d921881465253c2f2c25039f649f65b0ce1b2d35c`.

## 2. Restrição operacional

Os Termos de Uso do Site e os Termos do App identificados no levantamento anterior restringem scraping, mineração de dados, robôs, crawlers e extração automatizada sem autorização prévia.

Consequentemente:

1. Não executar crawler, spider, varredura recursiva ou download em lote das páginas AGF.
2. Não contornar login, paywall, autenticação, CAPTCHA ou restrições técnicas.
3. Não inferir que uma página pública autoriza redistribuição integral do seu conteúdo.
4. Preservar separadamente o URL original, data/hora de consulta, título, tipo de fonte, estado HTTP quando obtido legitimamente, hash do ficheiro e condições de uso.
5. Para páginas HTML sem ficheiro direto, usar captura manual pelo navegador, quando permitida, ou solicitar à AGF uma forma autorizada de arquivo/exportação.
6. Para documentos diretamente publicados para download, avaliar cada URL individualmente e guardar o original para análise interna, sem republicar binários protegidos no repositório público.

## 3. Política de armazenamento

Estrutura recomendada:

```text
arquivo/
  fontes/
    documentos/       # PDFs e ficheiros originais com download direto
    paginas/          # capturas manuais autorizadas (HTML/PDF)
    metadados/        # JSON de proveniência, datas, hashes e estado
  integridade/
    SHA256SUMS.txt
    inventario_preservacao.csv
```

O repositório público deve conter apenas:
- manifesto de fontes;
- metadados e hashes;
- análises autorais e citações curtas necessárias;
- scripts de validação de integridade;
- documentação operacional.

Os ficheiros integrais de terceiros devem permanecer em arquivo privado/local, salvo licença ou autorização expressa para redistribuição.

## 4. Ordem de execução

| Ordem | Grupo | Tratamento |
|---|---|---|
| 1 | PDF com URL direto | Download individual, validação MIME/assinatura, tamanho e SHA-256 |
| 2 | Termos do Site e Termos do App | Captura manual autorizada; guardar versão, data e hash |
| 3 | Política de Privacidade HTML | Captura manual autorizada; comparar com PDF 2025 |
| 4 | Artigos da Central de Ajuda | Captura manual, um artigo por vez; preservar título, URL e data |
| 5 | Índice regulatório | Inspecionar manualmente; listar documentos efetivamente publicados e avaliar cada download |
| 6 | Blog e páginas institucionais | Preservar páginas relevantes manualmente; não fazer varredura recursiva |

## 5. Critérios de conclusão

Uma fonte só recebe estado `PRESERVED` quando existir:

- cópia local efetiva do conteúdo ou ficheiro;
- URL original;
- data/hora de captura;
- tipo MIME ou formato identificado;
- tamanho em bytes;
- SHA-256;
- indicação de licença/condições de uso conhecidas;
- validação de leitura do ficheiro.

Estados permitidos:

- `PRESERVED`: cópia local validada.
- `REFERENCE_ONLY`: URL e metadados registados, sem cópia integral.
- `BLOCKED_TERMS`: captura automatizada não executada devido às condições aplicáveis.
- `UNAVAILABLE`: origem indisponível no momento da verificação.
- `AUTHORIZATION_REQUIRED`: método pretendido depende de autorização específica.

## 6. Próximo passo

Não marcar as 22 páginas como descarregadas. A próxima execução deve começar pela captura individual das páginas/documentos que possam ser preservados manualmente e pela inspeção manual do índice regulatório, sem crawling. O manifesto deverá ser atualizado fonte a fonte, apenas após validação real do artefacto.

## 7. Referências internas

- Manifesto: `config/fontes_publicas.json`
- Inventário: `research/INVENTARIO_FONTES_PUBLICAS_AGF_2026-11-06_V1.1.md`
- Operação do recuperador: `docs/OPERACAO_COLETA_PUBLICA_V1.0.md`
- Análise da Política de Privacidade: `research/ANALISE_POLITICA_PRIVACIDADE_AGF_2025_V1.0.md`
- Diligência cruzada: `research/DILIGENCIA_CRUZADA_TERMOS_PRIVACIDADE_AGF_V1.0.md`
