# FizzBuzz
# A program that prints the numbers from 1 to num (User given number)!
# For multiples of ‘3’ print “Fizz” instead of the number.
# For the multiples of ‘5’ print “Buzz”.
# If the number is divisible by both 3 and 5 then print "FizzBuzz".
# If none of the given conditions are true then just print the number!


def FizzBuzz(target_number):
    fizz_score = 0
    buzz_score = 0
    fizz_counter = 0
    buzz_counter = 0
    fizz_buzz_counter = 0
    sum_remainder = 0
    euler_value = 0

    for integer in range(1, target_number + 1, 1):
        fizz_score += 1
        buzz_score += 1

        if fizz_score == 3 and buzz_score == 5:
            print("FizzBuzz")
            fizz_score = 0
            buzz_score = 0
            fizz_counter += 1
            buzz_counter += 1
            fizz_buzz_counter +=1
            euler_value += integer
        elif fizz_score == 3:
            print("Fizz")
            fizz_score = 0
            fizz_counter +=1
            euler_value += integer
        elif buzz_score == 5:
            print("Buzz")
            buzz_score = 0
            buzz_counter +=1
            euler_value += integer
        else:
            print(integer)
            sum_remainder += integer
    print ("==========================")
    print (f"Fizz Total = {fizz_counter}")
    print (f"Buzz Total = {buzz_counter}")
    print (f"FizzBuzz = {fizz_buzz_counter}")
    print (f"Sum Remainder Total = {sum_remainder}")
    print ("==========================")
    print (f"Euler Answer = {euler_value}")


FizzBuzz(999) 
exit()
