# design-patterns-study - RESUMO

## Links

DESIGN PATTERS
+ https://www.opus-software.com.br/design-patterns/
+ https://github.com/kamranahmedse/design-patterns-for-humans

SOLID
+ https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530

CLEAN CODE
+ https://medium.com/desenvolvendo-com-paixao/2-clean-code-boas-pr%C3%A1ticas-para-escrever-c%C3%B3digos-impec%C3%A1veis-361997b3c8b5

## Design Patters

Criado pelo GoF do livro “Design Patterns: Elements of Reusable Object-Oriented Software”

**Creational Design Patterns**

+ Abstract Factory
+ Builder
+ Factory Method
+ Prototype
+ Singleton

**Structural Design Patterns**

+ Adapter
+ Bridge
+ Composite
+ Decorator
+ Façade
+ Flyweight
+ Proxy

**Behavioral Patterns**

+ Chain of Responsibility
+ Command
+ Interpreter
+ Iterator
+ Mediator
+ Memento
+ Observer
+ State
+ Strategy
+ Template Method
+ Visitor

## SOLID Principle

Esses princípios ajudam o programador a escrever códigos mais limpos, separando responsabilidades, diminuindo acoplamentos, facilitando na refatoração e estimulando o reaproveitamento do código.

**S — Single Responsiblity Principle**
+  (Princípio da responsabilidade única)
+ Em suma: evitar um GOdCLass, ou seja, uma classe que faça tudo

**O — Open-Closed Principle**
+ (Princípio Aberto-Fechado)
+ O que dá de errado se nâo for seguido:
  - Alterar uma classe já existente para adicionar um novo comportamento, corremos um sério risco de introduzir bugs em algo que já estava funcionando.
+ Soluçâo:
  - Separe o comportamento extensível por trás de uma interface e inverta as dependências.
+ Em suma: Se, para fazer um procedimento, voce tenha que verificar qual é o tipo da classe e com isso mudar o comporatemtneo, ao invez de fazr isso, voce deve usar INTERFACE para realizar esse procedimento. Asism, se uma nova classe for adiciconada, voce nao precisa mais fazer um novo IF, pois já estará usando um método da interface que é igal para todos
+ Esse principio é a base do padrao de projeto Strategy

**L — Liskov Substitution Principle**
+ (Princípio da substituição de Liskov) - Uma classe derivada deve ser substituível por sua classe base.
+ Seguir o LSP nos permite usar o polimorfismo com mais confiança. Podemos chamar nossas classes derivadas referindo-se à sua classe base sem preocupações com resultados inesperados.

**I — Interface Segregation Principle**
+ (Princípio da Segregação da Interface)
+ Uma classe não deve ser forçada a implementar interfaces e métodos que não irão utilizar.Esse princípio basicamente diz que é melhor criar interfaces mais específicas ao invés de termos uma única interface genérica
+ Em suma: Nâo crie interface genericas, apenas especificas, é melhor ter 3 intrfaces especificas do que 1 generica

**D — Dependency Inversion Principle**
+ (Princípio da inversão da dependência)
+  Dependa de abstrações e não de implementações.
+ OBS: Inversão de Dependência não é igual a Injeção de Dependência, fique ciente disso! A Inversão de Dependência é um princípio (Conceito) e a Injeção de Dependência é um padrão de projeto (Design Pattern)
+ Em suma: AO invez de criar um objeto dentro de um metodo de uma clase é melhor realizar duas coisa
  - Passar esse objeto que seria criado dentro por parametro
  - Esse objeto ser uma interface obrigatoriamente

## Clean Code

+ Use SEMPRE Nomes que façam sentido (em ingels)
  - ao inves de `for p in persons` use `for person i persons`
+ Use nomes passíveis de busca
  - ou seja, nada de `e` para error, pois se voce der um CTRL +F por 'e' vaia char em todo lugar
+ Não use numeros magicos
  - Se voce tem uma constante, é emlhor por elea numa variavel em que seu nome revele sua inençao do que jogar do nada o valor no codigo. Isso melhora a leitura do código
+ eviete fazer if que comece com not
+ encapsule condicinais
  - Ao invez de `var == 'x'` dê preferencia a chamar um método, isso deixa essa expressão boleana mais intercambeável no código.
+ Evite funçâo com flag
  - Se uma funçâo tem dois comportamentos distintos a depedner de um único valro,  entao é melhor separa em das funções
