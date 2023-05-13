Software engineering lab 6
Mohadese Ghafari 98109537 - Mehreagan Mohseni 97107245

Abstract Factor Design Pattern, Implementation Steps

1- Map out a matrix of distinct product types versus variants of these products.

2- Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.

3- Declare the abstract factory interface with a set of creation methods for all abstract products.

4- Implement a set of concrete factory classes, one for each product variant.

5- Create factory initialization code somewhere in the app. It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. Pass this factory object to all classes that construct products.

Scan through the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method on the factory object.

Builder Design Pattern, Implementation Steps

1- Create a concrete builder class for each of the product representations and implement their construction steps.

2- Implementing a method for fetching the result of the construction. 

3- Creating a director class. It may encapsulate various ways to construct a product using the same builder object.

4- The client code creates both the builder and the director objects. Before construction starts, the client must pass a builder object to the director. Usually, the client does this only once, via parameters of the director’s class constructor. The director uses the builder object in all further construction. There’s an alternative approach, where the builder is passed to a specific product construction method of the director.

5- The construction result can be obtained directly from the director only if all products follow the same interface.

Unit test:
We create a class that verifies the values of functions are equal to the expectation.



