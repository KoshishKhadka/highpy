name = "koshish khadka"
age = 20
college_year = "6th semester"

print(f"Hello, my name is {name}")
print(f"I am {age} years old")
print(f"I'm currently in {college_year}")

favorite_language = input("What's your favorite programming language? ")
print(f"Nice, {favorite_language} is a solid choice.")

birth_year_input = input("What year were you born? ")
birth_year = int(birth_year_input)
turning_30_year = birth_year + 30
print(f"You'll turn 30 in {turning_30_year}.")
if turning_30_year > 2026:
    print("youre not an old fart")
else:
    print("either youre already old or i aint good at coding.")
num1 = int(input("enter a number:"))
num2 = int(input("enter another number:"))
sum_result=num1 + num2
print(f"the sum of the two numbers is {sum_result}")
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")