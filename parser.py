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

# Takes in 2 a_expr's and an a_op, then return result of the operation
# def getResult(op, e1, e2):
#     if op == 'MUL':
#         return e1.value * e2.value
#     elif op == 'DIV':
#         return e1.value / e2.value
#     elif op == 'ADD':
#         return e1.value + e2.value
#     elif op == 'SUB':
#         return e1.value - e2.value
#     else: return None


import re

def p_program(p):
    '''program : stmt_list SEMICOLON'''
    print('{} ;'.format(p[1]))

def p_stmt_list(p):
    '''stmt_list : stmt_list SEMICOLON stmt 
        | stmt'''
    try:
        p[0] = (p[1], ';', p[3])
    except IndexError:
        p[0] = p[1]

def p_stmt(p):
    '''stmt : assignment 
        | read 
        | write 
        | declaration'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : varref ASSIGN a_expr'''
    p[0] = (':=', p[1], p[3])

def p_declaration(p):
    '''declaration : datatype ID'''
    p[0] = (p[1], p[2])
    
    # =======- CHECK ME -=======
    
    # if p[1] == 'DT_INT':
    #     p[0] = int(p[2])
    # elif p[1] == 'DT_FLOAT':
    #     p[0] = float(p[2])

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
              | LPAREN a_expr RPAREN'''
    try:
        if re.compile(r'\+|-|\*|/').match(p[2]): p[0] = (p[2], p[1], p[3])
    except IndexError:
        if p[1] == 'SUB': p[0] = ('NEGATIVE', p[2])
        elif p[1] == 'LPAREN': p[0] = ('(', p[2], ')')
        else: p[0] = p[1]
    

    # =======- CHECK ME -=======

    # if p[1] == 'SUB':
    #     p[0] = -1 * p[2]
    # elif p[1] == 'INTEGER':
    #     if p[2] is None:
    #         p[0] = int(p[1])
    #     elif p[2] == 'a_op' and p[3] == 'FLOAT':
    #         p[0] = getResult(p[2], float(p[1]),  float(p[3]))
    #     else:
    #         p[0] = getResult(p[2], int(p[1]),  int(p[3]))
    # elif p[1] == 'FLOAT':
    #     if p[2] is None:
    #         p[0] = float(p[1])
    #     elif p[2] == 'a_op':
    #         p[0] = getResult(p[2], float(p[1]),  float(p[3]))

def p_a_op(p):
    '''a_op : ADD 
            | SUB 
            | MUL 
            | DIV'''
    p[0] = p[1]

def p_varref(p):
    '''varref : ID'''
    p[0] = p[1]
    # ACTION: find associated variable (see symtab.cc)

def p_read(p):
    '''read : READ varlist'''
    p[0] = (p[1], p[2])
    # ACTION: iterate through varref objects (see OP_READ)

def p_write(p):
    '''write : WRITE expr_list'''
    p[0] = (p[1], p[2])
    # ACTION: write given variable to symbol_t objects (see OP_WRITE)

def p_varlist(p):
    '''varlist : varlist COMMA varref 
        | varref'''
    try:
        p[0] = (p[1], p[3])
    except IndexError:
        p[0] = p[1]
    # ACTION: stack manipulation, not sure if python needs this (see grammar.y)

def p_expr_list(p):
    '''expr_list : expr_list COMMA a_expr 
        | a_expr'''
    try:
        p[0] = (p[1], p[3])
    except IndexError:
        p[0] = p[1]
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