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

full list of mnemonics is available at pt. 5 in [AVR-Instruction-Set-Manual](https://ww1.microchip.com/downloads/en/devicedoc/AVR-Instruction-Set-Manual-DS40002198A.pdf).

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
mnemonic        : 'ADC' | 'ADD' | 'ADIW' | 'AND' | 'ANDI' | 'ASR' | 'BCLR' | 'BLD' | 'BRBC' | 'BRBS' | 'BRCC' | 'BRCS' | 'BREAK'| ...;
REGISTER        : 'R' [0-9] | 'R'{1,2}[0-9] | 'R30' | 'R31' ;
NUMBER          : '0x' [0-9a-fA-F]+ | '0X' [0-9a-fA-F]+ | [0-9]+ ;
LABEL_DEF       : [a-zA-Z_][a-zA-Z0-9_]* ':' ;
LABEL_REF       : [a-zA-Z_][a-zA-Z0-9_]* ;
DOT_DIRECTIVE   : '.' [a-zA-Z]+ ;
COMMENT         : ';' ~[\r\n]* ;

NEWLINE         : [\r\n]+ ;
WS              : [ \t]+ -> skip ;

```
---
# instalation
```
pip install antlr4-python3-runtime
curl -O https://www.antlr.org/download/antlr-4.13.0-complete.jar
java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 -visitor AVR.g4
pip install intelhex
pip install tkinter
```
# Usage
program allows CLI and GUI usage.
When run with arguments:
`python main.py [input_file.asm] [output_file.bin | output_file.hex] `
will create .bin or .hex file with output_file name in the same directory.
when run without arguments:
`python main.py`
will start GUI interface:
![GUI Image](https://github.com/JChachowski/Python-AVR-ASM-to-machine-code-compilator/blob/main/gui_tkik.jpg?raw=true)

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
```hex
03 E0 1F EF 1D BF 0E BF 41 E0 50 E0 47 BB 48 BB 0E 94 00 00 58 BB 0E 94 00 00 0C 94 00 00 02 E5 1B E2 20 E0 2A 95 01 F4 1A 95 01 F4 0A 95 01 F4 C8 95 00 00 08 95
```
