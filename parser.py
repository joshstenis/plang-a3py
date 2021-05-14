# ------------------------------------------------------------
# Programming Assignment #3 Python Rewrite
# ---------------------------------------------
# Author: Josh Stenis
# ------------------------------------------------------------

tokens = (
    'WRITE', 'READ', 'LPAREN', 'RPAREN', 'ASSIGN', 'SEMICOLON', 'COMMA',  
    'ADD', 'SUB', 'MUL', 'DIV', 
    'DT_INT', 'DT_FLOAT', 'FLOAT', 'INTEGER', 'ID'
)

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
def t_ASSIGN(t):
    r':='
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
    t.value = float(t.value)
    return t
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_ID(t):
    r'([a-zA-Z_])\w*'
    return t

t_ignore = ' \t'

# Skips new line characters and updates lexer.lineno
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    pass

import ply.lex as lex
l = lex.lex()


# ---------------------------------------------
# Grammar rules (.y) below
# ---------------------------------------------

import re

env = {}
stack = []

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
    '''assignment : ID ASSIGN a_expr'''
    env[p[1]] = p[3]

def p_declaration(p):
    '''declaration : datatype ID'''
    if p[1] == 'int':
        env[p[2]] = int(0)
    elif p[1] == 'float':
        env[p[2]] = float(0)

def p_datatype(p):
    '''datatype : DT_INT 
        | DT_FLOAT'''
    p[0] = p[1]

def p_a_expr(p):
    '''a_expr : a_expr a_op a_expr
              | varref
              | INTEGER
              | FLOAT
              | LPAREN a_expr RPAREN
              | SUB a_expr'''
    try:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
        elif p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    except:
        if p[1] == '(':
            p[0] = p[1]
        elif p[1] == '-':
            p[0] = p[2] * -1
        else: p[0] = p[1]

def p_a_op(p):
    '''a_op : MUL 
            | DIV
            | ADD 
            | SUB'''
    p[0] = p[1]

def p_varref(p):
    '''varref : ID'''
    print(env[p[1]])
    p[0] = env[p[1]]

def p_read(p):
    '''read : READ varlist'''
    stackReadWrite(p[2], 'r')

def p_write(p):
    '''write : WRITE expr_list'''
    stackReadWrite(p[2], 'w')

def p_varlist(p):
    '''varlist : varlist COMMA varref 
        | varref'''
    try:
        p[0] = [p[1], p[3]]
    except IndexError:
        p[0] = p[1]

def p_expr_list(p):
    '''expr_list : expr_list COMMA a_expr 
        | a_expr'''
    try:
        p[0] = [p[1], p[3]]
    except IndexError:
        p[0] = p[1]

def p_error(p):
    print('Parsing error: "{0}" at line {1}'.format(p, p.lexer.lineno))

import ply.yacc as yacc
p = yacc.yacc()

# Evaluates a_expr then returns result (i.e. calculator)
def evalExpr(e):
    global env
    if type(e) is list:
        if e[0] == 'NEGATIVE':
            return evalExpr(e[1]) * -1
        elif e[0] == '*':
            return evalExpr(e[1]) * evalExpr(e[2])
        elif e[0] == '/':
            return evalExpr(e[1]) / evalExpr(e[2])
        elif e[0] == '+':
            return evalExpr(e[1]) + evalExpr(e[2])
        elif e[0] == '-':
            return evalExpr(e[1]) - evalExpr(e[2])
    else:
        if type(e) is str:
            return env[e]
        else:
            return e

# Traverses next lists (expr_list and varlist)
# NOTE: Specifically for READ and WRITE
def stackReadWrite(l, op):
    if op == 'w':
        if type(l) is list:
            stackReadWrite(l[0], op)
            stackReadWrite(l[1], op)
        else:
            stack.append(l)
    if op == 'r':
        if type(l) is list:
            stackReadWrite(l[0], op)
            stackReadWrite(l[1], op)
        else:
            if l in stack:
                print('Read \'{}\''.format(l))
            else:
                print('Var \'{}\' not in stack.'.format(l))


# ---------------------------------------------
# Run parser
# ---------------------------------------------

prgm = open('inputs-{0}/{1}.smp'.format(input('Type: '), input('File: ')), 'r').read()
p.parse(prgm, l)
print('Declaration environment: {0}\nStack: {1}'.format(env, stack))