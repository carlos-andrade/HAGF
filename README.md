# HAGF — Pesquisa e inteligência sobre o ecossistema AGF

Repositório independente para pesquisa documental, mapeamento de fontes públicas e análise autoral do ecossistema Ações Garantem o Futuro (AGF), seus produtos, ferramentas, metodologia de dividendos e estrutura institucional.

## Objetivos

- Mapear fontes institucionais e documentais públicas da AGF.
- Registrar conceitos, indicadores e metodologia com proveniência.
- Separar fatos declarados pela AGF, evidências externas, inferências e lacunas.
- Construir uma base de conhecimento auditável para análises futuras.
- Respeitar direitos autorais, privacidade e controles de acesso.

## Diretriz operacional

**Toda documentação, captura, catalogação, validação, versionamento e geração de relatórios deve ser automatizada.** A automação deve usar APIs, exportações ou métodos expressamente permitidos pela origem. Não contornar autenticação, paywall, CAPTCHA ou restrições contratuais.

## Estado atual

**Fase:** inventário documental público e recuperação controlada.

- Prompt de pesquisa: [Agente HAGF PhD](PROMPTS/PROMPT_AGENTE_HAGF_PHD_V1.0.md)
- Primeira execução: [Relatório inicial](research/EXECUCAO_INICIAL_AGF_2026-11-06_V1.0.md)
- Correção de escopo de dados públicos: [Nota de correção](research/NOTA_CORRECAO_ACESSO_DADOS_PUBLICOS_V1.0.md)
- Inventário atualizado: [Fontes públicas AGF V1.1](research/INVENTARIO_FONTES_PUBLICAS_AGF_2026-11-06_V1.1.md)
- Plano de preservação automatizada: [Plano V1.1](docs/PLANO_PRESERVACAO_DOCUMENTAL_AGF_V1.1.md)
- Plano anterior: [Plano V1.0](docs/PLANO_PRESERVACAO_DOCUMENTAL_AGF_V1.0.md)
- Análise do PDF de Privacidade: [Relatório V1.0](research/ANALISE_POLITICA_PRIVACIDADE_AGF_2025_V1.0.md)
- Comparação de termos e políticas: [Diligência cruzada V1.0](research/DILIGENCIA_CRUZADA_TERMOS_PRIVACIDADE_AGF_V1.0.md)
- Dicionário técnico: [Métricas AGF e regras de qualidade de dados](knowledge/dicionario_metodologia_agf_v1.0.json)
- Integração B3: [Impacto na qualidade e reconstrução histórica](research/IMPACTO_INTEGRACAO_B3_AGF_V1.0.md)
- Execução confirmada: [Relatório JSON de 06/11/2026](research/execucoes/HAGF_PUBLIC_RECOVERY_20261106T160428Z.json)
- Operação de recuperação: [Manual do coletor](docs/OPERACAO_COLETA_PUBLICA_V1.0.md)

## Coletor de documentos públicos

O coletor baixa somente arquivos com URLs diretas, cadastradas explicitamente no manifesto.

- Script: [scripts/hagf_public_recovery.py](scripts/hagf_public_recovery.py)
- Manifesto: [config/fontes_publicas.json](config/fontes_publicas.json)
- Testes: [tests/test_hagf_public_recovery.py](tests/test_hagf_public_recovery.py)
- Workflow: [HAGF Public Recovery](.github/workflows/hagf-public-recovery.yml)

O processo não rastreia páginas, não descobre links automaticamente, não acessa áreas autenticadas, não contorna paywalls ou CAPTCHAs e não coleta dados pessoais. Em razão das restrições de automação publicadas nos Termos do Site AGF, a ingestão automatizada dessas páginas depende de API/exportação oficial ou autorização específica. O workflow atual valida o código e os testes; não deve ser interpretado como execução de download das 22 referências HTML.

## Política de preservação

As 23 fontes do manifesto não são 23 ficheiros descarregáveis: há 1 PDF com URL direto de download e 22 páginas/referências HTML. O estado real de preservação deve ser registado individualmente. Consulte o [Plano de Preservação Automatizada](docs/PLANO_PRESERVACAO_DOCUMENTAL_AGF_V1.1.md). Não marcar uma referência como preservada sem cópia efetiva, metadados e hash validados.

## Estrutura

```text
config/                 Manifestos e configuração
docs/                   Documentação operacional e arquitetura
research/               Relatórios, inventários e evidências
scripts/                Ferramentas de coleta e validação
tests/                  Testes automatizados
dados/recovery/         Arquivos públicos recuperados
```

## Critério de evidência

Cada afirmação relevante deve possuir fonte, URL, data de consulta e classificação. Conteúdo de cursos, livros, aulas e áreas contratadas não deve ser reproduzido integralmente. O projeto prioriza metadados, definições, resumos autorais e referências verificáveis.

## Licença

Consulte [LICENSE](LICENSE). A licença do repositório não substitui direitos de terceiros sobre materiais de origem.
