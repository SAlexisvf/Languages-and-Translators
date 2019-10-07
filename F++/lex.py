import ply.lex as lex

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
    'while':'while',
    'for':'for',
    'and':'and',
    'or':'or',
}

# List of token names.   This is always required
tokens = [
    # identifier for variables and functions
    'id',

    # data types and values
    'int',
    'double',
    'intValue',
    'doubleValue',

    # logic operators
    'and',
    'or',
    'isEqual',
    'notEqual',
    'greaterThan',
    'lessThan',

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

    # conditionals and cycles
    'if',
    'else',
    'while',
    'for',

    # data input/output
    'consoleRead',
    'consoleWrite',

    # reserved names
    'main',
    'function',

    # comment 
    'comment'
]

tokens = tokens + list(reserved.values())

# Regular expression rules for simple tokens
t_isEqual = r'\=\='
t_notEqual = r'\!\='
t_greaterThan = r'\>'
t_lessThan = r'\<'
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
    t.type = reserved.get(t.value,'id')    # Check for reserved words
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()