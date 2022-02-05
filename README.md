# Python 3 - Avançando na Orientação a Objetos

Curso da Alura sobre Python 3 e Orientação a Objetos

## Objetivo Final &#x1F3AF;

Criar classes de Movie e Series para treinar outros conceitos de orientação a objetos

URL do curso -> [Python 3 - Avançando na Orientação a Objetos](https://cursos.alura.com.br/course/python-3-avancando-orientacao-objetos)

![Python 3 - Avançando na Orientação a Objetos](https://www.alura.com.br/assets/api/share/curso-python-3-avancando-orientacao-objetos.png)

## Siglas &#x1F5FA;
* **ABC** - **A**bstract **B**ase **C**lasses.

## Atalhos &#x2328;
* Re-ordenar linhas no Pycharm:
    * 1º: Segurar ***CTRL** + ***SHIFT*** + ***ARROW_UP***/***ARROW_DOWN***.
* Duplicar linha no Pycharm:
    * 1º: Apertar ***CTRL*** + ***D*** na linha que deseja duplicar.

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
* Os **attributos privados** da classe mãe **NÃO SÃO PASSADOS** por herança para a classe filha.
* Convenção de somente usar 1 `_` antes do nome do atributo para evitar confusões com **herança** e seus **atributos**.

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

## 04 - Quando não Usar Herança &#x1F516;
* Herança de um tipo *built-in* (nativo).
* Vantagens da herança de um iterável.
* Desvantagem de fazer herança.

### 01 - Criando a Playlist
* A função `len(LIST)` retorna o tamanho de uma **lista**.
* É conhecido como **encapsulamento**, o desconhecimento de toda a estrutura interna de um objeto, deixando para fora apenas o que se quer que interaja com o mundo externo.

### 02 - Reaproveitando um List
* `VARIABLE_NAME in OBJECT` para verificar se um objeto está contido dentro de outro objeto que seja uma **lista**.
* A palavra **in** no `for x in y` espera um **iterável**, já que ele itera sobre uma listagem qualquer.
* Um ***sizeable*** é um objeto que **consegue informar seu próprio tamanho**.

### 03 - Fugindo da Complexidade
* Retirar herança da classe **list** para reduzir a complexidade do código.

## 05 - Duck Typing e um Modelo de Dados &#x1F516;
* *Duck typing*.
* *Python data (object) model*.
* *Dunder methods*.
* Uso de ABCs.

### 01 - Se anda como um Pato
* Para dizer para o **Python** que a classe é um **iterável**, usamos o `def __getitem__(self, item)`.
* A **herança** é uma boa ideia para implementar nos casos de:
    * **Interface**, quando queremos resolver questões relativas a polimorfismo.
    * **Reuso** do código, ou remoção de duplicações.
* A **Herança** é uma **extensão** e a frase chave para a sua definição é "***é um***", ou seja, se pega todo o código da super classe e transmite para a classe filha todos os seus comportamentos.
* Ao usar **composição**, a sua frase chave é "***tem um***", ou seja, se pode ter uma lista interna dentro da classe, sem extender a classe `list`.
* O ***duck typing*** é uma maneira de se dizer que uma classe só precisa implementar um método específico da outra classe, sem extende-la totalmente.

### 02 - Modelo de Dados Python
* Para dizer que uma classe tem tamanho, usamos o `def __len__(self)`.
* No ***Python Data Model***, todo objeto em Python pode se comportar de forma a ser compatível e mais próximo à linguagem, e de toda a ideia idiomática dela, as principais dela são:
    * **Inicialização**: `__init__`.
    * **Representação**: `__str__`, `__repr__`.
    * **Container, sequência**: `__contains__`, `__iter__`, `__len__`, `__getitem__`.
    * **Numéricos**: `__add__`, `__sub__`, `__mul__`, `__mod__`.

    Seu funcionamento é respectivo à:
    * **Inicialização**: `obj = New()`.
    * **Representação**: `print(obj)`, `str(obj)`, `repr(obj)`.
    * **Container, sequência**: `item in obj`, `for i in obj`, `len(obj)`, `obj[2, 3]`.
    * **Numéricos**: `obj + other_obj`, `obj * other_obj`.
* No **Python**, existe a ideia de **protocolo**. Isto quer dizer que nosso objeto precisa se comportar daquele modo específico, sendo necessária a implementação de métodos que comportem segundo um protocolo específico.

### 03 - Classes Abstratas ou ABCs
* A classe `ABC` do **Python** é uma biblioteca de classes abstratas que define métodos que as classes mãe implementam, e toda sub-classe dessa classe mãe deve implementar esses métodos.

## 06 - Herança Múltipla &#x1F516;
* Herança múltipla.
* Resolução da ordem de chamada de métodos.
* *Mixins*.

### 01 - Mais de uma Classe Mãe
* Para usar **Herança Múltipla**, usamos `class CLASS_NAME(1_CLASS, 2_CLASS)`.

### 02 - Resolução de Métodos
* Para escolher o método que será executado na herança múltipla, ele primeiro procura na **classe atual**, depois ele procura na **1ª classe mãe**, em seguida para as classes mãe das classes mãe.

### 03 - Mixins
* Para fazer uma classe herdar um comportamento mas sem poluir as sub-classes, usa-se o **Mixin**.