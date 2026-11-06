# Impacto da integração B3 do App AGF na qualidade dos dados

**Versão:** 1.0  
**Data:** 2026-11-06  
**Base:** Central de Ajuda AGF e artigo institucional de 13/12/2024.  
**Objetivo:** transformar limitações declaradas pela AGF em regras de validação para a base HAGF.

## 1. Achado principal

A AGF informa que a sincronização com a B3 considera o histórico disponível a partir de **novembro de 2019**. Para posições anteriores, pode ser criada uma compra de ajuste em **01/11/2019**, utilizando o preço de fechamento dessa data. A própria AGF esclarece que esse procedimento não representa o histórico completo de compras ou proventos anteriores.

Fonte: https://ajuda.agf.com.br/pt-BR/articles/16753937-minha-carteira-apresenta-divergencias-ou-operacoes-duplicadas-o-que-pode-causar-isso

## 2. Efeito sobre reconstrução histórica

Uma carteira sincronizada com o App AGF não deve ser tratada como livro de operações completo desde a primeira aquisição do investidor. O ajuste de 01/11/2019 é uma representação de posição inicial, não uma transação histórica real.

**Regra HAGF:** operações sintéticas de abertura devem receber tipo de evento próprio, por exemplo `INITIAL_POSITION_ADJUSTMENT`, e não ser misturadas com compras executadas em mercado.

## 3. Taxas de corretagem

A AGF informa que os dados recebidos pela integração B3 não consideram taxas de corretagem. Em contrapartida, a importação por nota de corretagem pode distribuir os custos entre os ativos.

**Regra HAGF:** manter custo bruto de aquisição, taxas/custos e custo total em campos separados. Não preencher taxa ausente com zero; utilizar nulo e indicador de completude.

## 4. Eventos societários e ajustes

A AGF cita bonificações, desdobramentos, grupamentos e subscrições como eventos que podem alterar quantidade, valor unitário ou preço médio. Também informa que um lançamento chamado “Ajuste” pode ser criado para alinhar a posição aos dados importados.

**Regra HAGF:** eventos societários devem ser registrados como eventos explícitos, com data, tipo, fator/quantidade, origem e efeito sobre custo. Lançamentos de ajuste devem ser preservados com sua proveniência e nunca apagados apenas para fazer o saldo coincidir.

## 5. Implicações para indicadores

| Indicador | Risco de qualidade | Controle HAGF |
|---|---|---|
| Preço médio | Taxas ausentes ou histórico inicial sintético | Calcular nível de completude e origem do custo |
| Retorno total | Histórico incompleto pré-nov/2019 | Não publicar CAGR histórico sem ressalva |
| YOC | Base de custo pode não conter taxas | Exibir YOC bruto e, se possível, YOC sobre custo total |
| Proventos acumulados | Eventos anteriores a nov/2019 ausentes | Não presumir série integral |
| Quantidade atual | Eventos societários e ajustes | Reconciliação de posição por evento |
| Rentabilidade por ativo | Dados mistos de B3, notas e ajustes | Priorizar trilha de proveniência por lançamento |

## 6. Hierarquia de fontes recomendada

1. Notas de corretagem e documentos originais de negociação, quando disponíveis.
2. Extratos oficiais e eventos corporativos da B3/emissor.
3. Dados sincronizados da carteira AGF, com limites de cobertura conhecidos.
4. Ajustes manuais/sintéticos, sempre identificados como tal.

Essa hierarquia é uma regra de engenharia de dados do HAGF, não uma declaração da AGF.

## 7. Diferença entre material atual e histórico

Um artigo institucional publicado em 13/12/2024 descreve o processo de sincronização pelo app e afirma que a atualização costuma ocorrer rapidamente, embora mencione prazo oficial de até 24 horas. Esse texto é material histórico. Para limites de cobertura, divergências e taxas, priorizar a Central de Ajuda atualizada.

Artigo institucional: https://institucional.acoesgarantem.com.br/blog/aplicativo-agf-conheca-todas-as-facilidades-e-funcionalidades-do-app/

## 8. Critérios de aceitação para dados importados

Um registro importado só pode ser classificado como histórico íntegro quando:
- a data e a origem da operação são identificáveis;
- não é um ajuste de abertura sintético;
- custos e taxas estão documentados ou marcados como ausentes;
- eventos societários foram reconciliados;
- quantidade e preço médio fecham com o extrato de referência;
- a série temporal possui cobertura explícita.

## 9. Conclusão

A sincronização B3 do App AGF é útil para acompanhamento de carteira, mas a própria documentação da AGF identifica limitações relevantes para reconstrução histórica e custo de aquisição. O HAGF deve tratar a integração como uma fonte com cobertura e completude conhecidas, nunca como verdade transacional integral sem reconciliação.
