# Notes on Reverse Engineering

# x86_64 calling conventions



The first 6 parameters are passed via registers ([source](https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64))

    rdi, rsi, rdx, rcx, r8, r9

The return value is passed in

    rax

Call Stack

    RBP + 24  extra parameter #1
    RBP + 16  extra parameter #2
    RBP + 8   return address
    RBP       saved RBP         <--- RBP
    RBP - 8   local variable #1
    RBP - 16  local variable #2 <--- RSP
              128B "red zone"
              




## Static Analysis Using objdump

Disassemble a binary in Intel assembly format

    objdump -d -M intel <binary> > <binary>.disasm

List headers

    objdump -h <binary>

Examine a specific header

    objdump -j <header> -d <binary>


## Strings

List strings in a binary with offset in hexadecimal

    strings -tx <binary>


# Dynamic Analysis Using GDB

Set a breakpoint at an instruction

    break *0x<address>

Print address as string

    x/s <address>

Print 4 words as strings above the stack pointer
    x/4ws $esp

Current instruction

    p $eip

Print all registers

    info reg
