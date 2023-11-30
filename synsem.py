'''@module aaa'''
'''
    @Author: Rostislav Kral xkralr06
'''
from stackframe import *
from Instruction import *
from NilType import NilType
from Lexer import Lexer

class Analyzer:
    '''@class Analyzer is wrapper for whole interpret'''
    def __init__(self, instructions: list) -> None:
        self.stack = []
        self.instructions = []
        self._stackframe = StackFrame()
        self.execution_line = 0 # Will be changed in jumps
        instructions = sorted(instructions, key=lambda x: x['order'])
        for instruction in instructions:
            self.instructions.append(Instruction(instruction['name'], instruction['order'], instruction['args'], self._stackframe)) # Make set of instructions to interpret
    

    def escape_sequences(self):
        sequencesToReplace = []
        for instruction in self.instructions:
            for operand in instruction.operands:
                if operand['type'] == 'string':
                    if operand['val'] == None:
                        break
                    sequencesToReplace = re.findall(r'(\\[0-9]{3})+', operand['val'])

                for sequence in sequencesToReplace:
                    escaped = chr(int(sequence[1:]))
                    operand['val'] = operand['val'].replace(sequence, escaped)

    def map_labels(self): # Map labels get to know if they exists or where to jump 
        mappedLabels = {}
        for instruction in self.instructions:
            #print(instruction._opcode)
            if instruction._opcode == "LABEL":
                if instruction.operands[0]['val'] in mappedLabels:
                    exit(52)
                mappedLabels[instruction.operands[0]['val']] = instruction.order

        return mappedLabels

    def interpret(self):
        
        dest = None
        src1 = None
        src2 = None
        tmp = None
        i = 0

        lexer = Lexer(self.instructions)
        lexer.regexCheckForOperands()
        self._stackframe.setLabels(self.map_labels())

        while i < len(self.instructions):
            self.execution_line += 1
            instructionToExec = self.instructions[i]
            #print(instructionToExec._opcode)
            
            
            for operand in instructionToExec.operands: ## Variables extraction from Stackframe class
               #print(operand)
               if(operand['type'] == 'var' and operand['order'] == 1 and instructionToExec._opcode not in ('PUSHS', 'WRITE', 'EXIT', 'DPRINT')):
                    frameType, var= operand['val'].split('@')
                    #print(operand)
                    if(instructionToExec._opcode != 'DEFVAR'):
                        dest = self._stackframe.find(frameType, var)
                    else:
                        dest = self._stackframe.push(frameType, var)

               if(operand['order'] == 2 or operand['order'] == 3 or instructionToExec._opcode in ('PUSHS', 'WRITE', 'EXIT', 'DPRINT')):
                    #print(operand)
                    if operand['type'] == 'var':
                        frameType, var= operand['val'].split('@')

                        if(instructionToExec._opcode != 'DEFVAR'):
                            tmp = self._stackframe.find(frameType, var)
                            # TODO: TYPE osetreti
                    elif operand['type'] == 'type' or operand['type'] == 'string':
                        tmp = operand['val']
                    elif operand['type'] == "int":
                        tmp = int(operand['val'])
                    elif operand['type'] == "bool":
                        tmp = operand['val'] == "true"
                    elif operand['type'] == "nil":
                        tmp = NilType()

                    if operand['order'] == 1 or operand['order'] == 2:
                        src1 = tmp
                    elif operand['order'] == 3:
                        src2 = tmp
               elif operand['type'] == 'label':
                    dest = operand['val']

            #print(self._stackframe._gframe)
            i+=1
            i = instructionToExec.run([dest, src1, src2], i)
        #print(self._stackframe._gframe)