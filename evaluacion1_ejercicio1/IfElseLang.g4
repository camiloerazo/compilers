grammar IfElseLang;

program: statement+ EOF;

statement: assignment | ifStatement;

assignment: ID ASSIGN expr SEMI;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

condition: expr operator expr;

expr: ID | NUMBER;

operator: LT | GE | LE | NE | GT | EE;

IF: 'if';
ELSE: 'else';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
LT: '<';
GT: '>';
GE: '>=';
LE: '<=';
NE: '!=';
EE: '==';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;