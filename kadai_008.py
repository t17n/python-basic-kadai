import random
var = random.randint(0, 100)
print(var)

if var % 3 == 0:
     print("Fizz")
elif var % 5 == 0:
     print("Buzz")
elif (var % 3 == 0) and (var % 5 == 0):
     print("FizzBuzz")
else:
     print(var)
