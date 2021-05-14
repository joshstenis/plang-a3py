
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ASSIGN COLON COMMA COMMENT DIV DT_FLOAT DT_INT FLOAT ID INTEGER LBRACK LITERAL_STR LPAREN MUL RBRACK READ RPAREN SEMICOLON SUB WRITEprogram : stmt_list SEMICOLONstmt_list : stmt_list SEMICOLON stmt \n        | stmtstmt : assignment \n        | read \n        | write \n        | declarationassignment : varref ASSIGN a_exprdeclaration : datatype IDdatatype : DT_INT \n        | DT_FLOATa_expr : a_expr a_op a_expr\n              | SUB a_expr \n              | INTEGER\n              | FLOAT\n              | varref\n              | LPAREN a_expr RPARENa_op : ADD \n            | SUB \n            | MUL \n            | DIVvarref : IDread : READ varlistwrite : WRITE expr_listvarlist : varlist COMMA varref \n        | varrefexpr_list : expr_list COMMA a_expr \n        | a_expr'
    
_lr_action_items = {'READ':([0,15,],[9,9,]),'WRITE':([0,15,],[10,10,]),'ID':([0,9,10,11,13,14,15,16,21,25,29,30,31,32,33,34,35,],[12,12,12,26,-10,-11,12,12,12,12,12,12,12,-18,-19,-20,-21,]),'DT_INT':([0,15,],[13,13,]),'DT_FLOAT':([0,15,],[14,14,]),'$end':([1,15,],[0,-1,]),'SEMICOLON':([2,3,4,5,6,7,12,17,18,19,20,22,23,24,26,27,28,36,38,39,40,41,],[15,-3,-4,-5,-6,-7,-22,-23,-26,-24,-28,-14,-15,-16,-9,-2,-8,-13,-25,-27,-12,-17,]),'ASSIGN':([8,12,],[16,-22,]),'SUB':([10,12,16,20,21,22,23,24,25,28,30,31,32,33,34,35,36,37,39,40,41,],[21,-22,21,33,21,-14,-15,-16,21,33,21,21,-18,-19,-20,-21,33,33,33,33,-17,]),'INTEGER':([10,16,21,25,30,31,32,33,34,35,],[22,22,22,22,22,22,-18,-19,-20,-21,]),'FLOAT':([10,16,21,25,30,31,32,33,34,35,],[23,23,23,23,23,23,-18,-19,-20,-21,]),'LPAREN':([10,16,21,25,30,31,32,33,34,35,],[25,25,25,25,25,25,-18,-19,-20,-21,]),'COMMA':([12,17,18,19,20,22,23,24,36,38,39,40,41,],[-22,29,-26,30,-28,-14,-15,-16,-13,-25,-27,-12,-17,]),'ADD':([12,20,22,23,24,28,36,37,39,40,41,],[-22,32,-14,-15,-16,32,32,32,32,32,-17,]),'MUL':([12,20,22,23,24,28,36,37,39,40,41,],[-22,34,-14,-15,-16,34,34,34,34,34,-17,]),'DIV':([12,20,22,23,24,28,36,37,39,40,41,],[-22,35,-14,-15,-16,35,35,35,35,35,-17,]),'RPAREN':([12,22,23,24,36,37,40,41,],[-22,-14,-15,-16,-13,41,-12,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([0,],[2,]),'stmt':([0,15,],[3,27,]),'assignment':([0,15,],[4,4,]),'read':([0,15,],[5,5,]),'write':([0,15,],[6,6,]),'declaration':([0,15,],[7,7,]),'varref':([0,9,10,15,16,21,25,29,30,31,],[8,18,24,8,24,24,24,38,24,24,]),'datatype':([0,15,],[11,11,]),'varlist':([9,],[17,]),'expr_list':([10,],[19,]),'a_expr':([10,16,21,25,30,31,],[20,28,36,37,39,40,]),'a_op':([20,28,36,37,39,40,],[31,31,31,31,31,31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list SEMICOLON','program',2,'p_program','parser.py',110),
  ('stmt_list -> stmt_list SEMICOLON stmt','stmt_list',3,'p_stmt_list','parser.py',114),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','parser.py',115),
  ('stmt -> assignment','stmt',1,'p_stmt','parser.py',120),
  ('stmt -> read','stmt',1,'p_stmt','parser.py',121),
  ('stmt -> write','stmt',1,'p_stmt','parser.py',122),
  ('stmt -> declaration','stmt',1,'p_stmt','parser.py',123),
  ('assignment -> varref ASSIGN a_expr','assignment',3,'p_assignment','parser.py',127),
  ('declaration -> datatype ID','declaration',2,'p_declaration','parser.py',131),
  ('datatype -> DT_INT','datatype',1,'p_datatype','parser.py',142),
  ('datatype -> DT_FLOAT','datatype',1,'p_datatype','parser.py',143),
  ('a_expr -> a_expr a_op a_expr','a_expr',3,'p_a_expr','parser.py',147),
  ('a_expr -> SUB a_expr','a_expr',2,'p_a_expr','parser.py',148),
  ('a_expr -> INTEGER','a_expr',1,'p_a_expr','parser.py',149),
  ('a_expr -> FLOAT','a_expr',1,'p_a_expr','parser.py',150),
  ('a_expr -> varref','a_expr',1,'p_a_expr','parser.py',151),
  ('a_expr -> LPAREN a_expr RPAREN','a_expr',3,'p_a_expr','parser.py',152),
  ('a_op -> ADD','a_op',1,'p_a_op','parser.py',177),
  ('a_op -> SUB','a_op',1,'p_a_op','parser.py',178),
  ('a_op -> MUL','a_op',1,'p_a_op','parser.py',179),
  ('a_op -> DIV','a_op',1,'p_a_op','parser.py',180),
  ('varref -> ID','varref',1,'p_varref','parser.py',184),
  ('read -> READ varlist','read',2,'p_read','parser.py',189),
  ('write -> WRITE expr_list','write',2,'p_write','parser.py',194),
  ('varlist -> varlist COMMA varref','varlist',3,'p_varlist','parser.py',199),
  ('varlist -> varref','varlist',1,'p_varlist','parser.py',200),
  ('expr_list -> expr_list COMMA a_expr','expr_list',3,'p_expr_list','parser.py',206),
  ('expr_list -> a_expr','expr_list',1,'p_expr_list','parser.py',207),
]
