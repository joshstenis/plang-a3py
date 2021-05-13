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

t_LITERAL_STR = r'\".+\"'
t_WRITE = r'write'
t_READ = r'read'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_COLON = r':'
t_ASSIGN = r':='
t_SEMICOLON = r';'
t_COMMA = r','
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_DT_INT = r'int'
t_DT_FLOAT = r'float'
t_FLOAT = r'\d+[.]\d+'
t_INTEGER = r'\d+'
t_ID = r'([a-zA-Z_])\w*'

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

def p_program(t):
    '''program : stmt_list SEMICOLON'''

def p_stmt_list(t):
    '''stmt_list : stmt_list SEMICOLON stmt 
        | stmt'''

def p_stmt(t):
    '''stmt : assignment 
        | read 
        | write 
        | declaration'''

def p_assignment(t):
    '''assignment : varref ASSIGN a_expr'''
    # ACTION: store value and datatype (view OP_STORE)

def p_declaration(t):
    '''declaration : datatype ID'''
    # ACTION: create symbol object (see symbol_create)

def p_datatype(t):
    '''datatype : DT_INT 
        | DT_FLOAT'''
    # ACTION: typecast for DT_INT and DT_FLOAT (see grammar.y)

def p_a_expr(t):
    '''a_expr : a_expr ADD a_term 
        | a_expr SUB a_term 
        | a_term'''
    # ACTION: handle terms with care for typing (see grammar.y)

def p_a_term(t):
    '''a_term : a_term MUL a_fact 
        | a_term DIV a_fact 
        | a_fact'''
    # ACTION: handle terms with care for typing (see grammar.y)

def p_a_fact(t):
    '''a_fact : varref 
        | INTEGER 
        | FLOAT 
        | LPAREN a_expr RPAREN 
        | SUB a_fact
        | LITERAL_STR'''
    # ACTION: load associated value (see OP_LOAD and OP_LOADCST)

def p_varref(t):
    '''varref : ID'''
    # ACTION: find associated variable (see symtab.cc)

def p_read(t):
    '''read : READ varlist'''
    # ACTION: iterate through varref objects (see OP_READ)

def p_write(t):
    '''write : WRITE expr_list'''
    # ACTION: write given variable to symbol_t objects (see OP_WRITE)

def p_varlist(t):
    '''varlist : varlist COMMA varref 
        | varref'''
    # ACTION: stack manipulation, not sure if python needs this (see grammar.y)

def p_expr_list(t):
    '''expr_list : expr_list COMMA a_expr 
        | a_expr'''
    # ACTION: stack manipulation, not sure if python needs this (see grammar.y)

def p_error(t):
    print('Parsing error: "{0}" at line {1}'.format(t.value, t.lexer.lineno))

import ply.yacc as yacc
p = yacc.yacc()


# ---------------------------------------------
# Run parser
# ---------------------------------------------

prgm = open('inputs-{0}/{1}.smp'.format(input('Type: '), input('File: ')), 'r').read()
p.parse(prgm, l)