


"""
COHESION
--------
Source: https://ducmanhphan.github.io/2019-03-23-Coupling-and-Cohension-in-OOP/

Cohesion refers to the degree to which the elements inside a module belong together.
Cohesion represents the degree of separation of the responsibilities within a module.
The higher the cohesiveness of the module/class, the better is the OOP design.

    a) it is a measure of the strength of relationship between the methods and data of
        a class and some unifying purpose or concept served by that class.
    b) it is a measure of the strength of relationship between the class's method and data themselves.

Single Responsibility Principle aims at creating highly cohesive classes.
    * If our module performs one task and nothing else or has a clear purpose,
        then it has high cohesion.
    * If our module tries to encapsulate more than one purpose or has an unclear purpose,
        then it  has low cohesion.

Advantages of high cohesion:
    * Reduced module complexity, better understandability.
    * Increased system maintainability, because changes in one module
        require fewer changes in other modules.
    * Increased module reusability, because application developers will find the component
        they need more easily among the cohesive set of operations provided by the module.


High cohesion often correlates with loose coupling, and vice versa.

"""







"""
COUPLING
--------
Source: https://ducmanhphan.github.io/2019-03-23-Coupling-and-Cohension-in-OOP/


Coupling is the degree of interdependence between software modules;
a measure of how closely connected two routines or modules are.
Coupling increases between two classes A and B if:

* A has an attribute that refers to (is of type) B.
* A calls on services of an object B.
* A has a method that references B (via return type or parameter).
* A is a subclass of (or implements) class B.


Low coupling refers to a relationship in which modules interact with each other
through a simple and stable interface and don't need to be concerned
with the other module's internal implementation.


Disadvantages of tightly coupling
    1) A change in one module usually results in a cascade of changes in others.
    2) Assembly of modules might require more effort or time due to the increased inter-module dependency.
    3) A particular module might be harder to reuse or test because dependent modules must be included.


"""





"""
Differences between cohesion and coupling


Cohesion: is an intra-module concept
Coupling: is inter-module concept


Cohesion: shows the module's relative functional strength
Coupling: shows the relative independence among the modules


Cohesion: is a degree to which a component / module focuses on the single thing
Coupling: is a degree to which a component / module is connected to the other modules


Cohesion: While designing we should strive for high cohesion. Ex: cohesive component/module
            focuses on a single task with little interaction with other modules of the system
Coupling: While designing we should strive for low coupling. Ex: dependency between modules should be low.


Cohesion: is a natural extension of data hiding,
Coupling: making private fields, private methods and non public classes provides loose coupling


"""







"""
Extras on Coupling
------------------

In Coupling, we need to consider some properties:

Degree
Degree is the number of connections between the module and others.
With coupling, we want to keep the degree small. For instance,
if the module needed to connect to other modules through a few parameters or narrow interfaces,
then the degree would be small, and coupling would be loose.

Ease
Ease is how obvious are the connections between the module and others.
With coupling, we want the connections to be easy to make without needing
to understand the implementations of the other modules.

Flexibility
Flexibility is how interchangeable the other modules are for this module.
With coupling, we want the other modules easily replaceable for something better in the future.



Types of coupling in PROCEDURAL PROGRAMMING:

* Content coupling (high)
Content coupling is said to occur when one module uses the code of other module, for instance a branch.
This violates information hiding - a basic design concept.

* Common coupling
Common coupling is said to occur when several modules have access to the same global data.
But it can lead to uncontrolled error propagation and unforeseen side-effects when changes are made.

* External coupling
External coupling occurs when two modules share an externally imposed data format,
communication protocol, or device interface.
This is basically related to the communication to external tools and devices.

* Control coupling
Control coupling is one module controlling the flow of another,
by passing it information on what to do. For example: passing a what-to-do flag.

* Stamp coupling (data-structured coupling)
Stamp coupling occurs when modules share a composite data structure and use only parts of it,
possibly different parts (Ex: passing a whole record to a function that needs only one field of it).

* Data coupling
Data coupling occurs when modules share data through, for example, parameters.
Each datum is an elementary piece, and these are the only data shared
(Ex: passing an integer to a function that computes a square root).



Types of coupling in OBJECT ORIENTED PROGRAMMING:

* Subclass coupling
Describes the relationship between a child and its parent.
The child is connected to its parent, but the parent is not connected to the child.

* Temporal coupling
When two actions are bundled together into one module just because
they happen to occur at the same time.

* Dynamic coupling
The goal of this type of coupling is to provide a run-time evaluation of a software system.
It has been argued that static coupling metrics lose precision when dealing with
an intensive use of dynamic binding or inheritance.
In the attempt to solve this issue, dynamic coupling measures have been taken into account.

* Semantic coupling
This kind of coupling considers the conceptual similarities between software entities using,
for example, comments and identifiers and relying on techniques.

* Logical coupling
Logical coupling exploits the release history of a software system
to find change patterns among modules or classes.

For example: Entities that are likely to be changed or sequences of changes
(a change in a class A is always followed by a change in a class B).


"""