'''
    @Author: Rostislav Kral xkralr06
'''

import re

class Lexer:
    def __init__(self, instructions) -> None:
        self._instructions = instructions
        self._rules = {
        'DEFVAR': ['var'],
        'MOVE': ['var', 'symbol'],
        'CREATEFRAME': [],
        'PUSHFRAME': [],
        'POPFRAME': [],
        'CALL': ['label'],
        'RETURN': [],
        'PUSHS': ['symbol'],
        'POPS': ['var'],
        'ADD': ['var', 'symbol', 'symbol'],
        'SUB': ['var', 'symbol', 'symbol'],
        'MUL': ['var', 'symbol', 'symbol'],
        'IDIV': ['var', 'symbol', 'symbol'],
        'LT': ['var', 'symbol', 'symbol'],
        'GT': ['var', 'symbol', 'symbol'],
        'EQ': ['var', 'symbol', 'symbol'],
        'AND': ['var', 'symbol', 'symbol'],
        'NOT': ['var', 'symbol'],
        'OR': ['var', 'symbol', 'symbol'],
        'STRI2INT': ['var', 'symbol', 'symbol'],
        'CONCAT': ['var', 'symbol', 'symbol'],
        'GETCHAR': ['var', 'symbol', 'symbol'],
        'SETCHAR': ['var', 'symbol', 'symbol'],
        'INT2CHAR': ['var', 'symbol'],
        'READ': ['var', 'type'],
        'WRITE': ['symbol'],
        'STRLEN': ['var', 'symbol'],
        'TYPE': ['var', 'symbol'],
        'LABEL': ['label'],
        'BREAK': [],
        'DPRINT': ['symbol'],
        'JUMP':['label'],
        'EXIT': [],
        'JUMPIFEQ': ['label', 'symbol', 'symbol'],
        'JUMPIFNEQ': ['label', 'symbol', 'symbol'],
    }


    def regexCheckForOperands(self):
        return
        for instruction in self._instructions:
            if instruction._opcode not in self._rules.keys():
                exit(32)

            if len(instruction.operands) != len(self._rules[instruction._opcode]):
                exit(32)
            return
