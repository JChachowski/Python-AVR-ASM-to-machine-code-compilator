# AVR ASM to machine code compiler (in Python3)
### Author
Chachowski Jakub
### Contact
jchachowski@student.agh.edu.pl
### Objectives
Create Assembler for AVR writen in Python.

### Implementation language: Python
### Scanner & Parser implementation: [ANTLR4](https://www.antlr.org/) for parser and lexer.
---
# Grammar Summary

## Parser Rules

| Rule         | Description                                |
|--------------|--------------------------------------------|
| `program`    | Whole source file                          |
| `line`       | Single line: instruction, label, directive |
| `instruction`| AVR opcode + optional operands             |
| `operandList`| List of operands separated by commas       |
| `operand`    | Can be a register, number, or label ref    |
| `label`      | Label definition with colon                |
| `directive`  | Assembler directive (e.g. `.org`)          |
| `comment`    | Comment line starting with `;`             |

## Lexer Tokens

| Token         | Example         | Description                            |
|---------------|-----------------|----------------------------------------|
| `mnemonic`    | `LDI`, `ADD`    | Instruction name (uppercase only)      |
| `REGISTER`    | `R16`           | CPU registers                          |
| `NUMBER`      | `42`, `0x2A`    | Decimal or hexadecimal numbers         |
| `LABEL_DEF`   | `start:`        | Label definition (ends with `:`)       |
| `LABEL_REF`   | `loop`          | Reference to a label                   |
| `DOT_DIRECTIVE`| `.org`, `.byte`| Assembler directive                    |
| `COMMENT`     | `; This is a comment` | Comment till end of line         |
| `NEWLINE`     | `\n`            | Line breaks                            |
| `WS`          | `[ \t]+`        | Whitespace (ignored)                   |

full list of mnemonics is available at pt. 5 in [AVR-Instruction-Set-Manual](https://ww1.microchip.com/downloads/en/devicedoc/AVR-Instruction-Set-Manual-DS40002198A.pdf) and will be added to AVR.g4 file later as a " ADD | ADC | ADIW |..." list

```
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
```
---
# Examples (WIP)

### Miganie diodą na PB0
```ASM
ldi    R16, 0x03
    ldi    R17, 0xFF
    out    0x3D, R17
    out    0x3E, R16
    ldi    R20, 0b00000001
    ldi    R21, 0
    out    0x17, R20
LOOP:
    out    0x18, R20
    call    DELAY_1S
    out    0x18, R21
    call    DELAY_1S
    jmp    LOOP

DELAY_1S:
    ldi    r16, 82
    ldi    r17, 43
    ldi    r18, 0
DELAY_1S_1: 
    dec    r18
    brne    DELAY_1S_1
    dec    r17
    brne    DELAY_1S_1
    dec    r16
    brne    DELAY_1S_1
    lpm
    nop
    ret
```

