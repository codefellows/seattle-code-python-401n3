def fizz_buzz(num):
    """
    For number divisible by 3 return 'Fizz'
    For number divisible by 5 return 'Buzz'
    For number divisible by 3 and 5  return 'FizzBuzz'
    For number not divisible by 3 or 5 return number
    """
    # Run a test to see if num is a number
    # if not return "Error Message"

    
    if num %3 == 0 and num %5 == 0:
        return 'FizzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    elif num % 5 == 0:
        return 'Buzz'

    return num

    # for num in range(15):
    #     if num % 3 == 0 and num % 5 == 0:
    #         return 'FizzBuzz'
    #     elif num %3 == 0:
    #         return 'Fizz'
    #     elif num % 5 == 0:
    #         return 'Buzz'
    #     else:
    #         return num

    # word = ''
    # if num % 3 == 0:
    #     word = 'Fizz'
    # if num % 5 == 0:
    #     word += 'Buzz'
    # return word or num
