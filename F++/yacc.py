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
jumps_stack = []
ifs_stack = []
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
    for i in range (len(quadruplets)):
        print(str(i+1) + ') ' + quadruplets[i])
	
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
    unaryExpression : id plusPlus
    | id minusMinus
    | plusPlus id
    | minusMinus id
    '''

def p_value(p):
    '''
    value : intValue ACTION_INT_VALUE
    | doubleValue ACTION_DOUBLE_VALUE
    | id ACTION_VAR_VALUE
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
    | if openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_NEW_IF ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement ACTION_FILL_JUMP_END_IF subroutine
    | while openParenthesis statement closeParenthesis openBrace subroutine closeBrace subroutine
    | for openParenthesis varSequence semicolon statement semicolon arithmeticExpression closeParenthesis openBrace subroutine closeBrace subroutine
    | id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon subroutine
    | unaryExpression semicolon subroutine
    | call id openParenthesis closeParenthesis semicolon subroutine
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
    p[0] = p[1]

def p_cout(p):
    '''
    cout : arithmeticExpression
    | string
    '''

# Error rule for syntax errors
def p_error(p):
    raise Exception("Syntax error in input!")

def add_symbol(name, data_type):
    global symbols_table_index
    symbols_table[name] = symbols_table_structure(name, data_type, '#' + str(symbols_table_index))
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
    global quadruplet_index
    global available
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

def p_ACTION_FILL_JUMP_end_if(p):
    "ACTION_FILL_JUMP_END_IF :"
    for goto_index in ifs_stack[len(ifs_stack) - 1]:
        fill_jump(goto_index - 1, quadruplet_index)
    ifs_stack.pop()

def p_action_fill_jump(p):
    "ACTION_FILL_JUMP :"
    fill_jump(jumps_stack.pop() - 1, quadruplet_index)

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
else:
    raise Exception('''Test file not provided''')