# Quick Talk on Python Decorators

- Ashish Sharma (accssharma@gmail.com)
- [Boise Area Python User Group](https://www.meetup.com/boise-area-python-user-group/events/260155341/) -- April 17, 2019 

# Two important concepts

(a) First class functions
  - allow us to treat functions like any other objects:
    - pass function as argument
    - pass function as a return value
    - assign function to a variable

(b) Closures
    - like any other "nested" concept in programming, a nested function is a function defined inside a function 
    - these nested functions can use variables from the enclosing environment (outer functions)

Wikipedia: "...Operationally, a closure is a record storing function [a] together 
with an environment. The environment is a mapping associating each free variable 
of the function (variables that are used locally, but defined in an enclosing scope) 
with the value or reference to which the name was bound when the closure was created.
[b] Unlike a plain function, a closure allows the function to access those captured 
variables through the closure's copies of their values or references, even when 
the function is invoked outside their scope...."
    - Commonly used in: Python, Javascript
    - In simple words, closures help persisting values of the local 
      variables outside their scope
    - Provides functions portability

