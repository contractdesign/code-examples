package main

import "fmt"

type Opcode int

const (
	NOP Opcode = 0
	ADD Opcode = 1
	SUB Opcode = 2
	JEZ Opcode = 3
	JNZ Opcode = 4
	JGZ Opcode = 5
	JLZ Opcode = 6
	JMP Opcode = 7
	JRO Opcode = 8
	SWP Opcode = 9
	SAV Opcode = 10
	NEG Opcode = 11
	MOV Opcode = 12
)

type Reg int

const (
	NIL   Reg = -1
	ACC   Reg = 0
	BAK   Reg = 1
	LEFT  Reg = 2
	RIGHT Reg = 3
	DOWN  Reg = 4
	UP    Reg = 5
	ANY   Reg = 6
	LAST  Reg = 7
)

type Instruction struct {
	opcode        Opcode
	rnumA         Reg
	rnumB         Reg
	literal       int
	valid_literal bool
}

// the state of a node
type Node struct {
	iptr   int
	instrs [10]Instruction
	regs   [10]int
}

func (n *Node) lookup(reg Reg) int {
	if reg == NIL {
		return 0
	} else {
		return n.regs[reg]
	}
}

func (n *Node) reset() {
	n.iptr = 0
	n.regs[ACC] = 0
	n.regs[BAK] = 0

	for i := 0; i < 10; i++ {
		n.instrs[i] = Instruction{opcode: NOP, rnumA: NIL, rnumB: NIL, literal: 0, valid_literal: false}
	}
}

func (n *Node) print() {
	fmt.Println("iptr:", n.iptr, "\nACC:", n.regs[ACC], "\nBAK:", n.regs[BAK])
	fmt.Println()
}

func (n *Node) incr_iptr() {
	n.iptr = (n.iptr + 1) % 10 // TODO fix
}

func (n *Node) exec() {
	var sign int

	instr := n.instrs[n.iptr]
	switch instr.opcode {
	case NOP:
		// do nothing, go to next instruction
		fmt.Println( "here" )
		n.incr_iptr()

	case NEG:
		// negate ACC
		n.regs[ACC] = -n.regs[ACC]
		n.incr_iptr()

	case SAV:
		// save ACC to BAK
		n.regs[BAK] = n.regs[ACC]
		n.incr_iptr()

	case SWP:
		// swap ACC and BAK
		temp := n.regs[ACC]
		n.regs[ACC] = n.regs[BAK]
		n.regs[BAK] = temp
		n.incr_iptr()

	// subtraction and addition are almost the same
	case SUB:
		// subtract the indicated literal / register from ACC
		sign = -1
		fallthrough
	case ADD:
		// add the indicated literal / register to ACC
		sign = 1
		var summand int

		if instr.valid_literal {
			summand = instr.literal
		} else {
			summand = n.lookup(instr.rnumA)
		}
		n.regs[ACC] += sign * summand % 1000 // TODO check this

	case MOV:
		var src_value int
		if instr.valid_literal {
			src_value = instr.literal
		} else {
			src_value = n.lookup(instr.rnumA)
		}
		if instr.rnumB != NIL {
			n.regs[instr.rnumB] = src_value
		}

	case JMP:
		n.iptr = instr.literal
		n.incr_iptr()

	case JEZ:
		if n.regs[ACC] == 0 {
			n.iptr = instr.literal
		} else {
			n.incr_iptr()
		}

	case JGZ:
		if n.regs[ACC] > 0 {
			n.iptr = instr.literal
		} else {
			n.incr_iptr()
		}

	case JLZ:
		if n.regs[ACC] < 0 {
			n.iptr = instr.literal
		} else {
			n.incr_iptr()
		}

	case JRO:
		n.iptr += instr.literal // TODO check
	}
}

func main() {
	var n Node
	n.reset()

	for i := 0; i < 10; i++ {
		n.exec()
		n.print()
	}

}
