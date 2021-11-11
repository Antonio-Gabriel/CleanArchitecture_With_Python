# Learning about the clean architecture

# Architecture -> What is?

A arquitetura de software de um sistema consiste na definição dos componentes de software, suas propriedades externas, e seus relacionamentos com outros softwares.

Ao longo dos anos, diferentes conceitos de arquitetura de software são idealizados, mas todos tem um ponto em comum conhecido como SoC (Separation of Concerns).

Em tradução livre a “Separação de Conceitos” é um princípio de design que tende a separar um software em seções distintas.

Aplicado na ciência da computação, isso significa que em um código, cada conjunto de informações ou seção deve se tratar de um assunto separado de forma clara.

Em outras palavras, nessa estrutura de projeto os ativos são separados em camadas que ajudam a poupar o desenvolvedor de muitos problemas de manutenção futuros.

Isso porque a Clean Code estabelece uma regra de dependência bem aplicada que deixa qualquer sistema completamente testável e passível de otimizações.

Com isso, quando um framework, um banco de dados, ou uma API se tornar obsoleta a substituição de uma camada não será um problema garantir a integridade do projeto.

# Vantagens e desvantagens

Sobre as vantagens de se utilizar uma filosofia de arquitetura de código em camadas, podemos citar algumas como:
 

## Arquitetura de software testável
Por ser dividida em camadas, as regras de negócio podem ser testadas sem interferir na interface do usuário, banco de dados, servidor ou qualquer outro elemento externo.

## Arquitetura de software independente da interface do usuário
Assim como as regras de negócio podem ser testadas sem interferir em nenhum outro componente do sistema, a interface também pode ser alterada com facilidade. Uma UI da Web pode ser substituída por uma UI do console, por exemplo, sem alterar as regras de negócio.

## Arquitetura de software independente de banco de dados
Como as camadas do projeto operam de forma independente, as regras de negócio também podem não ter vínculo com o banco dados do sistema. Com isso, é possível trocar o Oracle ou SQL Server, por Mongo, BigTable, CouchDB ou qualquer outro.

## Arquitetura de software independente de qualquer agente externo 
Na verdade, suas regras de negócios simplesmente não sabem nada sobre o mundo exterior, não estão ligadas a nenhum Framework.


# Clicle of clean architecture and concepts.

**Entities**: Responsáveis por concentrar os principais participantes das regras de negócio.
_Aplicam regras que geralmente fazem parte apenas da entidade,
_Sem vinculo com frameworks (ORM)

**UseCases**: Realizam a orquestração das entidades da concepção das regras de negócio.
_Representa as regras de negócios,
_Lançam exceções de negócio.

**Interface Adapter**: fazem a tradução entre o mundo externo e as regras de negócios.
_Fazem intercâmbio de dados entre base de dados, interface gráfica e outros serviços
utilizados pela aplicação.
_Definem interfaces de modo que uma ou mais implementações podem existir.

**Frameworks and Drivers**: São os recursos não funcionais, como base de dados entre outros.

`As camadas da clean architecture são lógicas`, não tem relação física, ou seja, com as pastas
que devem ser criadas.