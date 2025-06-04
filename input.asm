        .org 0x0000

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
