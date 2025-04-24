grammar AVR;

// Parser rules
program         : line* EOF ;
line            : instruction | label | directive | comment | NEWLINE ;
instruction     : mnemonic operandList? ;
operandList     : operand (',' operand)* ;
operand         : REGISTER | NUMBER | LABEL_REF ;

label           : LABEL_DEF ;
directive       : DOT_DIRECTIVE operandList? ;

comment         : COMMENT ;

// Lexer rules
mnemonic        : [A-Z]+ ;
REGISTER        : 'R' [0-9]{1,2} ;
NUMBER          : '0x' [0-9a-fA-F]+ | [0-9]+ ;
LABEL_DEF       : [a-zA-Z_][a-zA-Z0-9_]* ':' ;
LABEL_REF       : [a-zA-Z_][a-zA-Z0-9_]* ;
DOT_DIRECTIVE   : '.' [a-zA-Z]+ ;
COMMENT         : ';' ~[\r\n]* ;

NEWLINE         : [\r\n]+ ;
WS              : [ \t]+ -> skip ;
