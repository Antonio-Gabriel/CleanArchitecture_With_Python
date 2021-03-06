# Definição de tipos e interfaces no python.

Este artigo foi escrito com base em alguns recursos que fui explorando dentro da linguagem python, alguns conceitos que por convenção não nos é disponibilizado pelo python mas eu
sentia a necessidade de usar devido alguns pontos que considero que me gerariam problemas
futuros caso eu venha trabalhar com mais elementos no meu team.

O grande barato da história é que eu olhava no que o superset do javascript(Typescript)
dava como poderes a ele e eu pensei não em criar um superset como o typescript mas sim
trazer um pouco dessa realidade para o python desde a criação de tipos até as interfaces porém
manter a segregação propriamente dita das mesmas.

## Problematica identificada.

Quis criar um método que como parametro recebia apenas valores que eu defini, obvio que seria especificar todos os parâmetros que eu gostaria de utilizar e sair codando.

Mas surge um outro ponto.

Estava a trabalhar com inversão de dependência e em momento algum quis deixar todos os parâmetros em uma determinada classe.

**Exemplo que que havia feito**:

```python

def save(name: str, email: str, phone: int, code: str):
    # ... code
    return {
        "name"  : name,
        "email" : email,
        "phone" : phone,
        "code"  : code
    }    

response = save("António Gabriel", "antoniocamposgabriel@gmail.com", 998987884, "00893CDF")
print(response)

# Response
# {'name': 'António Gabriel', 'email': 'antoniocamposgabriel@gmail.com', 'phone': 998987884, 'code': '00893CDF'}

```

Funcionaria muito bem e sem nenhum problemas mas eu precisava implementar um DTO para fazer transferência de dados e fazer com que seja forçado os tipos de dados na aplicação.

Algumas pesquisas onde encontrei o namedtuple, dataclasses, attr entre outros decidi explorar cada um dele. Testei e testei, no final das contas o dataclasses acabou por me resolver melhor que todos os outros recursos.

Fiz alguns testes e obtive esse resultado:

```python

from dataclasses import dataclass
from typing import Type

@dataclass(frozen=True)
class IPersonRequestDTO:
    name  : str
    email : str 
    phone : int 
    code  : str
    

def save(person_request: Type[IPersonRequestDTO]):
    return {
        "name"  : person_request.name,
        "email" : person_request.email,
        "phone" : person_request.phone,
        "code"  : person_request.code,
    }

response = save(IPersonRequestDTO(
        name="John", 
        email="john@example.com", 
        phone=978989876, 
        code="00893CDF"
        )
    )
print(response)

# Response
# {'name': 'John', 'email': 'john@example.com', 'phone': 978989876, 'code': '00893CDF'}
```

Basicamente também funcionaria, e já não dependeria mais dos parâmetros directamente inseridos na função ou método mas sim de um objecto ou um DTO.

Mas ainda assim eu poderia muito bem passar uma string no lugar do phone e ele funcionaria normalmente e a ideia nunca foi essa, seria também ter uma tipagem forte e fazer com que seja implementado apenas dados que correspondem aos seus tipos.

**Estava assim**:

```python
response = save(IPersonRequestDTO(
        name="John", 
        email="john@example.com", 
        phone="978989876", 
        code="00893CDF"
        )
    )
print(response)

# Response
# {'name': 'John', 'email': 'john@example.com', 'phone': '978989876', 'code': '00893CDF'}
```

A partir dessa situação fui fazendo algumas pesquisas e descobri que tinha sim como implementar algumas verificaçõas usando o `isistance(obj)` que é uma função nativa do python e aí pensei.

Que tal criar uma função que me facilitaria nessa resolução?.
Daí criei a seguinte função.

```python

from dataclasses import dataclass, fields
from typing import Type

@dataclass(frozen=True)
class IPersonRequestDTO:
    name  : str
    email : str 
    phone : int 
    code  : str
    
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be {field.type}, got {repr(value)}"
                )

def save(person_request: Type[IPersonRequestDTO]):
    return {
        "name"  : person_request.name,
        "email" : person_request.email,
        "phone" : person_request.phone,
        "code"  : person_request.code,
    }

response = save(IPersonRequestDTO(
        name="John", 
        email="john@example.com", 
        phone="978989876", 
        code="00893CDF"
        )
    )
print(response)

# Response
# raise ValueError
# ValueError: Expected phone to be <class 'int'>, got '978989876'

```

Agora assim consegui atingir o objectivo esperado.
Foi bom ter descoberto essa possibilidade e tornar mais fácil a implementação em nossos apps.

No meio do percurso surgiu mais um outro probleminha aonde quis criar uma validator para verificar se os dados que estou inserindo não estão vazios.

E tente advinhar?... 

Deu sim um erro porque o DTO não era iterable.
Logo tinha que pensar em uma outra estratégia para conseguir solicionar devidamente essa problemática, foi aí onde pensei em criar uma validação a nível dos meus DTO e ver qual seria o resultado.

No entanto consegui um bom resultado.

Apresentarei agora o antes e depois.


**Antes**:

``` python

from dataclasses import dataclass, fields
from typing import Type

@dataclass(frozen=False, init=True)
class IPersonRequestDTO:
    name: str
    email: int

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be {field.type}, got {repr(value)}"
                    )


def save(person_request: Type[IPersonRequestDTO]):   

    for attrib in person_request:
        print(attrib)


save(IPersonRequestDTO(name="Ag", email=0))

# Response
# TypeError: 'IPersonRequestDTO' object is not iterable
```

Na realidade quis percorrer todos os attributos e validar apenas se estiver vazio os dados
inseridos pelo DTO.

Pensei mais um pouquinho e encontrei uma solução ainda melhor que seria implementar essa regra
a nível do meu DTO.

Daí consegui encontrar o seguinte resultado

**Depois**:

``` python

from dataclasses import dataclass, fields
from typing import Type

@dataclass(frozen=False, init=True)
class IPersonRequestDTO:
    name: str
    email: int

    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type):
                raise ValueError(
                    f"Expected {field.name} to be {field.type}, got {repr(value)}"
                    )

        self.__required_args()


    def __required_args(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if value == "" or None:
                raise TypeError(
                    f"Value {field.name} is required"
                    )


def save(person_request: Type[IPersonRequestDTO]):   
    print(person_request)


save(IPersonRequestDTO(name="Ag", email=""))

# Response
# ValueError: Expected email to be <class 'int'>, got ''
```

Agora sempre que eu errar ao passar os dados como parâmetro vai automaticamente ser lançado uma exceção apresentando a coluna e o erro.


Mais uma vez consegui chegar ao que eu pretendia.