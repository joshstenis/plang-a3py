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

# Yields lines one at a time for runLine to properly engage action code
def run(tree):
    line = []
    print(tree)

    for i in tree:
        if type(i) is not list:
            print(line)
            action(line[0])
            line.clear()
        else:
            line.append(i)

def p_program(p):
    '''program : stmt_list SEMICOLON'''
    # print('\n{}'.format(p[1]))
    run(p[1])

def p_stmt_list(p):
    '''stmt_list : stmt_list SEMICOLON stmt 
        | stmt'''
    try:
        p[0] = [p[1], ';', p[3]]
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
    p[0] = [':=', p[1], p[3]]

def p_declaration(p):
    '''declaration : datatype ID'''
    p[0] = [p[1], p[2]]

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
        if re.compile(r'\+|-|\*|/').match(p[2]): p[0] = [p[2], p[1], p[3]]
    except IndexError:
        if p[1] == 'SUB': p[0] = ('NEGATIVE', p[2])
        elif p[1] == 'LPAREN': p[0] = ['(', p[2], ')']
        else: p[0] = p[1]

def p_a_op(p):
    '''a_op : ADD 
            | SUB 
            | MUL 
            | DIV'''
    p[0] = p[1]

def p_varref(p):
    '''varref : ID'''
    p[0] = p[1]

def p_read(p):
    '''read : READ varlist'''
    p[0] = [p[1], p[2]]

def p_write(p):
    '''write : WRITE expr_list'''
    p[0] = [p[1], p[2]]

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

# ((('int', 'a'), ';', (':=', 'a', ('+', '1', '1'))), ';', ('write', 'a')

env = {}
stack = []
# Action code executed here
def action(p):
    global env, stack

    if type(p) is list:
        if p[0] == 'int':
            env[p[1]] = int(0)
            print(p)
        if p[0] == ':=':
            env[p[1]] = action(p[2])
            print('{0} assigned to {1}'.format(env[p[1]], p[1]))
        if p[0] == '*':
            return action(p[1]) * action(p[2])
        elif p[0] == '/':
            return action(p[1]) / action(p[2])
        elif p[0] == '+':
            return action(p[1]) + action(p[2])
        elif p[0] == '-':
            return action(p[1]) - action(p[2])
    else:
        return p




    #     elif p[0] == 'write':
    #     if run(p[1]) in env:
    #         stack.insert(0, (run(p[1]), env[run(p[1])]))
    #         return 'Wrote {} to stack'.format(env[run(p[1])])
    #     else:
    #         stack.insert(0, run(p[1]))
    # elif p[0] == 'read':
    #     if run(p[1]) in stack:
    #         return '{}'.format(stack[run(p[1])])
    #     else:
    #         return 'Variable not in stack.'

# ---------------------------------------------
# Run parser
# ---------------------------------------------

prgm = open('inputs-{0}/{1}.smp'.format(input('Type: '), input('File: ')), 'r').read()
p.parse(prgm, l)
print('Declaration environment: {0}\nStack: {1}'.format(env, stack))