# Design Patterns using Python #
I was remembering some design patterns and I thought to create a repository with clear examples of the main design patterns using Python.


## How to run it
This project uses docker and it contains a Makefile to be easier to build the image and run the tests.
#### Initialize the docker container and run the unit tests:
`make deploy`


## Components
* **src**: Source code
    * **common**: Common classes for the examples
    * **creational**: Examples of creational design patterns
        * **abstract factory**: Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
        * **builder**: Separate the construction of a complex object from its representation so that the same construction process can create different representations.
        * **factory method**: Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
    * **structural**: Examples of structural design patterns
        * **adapter**: Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.
        * **bridge**: Decouple an abstraction from its implementation so that the two can vary independently.
        * **composite**: Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
        * **decorator**: Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
    * **behavioral**: Examples of behavioral design patterns
        * **chain of responsibility**: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
* **tests**: Unit tests for every pattern
