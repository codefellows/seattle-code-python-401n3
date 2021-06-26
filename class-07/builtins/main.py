import builtins

_print = builtins.print
_input = builtins.input

def alter():
    builtins.print = _input
    builtins.input = _print

def alter_back():
    builtins.print = _print
    builtins.input = _input

alter()

print('This is a General Print Statement')

input('I Want to grab some info > ')

input('Hi I am Roger!')
