
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'and call closeBrace closeBracket closeParenthesis comma consoleRead consoleWrite divide do double doubleValue elif else equal for function greaterOrEqual greaterThan id if int intValue isEqual lessOrEqual lessThan main minus minusMinus multiply not notEqual openBrace openBracket openParenthesis or plus plusPlus semicolon string while\n\tprogram : var func mainProgram\n    \n    var : type varSequence semicolon var\n    |\n    \n    varSequence : variable equal arithmeticExpression\n        | variable\n        | variable equal arithmeticExpression comma varSequence\n        | variable comma varSequence\n    \n    variable : id dimentions\n    \n    dimentions : openBracket value closeBracket\n    | openBracket value closeBracket openBracket value closeBracket\n    |\n    \n    type : int\n    | double\n    \n    arithmeticExpression : multiplyDivide\n    | arithmeticExpression plus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET\n    | arithmeticExpression minus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET\n    \n    multiplyDivide : val\n    | multiplyDivide multiply ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET\n    | multiplyDivide divide ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET\n    \n    val : value\n    | unaryExpression\n    | openParenthesis arithmeticExpression closeParenthesis\n    \n    unaryExpression : id ACTION_UNARY_ADD_OPERANDS plusPlus ACTION_UNARY_PLUS\n    | id ACTION_UNARY_ADD_OPERANDS minusMinus ACTION_UNARY_MINUS\n    \n    value : intValue ACTION_INT_VALUE\n    | doubleValue ACTION_DOUBLE_VALUE\n    | id ACTION_VAR_VALUE\n    \n    func : function id openParenthesis closeParenthesis openBrace subroutine closeBrace func\n    |\n    \n    mainProgram : main openParenthesis closeParenthesis openBrace subroutine closeBrace\n    \n    subroutine : consoleWrite openParenthesis cout closeParenthesis semicolon subroutine\n    | consoleRead openParenthesis id closeParenthesis semicolon subroutine\n    | if openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_NEW_IF ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement ACTION_FILL_JUMP_END_IF subroutine\n    | while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_WHILE_GOTO subroutine\n    | do ACTION_DO_WHILE_INDEX openBrace subroutine closeBrace while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE semicolon subroutine\n    | for openParenthesis id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon statement semicolon ACTION_QUADRUPLET_EMPTY_JUMP arithmeticExpression closeParenthesis openBrace subroutine closeBrace ACTION_WHILE_GOTO subroutine\n    | id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon subroutine\n    | unaryExpression semicolon subroutine\n    | call id openParenthesis closeParenthesis semicolon subroutine\n    |\n    \n    elseStatement : elif ACTION_FILL_JUMP openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement\n    | else ACTION_FILL_JUMP openBrace subroutine closeBrace\n    | ACTION_FILL_JUMP\n    \n    statement : arithmeticExpression \n    | arithmeticExpression logicExpression ACTION_ADD_OPERATOR arithmeticExpression ACTION_ADD_QUADRUPLET\n    | statement logicExpression ACTION_ADD_OPERATOR statement ACTION_ADD_QUADRUPLET\n    \n    logicExpression : greaterThan\n    | lessThan\n    | isEqual\n    | notEqual\n    | greaterOrEqual\n    | lessOrEqual\n    | and\n    | or\n    \n    cout : arithmeticExpression\n    | string\n    ACTION_VAR_VALUE :ACTION_INT_VALUE :ACTION_DOUBLE_VALUE :ACTION_UNARY_ADD_OPERANDS :ACTION_UNARY_PLUS :ACTION_UNARY_MINUS :ACTION_ADD_OPERATOR :ACTION_GENERATE_QUADRUPLET :ACTION_ADD_QUADRUPLET :ACTION_QUADRUPLET_EMPTY_JUMP :ACTION_NEW_IF :ACTION_QUADRUPLET_EMPTY_JUMP_END_IF :ACTION_FILL_JUMP_END_IF :ACTION_FILL_JUMP :ACTION_WHILE_GOTO :ACTION_DO_WHILE_INDEX :ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE :'
    
_lr_action_items = {'function':([0,2,14,21,86,],[-3,7,-3,-2,7,]),'main':([0,2,6,14,21,86,104,],[-3,-29,12,-3,-2,-29,-28,]),'int':([0,14,],[4,4,]),'double':([0,14,],[5,5,]),'$end':([1,11,76,],[0,-1,-30,]),'id':([3,4,5,7,15,16,18,27,36,37,38,39,40,47,48,50,51,52,53,57,67,77,78,79,80,81,83,84,100,109,110,111,112,113,114,115,116,117,118,121,123,124,125,127,128,132,136,139,147,148,149,150,153,154,156,157,160,161,163,165,167,173,174,175,180,181,183,184,187,188,189,],[10,-12,-13,13,30,10,33,30,10,-63,-63,-63,-63,61,61,30,30,30,30,33,85,30,95,30,30,30,101,61,61,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,30,61,61,61,30,30,61,61,61,30,30,-67,-71,-68,61,-66,-70,30,-69,-43,61,61,30,61,61,-42,-71,61,61,-68,-70,-41,]),'semicolon':([8,9,10,17,22,23,24,25,26,28,29,30,31,42,43,44,46,49,54,55,56,66,69,70,71,72,73,74,87,88,89,90,91,96,98,105,106,107,122,131,137,138,141,144,145,152,155,159,],[14,-5,-11,-8,-4,-14,-17,-20,-21,-58,-59,-57,-7,-25,-26,-27,-9,-6,-22,-61,-62,84,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,-10,-64,-44,123,124,125,132,-64,-65,-65,148,-46,-45,156,-73,165,]),'equal':([9,10,17,46,61,91,101,],[15,-11,-8,-9,79,-10,121,]),'comma':([9,10,17,22,23,24,25,26,28,29,30,42,43,44,46,54,55,56,69,70,71,72,73,74,87,88,89,90,91,],[16,-11,-8,36,-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-9,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,-10,]),'openBracket':([10,46,],[18,57,]),'openParenthesis':([12,13,15,27,37,38,39,40,50,51,52,53,59,60,62,63,65,77,79,80,81,85,109,110,111,112,113,114,115,116,117,118,121,127,128,140,147,148,156,160,162,168,173,],[19,20,27,27,-63,-63,-63,-63,27,27,27,27,77,78,80,81,83,27,27,27,27,103,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,27,27,27,147,27,27,-66,27,-70,173,27,]),'intValue':([15,18,27,37,38,39,40,50,51,52,53,57,77,79,80,81,109,110,111,112,113,114,115,116,117,118,121,127,128,147,148,156,160,173,],[28,28,28,-63,-63,-63,-63,28,28,28,28,28,28,28,28,28,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,28,28,28,28,28,-66,28,28,]),'doubleValue':([15,18,27,37,38,39,40,50,51,52,53,57,77,79,80,81,109,110,111,112,113,114,115,116,117,118,121,127,128,147,148,156,160,173,],[29,29,29,-63,-63,-63,-63,29,29,29,29,29,29,29,29,29,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,29,29,29,29,29,-66,29,29,]),'closeParenthesis':([19,20,23,24,25,26,28,29,30,41,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,92,93,94,95,97,98,99,103,137,138,144,145,151,166,176,],[34,35,-14,-17,-20,-21,-58,-59,-57,54,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,105,-55,-56,106,108,-44,119,122,-65,-65,-46,-45,155,171,179,]),'plus':([22,23,24,25,26,28,29,30,41,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,93,96,98,131,138,166,],[37,-14,-17,-20,-21,-58,-59,-57,37,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,37,37,37,37,37,37,]),'minus':([22,23,24,25,26,28,29,30,41,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,93,96,98,131,138,166,],[38,-14,-17,-20,-21,-58,-59,-57,38,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,38,38,38,38,38,38,]),'greaterThan':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,110,110,110,110,-65,-46,-45,110,110,110,]),'lessThan':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,111,111,111,111,-65,-46,-45,111,111,111,]),'isEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,112,112,112,112,-65,-46,-45,112,112,112,]),'notEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,113,113,113,113,-65,-46,-45,113,113,113,]),'greaterOrEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,114,114,114,114,-65,-46,-45,114,114,114,]),'lessOrEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,115,115,115,115,-65,-46,-45,115,115,115,]),'and':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,116,116,116,116,-65,-46,-45,116,116,116,]),'or':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,137,138,144,145,151,152,176,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,117,117,117,117,-65,-46,-45,117,117,117,]),'multiply':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,89,90,],[39,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,39,39,-65,-65,-23,-24,-18,-19,]),'divide':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,89,90,],[40,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,40,40,-65,-65,-23,-24,-18,-19,]),'closeBracket':([28,29,32,33,42,43,44,75,],[-58,-59,46,-57,-25,-26,-27,91,]),'plusPlus':([30,45,61,],[-60,55,-60,]),'minusMinus':([30,45,61,],[-60,56,-60,]),'openBrace':([34,35,64,82,108,119,126,129,164,169,171,179,182,],[47,48,-72,100,-66,-66,136,139,-70,174,175,-66,184,]),'consoleWrite':([47,48,84,100,123,124,125,132,136,139,149,150,153,154,157,161,163,165,167,174,175,180,181,183,184,187,188,189,],[59,59,59,59,59,59,59,59,59,59,-67,-71,-68,59,-70,-69,-43,59,59,59,59,-42,-71,59,59,-68,-70,-41,]),'consoleRead':([47,48,84,100,123,124,125,132,136,139,149,150,153,154,157,161,163,165,167,174,175,180,181,183,184,187,188,189,],[60,60,60,60,60,60,60,60,60,60,-67,-71,-68,60,-70,-69,-43,60,60,60,60,-42,-71,60,60,-68,-70,-41,]),'if':([47,48,84,100,123,124,125,132,136,139,149,150,153,154,157,161,163,165,167,174,175,180,181,183,184,187,188,189,],[62,62,62,62,62,62,62,62,62,62,-67,-71,-68,62,-70,-69,-43,62,62,62,62,-42,-71,62,62,-68,-70,-41,]),'while':([47,48,84,100,123,124,125,130,132,136,139,149,150,153,154,157,161,163,165,167,174,175,180,181,183,184,187,188,189,],[63,63,63,63,63,63,63,140,63,63,63,-67,-71,-68,63,-70,-69,-43,63,63,63,63,-42,-71,63,63,-68,-70,-41,]),'do':([47,48,84,100,123,124,125,132,136,139,149,150,153,154,157,161,163,165,167,174,175,180,181,183,184,187,188,189,],[64,64,64,64,64,64,64,64,64,64,-67,-71,-68,64,-70,-69,-43,64,64,64,64,-42,-71,64,64,-68,-70,-41,]),'for':([47,48,84,100,123,124,125,132,136,139,149,150,153,154,157,161,163,165,167,174,175,180,181,183,184,187,188,189,],[65,65,65,65,65,65,65,65,65,65,-67,-71,-68,65,-70,-69,-43,65,65,65,65,-42,-71,65,65,-68,-70,-41,]),'call':([47,48,84,100,123,124,125,132,136,139,149,150,153,154,157,161,163,165,167,174,175,180,181,183,184,187,188,189,],[67,67,67,67,67,67,67,67,67,67,-67,-71,-68,67,-70,-69,-43,67,67,67,67,-42,-71,67,67,-68,-70,-41,]),'closeBrace':([47,48,58,68,84,100,102,120,123,124,125,132,133,134,135,136,139,142,143,146,149,150,153,154,157,158,161,163,165,167,170,172,174,175,177,178,180,181,183,184,185,186,187,188,189,],[-40,-40,76,86,-40,-40,-38,130,-40,-40,-40,-40,-31,-32,-37,-40,-40,-39,149,150,-67,-71,-68,-40,-70,-34,-69,-43,-40,-40,-35,-33,-40,-40,180,181,-42,-71,-40,-40,-36,187,-68,-70,-41,]),'string':([77,],[94,]),'elif':([149,153,157,187,188,],[-67,-68,162,-68,162,]),'else':([149,153,157,187,188,],[-67,-68,164,-68,164,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'var':([0,14,],[2,21,]),'type':([0,14,],[3,3,]),'func':([2,86,],[6,104,]),'varSequence':([3,16,36,],[8,31,49,]),'variable':([3,16,36,],[9,9,9,]),'mainProgram':([6,],[11,]),'dimentions':([10,],[17,]),'arithmeticExpression':([15,27,77,79,80,81,121,127,128,147,148,160,173,],[22,41,93,96,98,98,131,98,138,98,98,166,98,]),'multiplyDivide':([15,27,50,51,77,79,80,81,121,127,128,147,148,160,173,],[23,23,69,70,23,23,23,23,23,23,23,23,23,23,23,]),'val':([15,27,50,51,52,53,77,79,80,81,121,127,128,147,148,160,173,],[24,24,24,24,71,72,24,24,24,24,24,24,24,24,24,24,24,]),'value':([15,18,27,50,51,52,53,57,77,79,80,81,121,127,128,147,148,160,173,],[25,32,25,25,25,25,25,75,25,25,25,25,25,25,25,25,25,25,25,]),'unaryExpression':([15,27,47,48,50,51,52,53,77,79,80,81,84,100,121,123,124,125,127,128,132,136,139,147,148,154,160,165,167,173,174,175,183,184,],[26,26,66,66,26,26,26,26,26,26,26,26,66,66,26,66,66,66,26,26,66,66,66,26,26,66,26,66,66,26,66,66,66,66,]),'ACTION_INT_VALUE':([28,],[42,]),'ACTION_DOUBLE_VALUE':([29,],[43,]),'ACTION_VAR_VALUE':([30,33,],[44,44,]),'ACTION_UNARY_ADD_OPERANDS':([30,61,],[45,45,]),'ACTION_ADD_OPERATOR':([37,38,39,40,109,118,],[50,51,52,53,127,128,]),'subroutine':([47,48,84,100,123,124,125,132,136,139,154,165,167,174,175,183,184,],[58,68,102,120,133,134,135,142,143,146,158,170,172,177,178,185,186,]),'ACTION_UNARY_PLUS':([55,],[73,]),'ACTION_UNARY_MINUS':([56,],[74,]),'ACTION_DO_WHILE_INDEX':([64,],[82,]),'ACTION_ADD_QUADRUPLET':([69,70,71,72,137,138,],[87,88,89,90,144,145,]),'cout':([77,],[92,]),'statement':([80,81,127,147,148,173,],[97,99,137,151,152,176,]),'ACTION_GENERATE_QUADRUPLET':([96,131,],[107,141,]),'logicExpression':([97,98,99,137,151,152,176,],[109,118,109,109,109,109,109,]),'ACTION_QUADRUPLET_EMPTY_JUMP':([108,119,156,179,],[126,129,160,182,]),'ACTION_NEW_IF':([149,],[153,]),'ACTION_WHILE_GOTO':([150,181,],[154,183,]),'ACTION_QUADRUPLET_EMPTY_JUMP_END_IF':([153,187,],[157,188,]),'ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE':([155,],[159,]),'elseStatement':([157,188,],[161,189,]),'ACTION_FILL_JUMP':([157,162,164,188,],[163,168,169,163,]),'ACTION_FILL_JUMP_END_IF':([161,],[167,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> var func mainProgram','program',3,'p_program','yacc.py',31),
  ('var -> type varSequence semicolon var','var',4,'p_var','yacc.py',45),
  ('var -> <empty>','var',0,'p_var','yacc.py',46),
  ('varSequence -> variable equal arithmeticExpression','varSequence',3,'p_varSequence','yacc.py',54),
  ('varSequence -> variable','varSequence',1,'p_varSequence','yacc.py',55),
  ('varSequence -> variable equal arithmeticExpression comma varSequence','varSequence',5,'p_varSequence','yacc.py',56),
  ('varSequence -> variable comma varSequence','varSequence',3,'p_varSequence','yacc.py',57),
  ('variable -> id dimentions','variable',2,'p_variable','yacc.py',66),
  ('dimentions -> openBracket value closeBracket','dimentions',3,'p_dimentions','yacc.py',72),
  ('dimentions -> openBracket value closeBracket openBracket value closeBracket','dimentions',6,'p_dimentions','yacc.py',73),
  ('dimentions -> <empty>','dimentions',0,'p_dimentions','yacc.py',74),
  ('type -> int','type',1,'p_type','yacc.py',79),
  ('type -> double','type',1,'p_type','yacc.py',80),
  ('arithmeticExpression -> multiplyDivide','arithmeticExpression',1,'p_arithmeticExpression','yacc.py',86),
  ('arithmeticExpression -> arithmeticExpression plus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET','arithmeticExpression',5,'p_arithmeticExpression','yacc.py',87),
  ('arithmeticExpression -> arithmeticExpression minus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET','arithmeticExpression',5,'p_arithmeticExpression','yacc.py',88),
  ('multiplyDivide -> val','multiplyDivide',1,'p_multiplyDivide','yacc.py',93),
  ('multiplyDivide -> multiplyDivide multiply ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET','multiplyDivide',5,'p_multiplyDivide','yacc.py',94),
  ('multiplyDivide -> multiplyDivide divide ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET','multiplyDivide',5,'p_multiplyDivide','yacc.py',95),
  ('val -> value','val',1,'p_val','yacc.py',100),
  ('val -> unaryExpression','val',1,'p_val','yacc.py',101),
  ('val -> openParenthesis arithmeticExpression closeParenthesis','val',3,'p_val','yacc.py',102),
  ('unaryExpression -> id ACTION_UNARY_ADD_OPERANDS plusPlus ACTION_UNARY_PLUS','unaryExpression',4,'p_unaryExpression','yacc.py',107),
  ('unaryExpression -> id ACTION_UNARY_ADD_OPERANDS minusMinus ACTION_UNARY_MINUS','unaryExpression',4,'p_unaryExpression','yacc.py',108),
  ('value -> intValue ACTION_INT_VALUE','value',2,'p_value','yacc.py',113),
  ('value -> doubleValue ACTION_DOUBLE_VALUE','value',2,'p_value','yacc.py',114),
  ('value -> id ACTION_VAR_VALUE','value',2,'p_value','yacc.py',115),
  ('func -> function id openParenthesis closeParenthesis openBrace subroutine closeBrace func','func',8,'p_func','yacc.py',120),
  ('func -> <empty>','func',0,'p_func','yacc.py',121),
  ('mainProgram -> main openParenthesis closeParenthesis openBrace subroutine closeBrace','mainProgram',6,'p_mainProgram','yacc.py',126),
  ('subroutine -> consoleWrite openParenthesis cout closeParenthesis semicolon subroutine','subroutine',6,'p_subroutine','yacc.py',131),
  ('subroutine -> consoleRead openParenthesis id closeParenthesis semicolon subroutine','subroutine',6,'p_subroutine','yacc.py',132),
  ('subroutine -> if openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_NEW_IF ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement ACTION_FILL_JUMP_END_IF subroutine','subroutine',13,'p_subroutine','yacc.py',133),
  ('subroutine -> while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_WHILE_GOTO subroutine','subroutine',10,'p_subroutine','yacc.py',134),
  ('subroutine -> do ACTION_DO_WHILE_INDEX openBrace subroutine closeBrace while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE semicolon subroutine','subroutine',12,'p_subroutine','yacc.py',135),
  ('subroutine -> for openParenthesis id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon statement semicolon ACTION_QUADRUPLET_EMPTY_JUMP arithmeticExpression closeParenthesis openBrace subroutine closeBrace ACTION_WHILE_GOTO subroutine','subroutine',17,'p_subroutine','yacc.py',136),
  ('subroutine -> id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon subroutine','subroutine',6,'p_subroutine','yacc.py',137),
  ('subroutine -> unaryExpression semicolon subroutine','subroutine',3,'p_subroutine','yacc.py',138),
  ('subroutine -> call id openParenthesis closeParenthesis semicolon subroutine','subroutine',6,'p_subroutine','yacc.py',139),
  ('subroutine -> <empty>','subroutine',0,'p_subroutine','yacc.py',140),
  ('elseStatement -> elif ACTION_FILL_JUMP openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement','elseStatement',11,'p_elseStatement','yacc.py',144),
  ('elseStatement -> else ACTION_FILL_JUMP openBrace subroutine closeBrace','elseStatement',5,'p_elseStatement','yacc.py',145),
  ('elseStatement -> ACTION_FILL_JUMP','elseStatement',1,'p_elseStatement','yacc.py',146),
  ('statement -> arithmeticExpression','statement',1,'p_statement','yacc.py',151),
  ('statement -> arithmeticExpression logicExpression ACTION_ADD_OPERATOR arithmeticExpression ACTION_ADD_QUADRUPLET','statement',5,'p_statement','yacc.py',152),
  ('statement -> statement logicExpression ACTION_ADD_OPERATOR statement ACTION_ADD_QUADRUPLET','statement',5,'p_statement','yacc.py',153),
  ('logicExpression -> greaterThan','logicExpression',1,'p_logicExpression','yacc.py',158),
  ('logicExpression -> lessThan','logicExpression',1,'p_logicExpression','yacc.py',159),
  ('logicExpression -> isEqual','logicExpression',1,'p_logicExpression','yacc.py',160),
  ('logicExpression -> notEqual','logicExpression',1,'p_logicExpression','yacc.py',161),
  ('logicExpression -> greaterOrEqual','logicExpression',1,'p_logicExpression','yacc.py',162),
  ('logicExpression -> lessOrEqual','logicExpression',1,'p_logicExpression','yacc.py',163),
  ('logicExpression -> and','logicExpression',1,'p_logicExpression','yacc.py',164),
  ('logicExpression -> or','logicExpression',1,'p_logicExpression','yacc.py',165),
  ('cout -> arithmeticExpression','cout',1,'p_cout','yacc.py',171),
  ('cout -> string','cout',1,'p_cout','yacc.py',172),
  ('ACTION_VAR_VALUE -> <empty>','ACTION_VAR_VALUE',0,'p_action_var_value','yacc.py',185),
  ('ACTION_INT_VALUE -> <empty>','ACTION_INT_VALUE',0,'p_action_int_value','yacc.py',190),
  ('ACTION_DOUBLE_VALUE -> <empty>','ACTION_DOUBLE_VALUE',0,'p_action_double_value','yacc.py',195),
  ('ACTION_UNARY_ADD_OPERANDS -> <empty>','ACTION_UNARY_ADD_OPERANDS',0,'p_action_unary_add_operands','yacc.py',200),
  ('ACTION_UNARY_PLUS -> <empty>','ACTION_UNARY_PLUS',0,'p_action_unary_plus','yacc.py',205),
  ('ACTION_UNARY_MINUS -> <empty>','ACTION_UNARY_MINUS',0,'p_action_unary_minus','yacc.py',209),
  ('ACTION_ADD_OPERATOR -> <empty>','ACTION_ADD_OPERATOR',0,'p_action_add_operator','yacc.py',220),
  ('ACTION_GENERATE_QUADRUPLET -> <empty>','ACTION_GENERATE_QUADRUPLET',0,'p_action_generate_quadruplet','yacc.py',224),
  ('ACTION_ADD_QUADRUPLET -> <empty>','ACTION_ADD_QUADRUPLET',0,'p_action_add_quadruplet','yacc.py',234),
  ('ACTION_QUADRUPLET_EMPTY_JUMP -> <empty>','ACTION_QUADRUPLET_EMPTY_JUMP',0,'p_action_quadruplet_empty_jump','yacc.py',246),
  ('ACTION_NEW_IF -> <empty>','ACTION_NEW_IF',0,'p_action_new_if','yacc.py',254),
  ('ACTION_QUADRUPLET_EMPTY_JUMP_END_IF -> <empty>','ACTION_QUADRUPLET_EMPTY_JUMP_END_IF',0,'p_action_quadruplet_empty_jump_end_if','yacc.py',258),
  ('ACTION_FILL_JUMP_END_IF -> <empty>','ACTION_FILL_JUMP_END_IF',0,'p_action_fill_jump_end_if','yacc.py',265),
  ('ACTION_FILL_JUMP -> <empty>','ACTION_FILL_JUMP',0,'p_action_fill_jump','yacc.py',271),
  ('ACTION_WHILE_GOTO -> <empty>','ACTION_WHILE_GOTO',0,'p_action_while_goto','yacc.py',275),
  ('ACTION_DO_WHILE_INDEX -> <empty>','ACTION_DO_WHILE_INDEX',0,'p_action_do_while_jump_index','yacc.py',283),
  ('ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE -> <empty>','ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE',0,'p_action_quadruplet_empty_jump_do_while','yacc.py',288),
]
