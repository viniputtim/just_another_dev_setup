import os
import re


CHEATSHEET_PATH = '/home/vinicius/Documentos/raylib_cheatsheet.txt'
FUNCTION_REGEX = re.compile(r'^[\w\s]+?([\w\*]+)\(([\w\s\*,]+)\);\s+\/\/\s+(.*)$')


def read_cheatsheet():
    lines = ''

    with open(CHEATSHEET_PATH) as file:
        lines = file.readlines()

    return lines


def process_lines(lines):
    functions = []


    for line in lines:
        f, a, c = process_line(line.strip())

        if f and a and c:
            functions.append([f, a, c])

    return functions


def process_line(line):
    match = re.search(FUNCTION_REGEX, line)
    function = [match.group(1), match.group(2), match.group(3)] if match else [0, 0, 0]

    return function


def process_functions(functions):
    content = ''

    for function in functions:
        c = process_function(function)
        content = f'{content}{c}\n' if c else content

    return content


def process_function(function):
    function[0] = remove_star(function[0])
    args = process_args(function[1])

    trigger = f'"trigger": "{function[0]}"'
    annotation = f'"annotation": "{function[2]}"'
    annotation = annotation.replace('\\0', '\\\\0')
    contents = f'"contents": "{function[0]}({args})"'

    content = f'{{\n{" " * 4}{trigger},\n{" " * 4}{annotation},\n{" " * 4}{contents}\n}},'

    return content


def remove_star(name):
    name = name.replace(' *', ' [replaced]')
    name = name.replace('*', '')
    name = name.replace(' [replaced]', ' *')

    return name


def process_args(args):
    arguments = []
    args = args.split(',')

    for i, arg in enumerate(args):
        parts = arg.split(' ')
        arg = parts[-1]

        if arg != 'void':
            arguments.append(f'${{{i + 1}:{arg}}}')

    args = ', '.join(arguments)

    return args


def insert_body(content):
    completions = []
    opening_body = f'{{\n{" " * 4}"scope": "source.c, source.c++",\n{" " * 4}"completions": ['
    ending_body = f'{" " * 4}]\n}}'
    indentation = f'{" " * 8}'
    lines = content.split('\n')

    for line in lines[0:-1]:
        completions.append(f'{indentation}{line}')

    completions = '\n'.join(completions)
    content = f'{opening_body}\n{completions}\n{ending_body}'

    return content


def main():
    cheatsheet_lines = read_cheatsheet()
    functions = process_lines(cheatsheet_lines)
    content = process_functions(functions)
    content = insert_body(content)

    print(content)


if __name__ == '__main__':
    main()
