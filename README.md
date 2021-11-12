# Arquitetura limpa

Aplicação denominada `Registro de funcionário` (Employee Register)

Modelando uma aplicação minimalista usando os conceitos de clean architecture, solid
em uma aplicação de modo a solidificar os conhecimentos.

## Overview 

Basicamente a aplicação vai registrar um funcionário, e sua localização, para tal estaremos 
utilizando a clean architecture como guia de estudo.

### Entidades

Funcionário
: Id
: Nome
: Email
: Phone

Localização
: Bairro
: Rua
: Cidade

Sabendo que `funcionário` agrega `localização`

### ou

| Funcionário | Localização |
| :---        |    :----:   |
| Id          | Bairro      |
| Nome        | Rua         | 
| Email       | Cidade      |
| Phone       |             |

## Funcionalidades

- [x] Registrar usuário e sua localização
- [x] Apresentar os usuários e as suas localização
- [ ] Remover usuário pelo identificador