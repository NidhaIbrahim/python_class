def check_prime(number):
    flag = False
    if number == 1:
        print( number, " is not a prime number" )
    elif number > 1:
        for i in range(2,number):
            if (number % i) == 0: 
                flag = True
                break
        if flag:
            print(number, " is not prime number")
        else:
            print(number, " is prime number")

# check_prime(23)



def even_or_odd(num):
    if num == 0:
        print( num, "is zero")
    elif num > 0:
        if num % 2 == 0:
            print( num, "is even")
        else:
            print( num, "is odd")
    else:
        print(num, "is negative")

# even_or_odd(9)