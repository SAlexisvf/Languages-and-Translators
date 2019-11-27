import ast

from common import symbols_table_structure

functions_stack = []

def execute(quadruplets, symbols_table, temporal_variables):
    print_quadruplets_and_memory(quadruplets, symbols_table)
    for i in range (temporal_variables):
        symbols_table['temp_' + str(i)] = symbols_table_structure('temp_' + str(i), 'temp', '#' + str(i), 0, 0, 0)
    
    current_quadruplet = 1
    while current_quadruplet <= len(quadruplets):
        current_quadruplet = execute_single_quadruplet(quadruplets[current_quadruplet-1].split(), current_quadruplet, symbols_table)

def execute_single_quadruplet(single_quadruplet, current_quadruplet, symbols_table):
    if single_quadruplet[0] == 'consoleWrite':
        for data in single_quadruplet[1:]:
            if data[0] == '#':
                if data[1:] in symbols_table:
                    print(symbols_table[data[1:]].value, end=' ')
                else:
                    raise Exception (f'ConsoleWrite Error! variable {data[1:]} is not defined')
            elif '**' in data:
                parsed_matrix = parse_matrix(data, symbols_table)
                if parsed_matrix[0] in symbols_table:
                    print(symbols_table[parsed_matrix[0]].value[parsed_matrix[1]][parsed_matrix[2]], end=' ')
                else:
                    raise Exception (f'ConsoleWrite Error! variable {data[1:]} is not defined')
            elif data[0] == '*':    
                parsed_matrix = parse_matrix(data, symbols_table) 
                if parsed_matrix[0] in symbols_table:
                    print(symbols_table[parsed_matrix[0]].value[parsed_matrix[1]], end=' ')
                else:
                    raise Exception (f'ConsoleWrite Error! variable {data[1:]} is not defined')
            elif data == '%n':
                print()
            else:
                print(data, end=' ')

    elif single_quadruplet[0] == 'consoleRead':
        for data in single_quadruplet[1:]:
            if '**' in data:
                parsed_matrix = parse_matrix(data, symbols_table)
                if parsed_matrix[0] in symbols_table:
                    symbols_table[parsed_matrix[0]].value[parsed_matrix[1]][parsed_matrix[2]] = ast.literal_eval(input())
                else:
                    raise Exception (f'ConsoleWrite Error! variable {data[1:]} is not defined')
            elif data[0] == '*':    
                parsed_matrix = parse_matrix(data, symbols_table) 
                if parsed_matrix[0] in symbols_table:
                    symbols_table[parsed_matrix[0]].value[parsed_matrix[1]] = ast.literal_eval(input())
                else:
                    raise Exception (f'ConsoleWrite Error! variable {data[1:]} is not defined')
            elif data in symbols_table:
                symbols_table[data].value = ast.literal_eval(input())
            else:
                raise Exception (f'ConsoleRead Error! variable {data} is not defined')

    elif single_quadruplet[0] in ['+', '-', '*', '/', '==', '!=', '<=', '>=', '<', '>', 'and', 'or']:
        symbols_table[get_name_with_address(single_quadruplet[3], symbols_table)].value = arithmetic_operation(single_quadruplet[0], single_quadruplet[1], single_quadruplet[2], symbols_table)
    
    elif single_quadruplet[0] == '=':
        if single_quadruplet[1][0] == '#':
            single_quadruplet[1] = symbols_table[get_name_with_address(single_quadruplet[1], symbols_table)].value
            if '**' in single_quadruplet[2]:
                parsed_matrix = parse_matrix(single_quadruplet[2], symbols_table)
                symbols_table[parsed_matrix[0]].value[parsed_matrix[1]][parsed_matrix[2]] = single_quadruplet[1]
            elif '*' in single_quadruplet[2]:
                parsed_matrix = parse_matrix(single_quadruplet[2], symbols_table)
                symbols_table[parsed_matrix[0]].value[parsed_matrix[1]] = single_quadruplet[1]
            else:
                symbols_table[get_name_with_address(single_quadruplet[2], symbols_table)].value = single_quadruplet[1]
        else:
            if '**' in single_quadruplet[2]:
                parsed_matrix = parse_matrix(single_quadruplet[2], symbols_table)
                symbols_table[parsed_matrix[0]].value[parsed_matrix[1]][parsed_matrix[2]] = single_quadruplet[1]
            elif '*' in single_quadruplet[2]:
                parsed_matrix = parse_matrix(single_quadruplet[2], symbols_table)
                symbols_table[parsed_matrix[0]].value[parsed_matrix[1]] = single_quadruplet[1]
            else:
                symbols_table[get_name_with_address(single_quadruplet[2], symbols_table)].value = ast.literal_eval(single_quadruplet[1])
        
    elif single_quadruplet[0] == 'gotoF':
        if not symbols_table[get_name_with_address(single_quadruplet[1], symbols_table)].value:
            return ast.literal_eval(single_quadruplet[2])

    elif single_quadruplet[0] == 'gotoT':
        if symbols_table[get_name_with_address(single_quadruplet[1], symbols_table)].value:
            return ast.literal_eval(single_quadruplet[2])

    elif single_quadruplet[0] == 'goto':
        return ast.literal_eval(single_quadruplet[1])

    elif single_quadruplet[0] == 'call':
        functions_stack.append(current_quadruplet + 1)
        return ast.literal_eval(single_quadruplet[1])

    elif single_quadruplet[0] == 'return':
        return functions_stack.pop()

    return current_quadruplet + 1

def get_name_with_address(address, symbols_table):
    for key in symbols_table:
        if symbols_table[key].address == address:
            return key

def parse_matrix(matrix, symbols_table):
    parsed_matrix = []
    if '**' in matrix:
        matrix = matrix.replace('**','')
        if '[' in matrix:
            index_1 = matrix[matrix.find('[')+1:matrix.find('[', matrix.find('[')+1)-1]
            index_2 = matrix[matrix.find('[', matrix.find('[')+1)+1:-1]
            parsed_matrix.append(matrix[:matrix.find('[')])
            if '#' in index_1:
                parsed_matrix.append(symbols_table[get_name_with_address(index_1, symbols_table)].value)
            if '#' in index_2:
                parsed_matrix.append(symbols_table[get_name_with_address(index_2, symbols_table)].value)
            else:
                parsed_matrix.append(ast.literal_eval(index_1))
                parsed_matrix.append(ast.literal_eval(index_2))
        else:
            parsed_matrix.append(matrix[:matrix.find('_')])
            index_1 = matrix[matrix.find('_')+1:matrix.find('_', matrix.find('_')+1)]
            index_2 = matrix[matrix.find('_', matrix.find('_')+1)+1:]
            if '#' in index_1:
                parsed_matrix.append(symbols_table[get_name_with_address(index_1, symbols_table)].value)
            if '#' in index_2:
                parsed_matrix.append(symbols_table[get_name_with_address(index_2, symbols_table)].value)
            else:
                parsed_matrix.append(int(index_1))
                parsed_matrix.append(int(index_2))
    else:
        matrix = matrix.replace('*','')
        if '[' in matrix:
            open_bracket = matrix.find('[')
            close_bracket = matrix.find(']')
            index_1 = matrix[open_bracket+1:close_bracket]
            parsed_matrix.append(matrix[:open_bracket])

            if '#' in index_1:
                parsed_matrix.append(symbols_table[get_name_with_address(index_1, symbols_table)].value)
            else:
                parsed_matrix.append(ast.literal_eval(index_1))
        else:
            parsed_matrix.append(matrix[:matrix.find('_')])
            if '#' in matrix:
                parsed_matrix.append(symbols_table[get_name_with_address(matrix[matrix.find('#'):], symbols_table)].value)
            else:
                parsed_matrix.append(int(matrix[matrix.find('_')+1:]))

    return parsed_matrix

def arithmetic_operation(operator, operand_1, operand_2, symbols_table):
    if operand_1[0] == '#':
        operand_1 = symbols_table[get_name_with_address(operand_1, symbols_table)].value
    else:
        operand_1 = ast.literal_eval(operand_1)

    if operand_2[0] == '#':
        operand_2 = symbols_table[get_name_with_address(operand_2, symbols_table)].value
    else:
        operand_2 = ast.literal_eval(operand_2)
    
    if operator == '+':
        return operand_1 + operand_2
    elif operator == '-':
        return operand_1 - operand_2
    elif operator == '*':
        return operand_1 * operand_2
    elif operator == '/':
        return operand_1 / operand_2
    elif operator == '>':
        return operand_1 > operand_2
    elif operator == '<':
        return operand_1 < operand_2
    elif operator == '>=':
        return operand_1 >= operand_2
    elif operator == '<=':
        return operand_1 <= operand_2
    elif operator == '==':
        return operand_1 == operand_2
    elif operator == '!=':
        return operand_1 != operand_2
    elif operator == 'and':
        return operand_1 and operand_2
    elif operator == 'or':
        return operand_1 or operand_2

def print_quadruplets_and_memory(quadruplets, symbols_table):
    print('Memory:')
    for variable in symbols_table:
        print('variable name:', symbols_table[variable].id + '     ' + 'type:', symbols_table[variable].type + '    ' + 'address:', symbols_table[variable].address)
    print()
    print('Quadruplets:')
    for i in range (len(quadruplets)):
        print(str(i+1) + ') ' + quadruplets[i])
    print()