'''@module instruction'''
'''
    @Author: Rostislav Kral xkralr06
'''
from stackframe import *
from NilType import NilType
import re
import sys

class InstructionRule:
    pass

class Instruction:
    def __init__(self, name: str, order: int, operands: list, stackframe: StackFrame):
        self._opcode = name.upper()
        self.order = order
        self.operands = operands
        self._stackframe = stackframe

    def parseOperands(self):
        pass

    def parseVar(self, operand):
        pass

    def run(self, data:list, i:int): # Returns index of instruction that should be executed next (due to jumps)
        tmp = None
        if(self._opcode == "CREATEFRAME"):
            self._stackframe.make()
        elif(self._opcode == 'MOVE'):
            #print(data)
            tmp = data[1]
        elif(self._opcode == 'JMP'):
            i = self._stackframe.getLabel(data[0])

        elif(self._opcode == 'ADD'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != int or type(data[2]) != int):
                exit(53)
            tmp = data[1] + data[2]
        elif(self._opcode == 'IDIV'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != int or type(data[2]) != int):
                exit(53)
            if(data[2] == 0):
                exit(57)
            tmp = data[1] // data[2]
        elif(self._opcode == 'MUL'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != int or type(data[2]) != int):
                exit(53)
            tmp = data[1] * data[2]
        elif(self._opcode == 'LT'):
            if(data[1] == None or data[2] == None or isinstance(data[1], NilType) or isinstance(data[2], NilType)):
                exit(56)
            if(type(data[1]) != type(data[2])):
                exit(53)
            tmp = data[1] < data[2]
        elif(self._opcode == 'GT'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != type(data[2]) or isinstance(data[1], NilType)):
                exit(53)
            tmp = data[1] > data[2]
        elif(self._opcode == 'SUB'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != int or type(data[2]) != int):
                exit(53)
            tmp = data[1] - data[2]
        elif(self._opcode == 'PUSHFRAME'):
            self._stackframe.pushFrame()
        elif(self._opcode == 'POPFRAME'):
            self._stackframe.popFrame()
        elif(self._opcode == 'EQ'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != type(data[2]) or isinstance(data[1], NilType) or isinstance(data[2], NilType )):
                exit(53)
            tmp = data[1] == data[2]
        elif(self._opcode == 'AND'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != bool or type(data[2]) != bool):
                exit(53)
            tmp = data[1] and data[2]
        elif(self._opcode == 'OR'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != bool or type(data[2]) != bool):
                exit(53)
            tmp = data[1] or data[2]
        elif(self._opcode == 'NOT'):
            if(data[1] == None):
                exit(56)

            if(type(data[1]) != bool):
                exit(53)


            tmp = not data[1]

        elif(self._opcode == 'JUMPIFNEQ'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != type(data[2])):
                exit(53)
        
            i = self._stackframe.getLabel(data[0]) if data[1] != data[2] else i
        elif(self._opcode == 'JUMPIFEQ'):
            if(type(data[1]) != type(data[2])):
                exit(53)
        
            i = i if data[1] != data[2] else self._stackframe.getLabel(data[0])

        elif(self._opcode == 'STRLEN'):
            if(type(data[1]) != str):
                exit(53)

            tmp = len(data[1])

        elif(self._opcode == 'EXIT'):
            if(type(data[1]) != int):
                exit(53)
            if(data[1] < 0 or data[1] > 49):
                exit(53)

            sys.exit(data[1])
        elif(self._opcode == 'TYPE'):
            if(type(data[1]) == NilType):
                tmp = 'nil'
            
            elif(type(data[1]) == int):
                tmp = 'int'
            elif(type(data[1]) == bool):
                tmp = 'bool'
            elif(type(data[1]) == str):
                tmp = 'string'
            elif(type(data[1]) == None):
                tmp = ''
                
        elif(self._opcode == 'WRITE'):
            if(data[1] == None):
                exit(56)
            if(type(data[1]) != NilType):
                if(type(data[1]) == bool):
                    print(str(data[1]).lower(), end='')
                else:
                    print(data[1], end='')
        elif(self._opcode == "PUSHS"):
            self._stackframe.stackPush(data[1])
        elif(self._opcode == 'POPS'):
            tmp = self._stackframe.stackPop()

        elif(self._opcode == 'STRI2INT'):
            #print(data[1])
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != str or type(data[2]) != int):
                exit(53)

            try:  
                tmp = ord(data[1][data[2]])
            except:
                exit(58)
        elif(self._opcode == 'SETCHAR'):
            if(data[1] == None or data[2] == None):
                exit(56)
            if(type(data[1]) != int or type(data[2]) != str or type(data[0]) != str ):
                exit(53)
            
            listForChars = list(data[0])
            #TODO: prepsat
            try:
                listForChars[data[1]] = data[2][0]
                tmp = "".join(listForChars)
            except:
                exit(58)
        elif(self._opcode == 'DPRINT'):
            if(type(data[1]) != NilType):
                print(data[1] if type(data[1]) != bool else str(data[1]).lower(), end='', file=sys.stderr)
        elif(self._opcode == 'BREAK'):
            print("TF:", self._stackframe._tframe, file=sys.stderr)
            print('GF:', self._stackframe._gframe, file=sys.stderr)
            print('LF:', self._stackframe._lframe, file=sys.stderr)
            print('Instruction index:', i, file=sys.stderr)
        elif(self._opcode == 'GETCHAR'):
            if(type(data[1]) != str or type(data[2]) != int):
                exit(53)
            try:
                tmp = data[1][data[2]]
            except:
                exit(58)
        elif(self._opcode == 'CONCAT'):
            if(type(data[1]) != str or type(data[2]) != str):
                exit(53)

            tmp = data[1] + data[2]
        elif(self._opcode == 'CALL'):
            self._stackframe.pushFunctionStack(i)
            i = self._stackframe.getLabel(data[0])

        elif(self._opcode == 'RETURN'):
            i = self._stackframe.popFunctionStack()
        elif(self._opcode == 'INT2CHAR'):
            #print(data[1])
            if(type(data[1]) != int):
                exit(53)

            try:  
                tmp = chr(data[1])
            except:
                exit(58)
        if(len(self.operands) != 0):
            if self.operands[0]['type'] == 'var' and self._opcode not in ("PUSHS", "WRITE", "EXIT", "DPRINT"):
                frameType, var= self.operands[0]['val'].split('@')
                self._stackframe.insert(frameType, var, tmp)
        return i