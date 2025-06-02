start:
        LDI R16, 0x20      ; R16 = 0b00100000 (PB5 mask)
        OUT 0x04, R16          ; DDRB ← R16 (set PB5 as output)
main_loop:
        CALL led_on
        CALL delay
        CALL led_off
        CALL delay
        BRCC main_loop         ; Loop forever (unconditional)
led_on:
        OUT 0x05, R16          ; PORTB ← R16 → LED ON
        RET
led_off:
        LDI R17, 0x00
        OUT 0x05, R17          ; PORTB ← 0 → LED OFF
        RET
delay:
        LDI R18, 100
delay_loop1:
        LDI R19, 255
delay_loop2:
        LDI R20, 255
delay_loop3:
        NOP
        ADD R20, R21           ; R21 = 0, so this acts like DEC
        BRNE delay_loop3
        ADD R19, R21
        BRNE delay_loop2
        ADD R18, R21
        BRNE delay_loop1
        RET