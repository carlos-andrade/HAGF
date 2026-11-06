# Análise documental — Política de Privacidade AGF (outubro/2025)

**Documento:** Política de Privacidade AGF Geral  
**Fonte oficial:** https://lp.agf.com.br/hubfs/Politica-de-Privacidade/Politica-de-Privacidade-AGF-Geral-rev-final-03-12.pdf  
**Versão declarada:** última atualização em outubro de 2025  
**Arquivo:** `Politica-de-Privacidade-AGF-Geral-rev-final-03-12.pdf`  
**Páginas:** 12  
**Tamanho:** 236.126 bytes  
**SHA-256:** `3eade497f8d95802deae454d921881465253c2f2c25039f649f65b0ce1b2d35c`  
**Status:** baixado pelo GitHub Actions, assinatura PDF 1.7 verificada e texto das 12 páginas extraído para análise.

## 1. Identificação e escopo

A política identifica como controladora a **AGF Soluções Digitais Ltda.**, CNPJ **33.726.252/0001-51**, com endereço indicado na Rua Líbero Badaró, 425, conjunto 171, Centro, São Paulo/SP. A AGF declara ser detentora da marca AGF e dos direitos a ela relacionados (p. 1).

O escopo declarado abrange o website, o aplicativo e o ambiente digital da plataforma AGF, incluindo cadastro, newsletter, navegação, serviços integrados e comunidade (pp. 1–2).

## 2. Fluxo de cadastro, pagamento e dados

A política descreve a Eduzz como ferramenta de divulgação, promoção e comercialização de produtos digitais. Após a confirmação do pagamento pela Eduzz, os dados do usuário são encaminhados à AGF por intermédio de um parceiro comercial; em seguida, o usuário cria conta e senha na plataforma AGF (p. 3).

Dados enumerados no documento:
- nome e sobrenome;
- e-mail;
- CPF;
- telefone;
- data de nascimento;
- nome de usuário na comunidade;
- dados sobre ativos financeiros e movimentações;
- informações integradas ao Portal do Investidor B3, mediante solicitação expressa do usuário;
- conteúdos publicados pelo usuário na comunidade (p. 3).

**Implicação para o projeto HAGF:** há evidência documental de que a plataforma contempla dados de carteira e integração com o Portal do Investidor B3 quando solicitada pelo próprio usuário. A política não descreve arquitetura, API, endpoints, protocolo, esquema de dados, periodicidade de sincronização ou fornecedor técnico dessa integração. Esses detalhes permanecem desconhecidos.

## 3. Dados de navegação e telemetria

A política prevê o uso de cookies, tags de pixel, log files e web beacons. O texto menciona histórico de navegação, data e hora de acesso, endereço IP, navegador, sistema operacional, páginas visitadas, URL, identificador único do dispositivo, rede, desempenho do computador, idioma, localização, termos de pesquisa e informações de cookies (pp. 4–6).

Também prevê uso dessas informações para:
- melhorar serviços e experiência do usuário;
- personalizar conteúdo;
- analisar tráfego e padrões demográficos;
- publicidade personalizada;
- diagnosticar problemas técnicos;
- monitorar eficácia de produtos e canais (pp. 5–7).

## 4. Finalidades e compartilhamento

As finalidades listadas incluem prestação dos serviços, gestão e intermediação de pagamentos, criação e autenticação de contas, atendimento, análise estatística, personalização, monitoramento, desenvolvimento de produtos, prevenção de fraude e comunicação de ofertas e novidades (pp. 6–7).

A política cita compartilhamento com afiliadas, prestadores de serviços, Eduzz, parceiro comercial, terceiros de publicidade e, quando solicitado pelo usuário, Portal do Investidor B3 (p. 7). O parceiro comercial é mencionado sem identificação nominal no trecho analisado.

O documento admite armazenamento em servidores ou bases de terceiros e declara que os dados podem ser armazenados em qualquer servidor e localidade (p. 9).

## 5. Direitos do titular e canal de privacidade

A política lista direitos como confirmação de tratamento, acesso, correção, anonimização, bloqueio, eliminação, portabilidade, revogação do consentimento e informação sobre entidades com as quais ocorre compartilhamento. O canal indicado é **privacidade@acoesgarantem.com.br** (p. 4 e p. 11).

A política identifica o canal como meio de atendimento a titulares e à ANPD (p. 11).

## 6. Segurança declarada

O documento declara uso de:
- autenticação dupla;
- inventário detalhado de acessos;
- controles de acesso por necessidade funcional;
- firewalls e SSL;
- camada mTLS para autenticação mútua entre cliente e servidor (p. 10).

**Limite probatório:** são declarações da própria política. O PDF não fornece evidência técnica independente, arquitetura, configuração, auditoria, certificação ou relatório de testes que permita verificar a implementação efetiva desses controles.

## 7. Observações críticas e lacunas documentais

As observações abaixo são pontos de diligência documental, não conclusões de ilegalidade.

1. **Bases legais e consentimento:** o documento usa linguagem ampla de autorização/consentimento em cláusulas como 1.4, 1.5 e 3.7.1, mas também enumera execução de contrato, obrigação legal, legítimo interesse e consentimento na cláusula 3.8 (pp. 2 e 7). A política não apresenta uma matriz detalhada que associe cada finalidade, categoria de dado e operação à respectiva base legal.
2. **Parceiro comercial não identificado:** o fluxo de cadastro e pagamento menciona parceiro comercial sem identificá-lo nominalmente no texto examinado (p. 3).
3. **Transferência e localização:** a cláusula 7.1 admite armazenamento em qualquer servidor e localidade, mas o documento não especifica países, mecanismos de transferência internacional ou salvaguardas por destino (p. 9).
4. **Retenção:** o documento descreve hipóteses de término e eliminação, mas não apresenta tabela com prazos concretos por categoria de dado (p. 9).
5. **Cookies e tecnologias similares:** são descritos tipos e finalidades, mas o PDF não apresenta inventário de cookies, duração, fornecedores, categorias ou configuração granular de preferências (pp. 4–6).
6. **Integração B3:** a existência da integração é declarada, mas não há documentação técnica sobre consentimento operacional, escopo de dados, autenticação, frequência, formato ou tratamento de falhas (p. 3).
7. **Numeração editorial:** a seção 7.4 aparece em duplicidade, primeiro para medidas de segurança e depois para responsabilidade do usuário por senha (pp. 9–10). É uma inconsistência editorial do documento.
8. **Fórmula e metodologia de investimentos:** a política de privacidade não documenta DPA, Preço Teto, YOC, MDI, BESST ou Fórmula AGF. Esses assuntos precisam de fontes específicas da Central de Ajuda ou materiais institucionais.

## 8. O que o HAGF pode afirmar com base neste PDF

- A entidade controladora declarada no documento é AGF Soluções Digitais Ltda.
- A plataforma declara tratar dados cadastrais, dados de carteira e conteúdos de comunidade.
- A integração com o Portal do Investidor B3 é prevista mediante solicitação expressa do usuário.
- A Eduzz e um parceiro comercial participam do fluxo descrito de cadastro/pagamento.
- A política declara uso de cookies, pixels, logs e web beacons.
- O canal de privacidade publicado é privacidade@acoesgarantem.com.br.
- O documento declara controles como autenticação dupla, inventário de acessos e mTLS.

## 9. O que NÃO se pode concluir

- Que a integração B3 utiliza uma API específica, scraping, Open Finance ou outro protocolo.
- Que a AGF recebe todos os dados da carteira ou todas as movimentações do usuário.
- Que os controles de segurança declarados foram auditados ou testados por terceiro.
- Que a política, por si só, demonstra conformidade integral com a LGPD.
- Que os dados são armazenados em um país específico.
- Que o parceiro comercial é determinada empresa, sem fonte adicional.

## 10. Próximas diligências

1. Localizar termos de uso do site e do aplicativo e comparar suas versões com esta política.
2. Localizar política de cookies e inventário de tecnologias efetivamente publicado.
3. Investigar, por fontes públicas, a integração com o Portal do Investidor B3, sem acessar contas de usuários nem endpoints privados.
4. Mapear a identificação jurídica das entidades do grupo e distinguir controlador, operador, fornecedor e parceiro comercial.
5. Continuar a pesquisa de PDFs e documentos diretamente oferecidos para download.
6. Construir matriz de evidências por finalidade, dado, base legal declarada, compartilhamento, retenção e fonte.

## 11. Proveniência e integridade

O arquivo foi recuperado em 2026-11-06T16:04:28Z pelo workflow `HAGF Public Recovery`, execução 6, run ID `42248916854`. O relatório do coletor registra 17 fontes, 1 download concluído e 16 fontes sem URL direta de arquivo.

SHA-256 do PDF: `3eade497f8d95802deae454d921881465253c2f2c25039f649f65b0ce1b2d35c`.

SHA-256 do relatório JSON de execução extraído do artefato: `c5e1739f9603c6e9e2598f89556286c411b8cc33d1913034a4d1da5a5289da3a`.

O arquivo original foi mantido no artefato do GitHub Actions. O HAGF registra neste relatório metadados, hash e síntese autoral; a publicação integral do PDF no repositório público não foi realizada.
