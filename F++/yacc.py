import ply.yacc as yacc
import sys

# Get the token map from the lexer.  This is required.
from lex import tokens

def p_program(p):
    '''
	program : var
    '''
	print('Valid program')

def p_var(p):
    '''
    var : type varSequence var
    |
    '''

def p_varSequence(p):
    '''
    varSequence : id equal arithmeticExpression semicolon
        | id semicolon
        | matrix semicolon
        | id equal arithmeticExpression comma varSequence
        | id comma varSequence
        | matrix comma varSequence
    '''

def p_type(p):
    '''
    type : int
    | double
    '''

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
    '''

def p_value(p):
    '''
    value : intValue
    | doubleValue
    | id
    '''

def p_matrix(p):
    '''
    matrix : id openBracket value closeBracket
    | id openBracket value closeBracket openBracket value closeBracket
    '''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
 
if (len(sys.argv) > 1):
    programName = sys.argv[1]
    programFile = open(programName, "r")
    program = programFile.read().replace('\\n', '\n')
    parser.parse(program)
    programFile.close()
else:
    raise Exception('''Test file not provided''')