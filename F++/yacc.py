import ply.yacc as yacc
import sys
from common import symbols_table_structure

# Get the token map from the lexer.  This is required.
from lex import tokens

available_variables_in_memory = 50
quadruplet_index = 1
available = []
symbols_table = {}
operands_stack = []
operators_stack = []
types_stack = []
quadruplets = []

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
    print('Valid program!!!')
    print()
    print('Memory:')
    for variable in symbols_table:
        print('variable name:', symbols_table[variable].id + '     ' + 'type:', symbols_table[variable].type + '    ' + 'address:', symbols_table[variable].address)
    print()
    print('Quadruplets:')
    for quadruplet in quadruplets:
        print(quadruplet)
	
def p_var(p):
    '''
    var : type varSequence semicolon var
    |
    '''
    if (len(p) > 1):
        for name in p[2]:
            add_symbol(name, p[1])

def p_varSequence(p):
    '''
    varSequence : variable equal arithmeticExpression
        | variable
        | variable equal arithmeticExpression comma varSequence
        | variable comma varSequence
    '''
    if (len(p) == 2 or p[len(p)-2] == '='):
        p[0] = [p[1]]
    else:
        p[0] = p[len(p)-1] + [p[1]]

def p_variable(p):
    '''
    variable : id dimentions
    '''
    p[0] = p[1]

def p_dimentions(p):
    '''
    dimentions : openBracket value closeBracket
    | openBracket value closeBracket openBracket value closeBracket
    |
    '''

def p_type(p):
    '''
    type : int
    | double
    '''
    p[0] = p[1]

def p_arithmeticExpression(p):
    '''
    arithmeticExpression : multiplyDivide
    | arithmeticExpression plus action_add_operator multiplyDivide action_quadruplet_arithmetic_expression
    | arithmeticExpression minus action_add_operator multiplyDivide action_quadruplet_arithmetic_expression
    '''

def p_multiplyDivide(p):
    '''
    multiplyDivide : val
    | multiplyDivide multiply action_add_operator val action_quadruplet_multiply_divide
    | multiplyDivide divide action_add_operator val action_quadruplet_multiply_divide
    '''

def p_val(p):
    '''
    val : value
    | openParenthesis arithmeticExpression closeParenthesis
    '''

def p_unaryExpression(p):
    '''
    unaryExpression : id plusPlus
    | id minusMinus
    | plusPlus id
    | minusMinus id
    '''

def p_value(p):
    '''
    value : intValue action_int_value
    | doubleValue action_double_value
    | id action_var_value
    '''

def p_func(p):
    '''
    func : function id openParenthesis closeParenthesis openBrace subroutine closeBrace func
    |
    '''

def p_mainProgram(p):
    '''
    mainProgram : main openParenthesis closeParenthesis openBrace subroutine closeBrace
    '''

def p_subroutine(p):
    '''
    subroutine : consoleWrite openParenthesis cout closeParenthesis semicolon subroutine
    | consoleRead openParenthesis id closeParenthesis semicolon subroutine
    | if openParenthesis statement closeParenthesis openBrace subroutine closeBrace elseStatement subroutine
    | while openParenthesis statement closeParenthesis openBrace subroutine closeBrace subroutine
    | for openParenthesis varSequence semicolon statement semicolon arithmeticExpression closeParenthesis openBrace subroutine closeBrace subroutine
    | id equal arithmeticExpression action_generate_quadruplet semicolon subroutine
    | unaryExpression semicolon subroutine
    | call id openParenthesis closeParenthesis semicolon subroutine
    |
    '''
def p_elseStatement(p):
    '''
    elseStatement : elif openParenthesis statement closeParenthesis openBrace subroutine closeBrace elseStatement
    | else openBrace subroutine closeBrace
    |
    '''

def p_statement(p):
    '''
    statement : arithmeticExpression
    | arithmeticExpression logicExpression arithmeticExpression
    | statement logicExpression statement
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

def p_cout(p):
    '''
    cout : arithmeticExpression
    | string
    '''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def add_symbol(name, data_type):
    global symbols_table_index
    symbols_table[name] = symbols_table_structure(name, data_type, '#' + str(symbols_table_index))
    symbols_table_index += 1

def p_action_var_value(p):
    "action_var_value :"
    operands_stack.append(symbols_table[p[-1]].address)
    types_stack.append(symbols_table[p[-1]].type)

def p_action_int_value(p):
    "action_int_value :"
    operands_stack.append(p[-1])
    types_stack.append('int')

def p_action_double_value(p):
    "action_double_value :"
    operands_stack.append(p[-1])
    types_stack.append('double')

def p_action_add_operator(p):
    "action_add_operator :"
    operators_stack.append(p[-1])

def p_action_generate_quadruplet(p):
    "action_generate_quadruplet :"
    operator = p[-2]
    operand = p[-3]
    # variable_type = symbols_table[operand].type
    variable_address = symbols_table[operand].address
    value = operands_stack.pop()
    quadruplets.append(str(operator) + ' ' + str(value) + ' ' + str(variable_address))

def add_quadruplet():
    global quadruplet_index
    operator = operators_stack.pop()
    right_operand = operands_stack.pop()
    # right_operandType = typesStack.pop()
    left_operand = operands_stack.pop()
    # left_operandType = typesStack.pop()
    # typesStack.append(validType(operator, left_operandType, right_operandType))
    temp = available.pop(0)
    quadruplets.append(str(operator) + ' ' + str(left_operand) + ' ' + str(right_operand) + ' ' + str(temp))
    quadruplet_index += 1
    operands_stack.append(temp)

def p_action_quadruplet_arithmetic_expression(p):
    "action_quadruplet_arithmetic_expression :"
    operator = peek(operators_stack) 
    if operator == "+" or operator == "-":
        add_quadruplet()

def p_action_quadruplet_multiply_divide(p):
    "action_quadruplet_multiply_divide :"
    operator = peek(operators_stack) 
    if operator == "*" or operator == "/":
        add_quadruplet()    

# Build the parser
parser = yacc.yacc()
 
if (len(sys.argv) > 1):
    program_name = sys.argv[1]
    program_file = open(program_name, "r")
    program = program_file.read().replace('\\n', '\n')
    parser.parse(program)
    program_file.close()
else:
    raise Exception('''Test file not provided''')