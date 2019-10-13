import ply.yacc as yacc
import sys

# Get the token map from the lexer.  This is required.
from lex import tokens

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

def p_varSequence(p):
    '''
    varSequence : id equal arithmeticExpression
        | id
        | matrix
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

def p_matrix(p):
    '''
    matrix : id openBracket value closeBracket
    | id openBracket value closeBracket openBracket value closeBracket
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
    | matrix equal arithmeticExpression semicolon subroutine
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