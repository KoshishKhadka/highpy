def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

greet("Koshish")

result=add(5,3)
print(f"5+3 = {result}")

print(is_even(4))
print(is_even(5))
