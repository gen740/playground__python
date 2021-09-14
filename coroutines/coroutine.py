import time

def simple_gen():
    yield "Hello"
    yield "World"
 
 
gen = simple_gen()
print(next(gen)) # next(gen) == "Hello"
time.sleep(1)
print(next(gen)) # next(gen) == "World"
