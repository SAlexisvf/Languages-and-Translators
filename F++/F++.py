import sys

import ply.yacc as yacc
import ply.lex as lex
import numpy as np

from common import symbols_table_structure
from executor import execute

# reserved keywords
reserved = {
    'int':'int',
    'double':'double',
    'consoleRead':'consoleRead',
    'consoleWrite':'consoleWrite',
    'main':'main',
    'function':'function',
    'if':'if',
    'else':'else',
    'elif':'elif',
    'while':'while',
    'do':'do',
    'for':'for',
    'and':'and',
    'or':'or',
    'call':'call',
}

# List of token names.   This is always required
tokens = [
    # identifier for variables and functions
    'id',

    # data types and values
    'int',
    'double',
    'string',
    'intValue',
    'doubleValue',

    # logic operators
    'and',
    'or',
    'isEqual',
    'notEqual',
    'greaterThan',
    'lessThan',
    'greaterOrEqual',
    'lessOrEqual',

    # arithmetic operators
    'equal',
    'plus',
    'minus',
    'multiply',
    'divide',
    'plusPlus',
    'minusMinus',

    # syntax operators
    'comma',
    'semicolon',
    'openParenthesis',
    'closeParenthesis',
    'openBracket',
    'closeBracket',
    'openBrace',
    'closeBrace',
    'not',

    # conditionals and cycles
    'if',
    'else',
    'elif',
    'while',
    'do',
    'for',

    # data input/output
    'consoleRead',
    'consoleWrite',

    # reserved names
    'main',
    'function',
    'call',

]

# tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_isEqual = r'\=\='
t_notEqual = r'\!\='
t_greaterThan = r'\>'
t_lessThan = r'\<'
t_greaterOrEqual = r'\>\='
t_lessOrEqual = r'\<\='
t_equal = r'\='
t_plus = r'\+'
t_minus = r'\-'
t_multiply = r'\*'
t_divide = r'\/'
t_plusPlus = r'\+\+'
t_minusMinus = r'\-\-'
t_comma = r'\,'
t_semicolon = r'\;'
t_openParenthesis = r'\('
t_closeParenthesis = r'\)'
t_openBracket = r'\['
t_closeBracket = r'\]'
t_openBrace = r'\{'
t_closeBrace = r'\}'
t_not = r'\!'
t_string = r'\'[a-zA-Z0-9 \.\?\:\t\r\n\f()\[\]\&\!\@\#\$\%\^\-\=\+\/\,]*\''

# A string containing ignored characters (spaces and tabs)
t_ignore  =  ' \t\n'
t_ignore_COMMENT = r'\#.*'

def t_doubleValue(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_intValue(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_id(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
    else:  
        t.type = 'id'
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

available_variables_in_memory = 50
quadruplet_index = 1
available = []
symbols_table = {}
operands_stack = []
operators_stack = []
types_stack = []
jumps_stack = []
ifs_stack = []
quadruplets = []
for_increment = []
function_id = []
write_vars = []

def peek(list):
    if len(list) == 0:
        return None
    return list[len(list) - 1]

for i in range (available_variables_in_memory):
    available.append('#' + str(i))

symbols_table_index = available_variables_in_memory

def p_program(p):
    '''
	program : var func mainProgram
    '''
    # print('Valid program!!!')
    # print()
	
def p_var(p):
    '''
    var : type varSequence semicolon var
    | type id openBracket intValue ACTION_CREATE_ARRAY closeBracket semicolon var
    |
    '''
    if (len(p) == 5):
        for name in p[2]:
            add_symbol(name, p[1])

def p_varSequence(p):
    '''
    varSequence : id comma varSequence
        | id
    '''
    if (len(p) == 2 or p[len(p)-2] == '='):
        p[0] = [p[1]]
    else:
        p[0] = p[len(p)-1] + [p[1]]

def p_type(p):
    '''
    type : int
    | double
    '''
    p[0] = p[1]

def p_arithmeticExpression(p):
    '''
    arithmeticExpression : multiplyDivide
    | arithmeticExpression plus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET
    | arithmeticExpression minus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET
    '''

def p_multiplyDivide(p):
    '''
    multiplyDivide : val
    | multiplyDivide multiply ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET
    | multiplyDivide divide ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET
    '''

def p_val(p):
    '''
    val : value
    | unaryExpression
    | openParenthesis arithmeticExpression closeParenthesis
    '''

def p_unaryExpression(p):
    '''
    unaryExpression : id ACTION_UNARY_ADD_OPERANDS plusPlus ACTION_UNARY_PLUS
    | id ACTION_UNARY_ADD_OPERANDS minusMinus ACTION_UNARY_MINUS
    '''

def p_value(p):
    '''
    value : intValue ACTION_INT_VALUE
    | doubleValue ACTION_DOUBLE_VALUE
    | id ACTION_VAR_VALUE
    '''

def p_valueArray(p):
    '''
    valueArray : intValue
    | doubleValue
    | id
    '''
    p[0] = p[1]

def p_func(p):
    '''
    func : function id ACTION_ADD_FUNCTION openParenthesis closeParenthesis openBrace subroutine closeBrace ACTION_END_FUNCTION func
    |
    '''

def p_mainProgram(p):
    '''
    mainProgram : main openParenthesis closeParenthesis openBrace subroutine closeBrace
    '''

def p_subroutine(p):
    '''
    subroutine : consoleWrite openParenthesis cout ACTION_CONSOLE_WRITE closeParenthesis semicolon subroutine
    | consoleRead openParenthesis id ACTION_CONSOLE_READ closeParenthesis semicolon subroutine
    | if openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_NEW_IF ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement ACTION_FILL_JUMP_END_IF subroutine
    | while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_WHILE_GOTO subroutine
    | do ACTION_DO_WHILE_INDEX openBrace subroutine closeBrace while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE semicolon subroutine
    | for openParenthesis id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon statement semicolon ACTION_QUADRUPLET_EMPTY_JUMP arithmeticExpression ACTION_FOR_INCREMENT closeParenthesis openBrace subroutine closeBrace ACTION_FOR_GOTO subroutine
    | id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon subroutine
    | id openBracket arithmeticExpression closeBracket equal arithmeticExpression ACTION_GENERATE_ARRAY_QUADRUPLET semicolon subroutine
    | unaryExpression semicolon subroutine
    | call id ACTION_GOTO_FUNCTION openParenthesis closeParenthesis semicolon subroutine
    |
    '''
def p_elseStatement(p):
    '''
    elseStatement : elif ACTION_FILL_JUMP openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement
    | else ACTION_FILL_JUMP openBrace subroutine closeBrace
    | ACTION_FILL_JUMP
    '''

def p_statement(p):
    '''
    statement : arithmeticExpression 
    | arithmeticExpression logicExpression ACTION_ADD_OPERATOR arithmeticExpression ACTION_ADD_QUADRUPLET
    | statement logicExpression ACTION_ADD_OPERATOR statement ACTION_ADD_QUADRUPLET
    '''

def p_logicExpression(p):
    '''
    logicExpression : greaterThan
    | lessThan
    | isEqual
    | notEqual
    | greaterOrEqual
    | lessOrEqual
    | and
    | or
    '''
    p[0] = p[1]

def p_cout(p):
    '''
    cout : id multipleCout
    | string multipleCout
    | id openBracket arithmeticExpression closeBracket
    '''
    if len(p) > 3:
        write_vars.append(p[1]+p[2])
    else:
        write_vars.append(p[1])

def p_multipleCout(p):
    '''
    multipleCout : comma id multipleCout
    | comma string multipleCout
    |
    '''
    if len(p) == 4:
        write_vars.append(p[2])
        
# Error rule for syntax errors
def p_error(p):
    raise Exception("Syntax error in input!")

def add_symbol(name, data_type, index=0, dimention=0):
    global symbols_table_index
    if (data_type == 'int_array' or data_type == 'double_array'):
        symbols_table[name] = symbols_table_structure(name, data_type, '*' + str(symbols_table_index), index, dimention)
    else:
        symbols_table[name] = symbols_table_structure(name, data_type, '#' + str(symbols_table_index), index, dimention)
    symbols_table_index += 1

def p_action_var_value(p):
    "ACTION_VAR_VALUE :"
    operands_stack.append(symbols_table[p[-1]].address)
    types_stack.append(symbols_table[p[-1]].type)

def p_action_int_value(p):
    "ACTION_INT_VALUE :"
    operands_stack.append(p[-1])
    types_stack.append('int')

def p_action_double_value(p):
    "ACTION_DOUBLE_VALUE :"
    operands_stack.append(p[-1])
    types_stack.append('double')

def p_action_unary_add_operands(p):
    "ACTION_UNARY_ADD_OPERANDS :"
    operands_stack.append(symbols_table[p[-1]].address)
    operands_stack.append('1')

def p_action_unary_plus(p):
    "ACTION_UNARY_PLUS :"
    add_unary_quadruplet('+')

def p_action_unary_minus(p):
    "ACTION_UNARY_MINUS :"
    add_unary_quadruplet('-')

def add_unary_quadruplet(operator):
    global quadruplet_index
    right_operand = operands_stack.pop()
    left_operand = operands_stack.pop()
    quadruplets.append(operator + ' ' + str(left_operand) + ' ' + str(right_operand) + ' ' + str(left_operand))
    quadruplet_index += 1

def p_action_add_operator(p):
    "ACTION_ADD_OPERATOR :"
    operators_stack.append(p[-1])

def p_action_generate_quadruplet(p):
    "ACTION_GENERATE_QUADRUPLET :"
    global quadruplet_index
    operator = p[-2]
    operand = p[-3]
    variable_address = symbols_table[operand].address
    value = operands_stack.pop()
    quadruplets.append(str(operator) + ' ' + str(value) + ' ' + str(variable_address))
    quadruplet_index += 1

def p_action_add_quadruplet(p):
    "ACTION_ADD_QUADRUPLET :" 
    global quadruplet_index, available
    operator = operators_stack.pop()
    right_operand = operands_stack.pop()
    left_operand = operands_stack.pop()
    temp = available.pop(0)
    quadruplets.append(str(operator) + ' ' + str(left_operand) + ' ' + str(right_operand) + ' ' + str(temp))
    quadruplet_index += 1
    operands_stack.append(temp)

def p_action_quadruplet_empty_jump(p):
    "ACTION_QUADRUPLET_EMPTY_JUMP :"
    global quadruplet_index
    statement_result = quadruplets[quadruplet_index - 2].split()
    quadruplets.append(str("gotoF") + ' ' + str(statement_result[len(statement_result) - 1]) + ' ')
    jumps_stack.append(quadruplet_index)
    quadruplet_index += 1

def p_action_new_if(p):
    "ACTION_NEW_IF :"
    ifs_stack.append([])

def p_action_quadruplet_empty_jump_end_if(p):
    "ACTION_QUADRUPLET_EMPTY_JUMP_END_IF :"
    global quadruplet_index
    ifs_stack[len(ifs_stack) - 1].append(quadruplet_index)
    quadruplets.append(str("goto") + ' ')
    quadruplet_index += 1

def p_action_fill_jump_end_if(p):
    "ACTION_FILL_JUMP_END_IF :"
    for goto_index in ifs_stack[len(ifs_stack) - 1]:
        fill_jump(goto_index - 1, quadruplet_index)
    ifs_stack.pop()

def p_action_fill_jump(p):
    "ACTION_FILL_JUMP :"
    fill_jump(jumps_stack.pop() - 1, quadruplet_index)

def p_action_while_goto(p):
    "ACTION_WHILE_GOTO :"
    global quadruplet_index
    empty_jump_quadruplet_index = jumps_stack.pop() - 1
    quadruplets.append(str("goto ") + str(empty_jump_quadruplet_index))
    quadruplet_index += 1
    fill_jump(empty_jump_quadruplet_index, quadruplet_index)

def p_action_do_while_jump_index(p):
    "ACTION_DO_WHILE_INDEX :"
    global quadruplet_index
    jumps_stack.append(quadruplet_index)

def p_action_quadruplet_empty_jump_do_while(p):
    "ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE :"
    global quadruplet_index
    statement_result = quadruplets[quadruplet_index - 2].split()
    quadruplets.append(str("gotoT") + ' ' + str(statement_result[len(statement_result) - 1]) + ' ' + str(jumps_stack.pop()))
    quadruplet_index += 1

def p_action_for_increment(p):
    "ACTION_FOR_INCREMENT :"
    global quadruplet_index, for_increment
    for_increment.append(quadruplets[quadruplet_index-2])
    quadruplets.pop()
    quadruplet_index -= 1

def p_action_for_goto(p):
    "ACTION_FOR_GOTO :"
    global quadruplet_index, for_increment
    empty_jump_quadruplet_index = jumps_stack.pop() - 1
    quadruplets.append(for_increment.pop())
    quadruplet_index += 1
    quadruplets.append(str("goto ") + str(empty_jump_quadruplet_index))
    quadruplet_index += 1
    fill_jump(empty_jump_quadruplet_index, quadruplet_index)

def p_action_add_function(p):
    "ACTION_ADD_FUNCTION :"
    global quadruplet_index, function_id
    function_id.append(p[-1])
    add_symbol(function_id[-1], 'function', quadruplet_index)
    quadruplets.append('goto ')
    quadruplet_index += 1

def p_action_end_function(p):
    "ACTION_END_FUNCTION :"
    global quadruplet_index, symbols_table, function_id
    fill_jump(symbols_table[function_id.pop()].index-1, quadruplet_index+1)
    quadruplets.append('return')
    quadruplet_index += 1

def p_action_goto_function(p):
    "ACTION_GOTO_FUNCTION :"
    global quadruplet_index
    function_id = p[-1]
    quadruplets.append('call ' + str(symbols_table[function_id].index+1))
    quadruplet_index += 1

def p_action_console_write(p):
    "ACTION_CONSOLE_WRITE :"
    global quadruplet_index, write_vars
    cout = ''
    for var in write_vars:
        if var[0] == "'":
            cout = var.replace("'", "") + ' ' + cout
        elif var.find('[') > 0:
            cout = '*' + var + str(operands_stack.pop()) + ']' + ' ' + cout
        else:
            cout = '#' + var + ' ' + cout
    write_vars = []
    quadruplets.append('consoleWrite ' + cout)
    quadruplet_index += 1

def p_action_console_read(p):
    "ACTION_CONSOLE_READ :"
    global quadruplet_index
    cin = p[-1]
    quadruplets.append('consoleRead ' + str(cin))
    quadruplet_index += 1

def p_action_create_array(p):
    "ACTION_CREATE_ARRAY :"
    array_name = p[-3]
    dimention = p[-1]
    array_type = 'int_array' if p[-4] == 'int' else 'double_array'
    add_symbol(array_name, array_type, dimention=dimention)

def p_action_generate_array_quadruplet(p):
    "ACTION_GENERATE_ARRAY_QUADRUPLET :"
    global quadruplet_index
    operator = p[-2]
    operand = p[-6]
    value = operands_stack.pop()
    variable_address = '*' + operand + '_' + str(operands_stack.pop())
    quadruplets.append(str(operator) + ' ' + str(value) + ' ' + str(variable_address))
    quadruplet_index += 1
    
def fill_jump(empty_jump_quadruplet_index, goto_index):
    quadruplets[empty_jump_quadruplet_index] = quadruplets[empty_jump_quadruplet_index] + str(goto_index)

# Build the parser
parser = yacc.yacc()
 
if (len(sys.argv) > 1):
    program_name = sys.argv[1]
    program_file = open(program_name, "r")
    program = program_file.read().replace('\\n', '\n')
    parser.parse(program)
    program_file.close()

    execute(quadruplets, symbols_table, available_variables_in_memory)
else:
    raise Exception('''Test file not provided''')