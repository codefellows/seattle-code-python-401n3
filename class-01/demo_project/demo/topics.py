from new_mod import the_best_alwasy

print('What is the Best Star Wars Movie!')

best_movie = input('> ')

# print('Concat')
# print('The best Star Wars Movie is: ' + best_movie + '.')

# print('Older Way')
# print('The best Star Wars Movie is: {}.'.format(best_movie))

# print('Newer Way')
# print(f'The best Star Wars Movie is: {best_movie}.')

def get_the_best_movie(movie: str) -> str:
    return f'The best Star Wars Movie is: {movie}.'

print(get_the_best_movie('empire'))

print(the_best_alwasy('blah'))

if __name__ == "__main__":
    pass
