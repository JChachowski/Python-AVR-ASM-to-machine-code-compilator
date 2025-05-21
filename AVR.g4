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
mnemonic        : 'ADC' | 'ADD' | 'ADIW' | 'AND' | 'ANDI' | 'ASR' | 'BCLR' | 'BLD' | 'BRBC' | 'BRBS' | 'BRCC' | 'BRCS' | 'BREAK' | 'BREQ' | 'BRGE' | 'BRHC' | 'BRHS' | 'BRID' | 'BRIE' | 'BRLO' | 'BRLT' | 'BRMI' | 'BRNE' | 'BRPL' | 'BRSH' | 'BRTC' | 'BRTS' | 'BRVC' | 'BRVS' | 'BSET' | 'BST' | 'CALL' | 'CBI' | 'CBR' | 'CLC' | 'CLH' | 'CLI' | 'CLN' | 'CLR' | 'CLS' | 'CLT' | 'CLV' | 'CLZ' | 'COM' | 'CP' | 'CPC' | 'CPI' | 'CPSE' | 'DEC' | 'DES' | 'EICALL' | 'EIJMP' | 'ELPM' | 'EOR' | 'FMUL' | 'FMULS' | 'FMULSU' | 'ICALL' | 'IJMP' | 'IN' | 'INC' | 'JMP' | 'LAC' | 'LAS' | 'LAT' | 'LD' | 'LDD' | 'LDI' | 'LDS' | 'LPM' | 'LSL' | 'LSR' | 'MOV' | 'MOVW' | 'MUL' | 'MULS' | 'MULSU' | 'NEG' | 'NOP' | 'OR' | 'ORI' | 'OUT' | 'POP' | 'PUSH' | 'RCALL' | 'RET' | 'RETI' | 'RJMP' | 'ROL' | 'ROR' | 'SBC' | 'SBCI' | 'SBI' | 'SBIC' | 'SBIS' | 'SBIW' | 'SBR' | 'SBRC' | 'SBRS' | 'SEC' | 'SEH' | 'SEI' | 'SEN' | 'SER' | 'SES' | 'SET' | 'SEV' | 'SEZ' | 'SLEEP' | 'SPM' | 'ST' | 'STD' | 'STS' | 'SUB' | 'SUBI' | 'SWAP' | 'TST' | 'WDR' | 'XCH';
REGISTER        : 'R' [0-9] | 'R'{1,2}[0-9] | 'R30' | 'R31' ;
NUMBER          : '0x' [0-9a-fA-F]+ | '0X' [0-9a-fA-F]+ | [0-9]+ ;
LABEL_DEF       : [a-zA-Z_][a-zA-Z0-9_]* ':' ;
LABEL_REF       : [a-zA-Z_][a-zA-Z0-9_]* ;
DOT_DIRECTIVE   : '.' [a-zA-Z]+ ;
COMMENT         : ';' ~[\r\n]* ;

NEWLINE         : [\r\n]+ ;
WS              : [ \t]+ -> skip ;
