from functools import wraps

def yo_mamma_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Yo mamma says "{orig_val}"'
    return wrapper

def sophisticated_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Would you like some Tea and Crumpets as you say "{orig_val}"'
    return wrapper



@sophisticated_decorator
@yo_mamma_decorator
def just_saying(txt):
    return txt


if __name__ == "__main__":
    print(just_saying('I love star wars!'))
    # sith1 = 'Darth Revan'
    # sith2 = 'Darth Vader'
    # sith3 = 'Darth Bane'

    # def sith_args(*args):
    #     for sith in args:
    #         print(f'{sith} is a Dark Lord of the Sith!')

    # def sith_kwargs(**kwargs):
    #     for item, sith in kwargs.items():
    #         print(item, sith)
    

    # sith_kwargs(
    #     sith1 = 'Darth Revan',
    #     sith2 = 'Darth Vader',
    #     sith3 = 'Darth Bane')

    # sith_args(sith_kwargs)