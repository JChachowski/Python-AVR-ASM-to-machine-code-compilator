start:
        LDI R16, 0x20      ; R16 = 0b00100000 (PB5 mask)
        OUT 0x04, R16          ; DDRB ← R16 (set PB5 as output)

loop:
        OUT 0x05, R16          ; PORTB ← R16 → LED ON

        ; ~0.5 second delay (nested loops)
        LDI R17, 20            ; Outer loop count (tuned)
delay_on_outer:
        LDI R18, 255           ; Middle loop
delay_on_middle:
        LDI R19, 255           ; Inner loop
delay_on_inner:
        NOP
        NOP
        NOP
        NOP
        NOP
        ADD R19, R20           ; R20 = 0, so acts like DEC (loop R19 down)
        BRNE delay_on_inner
        ADD R18, R20
        BRNE delay_on_middle
        ADD R17, R20
        BRNE delay_on_outer

        LDI R21, 0x00
        OUT 0x05, R21          ; PORTB ← 0 → LED OFF

        ; ~0.5 second delay again
        LDI R17, 20
delay_off_outer:
        LDI R18, 255
delay_off_middle:
        LDI R19, 255
delay_off_inner:
        NOP
        NOP
        NOP
        NOP
        NOP
        ADD R19, R20
        BRNE delay_off_inner
        ADD R18, R20
        BRNE delay_off_middle
        ADD R17, R20
        BRNE delay_off_outer

        BRCC loop              ; Unconditional loop back