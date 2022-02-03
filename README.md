# Python 3 - Avançando na Orientação a Objetos

Curso da Alura sobre Python 3 e Orientação a Objetos

## Objetivo Final &#x1F3AF;

Criar classes de Movie e Series para treinar outros conceitos de orientação a objetos

URL do curso -> [Python 3 - Avançando na Orientação a Objetos](https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos)

![Python 3 - Avançando na Orientação a Objetos](https://www.alura.com.br/assets/api/share/curso-python-3-avancando-orientacao-objetos.png)

## 01 - Relembrando Classes e Objetos &#x1F516;
* Criação da classe.
* Definição de métodos assessores.
* `@property`.
* `name`.

### 01 - Relembrando Classes e Objetos
* Definindo **Classes**.

### 02 - Adicionando Atributos e Métodos
* Adicionar o atributo **likes**.
* A função `capitalize()` transforma a primeira letra da *string* em **MAIÚSCULA**.

### 03 - Encapsulando Comportamento
* Usar o `@property` para não quebrar o código do usuário.

## 02 - Resolvendo Duplicação com Herança &#x1F516;
* Herança.
* Generalização/especialização.
* Método `super()`.

### 01 - Removendo Duplicação
* Atribuir os atributos em comum nas classes `Movie` e `Series` para a classe `Program`.
* Usar o `(MOTHER_CLASS)` logo após o nome da classe para declarar suas **classes mãe**.
* Ao fazermos uso dos dois *underscores*, deixamos o atributo privado. Na realidade, o que acontece é que com isso `__` será transformado em uma outra variável, e esta ação recebe o nome de ***name mangling***.

### 02 - Reutilizando Ainda Mais
* Usar o construtor da classe mãe usando `super().__init__(PARAMETERS)`.

### 03 - Explicando a Herança
* Ao utilizar herança, obtemos as seguintes vantagens:
    * **Reutilização de informações da classe mãe**: As classes filhas herdam todos os métodos e atributos, assim é possível reaproveitar o código feito pela classe mãe.
    * **Extender a classe mãe**: Por exemplo o `__init__` das classes filhas e a possível utilização do `__init__` da classe mãe para algo mais genérico ou específico.
* Ao criar uma função nas classes filhas, essa função só será visível para a classe filha.

## 03 - Reduzindo ifs com Polimorfismo &#x1F516;
* Polimorfismo.
* Relacionamento **é um**.
* Representação textual de um objeto.

### 01 - Polimorfismo
* Em **Herança**, as classes filhas **são** a classe mãe, isso se chama **polimorfismo**.
* A função `hasattr(OBJECT, ATTRIBUTE_NAME)` verifica se o atributo existe em uma variável.
* Criar `if` de uma linha usando `VARIABLE = (FUNCTION_IF_CONDITION_IS_TRUE) if (CONDITION) else (FUNCTION_IF_CONDITION_IS_FALSE)`.

### 02 - Reduzindo ifs
* Uma **classe coesa** é a classe que sabe qual a sua responsabilidade, e quando ela não faz mais do que ela deve fazer.
* O `str(VARIABLE)` pode chamar o método interno de uma variável que não seja uma **string** para representar a variável de forma textual.

### 03 - Representação Textual de Objetos
* Um método especial tem o apelido de ***dunder***, por causa do **D**ouble **Under**score, que são métodos como o `__init__` e o `__str__` na classe.
* O `def __str__(self):` retorna uma representação em formato de *str* de um objeto.