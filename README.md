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

**Fase:** motor inicial implementado e validado no GitHub Actions; ingestão das 22 referências HTML bloqueada até canal oficial ou autorização específica.

- Prompt de pesquisa: [Agente HAGF PhD](PROMPTS/PROMPT_AGENTE_HAGF_PHD_V1.0.md)
- Primeira execução: [Relatório inicial](research/EXECUCAO_INICIAL_AGF_2026-11-06_V1.0.md)
- Correção de escopo de dados públicos: [Nota de correção](research/NOTA_CORRECAO_ACESSO_DADOS_PUBLICOS_V1.0.md)
- Inventário atualizado: [Fontes públicas AGF V1.1](research/INVENTARIO_FONTES_PUBLICAS_AGF_2026-11-06_V1.1.md)
- Plano de preservação automatizada: [Plano V1.1](docs/PLANO_PRESERVACAO_DOCUMENTAL_AGF_V1.1.md)
- Motor de preservação: [Documentação técnica V1.0](docs/MOTOR_PRESERVACAO_AUTOMATIZADA_V1.0.md)
- Solicitação de canal oficial de ingestão: [Minuta V1.0 — ainda não enviada](research/SOLICITACAO_CANAL_AUTOMATIZADO_AGF_V1.0.md)
- Análise do PDF de Privacidade: [Relatório V1.0](research/ANALISE_POLITICA_PRIVACIDADE_AGF_2025_V1.0.md)
- Comparação de termos e políticas: [Diligência cruzada V1.0](research/DILIGENCIA_CRUZADA_TERMOS_PRIVACIDADE_AGF_V1.0.md)
- Dicionário técnico: [Métricas AGF e regras de qualidade de dados](knowledge/dicionario_metodologia_agf_v1.0.json)
- Integração B3: [Impacto na qualidade e reconstrução histórica](research/IMPACTO_INTEGRACAO_B3_AGF_V1.0.md)
- Execução de validação do motor: [GitHub Actions #10 — sucesso](https://github.com/carlos-andrade/HAGF/actions/runs/42257952950)
- Solicitação de canal oficial de ingestão: [Minuta V1.0 — ainda não enviada](research/SOLICITACAO_CANAL_AUTOMATIZADO_AGF_V1.0.md)
- Execução de recuperação anterior: [Relatório JSON de 06/11/2026](research/execucoes/HAGF_PUBLIC_RECOVERY_20261106T160428Z.json)

## Motor de preservação

- Ledger: [scripts/hagf_preservation_ledger.py](scripts/hagf_preservation_ledger.py)
- Testes: [tests/test_hagf_preservation_ledger.py](tests/test_hagf_preservation_ledger.py)
- Coletor de ficheiros diretos: [scripts/hagf_public_recovery.py](scripts/hagf_public_recovery.py)
- Manifesto: [config/fontes_publicas.json](config/fontes_publicas.json)
- Workflow: [HAGF Public Recovery](.github/workflows/hagf-public-recovery.yml)

O ledger verifica automaticamente os artefactos locais declarados no manifesto, calcula tamanho e SHA-256 e gera relatórios JSON e CSV. O workflow compila os scripts, executa 11 testes, gera o ledger e publica os relatórios como artefacto. Na execução #10: 23 fontes catalogadas; 22 em AUTHORIZATION_REQUIRED; 1 recuperação anterior documentada com hash e tamanho, mas não materializada no workspace do runner. O ledger não requisita páginas web.

A ingestão automatizada das páginas AGF depende de API/exportação oficial ou autorização específica, conforme as condições de uso identificadas. Não se contornam autenticação, paywalls, CAPTCHA ou restrições contratuais.

## Política de preservação

As 23 fontes do manifesto não são 23 ficheiros descarregáveis: há 1 PDF com URL direto de download e 22 páginas/referências HTML. Não marcar uma referência como preservada sem cópia efetiva, metadados e hash validados.

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
