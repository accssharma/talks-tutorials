import time

ll = [1,2,3]
kk = [3,4,5]

def squares(nums):
    start = time.time()
    vals = [x*x for x in nums]
    end = time.time()
    print ("Squares: took {} ms to execute".format(end-start))
    return vals

def cubes(nums):
    start = time.time()
    vals = [x*x*x for x in nums]
    end = time.time()
    # f-strings
    print (f"Cubes: took {end-start} ms to execute")
    return vals

sqs = squares(ll)
cbs = cubes(ll)


################
# # decorators #
################
def timeit(func):
    print(f"entered decorator")
    x = "free variable for testing"
    def wrapper(*args, **kwargs):
        print("\ninside wrapper")
        start = time.time()
        results = func(*args, **kwargs)
        end = time.time()
        print (f"{func.__name__}: took {end-start} ms to execute. ('{x}')")
        return results
    return wrapper

@timeit
def squares(nums):
    return [x*x for x in nums]

@timeit
def cubes(nums):
    return [x*x*x for x in nums]

## function calls equivalent to decorators
sqs = timeit(squares)
cbs = timeit(cubes)
squares(ll)
cubes(ll)


@timeit
def list_sum(nums1, nums2):
    sum = []
    for a,b in zip(nums1, nums2):
        sum.append(a+b)
    return sum

list_sum(ll, kk)

## function calls with decorator syntax @decorator
squares(ll)
cubes(ll)
list_sum(ll, kk)

