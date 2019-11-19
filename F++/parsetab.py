
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'and call closeBrace closeBracket closeParenthesis comma consoleRead consoleWrite divide do double doubleValue elif else equal for function greaterOrEqual greaterThan id if int intValue isEqual lessOrEqual lessThan main minus minusMinus multiply not notEqual openBrace openBracket openParenthesis or plus plusPlus semicolon string while\n\tprogram : var func mainProgram\n    \n    var : type varSequence semicolon var\n    |\n    \n    varSequence : variable equal arithmeticExpression\n        | variable\n        | variable equal arithmeticExpression comma varSequence\n        | variable comma varSequence\n    \n    variable : id dimentions\n    \n    dimentions : openBracket value closeBracket\n    | openBracket value closeBracket openBracket value closeBracket\n    |\n    \n    type : int\n    | double\n    \n    arithmeticExpression : multiplyDivide\n    | arithmeticExpression plus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET\n    | arithmeticExpression minus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET\n    \n    multiplyDivide : val\n    | multiplyDivide multiply ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET\n    | multiplyDivide divide ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET\n    \n    val : value\n    | unaryExpression\n    | openParenthesis arithmeticExpression closeParenthesis\n    \n    unaryExpression : id ACTION_UNARY_ADD_OPERANDS plusPlus ACTION_UNARY_PLUS\n    | id ACTION_UNARY_ADD_OPERANDS minusMinus ACTION_UNARY_MINUS\n    \n    value : intValue ACTION_INT_VALUE\n    | doubleValue ACTION_DOUBLE_VALUE\n    | id ACTION_VAR_VALUE\n    \n    func : function id ACTION_ADD_FUNCTION openParenthesis closeParenthesis openBrace subroutine closeBrace ACTION_END_FUNCTION func\n    |\n    \n    mainProgram : main openParenthesis closeParenthesis openBrace subroutine closeBrace\n    \n    subroutine : consoleWrite openParenthesis cout ACTION_CONSOLE_WRITE closeParenthesis semicolon subroutine\n    | consoleRead openParenthesis id ACTION_CONSOLE_READ closeParenthesis semicolon subroutine\n    | if openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_NEW_IF ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement ACTION_FILL_JUMP_END_IF subroutine\n    | while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_WHILE_GOTO subroutine\n    | do ACTION_DO_WHILE_INDEX openBrace subroutine closeBrace while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE semicolon subroutine\n    | for openParenthesis id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon statement semicolon ACTION_QUADRUPLET_EMPTY_JUMP arithmeticExpression ACTION_FOR_INCREMENT closeParenthesis openBrace subroutine closeBrace ACTION_FOR_GOTO subroutine\n    | id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon subroutine\n    | unaryExpression semicolon subroutine\n    | call id ACTION_GOTO_FUNCTION openParenthesis closeParenthesis semicolon subroutine\n    |\n    \n    elseStatement : elif ACTION_FILL_JUMP openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement\n    | else ACTION_FILL_JUMP openBrace subroutine closeBrace\n    | ACTION_FILL_JUMP\n    \n    statement : arithmeticExpression \n    | arithmeticExpression logicExpression ACTION_ADD_OPERATOR arithmeticExpression ACTION_ADD_QUADRUPLET\n    | statement logicExpression ACTION_ADD_OPERATOR statement ACTION_ADD_QUADRUPLET\n    \n    logicExpression : greaterThan\n    | lessThan\n    | isEqual\n    | notEqual\n    | greaterOrEqual\n    | lessOrEqual\n    | and\n    | or\n    \n    cout : arithmeticExpression\n    | string\n    ACTION_VAR_VALUE :ACTION_INT_VALUE :ACTION_DOUBLE_VALUE :ACTION_UNARY_ADD_OPERANDS :ACTION_UNARY_PLUS :ACTION_UNARY_MINUS :ACTION_ADD_OPERATOR :ACTION_GENERATE_QUADRUPLET :ACTION_ADD_QUADRUPLET :ACTION_QUADRUPLET_EMPTY_JUMP :ACTION_NEW_IF :ACTION_QUADRUPLET_EMPTY_JUMP_END_IF :ACTION_FILL_JUMP_END_IF :ACTION_FILL_JUMP :ACTION_WHILE_GOTO :ACTION_DO_WHILE_INDEX :ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE :ACTION_FOR_INCREMENT :ACTION_FOR_GOTO :ACTION_ADD_FUNCTION :ACTION_END_FUNCTION :ACTION_GOTO_FUNCTION :ACTION_CONSOLE_WRITE :ACTION_CONSOLE_READ :'
    
_lr_action_items = {'function':([0,2,14,21,104,123,],[-3,7,-3,-2,-77,7,]),'main':([0,2,6,14,21,104,123,134,],[-3,-29,12,-3,-2,-77,-29,-28,]),'int':([0,14,],[4,4,]),'double':([0,14,],[5,5,]),'$end':([1,11,76,],[0,-1,-30,]),'id':([3,4,5,7,15,16,18,27,36,37,38,39,40,47,50,51,52,53,57,67,68,77,78,79,80,81,83,84,100,109,110,111,112,113,114,115,116,117,118,121,126,128,129,135,136,138,141,144,151,152,154,155,158,159,161,162,165,166,168,170,172,178,179,183,185,188,189,190,193,194,195,],[10,-12,-13,13,30,10,33,30,10,-63,-63,-63,-63,61,30,30,30,30,33,85,61,30,95,30,30,30,101,61,61,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,30,61,30,30,61,61,61,61,61,30,30,-67,-71,-68,61,-66,-70,30,-69,-43,61,61,30,61,61,-42,-75,61,61,-68,-70,-41,]),'semicolon':([8,9,10,17,22,23,24,25,26,28,29,30,31,42,43,44,46,49,54,55,56,66,69,70,71,72,73,74,87,88,89,90,91,96,98,107,124,125,132,133,139,140,143,148,149,157,160,164,],[14,-5,-11,-8,-4,-14,-17,-20,-21,-58,-59,-57,-7,-25,-26,-27,-9,-6,-22,-61,-62,84,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,-10,-64,-44,126,135,136,-64,144,-65,-65,152,-46,-45,161,-73,170,]),'equal':([9,10,17,46,61,91,101,],[15,-11,-8,-9,79,-10,121,]),'comma':([9,10,17,22,23,24,25,26,28,29,30,42,43,44,46,54,55,56,69,70,71,72,73,74,87,88,89,90,91,],[16,-11,-8,36,-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-9,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,-10,]),'openBracket':([10,46,],[18,57,]),'openParenthesis':([12,13,15,20,27,37,38,39,40,50,51,52,53,59,60,62,63,65,77,79,80,81,85,103,109,110,111,112,113,114,115,116,117,118,121,128,129,142,151,152,161,165,167,173,178,],[19,-76,27,35,27,-63,-63,-63,-63,27,27,27,27,77,78,80,81,83,27,27,27,27,-78,122,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,27,27,27,151,27,27,-66,27,-70,178,27,]),'intValue':([15,18,27,37,38,39,40,50,51,52,53,57,77,79,80,81,109,110,111,112,113,114,115,116,117,118,121,128,129,151,152,161,165,178,],[28,28,28,-63,-63,-63,-63,28,28,28,28,28,28,28,28,28,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,28,28,28,28,28,-66,28,28,]),'doubleValue':([15,18,27,37,38,39,40,50,51,52,53,57,77,79,80,81,109,110,111,112,113,114,115,116,117,118,121,128,129,151,152,161,165,178,],[29,29,29,-63,-63,-63,-63,29,29,29,29,29,29,29,29,29,-63,-47,-48,-49,-50,-51,-52,-53,-54,-63,29,29,29,29,29,-66,29,29,]),'closeParenthesis':([19,23,24,25,26,28,29,30,35,41,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,92,93,94,95,97,98,99,105,106,122,139,140,148,149,156,171,176,181,],[34,-14,-17,-20,-21,-58,-59,-57,48,54,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,-79,-55,-56,-80,108,-44,119,124,125,133,-65,-65,-46,-45,160,-74,180,184,]),'plus':([22,23,24,25,26,28,29,30,41,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,93,96,98,132,140,171,],[37,-14,-17,-20,-21,-58,-59,-57,37,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,37,37,37,37,37,37,]),'minus':([22,23,24,25,26,28,29,30,41,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,93,96,98,132,140,171,],[38,-14,-17,-20,-21,-58,-59,-57,38,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,38,38,38,38,38,38,]),'greaterThan':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,110,110,110,110,-65,-46,-45,110,110,110,]),'lessThan':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,111,111,111,111,-65,-46,-45,111,111,111,]),'isEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,112,112,112,112,-65,-46,-45,112,112,112,]),'notEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,113,113,113,113,-65,-46,-45,113,113,113,]),'greaterOrEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,114,114,114,114,-65,-46,-45,114,114,114,]),'lessOrEqual':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,115,115,115,115,-65,-46,-45,115,115,115,]),'and':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,116,116,116,116,-65,-46,-45,116,116,116,]),'or':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,87,88,89,90,97,98,99,139,140,148,149,156,157,181,],[-14,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,-65,-65,-65,-65,-23,-24,-15,-16,-18,-19,117,117,117,117,-65,-46,-45,117,117,117,]),'multiply':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,89,90,],[39,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,39,39,-65,-65,-23,-24,-18,-19,]),'divide':([23,24,25,26,28,29,30,42,43,44,54,55,56,69,70,71,72,73,74,89,90,],[40,-17,-20,-21,-58,-59,-57,-25,-26,-27,-22,-61,-62,40,40,-65,-65,-23,-24,-18,-19,]),'closeBracket':([28,29,32,33,42,43,44,75,],[-58,-59,46,-57,-25,-26,-27,91,]),'plusPlus':([30,45,61,],[-60,55,-60,]),'minusMinus':([30,45,61,],[-60,56,-60,]),'openBrace':([34,48,64,82,108,119,127,130,169,174,180,184,187,],[47,68,-72,100,-66,-66,138,141,-70,179,183,-66,189,]),'consoleWrite':([47,68,84,100,126,135,136,138,141,144,154,155,158,159,162,166,168,170,172,179,183,185,188,189,190,193,194,195,],[59,59,59,59,59,59,59,59,59,59,-67,-71,-68,59,-70,-69,-43,59,59,59,59,-42,-75,59,59,-68,-70,-41,]),'consoleRead':([47,68,84,100,126,135,136,138,141,144,154,155,158,159,162,166,168,170,172,179,183,185,188,189,190,193,194,195,],[60,60,60,60,60,60,60,60,60,60,-67,-71,-68,60,-70,-69,-43,60,60,60,60,-42,-75,60,60,-68,-70,-41,]),'if':([47,68,84,100,126,135,136,138,141,144,154,155,158,159,162,166,168,170,172,179,183,185,188,189,190,193,194,195,],[62,62,62,62,62,62,62,62,62,62,-67,-71,-68,62,-70,-69,-43,62,62,62,62,-42,-75,62,62,-68,-70,-41,]),'while':([47,68,84,100,126,131,135,136,138,141,144,154,155,158,159,162,166,168,170,172,179,183,185,188,189,190,193,194,195,],[63,63,63,63,63,142,63,63,63,63,63,-67,-71,-68,63,-70,-69,-43,63,63,63,63,-42,-75,63,63,-68,-70,-41,]),'do':([47,68,84,100,126,135,136,138,141,144,154,155,158,159,162,166,168,170,172,179,183,185,188,189,190,193,194,195,],[64,64,64,64,64,64,64,64,64,64,-67,-71,-68,64,-70,-69,-43,64,64,64,64,-42,-75,64,64,-68,-70,-41,]),'for':([47,68,84,100,126,135,136,138,141,144,154,155,158,159,162,166,168,170,172,179,183,185,188,189,190,193,194,195,],[65,65,65,65,65,65,65,65,65,65,-67,-71,-68,65,-70,-69,-43,65,65,65,65,-42,-75,65,65,-68,-70,-41,]),'call':([47,68,84,100,126,135,136,138,141,144,154,155,158,159,162,166,168,170,172,179,183,185,188,189,190,193,194,195,],[67,67,67,67,67,67,67,67,67,67,-67,-71,-68,67,-70,-69,-43,67,67,67,67,-42,-75,67,67,-68,-70,-41,]),'closeBrace':([47,58,68,84,86,100,102,120,126,135,136,137,138,141,144,145,146,147,150,153,154,155,158,159,162,163,166,168,170,172,175,177,179,182,183,185,186,188,189,190,191,192,193,194,195,],[-40,76,-40,-40,104,-40,-38,131,-40,-40,-40,-37,-40,-40,-40,-31,-32,154,155,-39,-67,-71,-68,-40,-70,-34,-69,-43,-40,-40,-35,-33,-40,185,-40,-42,188,-75,-40,-40,193,-36,-68,-70,-41,]),'string':([77,],[94,]),'elif':([154,158,162,193,194,],[-67,-68,167,-68,167,]),'else':([154,158,162,193,194,],[-67,-68,169,-68,169,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'var':([0,14,],[2,21,]),'type':([0,14,],[3,3,]),'func':([2,123,],[6,134,]),'varSequence':([3,16,36,],[8,31,49,]),'variable':([3,16,36,],[9,9,9,]),'mainProgram':([6,],[11,]),'dimentions':([10,],[17,]),'ACTION_ADD_FUNCTION':([13,],[20,]),'arithmeticExpression':([15,27,77,79,80,81,121,128,129,151,152,165,178,],[22,41,93,96,98,98,132,98,140,98,98,171,98,]),'multiplyDivide':([15,27,50,51,77,79,80,81,121,128,129,151,152,165,178,],[23,23,69,70,23,23,23,23,23,23,23,23,23,23,23,]),'val':([15,27,50,51,52,53,77,79,80,81,121,128,129,151,152,165,178,],[24,24,24,24,71,72,24,24,24,24,24,24,24,24,24,24,24,]),'value':([15,18,27,50,51,52,53,57,77,79,80,81,121,128,129,151,152,165,178,],[25,32,25,25,25,25,25,75,25,25,25,25,25,25,25,25,25,25,25,]),'unaryExpression':([15,27,47,50,51,52,53,68,77,79,80,81,84,100,121,126,128,129,135,136,138,141,144,151,152,159,165,170,172,178,179,183,189,190,],[26,26,66,26,26,26,26,66,26,26,26,26,66,66,26,66,26,26,66,66,66,66,66,26,26,66,26,66,66,26,66,66,66,66,]),'ACTION_INT_VALUE':([28,],[42,]),'ACTION_DOUBLE_VALUE':([29,],[43,]),'ACTION_VAR_VALUE':([30,33,],[44,44,]),'ACTION_UNARY_ADD_OPERANDS':([30,61,],[45,45,]),'ACTION_ADD_OPERATOR':([37,38,39,40,109,118,],[50,51,52,53,128,129,]),'subroutine':([47,68,84,100,126,135,136,138,141,144,159,170,172,179,183,189,190,],[58,86,102,120,137,145,146,147,150,153,163,175,177,182,186,191,192,]),'ACTION_UNARY_PLUS':([55,],[73,]),'ACTION_UNARY_MINUS':([56,],[74,]),'ACTION_DO_WHILE_INDEX':([64,],[82,]),'ACTION_ADD_QUADRUPLET':([69,70,71,72,139,140,],[87,88,89,90,148,149,]),'cout':([77,],[92,]),'statement':([80,81,128,151,152,178,],[97,99,139,156,157,181,]),'ACTION_GOTO_FUNCTION':([85,],[103,]),'ACTION_CONSOLE_WRITE':([92,],[105,]),'ACTION_CONSOLE_READ':([95,],[106,]),'ACTION_GENERATE_QUADRUPLET':([96,132,],[107,143,]),'logicExpression':([97,98,99,139,156,157,181,],[109,118,109,109,109,109,109,]),'ACTION_END_FUNCTION':([104,],[123,]),'ACTION_QUADRUPLET_EMPTY_JUMP':([108,119,161,184,],[127,130,165,187,]),'ACTION_NEW_IF':([154,],[158,]),'ACTION_WHILE_GOTO':([155,],[159,]),'ACTION_QUADRUPLET_EMPTY_JUMP_END_IF':([158,193,],[162,194,]),'ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE':([160,],[164,]),'elseStatement':([162,194,],[166,195,]),'ACTION_FILL_JUMP':([162,167,169,194,],[168,173,174,168,]),'ACTION_FILL_JUMP_END_IF':([166,],[172,]),'ACTION_FOR_INCREMENT':([171,],[176,]),'ACTION_FOR_GOTO':([188,],[190,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> var func mainProgram','program',3,'p_program','yacc.py',32),
  ('var -> type varSequence semicolon var','var',4,'p_var','yacc.py',46),
  ('var -> <empty>','var',0,'p_var','yacc.py',47),
  ('varSequence -> variable equal arithmeticExpression','varSequence',3,'p_varSequence','yacc.py',55),
  ('varSequence -> variable','varSequence',1,'p_varSequence','yacc.py',56),
  ('varSequence -> variable equal arithmeticExpression comma varSequence','varSequence',5,'p_varSequence','yacc.py',57),
  ('varSequence -> variable comma varSequence','varSequence',3,'p_varSequence','yacc.py',58),
  ('variable -> id dimentions','variable',2,'p_variable','yacc.py',67),
  ('dimentions -> openBracket value closeBracket','dimentions',3,'p_dimentions','yacc.py',73),
  ('dimentions -> openBracket value closeBracket openBracket value closeBracket','dimentions',6,'p_dimentions','yacc.py',74),
  ('dimentions -> <empty>','dimentions',0,'p_dimentions','yacc.py',75),
  ('type -> int','type',1,'p_type','yacc.py',80),
  ('type -> double','type',1,'p_type','yacc.py',81),
  ('arithmeticExpression -> multiplyDivide','arithmeticExpression',1,'p_arithmeticExpression','yacc.py',87),
  ('arithmeticExpression -> arithmeticExpression plus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET','arithmeticExpression',5,'p_arithmeticExpression','yacc.py',88),
  ('arithmeticExpression -> arithmeticExpression minus ACTION_ADD_OPERATOR multiplyDivide ACTION_ADD_QUADRUPLET','arithmeticExpression',5,'p_arithmeticExpression','yacc.py',89),
  ('multiplyDivide -> val','multiplyDivide',1,'p_multiplyDivide','yacc.py',94),
  ('multiplyDivide -> multiplyDivide multiply ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET','multiplyDivide',5,'p_multiplyDivide','yacc.py',95),
  ('multiplyDivide -> multiplyDivide divide ACTION_ADD_OPERATOR val ACTION_ADD_QUADRUPLET','multiplyDivide',5,'p_multiplyDivide','yacc.py',96),
  ('val -> value','val',1,'p_val','yacc.py',101),
  ('val -> unaryExpression','val',1,'p_val','yacc.py',102),
  ('val -> openParenthesis arithmeticExpression closeParenthesis','val',3,'p_val','yacc.py',103),
  ('unaryExpression -> id ACTION_UNARY_ADD_OPERANDS plusPlus ACTION_UNARY_PLUS','unaryExpression',4,'p_unaryExpression','yacc.py',108),
  ('unaryExpression -> id ACTION_UNARY_ADD_OPERANDS minusMinus ACTION_UNARY_MINUS','unaryExpression',4,'p_unaryExpression','yacc.py',109),
  ('value -> intValue ACTION_INT_VALUE','value',2,'p_value','yacc.py',114),
  ('value -> doubleValue ACTION_DOUBLE_VALUE','value',2,'p_value','yacc.py',115),
  ('value -> id ACTION_VAR_VALUE','value',2,'p_value','yacc.py',116),
  ('func -> function id ACTION_ADD_FUNCTION openParenthesis closeParenthesis openBrace subroutine closeBrace ACTION_END_FUNCTION func','func',10,'p_func','yacc.py',121),
  ('func -> <empty>','func',0,'p_func','yacc.py',122),
  ('mainProgram -> main openParenthesis closeParenthesis openBrace subroutine closeBrace','mainProgram',6,'p_mainProgram','yacc.py',127),
  ('subroutine -> consoleWrite openParenthesis cout ACTION_CONSOLE_WRITE closeParenthesis semicolon subroutine','subroutine',7,'p_subroutine','yacc.py',132),
  ('subroutine -> consoleRead openParenthesis id ACTION_CONSOLE_READ closeParenthesis semicolon subroutine','subroutine',7,'p_subroutine','yacc.py',133),
  ('subroutine -> if openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_NEW_IF ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement ACTION_FILL_JUMP_END_IF subroutine','subroutine',13,'p_subroutine','yacc.py',134),
  ('subroutine -> while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_WHILE_GOTO subroutine','subroutine',10,'p_subroutine','yacc.py',135),
  ('subroutine -> do ACTION_DO_WHILE_INDEX openBrace subroutine closeBrace while openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE semicolon subroutine','subroutine',12,'p_subroutine','yacc.py',136),
  ('subroutine -> for openParenthesis id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon statement semicolon ACTION_QUADRUPLET_EMPTY_JUMP arithmeticExpression ACTION_FOR_INCREMENT closeParenthesis openBrace subroutine closeBrace ACTION_FOR_GOTO subroutine','subroutine',18,'p_subroutine','yacc.py',137),
  ('subroutine -> id equal arithmeticExpression ACTION_GENERATE_QUADRUPLET semicolon subroutine','subroutine',6,'p_subroutine','yacc.py',138),
  ('subroutine -> unaryExpression semicolon subroutine','subroutine',3,'p_subroutine','yacc.py',139),
  ('subroutine -> call id ACTION_GOTO_FUNCTION openParenthesis closeParenthesis semicolon subroutine','subroutine',7,'p_subroutine','yacc.py',140),
  ('subroutine -> <empty>','subroutine',0,'p_subroutine','yacc.py',141),
  ('elseStatement -> elif ACTION_FILL_JUMP openParenthesis statement closeParenthesis ACTION_QUADRUPLET_EMPTY_JUMP openBrace subroutine closeBrace ACTION_QUADRUPLET_EMPTY_JUMP_END_IF elseStatement','elseStatement',11,'p_elseStatement','yacc.py',145),
  ('elseStatement -> else ACTION_FILL_JUMP openBrace subroutine closeBrace','elseStatement',5,'p_elseStatement','yacc.py',146),
  ('elseStatement -> ACTION_FILL_JUMP','elseStatement',1,'p_elseStatement','yacc.py',147),
  ('statement -> arithmeticExpression','statement',1,'p_statement','yacc.py',152),
  ('statement -> arithmeticExpression logicExpression ACTION_ADD_OPERATOR arithmeticExpression ACTION_ADD_QUADRUPLET','statement',5,'p_statement','yacc.py',153),
  ('statement -> statement logicExpression ACTION_ADD_OPERATOR statement ACTION_ADD_QUADRUPLET','statement',5,'p_statement','yacc.py',154),
  ('logicExpression -> greaterThan','logicExpression',1,'p_logicExpression','yacc.py',159),
  ('logicExpression -> lessThan','logicExpression',1,'p_logicExpression','yacc.py',160),
  ('logicExpression -> isEqual','logicExpression',1,'p_logicExpression','yacc.py',161),
  ('logicExpression -> notEqual','logicExpression',1,'p_logicExpression','yacc.py',162),
  ('logicExpression -> greaterOrEqual','logicExpression',1,'p_logicExpression','yacc.py',163),
  ('logicExpression -> lessOrEqual','logicExpression',1,'p_logicExpression','yacc.py',164),
  ('logicExpression -> and','logicExpression',1,'p_logicExpression','yacc.py',165),
  ('logicExpression -> or','logicExpression',1,'p_logicExpression','yacc.py',166),
  ('cout -> arithmeticExpression','cout',1,'p_cout','yacc.py',172),
  ('cout -> string','cout',1,'p_cout','yacc.py',173),
  ('ACTION_VAR_VALUE -> <empty>','ACTION_VAR_VALUE',0,'p_action_var_value','yacc.py',187),
  ('ACTION_INT_VALUE -> <empty>','ACTION_INT_VALUE',0,'p_action_int_value','yacc.py',192),
  ('ACTION_DOUBLE_VALUE -> <empty>','ACTION_DOUBLE_VALUE',0,'p_action_double_value','yacc.py',197),
  ('ACTION_UNARY_ADD_OPERANDS -> <empty>','ACTION_UNARY_ADD_OPERANDS',0,'p_action_unary_add_operands','yacc.py',202),
  ('ACTION_UNARY_PLUS -> <empty>','ACTION_UNARY_PLUS',0,'p_action_unary_plus','yacc.py',207),
  ('ACTION_UNARY_MINUS -> <empty>','ACTION_UNARY_MINUS',0,'p_action_unary_minus','yacc.py',211),
  ('ACTION_ADD_OPERATOR -> <empty>','ACTION_ADD_OPERATOR',0,'p_action_add_operator','yacc.py',222),
  ('ACTION_GENERATE_QUADRUPLET -> <empty>','ACTION_GENERATE_QUADRUPLET',0,'p_action_generate_quadruplet','yacc.py',226),
  ('ACTION_ADD_QUADRUPLET -> <empty>','ACTION_ADD_QUADRUPLET',0,'p_action_add_quadruplet','yacc.py',236),
  ('ACTION_QUADRUPLET_EMPTY_JUMP -> <empty>','ACTION_QUADRUPLET_EMPTY_JUMP',0,'p_action_quadruplet_empty_jump','yacc.py',247),
  ('ACTION_NEW_IF -> <empty>','ACTION_NEW_IF',0,'p_action_new_if','yacc.py',255),
  ('ACTION_QUADRUPLET_EMPTY_JUMP_END_IF -> <empty>','ACTION_QUADRUPLET_EMPTY_JUMP_END_IF',0,'p_action_quadruplet_empty_jump_end_if','yacc.py',259),
  ('ACTION_FILL_JUMP_END_IF -> <empty>','ACTION_FILL_JUMP_END_IF',0,'p_action_fill_jump_end_if','yacc.py',266),
  ('ACTION_FILL_JUMP -> <empty>','ACTION_FILL_JUMP',0,'p_action_fill_jump','yacc.py',272),
  ('ACTION_WHILE_GOTO -> <empty>','ACTION_WHILE_GOTO',0,'p_action_while_goto','yacc.py',276),
  ('ACTION_DO_WHILE_INDEX -> <empty>','ACTION_DO_WHILE_INDEX',0,'p_action_do_while_jump_index','yacc.py',284),
  ('ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE -> <empty>','ACTION_QUADRUPLET_EMPTY_JUMP_DO_WHILE',0,'p_action_quadruplet_empty_jump_do_while','yacc.py',289),
  ('ACTION_FOR_INCREMENT -> <empty>','ACTION_FOR_INCREMENT',0,'p_action_for_increment','yacc.py',296),
  ('ACTION_FOR_GOTO -> <empty>','ACTION_FOR_GOTO',0,'p_action_for_goto','yacc.py',303),
  ('ACTION_ADD_FUNCTION -> <empty>','ACTION_ADD_FUNCTION',0,'p_action_add_function','yacc.py',313),
  ('ACTION_END_FUNCTION -> <empty>','ACTION_END_FUNCTION',0,'p_action_end_function','yacc.py',319),
  ('ACTION_GOTO_FUNCTION -> <empty>','ACTION_GOTO_FUNCTION',0,'p_action_goto_function','yacc.py',325),
  ('ACTION_CONSOLE_WRITE -> <empty>','ACTION_CONSOLE_WRITE',0,'p_action_console_write','yacc.py',332),
  ('ACTION_CONSOLE_READ -> <empty>','ACTION_CONSOLE_READ',0,'p_action_console_read','yacc.py',339),
]
