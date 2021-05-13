# ------------------------------------------------------------
# Programming Assignment #3 Python Rewrite
# ---------------------------------------------
# Author: Josh Stenis
# ------------------------------------------------------------

tokens = (
    'LITERAL_STR', 'WRITE', 'READ', 'LPAREN', 'RPAREN', 'LBRACK', 'RBRACK', 'ASSIGN', 'SEMICOLON', 'COLON', 'COMMA', 'COMMENT', 
    'ADD', 'SUB', 'MUL', 'DIV', 
    'DT_INT', 'DT_FLOAT', 'FLOAT', 'INTEGER', 'ID'
)

def t_LITERAL_STR(t):
    r'\".+\"'
    return t
def t_WRITE(t):
    r'write'
    return t
def t_READ(t):
    r'read'
    return t
def t_LPAREN(t):
    r'\('
    return t
def t_RPAREN(t):
    r'\)'
    return t
def t_LBRACK(t):
    r'\['
    return t
def t_RBRACK(t):
    r'\]'
    return t
def t_ASSIGN(t):
    r':='
    return t
def t_COLON(t):
    r':'
    return t
def t_SEMICOLON(t):
    r';'
    return t
def t_COMMA(t):
    r','
    return t
def t_ADD(t):
    r'\+'
    return t
def t_SUB(t):
    r'-'
    return t
def t_MUL(t):
    r'\*'
    return t
def t_DIV(t):
    r'/'
    return t
def t_DT_INT(t):
    r'int'
    return t
def t_DT_FLOAT(t):
    r'float'
    return t
def t_FLOAT(t):
    r'\d+[.]\d+'
    return t
def t_INTEGER(t):
    r'\d+'
    return t
def t_ID(t):
    r'([a-zA-Z_])\w*'
    return t

t_ignore = ' \t'

# Skips new line characters and updates lexer.lineno
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Skips commented lines
def t_COMMENT(t):
    r'\/\/.*$'
    t.lexer.lineno += 1

def t_error(t):
    pass

import ply.lex as lex
l = lex.lex()


# ---------------------------------------------
# Grammar rules (.y) below
# ---------------------------------------------

def p_program(p):
    '''program : stmt_list SEMICOLON'''

def p_stmt_list(p):
    '''stmt_list : stmt_list SEMICOLON stmt 
        | stmt'''

def p_stmt(p):
    '''stmt : assignment 
        | read 
        | write 
        | declaration'''

def p_assignment(p):
    '''assignment : varref ASSIGN a_expr'''
    if p[3] == 'FLOAT':
        p[0] = float(p[3])
    elif p[3] == 'INTEGER':
        p[0] = int(p[3])

def p_declaration(p):
    '''declaration : datatype ID'''
    if p[1] == 'DT_INT':
        p[0] = int(p[2])
    elif p[1] == 'DT_FLOAT':
        p[0] = float(p[2])

def p_datatype(p):
    '''datatype : DT_INT 
        | DT_FLOAT'''
    p[0] = p[1]

def p_a_expr(p):
    '''a_expr : a_expr a_op a_expr
              | SUB a_expr 
              | INTEGER
              | FLOAT
              | varref
              | LITERAL_STR 
              | LPAREN a_expr RPAREN'''
    # ACTION: handle terms according to type (see grammar.y)

def p_a_op(p):
    '''a_op : ADD 
            | SUB 
            | MUL 
            | DIV'''
    # ACTION: load associated value (see OP_LOAD and OP_LOADCST)

def p_varref(p):
    '''varref : ID'''
    # ACTION: find associated variable (see symtab.cc)

def p_read(p):
    '''read : READ varlist'''
    # ACTION: iterate through varref objects (see OP_READ)

def p_write(p):
    '''write : WRITE expr_list'''
    # ACTION: write given variable to symbol_t objects (see OP_WRITE)

def p_varlist(p):
    '''varlist : varlist COMMA varref 
        | varref'''
    # ACTION: stack manipulation, not sure if python needs this (see grammar.y)

def p_expr_list(p):
    '''expr_list : expr_list COMMA a_expr 
        | a_expr'''
    # ACTION: stack manipulation, not sure if python needs this (see grammar.y)

def p_error(p):
    print('Parsing error: "{0}" at line {1}'.format(p, p.lexer.lineno))

import ply.yacc as yacc
p = yacc.yacc()


# ---------------------------------------------
# Run parser
# ---------------------------------------------

prgm = open('inputs-{0}/{1}.smp'.format(input('Type: '), input('File: ')), 'r').read()
p.parse(prgm, l)