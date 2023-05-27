grammar final;

WS: [ \t\r\n]+ -> skip;

PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';
MULTASGN: '*=';
ADDASGN: '+=';
SUBASGN: '-=';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
INC: '++';
DEC: '--';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACK: '[';
RBRACK: ']';
SEMICOLON: ';';
COMMA: ',';
FORAND: '&';
IF: 'if';
SO: 'so';
ELSE: 'else';
UNTIL: 'until';
LOOP: 'loop';
DO: 'do';
RETURN: 'return';
INT_TYPE: 'int';
FLOAT_TYPE: 'float';
CHAR_TYPE: 'char';
SELECTOR: 'selector';
SELECT: 'select';
OTHER: 'other';
COLON: ':';
READ: 'read';
WRITE: 'write';
BREAK: 'break';

prog: (declaration)*;

declaration: variableDeclaration | functionDeclaration ;

variableDeclaration: typeSpecifier variableDeclarator (COMMA variableDeclarator)* SEMICOLON;

variableDeclarator: ID (ASSIGN expression)?;

typeSpecifier: INT_TYPE | FLOAT_TYPE | CHAR_TYPE;

functionDeclaration: typeSpecifier ID LPAREN parameterList? RPAREN compoundStatement;

parameterList: parameter (COMMA parameter)*;

parameter: typeSpecifier ID;

compoundStatement: LBRACE statement* RBRACE;

statement: expressionStatement | compoundStatement | if_soStatement | untilStatement | loopStatement | selectorStatement | returnStatement | readStatement | writeStatement | declaration;

expressionStatement: expression? SEMICOLON;

if_soStatement: IF LPAREN expression RPAREN SO statement (ELSE statement)?;

untilStatement: UNTIL LPAREN expression RPAREN statement;

loopStatement: LOOP LPAREN expression? FORAND expression? FORAND expression? RPAREN compoundStatement;

selectorStatement: SELECTOR COLON expression LBRACE selectStatement* otherStatement? RBRACE;

selectStatement: SELECT expression COLON statement BREAK SEMICOLON;

otherStatement: OTHER COLON statement;

returnStatement: RETURN expression? SEMICOLON;

readStatement: READ LPAREN typeSpecifier COMMA ID RPAREN SEMICOLON;

writeStatement: WRITE LPAREN expression (COMMA expression)* RPAREN SEMICOLON;

expression: assignmentExpression;

assignmentExpression: logicalOrExpression (ASSIGN assignmentExpression)*;

logicalOrExpression: logicalAndExpression (OR logicalAndExpression)*;

logicalAndExpression: equalityExpression (AND equalityExpression)*;

equalityExpression: relationalExpression ((EQ | NEQ) relationalExpression)*;

relationalExpression: additiveExpression ((LT | GT | LTE | GTE) additiveExpression)*;

additiveExpression: multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression: unaryExpression ((MULT | DIV | MOD | MULTASGN | ADDASGN | SUBASGN) unaryExpression)*;

unaryExpression: (INC | DEC | PLUS | MINUS | NOT ) unaryExpression | primaryExpression (INC | DEC)*;

primaryExpression: INT | FLOAT | CHAR | STRING | ID | LPAREN expression RPAREN;

INT: [0-9] | [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;
STRING: '"' ~["\r\n]* '"';
CHAR: '\'' ~['\r\n]* '\'';
ID: [a-zA-Z_] | [a-zA-Z_][a-zA-Z0-9_]*;