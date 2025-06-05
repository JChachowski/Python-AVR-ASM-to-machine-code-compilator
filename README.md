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
program allows CLI and GUI usage.</br>
When run with arguments:</br>
`python main.py [input_file.asm] [output_file.bin | output_file.hex] `</br>
will create .bin or .hex file with output_file name in the same directory.</br>
when run without arguments:</br>
`python main.py`</br>
will start GUI interface:</br>
![GUI Image](https://github.com/JChachowski/Python-AVR-ASM-to-machine-code-compilator/blob/main/gui_tkik.jpg?raw=true)

# Examples (WIP)

### Miganie diodą na PB0
```ASM
start:
        LDI R16, 32          ; R16 = (1 << 5), PB5 mask
        OUT 4, R16           ; DDRB ← R16, set PB5 as output

loop:
        CALL led_on
        CALL delay_1s
        CALL led_off
        CALL delay_1s
        BRCC loop            ; Infinite loop

; ---------------------------
led_on:
        OUT 5, R16           ; PORTB ← R16, turn LED on
        RET

led_off:
        LDI R17, 0
        OUT 5, R17           ; PORTB ← 0, turn LED off
        RET

; ---------------------------
delay_1s:
        LDI R18, 8           ; Outer loop count (~8×125ms ≈ 1s)
delay_outer:
        CALL delay_125ms
        ADD R18, R19         ; R19 is 0 by default; emulate DEC
        BRNE delay_outer
        RET

; ---------------------------
delay_125ms:
        LDI R20, 250
delay_loop1:
        LDI R21, 250
delay_loop2:
        NOP
        ADD R21, R22         ; R22 = 0
        BRNE delay_loop2
        ADD R20, R22
        BRNE delay_loop1
        RET

```
```hex
:1000000000E204B90E940B000E9410000E940D0043
:100010000E941000B8F705B9089510E015B90895C9
:1000200028E00E941600230FE1F708954AEF5AEFE7
:0C0030000000560FE9F7460FD1F70895C5
:00000001FF
```
