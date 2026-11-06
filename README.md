# HAGF — Pesquisa e inteligência sobre o ecossistema AGF

Repositório independente para pesquisa documental, mapeamento de fontes públicas e análise autoral do ecossistema Ações Garantem o Futuro (AGF), seus produtos, ferramentas, metodologia de dividendos e estrutura institucional.

## Objetivos

- Mapear fontes institucionais e documentais públicas da AGF.
- Registrar conceitos, indicadores e metodologia com proveniência.
- Separar fatos declarados pela AGF, evidências externas, inferências e lacunas.
- Construir uma base de conhecimento auditável para análises futuras.
- Respeitar direitos autorais, privacidade e controles de acesso.

## Estado atual

**Fase:** inventário documental público e recuperação controlada.

- Prompt de pesquisa: [Agente HAGF PhD](PROMPTS/PROMPT_AGENTE_HAGF_PHD_V1.0.md)
- Primeira execução: [Relatório inicial](research/EXECUCAO_INICIAL_AGF_2026-11-06_V1.0.md)
- Correção de escopo de dados públicos: [Nota de correção](research/NOTA_CORRECAO_ACESSO_DADOS_PUBLICOS_V1.0.md)
- Inventário atualizado: [Fontes públicas AGF V1.1](research/INVENTARIO_FONTES_PUBLICAS_AGF_2026-11-06_V1.1.md)
- Operação de recuperação: [Manual do coletor](docs/OPERACAO_COLETA_PUBLICA_V1.0.md)

## Coletor de documentos públicos

O coletor baixa somente arquivos com URLs diretas, cadastradas explicitamente no manifesto.

- Script: [scripts/hagf_public_recovery.py](scripts/hagf_public_recovery.py)
- Manifesto: [config/fontes_publicas.json](config/fontes_publicas.json)
- Testes: [tests/test_hagf_public_recovery.py](tests/test_hagf_public_recovery.py)
- Workflow: [HAGF Public Recovery](.github/workflows/hagf-public-recovery.yml)

O processo não rastreia páginas, não descobre links automaticamente, não acessa áreas autenticadas, não contorna paywalls ou CAPTCHAs e não coleta dados pessoais. Os arquivos baixados são registrados com SHA-256 e relatório JSON.

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
