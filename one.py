#Your optional code here
#You can import some modules or create additional functions



def checkio(number):
    fizz = number % 3 == 0
    buzz = number % 5 == 0
    
    if fizz and buzz:
        return "Fizz Buzz"

    elif fizz: 
        return "Fizz"
        
    elif buzz: 
        return "Buzz"
        
    else:
        return str(number)



#Some hints:
#Convert a number in the string with str(n)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
