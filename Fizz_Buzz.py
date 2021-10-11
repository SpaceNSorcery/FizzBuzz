
def fizz_buzz(input):

    #Output if divisible by 3 & 5
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"

    #Output if divisible 3
    if input % 3 == 0:
        return  "Fizz"
        
    #Output if divisible 5
    if input % 5 == 0:
        return "Buzz"

    return input
print(fizz_buzz(15))
