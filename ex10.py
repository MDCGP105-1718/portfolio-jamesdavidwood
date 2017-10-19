high_value = int(input ("Enter your High Value Number"))
low_value = int(input ("Enter your Low Value Number"))

def fizz_buzz(low, high):
    for n in range(low, high):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print (n)

fizz_buzz(low_value, high_value)
