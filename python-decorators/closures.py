#!/usr/bin/env python
"""Closures and Decorators Examples"""

########################
# # Example 1: Closure #
########################

def normal_function():
    print("I am no special!")
    
def greet_as_ashish():
    """Simple function recording a closure"""
    # captured variable in outer context
    # also called a free variable
    greet_prefix = "Ashish says:"
    def greet(message):
        print("{} {}".format(greet_prefix, message))
    return greet

# greeter is actually the inner function greet
print()
greeter = greet_as_ashish()
print ("greeter object::: ", greeter)
print()
print ("greeter object name::: ", greeter.__name__)
print()

# access free variable from __closure__
print("dir(greeter):::\n", dir(greeter))
print()
print("Closure's free variable: " + greeter.__closure__[0].cell_contents)
print()
# normal function
print("Normal_function closure: {}".format(normal_function.__closure__))
print()

# A reference to a closure that always greet as Ashish
#
# What's different?
# Still invoking a function greet, but it can still use the value of
# greet_prefix even though we have already EVALUATED greet_as_ashish
# function.
# greet_prefix existed in the environment where the greet function
# was created. Being able to use this captured variable is different
greeter("Namaste, Python lovers!")

#exit(0)
########################
# # Example 2: Closure #
########################

def greet_as(greet_prefix):
    """A little more general function using closure"""
    def greet(message):
        print("{} says: {}".format(greet_prefix, message))
    return greet

greeter_travis = greet_as("Travis")
greeter_travis("I'm blessed to have a sweet and very smart son.")
greeter_travis("Nice to meet you!")


greeter_ashok = greet_as("Ashok")
greeter_ashok("You might be wondering who is this Ashok? I am Ashish's brother :)")
greeter_ashok("Thank you!")


###########################
# # Example 3: Decorators #
###########################
# Reference: https://www.youtube.com/watch?v=FsAPt_9Bf3U

# convenience function to manage multiple wrappers
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),
                        level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)


# Note: same decorator functionalitiy can be achieved by
# using class and __call__ method
