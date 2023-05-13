<h1>Software engineering lab 6 <\h1>
<h2>Mohadese Ghafari 98109537 - Mehreagan Mohseni 97107245<\h2>

<h3>Abstract Factor Design Pattern, Implementation Steps<\h3>

1- Map out a matrix of distinct product types versus variants of these products.

2- Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.

3- Declare the abstract factory interface with a set of creation methods for all abstract products.

4- Implement a set of concrete factory classes, one for each product variant.

5- Create factory initialization code somewhere in the app. It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. Pass this factory object to all classes that construct products.

6-Scan through the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method on the factory object.

<h3>Prototype Design Pattern, Implementation Steps<\h3>
1- Create the prototype interface and declare the clone method in it. Or just add the method to all classes of an existing class hierarchy, if you have one.

2- A prototype class must define the alternative constructor that accepts an object of that class as an argument. The constructor must copy the values of all fields defined in the class from the passed object into the newly created instance. If you’re changing a subclass, you must call the parent constructor to let the superclass handle the cloning of its private fields.

3- If your programming language doesn’t support method overloading, you won’t be able to create a separate “prototype” constructor. Thus, copying the object’s data into the newly created clone will have to be performed within the clone method. Still, having this code in a regular constructor is safer because the resulting object is returned fully configured right after you call the new operator.

4- The cloning method usually consists of just one line: running a new operator with the prototypical version of the constructor. Note, that every class must explicitly override the cloning method and use its own class name along with the new operator. Otherwise, the cloning method may produce an object of a parent class.

5- Optionally, create a centralized prototype registry to store a catalog of frequently used prototypes.

<h3>Unit Test<\h3>
test_shallow_copy: This test verifies the behavior of a shallow copy. It creates an instance of SomeComponent with various attributes, including a circular reference to a SelfReferencingEntity object. It then performs a shallow copy of the component using copy.copy(component). The test checks the following:

The shallow copied object is not the same object as the original object using self.assertIsNot(component, shallow_copied_component).
The attributes of the shallow copied object are the same as the original object's attributes using assertions like self.assertEqual(component.some_int, shallow_copied_component.some_int).
Changing attributes in the shallow copied object does not affect the original object, which is checked by modifying an attribute in the shallow copied object and verifying it doesn't affect the original object.
test_deep_copy: This test verifies the behavior of a deep copy. It follows a similar process as the test_shallow_copy but uses copy.deepcopy(component) to perform a deep copy. The test checks the following:

The deep copied object is not the same object as the original object using self.assertIsNot(component, deep_copied_component).
The attributes of the deep copied object are the same as the original object's attributes using assertions like self.assertEqual(component.some_int, deep_copied_component.some_int).
Changing attributes in the deep copied object does not affect the original object, including nested objects.
test_circular_reference: This test verifies that the circular reference is maintained correctly during the deep copy. It creates an instance of SomeComponent with a circular reference and performs a deep copy. The test checks the following:

The circular reference in the deep copied object points to itself and its parent correctly, demonstrating that the circular reference is maintained.
The circular reference in the deep copied object is not the same as the original object's circular reference.

<h3>Builder Design Pattern, Implementation Steps<\h3>

1- Create a concrete builder class for each of the product representations and implement their construction steps.

2- Implementing a method for fetching the result of the construction. 

3- Creating a director class. It may encapsulate various ways to construct a product using the same builder object.

4- The client code creates both the builder and the director objects. Before construction starts, the client must pass a builder object to the director. Usually, the client does this only once, via parameters of the director’s class constructor. The director uses the builder object in all further construction. There’s an alternative approach, where the builder is passed to a specific product construction method of the director.

5- The construction result can be obtained directly from the director only if all products follow the same interface.

<h3>Unit test<\h3>
test_build_minimal_viable_product: This test verifies that the director can build a minimal viable product using the builder. It checks if the product contains the expected parts after the construction.

test_build_full_featured_product: This test verifies that the director can build a full-featured product using the builder. It checks if the product contains the expected parts after the construction.

test_custom_product: This test verifies that the builder can be used directly without the director to create a custom product. It checks if the product contains the expected parts after the construction.




