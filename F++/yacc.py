import ply.yacc as yacc
import sys
from common import symbols_table_structure

# Get the token map from the lexer.  This is required.
from lex import tokens

symbols_table = {}

def p_program(p):
    '''
	program : var func mainProgram
    '''
    print('Valid program!!!')
	
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
    arithmeticExpression : value
    | value plus arithmeticExpression
    | value minus arithmeticExpression
    | value multiply arithmeticExpression
    | value divide arithmeticExpression
    | openParenthesis arithmeticExpression closeParenthesis
    | openParenthesis arithmeticExpression closeParenthesis plus arithmeticExpression
    | openParenthesis arithmeticExpression closeParenthesis minus arithmeticExpression
    | openParenthesis arithmeticExpression closeParenthesis divide arithmeticExpression
    | openParenthesis arithmeticExpression closeParenthesis multiply arithmeticExpression
    | unaryExpression
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
    value : intValue
    | doubleValue
    | id
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
    | id equal arithmeticExpression semicolon subroutine
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
    symbols_table[name] = symbols_table_structure(name, data_type)
    

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