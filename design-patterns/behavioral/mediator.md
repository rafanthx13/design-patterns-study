# Mediator

É como um controlador de tráfego aéreo, voce centraliza a comunicação entre os objetos num lugar só, e gerencia o tráfego.

## Links

https://refactoring.guru/pt-br/design-patterns/mediator
https://github.com/kamranahmedse/design-patterns-for-humans#-mediator
https://pt.wikipedia.org/wiki/Mediator

## Meu Resumo

## Wikipedia

**Definição**
É um padrão de projeto usado frequentemente quando deseja-se encapsular como os objetos interagem, ou seja, a comunicação entre os objetos é estabelecida através do Mediator. Este padrão é considerado um padrão comportamental, pois o padrão pode alterar o comportamento da aplicação (programa).O Mediator promove o fraco acoplamento ao evitar que objetos se referiram uns aos outros explicitamente.

**Participantes**
Mediator: responsável por definir a interface para a comunicação entre os objetos Colegas.

MediatorConcreto: responsável por implementar a interface Mediator e consequentemente gerenciar a comunicação entre os objetos Colegas.

ColegaConcreto: Objeto que se comunicará com outros objetos Colegas através do Mediator.

**Quando usar**
Um conjunto de objetos se comunicam de maneira bem definida, porém complexas o que dificulta o entendimento.

Quando um objeto é difícil de ser reutilizado pois ele se referencia e se comunica com muitos outros objetos.

Quando um comportamento está distribuído entre diversas classes que deveria ser customizável, evitando a especialização em subclasses.

**Vantagens do padrão Mediator**

Diminuí consideravelmente o acoplamento (entre os Colegas) e consequentemente aumenta o reuso.

Ocorre a eliminação de relacionamentos muitos para muitos (N para N)

A política de comunicações fica centralizada no Mediator, logo, podemos alterar essa política sem precisar alterar os Colegas.

**Desvantagens do padrão Mediator**

Em termos práticos a tendência do padrão Mediator é tornar-se complexo.A troca de complexidade, inicialmente na interação e, após a aplicação do padrão, a complexidade passa a ficar no Mediator o que dificulta a manutenção.

**Padrões relacionados**

Observer e Façade.


## Refactoring Guru

**Também conhecido como:** Mediador, Intermediário, Intermediary, Controlador, Controller

**O que é**
O Mediator é um padrão de projeto comportamental que permite que você reduza as dependências caóticas entre objetos. O padrão restringe comunicações diretas entre objetos e os força a colaborar apenas através do objeto mediador.

**Quando usar**
+ Utilize o padrão Mediator quando é difícil mudar algumas das classes porque elas estão firmemente acopladas a várias outras classes.
+ Utilize o padrão quando você não pode reutilizar um componente em um programa diferente porque ele é muito dependente de outros componentes.
+  Utilize o Mediator quando você se encontrar criando um monte de subclasses para componentes apenas para reutilizar algum comportamento básico em vários contextos.

## GitHub - kamranahmedse

https://github.com/kamranahmedse/design-patterns-for-humans#-mediator


👽 Mediator
========

Real world example
> A general example would be when you talk to someone on your mobile phone, there is a network provider sitting between you and them and your conversation goes through it instead of being directly sent. In this case network provider is mediator.

In plain words
> Mediator pattern adds a third party object (called mediator) to control the interaction between two objects (called colleagues). It helps reduce the coupling between the classes communicating with each other. Because now they don't need to have the knowledge of each other's implementation.

Wikipedia says
> In software engineering, the mediator pattern defines an object that encapsulates how a set of objects interact. This pattern is considered to be a behavioral pattern due to the way it can alter the program's running behavior.

**Programmatic Example**

Here is the simplest example of a chat room (i.e. mediator) with users (i.e. colleagues) sending messages to each other.

First of all, we have the mediator i.e. the chat room

```php
interface ChatRoomMediator 
{
    public function showMessage(User $user, string $message);
}

// Mediator
class ChatRoom implements ChatRoomMediator
{
    public function showMessage(User $user, string $message)
    {
        $time = date('M d, y H:i');
        $sender = $user->getName();

        echo $time . '[' . $sender . ']:' . $message;
    }
}
```

Then we have our users i.e. colleagues
```php
class User {
    protected $name;
    protected $chatMediator;

    public function __construct(string $name, ChatRoomMediator $chatMediator) {
        $this->name = $name;
        $this->chatMediator = $chatMediator;
    }

    public function getName() {
        return $this->name;
    }

    public function send($message) {
        $this->chatMediator->showMessage($this, $message);
    }
}
```
And the usage
```php
$mediator = new ChatRoom();

$john = new User('John Doe', $mediator);
$jane = new User('Jane Doe', $mediator);

$john->send('Hi there!');
$jane->send('Hey!');

// Output will be
// Feb 14, 10:58 [John]: Hi there!
// Feb 14, 10:58 [Jane]: Hey!
```
