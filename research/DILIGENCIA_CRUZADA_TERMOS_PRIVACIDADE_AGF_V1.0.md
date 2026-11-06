# Diligência cruzada — Termos do site, Termos do App e Política de Privacidade

**Data da análise:** 2026-11-06  
**Objetivo:** comparar documentos oficiais públicos e registrar diferenças que impactam a pesquisa documental HAGF.  
**Natureza:** análise documental, não parecer jurídico.

## 1. Documentos comparados

| Documento | Versão/data indicada | URL |
|---|---|---|
| Política de Privacidade AGF Geral | Outubro/2025 | https://lp.agf.com.br/hubfs/Politica-de-Privacidade/Politica-de-Privacidade-AGF-Geral-rev-final-03-12.pdf |
| Termos e Condições de Uso do Site | Dezembro/2025 | https://lp.agf.com.br/termos-e-condicoes-de-uso |
| Termos de Uso do App | Agosto/2024 | https://agfmais.s3.us-east-2.amazonaws.com/termo_de_uso.html |

## 2. Identidade jurídica

Os três documentos identificam a AGF Soluções Digitais Ltda., CNPJ 33.726.252/0001-51, como entidade proprietária/operadora ou controladora da plataforma/site, conforme o contexto de cada texto.

Os Termos do Site também listam no rodapé:
- AGF Gestão e Consultoria de Investimentos Ltda. — CNPJ 50.639.255/0001-77;
- AGF Educacional Ltda. — CNPJ 50.641.126/0001-13;
- AGF Soluções Digitais Ltda. — CNPJ 33.726.252/0001-51.

**Ponto de diligência:** a presença de três entidades no rodapé não permite, isoladamente, concluir a função regulatória, contratual ou operacional de cada uma. O HAGF deve manter cadastro societário separado, baseado em documentos oficiais específicos.

## 3. Encarregado/DPO e canais de contato

Há diferença entre os canais publicados:

- Política de Privacidade de outubro/2025: `privacidade@acoesgarantem.com.br`.
- Termos do Site de dezembro/2025: identifica Diego Ferreira como DPO e publica `diego.ferreira@acoesgarantem.com.br`.
- Termos do Site também publica `suporte@acoesgarantem.com.br` como canal de suporte.

**Interpretação prudente:** são documentos com datas e escopos diferentes. Não assumir automaticamente que um canal substituiu o outro. Registrar ambos, com a fonte e a data, e verificar qual canal é atualmente indicado para cada tipo de solicitação.

## 4. Bases legais e finalidades

A Política de Privacidade de outubro/2025 menciona execução de contrato, obrigação legal, legítimo interesse e consentimento, mas não apresenta no trecho consultado uma tabela que relacione cada finalidade e categoria de dados à sua base legal.

Os Termos do Site de dezembro/2025 apresentam tabela explícita:
- dados de navegação (IP, localização aproximada, páginas acessadas): legítimo interesse;
- dados cadastrais: execução de contrato;
- dados de pagamento: execução de contrato;
- cookies promocionais/marketing: consentimento;
- dados exigidos por lei: obrigação legal.

**Ponto de diligência:** a tabela dos Termos do Site é mais granular, mas não se deve presumir que ela substitua integralmente a Política de Privacidade ou cubra todos os tratamentos descritos no App. Exigir correspondência por finalidade, dado, sistema e entidade antes de qualquer conclusão jurídica.

## 5. Restrições de automação, scraping e reprodução

### 5.1 Termos do Site — dezembro/2025

As cláusulas 5.3 e 6.4 vedam mineração de dados, scraping e uso de ferramentas automatizadas, spiders ou bots sem autorização expressa/prévia. As cláusulas 5.1–5.2 também afirmam a proteção autoral e reserva de direitos sobre conteúdo do site.

### 5.2 Termos do App — agosto/2024

Os Termos do App descrevem conteúdos gratuitos e conteúdos exclusivos vinculados a planos de assinatura. Também contêm restrições de extração de dados, coleta de informações de outros usuários, uso de robôs/crawlers/spiders/data mining e reprodução/captura de telas ou conteúdo da plataforma.

### 5.3 Decisão operacional do HAGF

- Consulta humana de páginas públicas e leitura de documentos publicamente oferecidos: manter como pesquisa documental pontual.
- Download pontual de arquivo que a própria página disponibiliza diretamente ao público: registrar URL, origem, data, hash e finalidade, sem redistribuição automática.
- Crawler, spider, scraping, enumeração de endpoints ou coleta automatizada em lote nos domínios AGF: **não executar nesta fase**.
- Conteúdo autenticado, pago, de comunidade ou dados de outros usuários: fora do escopo.
- Reproduzir integralmente cursos, aulas, relatórios ou materiais protegidos: fora do escopo.

Esta decisão é uma medida de governança do projeto diante do texto contratual publicado; não constitui parecer sobre validade ou alcance jurídico de cada cláusula.

## 6. Integração B3

A Política de Privacidade de outubro/2025 declara que informações integradas ao Portal do Investidor B3 podem ser coletadas mediante solicitação expressa do usuário.

Os Termos do App descrevem a plataforma como fonte de informações e análises para apoiar decisões de investimento, mas não especificam o mecanismo técnico da integração B3.

**Não documentado:** API, autenticação, consentimento técnico, escopo de dados, periodicidade, fornecedor, tratamento de falhas, trilha de auditoria e formato de exportação.

## 7. Produtos, conteúdo e direitos

Os Termos do App diferenciam conteúdo gratuito de conteúdo exclusivo de assinantes. O documento também afirma que conteúdo e materiais da plataforma são protegidos por propriedade intelectual e que o acesso não transfere direitos de uso ou exploração.

O HAGF deve trabalhar com:
- fatos e metadados;
- definições resumidas em linguagem própria;
- análise crítica autoral;
- referências, URLs, datas e hashes;
- citações breves estritamente necessárias.

Não armazenar nem republicar conteúdo de cursos ou relatórios fechados.

## 8. Implicações para o roadmap

1. Manter o coletor como ferramenta de validação e inventário, sem disparo automático de downloads em push.
2. Não executar crawling ou coleta automatizada em lote nos domínios AGF.
3. Para novos documentos, cadastrar cada URL direta após verificação individual.
4. Registrar versões de termos e políticas separadamente; não sobrescrever documentos históricos.
5. Construir matriz de entidades jurídicas, funções e fontes.
6. Investigar a integração B3 apenas com documentação pública e sem testar endpoints privados.
7. Manter os arquivos originais fora da distribuição pública do repositório quando não houver licença explícita de redistribuição.

## 9. Fontes primárias

- Política de Privacidade AGF Geral, atualização outubro/2025: https://lp.agf.com.br/hubfs/Politica-de-Privacidade/Politica-de-Privacidade-AGF-Geral-rev-final-03-12.pdf
- Termos e Condições de Uso do Site, atualização dezembro/2025: https://lp.agf.com.br/termos-e-condicoes-de-uso
- Termos de Uso do App, agosto/2024: https://agfmais.s3.us-east-2.amazonaws.com/termo_de_uso.html
