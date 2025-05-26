FILE_PATH = '/home/vinicius/Documentos/raylib_cheatsheet.txt'


def read_lines():
    lines = ''

    with open(FILE_PATH) as file:
        lines = file.readlines()

    return lines


def process_line(line):
    content = ''

    if '/' in line:
        index = line.index('/')
        line = line[:index]
        line = line.strip()

    if ';' in line and '(' in line and ')' in line and not '#' in line:
        line = line.replace(';', '')

        if ' ' in line:
            index = line.index(' ')
            line = line[index + 1:]

        content = line

    return content


def process_function(function):
    content = ''
    arguments = ''
    name = ''

    function = function.replace(' *', ' %')
    function = function.replace('*', '')
    function = function.replace(' %', ' *')

    if '(' in function and ')' in function:
        start_index = function.index('(')
        end_index = function.index(')')
        args = function[start_index + 1:end_index]
        name = function[:start_index]

        arguments = process_args(args)

    open_bracket = f'{" " * 8}{{\n'
    trigger = f'{" " * 12}"trigger": "{function};",\n'
    contents = f'{" " * 12}"contents": "{name}({arguments});"\n'
    close_bracket = f'{" " * 8}}}'
    content = f'{open_bracket}{trigger}{contents}{close_bracket}'

    return content


def process_args(args):
    if args == 'void':
        return ''

    arguments = []
    args = args.split(',')

    for i, arg in enumerate(args):
        parts = arg.split(' ')
        arg = parts[-1]

        arguments.append(f'${{{i + 1}:{arg}}}')

    args = ', '.join(arguments)

    return args


def main():
    content = """{
    "scope": "source.c, source.c++",
    "completions": [\n"""
    functions = ''
    lines = read_lines()

    for line in lines:
        line_content = process_line(line)
        functions = f'{functions}{line_content}\n' if line_content else functions

    functions = functions.split('\n')

    for function in functions:
        line_content = process_function(function)
        content = f'{content}{line_content},\n' if line_content else content

    content += '    ]\n}'

    print(content)


if __name__ == '__main__':
    main()
