# Adapter

É você adaptar uma classe, ou seja, usar interface de *A e fazer com que *B execute algo igual a um **A real.

## Meu Resumo

Para que serve: Como o nome diz, é a pra que uma classe passe a ter o mesmo comportamento do que outra.

Como fazer: Primeiro, todas as classe devem ter 'implemnts interface'. COm isso voce cria uma classeAdpater que recebe a Classe $A no contrutor e implementa a classe $B. Assim, no metodo implmentado de $B usa o método intreno da classe $A que recebeu.

Exemplo de classe adapter:

````
// Aqui, $B é Lion (Uma interface que tem o método 'roar') e $A é WildDog. Usamos o dapater pois $A nâo tem o método 'roar' mas queremos que execute o seu 'bark' como se fosse o 'roar
class WildDogAdapter implements Lion
{
    protected $dog;

    public function __construct(WildDog $dog)
    {
        $this->dog = $dog;
    }

    public function roar()
    {
        $this->dog->bark();
    }
}
````

## GitHub - kamranahmedse

https://github.com/kamranahmedse/design-patterns-for-humans#-adapter

🔌 Adapter

-------
Real world example
> Consider that you have some pictures in your memory card and you need to transfer them to your computer. In order to transfer them you need some kind of adapter that is compatible with your computer ports so that you can attach memory card to your computer. In this case card reader is an adapter.
> Another example would be the famous power adapter; a three legged plug can't be connected to a two pronged outlet, it needs to use a power adapter that makes it compatible with the two pronged outlet.
> Yet another example would be a translator translating words spoken by one person to another

In plain words
> Adapter pattern lets you wrap an otherwise incompatible object in an adapter to make it compatible with another class.

Wikipedia says
> In software engineering, the adapter pattern is a software design pattern that allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.

**Programmatic Example**

Consider a game where there is a hunter and he hunts lions.

First we have an interface `Lion` that all types of lions have to implement

```php
interface Lion
{
    public function roar();
}

class AfricanLion implements Lion
{
    public function roar()
    {
    }
}

class AsianLion implements Lion
{
    public function roar()
    {
    }
}
```
And hunter expects any implementation of `Lion` interface to hunt.
```php
class Hunter
{
    public function hunt(Lion $lion)
    {
        $lion->roar();
    }
}
```

Now let's say we have to add a `WildDog` in our game so that hunter can hunt that also. But we can't do that directly because dog has a different interface. To make it compatible for our hunter, we will have to create an adapter that is compatible

```php
// This needs to be added to the game
class WildDog
{
    public function bark()
    {
    }
}

// Adapter around wild dog to make it compatible with our game
class WildDogAdapter implements Lion
{
    protected $dog;

    public function __construct(WildDog $dog)
    {
        $this->dog = $dog;
    }

    public function roar()
    {
        $this->dog->bark();
    }
}
```
And now the `WildDog` can be used in our game using `WildDogAdapter`.

```php
$wildDog = new WildDog();
$wildDogAdapter = new WildDogAdapter($wildDog);

$hunter = new Hunter();
$hunter->hunt($wildDogAdapter);
