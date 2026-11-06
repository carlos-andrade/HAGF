# SOLICITAÇÃO TÉCNICA — CANAL OFICIAL DE PRESERVAÇÃO DOCUMENTAL AUTOMATIZADA AGF

**Projeto solicitante:** HAGF — pesquisa documental independente  
**Responsável:** Carlos Andrade  
**Estado:** minuta para revisão; não enviada  
**Data:** 2026-11-06

## 1. Objetivo

Solicitar à AGF a indicação de um mecanismo oficial e autorizado para preservar, de forma automatizada e controlada, documentos e páginas públicas que já estão referenciados no inventário documental do projeto HAGF.

O objetivo é garantir integridade histórica, rastreabilidade de versões e citação correta das informações públicas. Não se pretende aceder a conteúdo reservado, áreas autenticadas, cursos, comunidades, dados de clientes ou informações pessoais.

## 2. Escopo inicial

O inventário atual contém 23 referências públicas, das quais:
- 1 documento PDF com URL direto, já recuperado em execução anterior;
- 22 referências a páginas institucionais, termos, artigos públicos, central de ajuda, blog e índice regulatório.

A lista exata de URLs está em config/fontes_publicas.json:
https://github.com/carlos-andrade/HAGF/blob/main/config/fontes_publicas.json

## 3. Mecanismo solicitado

A AGF pode indicar uma ou mais das seguintes opções:

1. API pública ou endpoint oficial de exportação documental;
2. feed RSS/Atom, sitemap ou índice de versões expressamente destinado à consulta automatizada;
3. exportação periódica dos documentos e artigos públicos em HTML, PDF, JSON ou ZIP;
4. autorização escrita para requisições automatizadas às URLs públicas do inventário.

Não se solicita acesso a endpoints privados nem a mecanismos internos não documentados.

## 4. Parâmetros técnicos propostos

Caso a AGF autorize requisições automatizadas, propomos:

- User-Agent identificável: HAGF-Document-Preservation/1.0;
- concorrência máxima: 1 requisição simultânea;
- intervalo mínimo entre requisições: 10 segundos;
- execução agendada máxima: uma vez por semana;
- respeito integral a limites de taxa e instruções comunicadas pela AGF;
- utilização de ETag e Last-Modified, se suportados, para evitar transferências desnecessárias;
- download apenas de URLs e formatos expressamente abrangidos pela autorização;
- limite de tamanho configurável e validação de MIME/assinatura;
- cálculo SHA-256, timestamp UTC e histórico imutável de versões;
- interrupção imediata diante de HTTP 401, 403, 429, CAPTCHA, bloqueio ou indicação de revogação;
- ausência de autenticação, bypass de paywall, scraping de áreas restritas ou recolha de dados pessoais.

## 5. Uso e distribuição

O material será utilizado para:
- preservação e consulta interna;
- investigação documental e comparação de versões;
- elaboração de análises autorais;
- referência bibliográfica e citação pontual.

Não se pretende republicar integralmente materiais protegidos, revender documentos, disponibilizar cópias públicas ou sugerir afiliação/endosso da AGF. Qualquer redistribuição dependerá de licença ou autorização específica.

## 6. Confirmações solicitadas

Solicitamos que a AGF esclareça:

1. Qual canal oficial recomenda para arquivo automatizado de páginas e documentos públicos?
2. A autorização pode abranger as URLs já enumeradas no manifesto HAGF?
3. Quais limites de frequência, concorrência, tamanho e formatos devem ser respeitados?
4. É permitido conservar cópias integrais para arquivo privado e investigação documental?
5. Existe política de retenção ou prazo após o qual as cópias devem ser eliminadas?
6. Qual contacto técnico e/ou responsável de privacidade deve acompanhar a solicitação?

## 7. Contacto e referência

O pedido deverá ser encaminhado ao canal institucional indicado pela AGF para assuntos técnicos e/ou ao Encarregado de Proteção de Dados, conforme os contactos oficiais vigentes.

Esta minuta não foi enviada. O envio depende de revisão e aprovação do responsável pelo projeto.

## 8. Repositório e transparência

O projeto mantém o inventário, a política de ingestão, os scripts de validação e os registos de execução no repositório HAGF. A autorização eventualmente concedida será arquivada com data, escopo, condições e validade, e aplicada tecnicamente antes de ativar qualquer adaptador de captura.
