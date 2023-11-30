'''
    @Author: Rostislav Kral xkralr06
'''

class StackFrame:
    '''
    
    Class for serving frames and stacks
    
    '''
    def __init__(self):
        self._gframe = {}
        self._tframe = None
        self._lframe = []
        self._stack = []
        self._functionStack = []

    def push(self,frame, var_name):
        if(frame == "GF"):
            #print(var_name)
            if var_name in self._gframe:
                exit(52)
            self._gframe[var_name] = None
        elif(frame == "LF"):
            if len(self._lframe) == 0:
                exit(55)
            if var_name in self._lframe[-1]:
                exit(52)
            self._lframe[-1][var_name] = None
        elif(frame == "TF"):
            #print(self._tframe)
            if self._tframe == None:
                exit(55)

            if var_name in self._tframe:
                exit(52)
            self._tframe = None

        return None
    def pushFrame(self):
        if(self._tframe == None):
            exit(55)
        self._lframe.append(self._tframe)
        self._tframe = None

    def popFrame(self):
        if(len(self._lframe) < 1):
            exit(55)
        self._tframe = self._lframe.pop()

    def get(self):
        return self._tframe
        
    def make(self):
        self._tframe = {}

    def find(self, frame, var_name):
        if(frame == "GF"):
            if var_name not in self._gframe:
                exit(54)

            return self._gframe[var_name]
        elif(frame == "LF"):
            if len(self._lframe) == 0:
                exit(55)
            
            if var_name not in self._lframe[-1]:
                exit(54)

            return self._lframe[-1][var_name]
        elif(frame == "TF"):
            if self._tframe == None:
                exit(55)
            if var_name not in self._tframe:
                exit(54)
            return self._tframe[var_name]
        
    def insert(self,frame, var_name, val):
        if(frame == "GF"):
            #print(self._gframe[var_name])
            if var_name not in self._gframe:
                exit(55)

            self._gframe[var_name] = val
        elif(frame == "LF"):
            if len(self._lframe) == 0:
                exit(55)
            
            if var_name not in self._lframe[-1]:
                exit(54)

            self._lframe[-1][var_name] = val
        elif(frame == "TF"):
            if self._tframe == None:
                exit(55)
            if var_name not in self._tframe:
                exit(54)

            self._tframe[var_name] = val
    def pushFunctionStack(self, val):
        self._functionStack.append(val)
    def popFunctionStack(self):
        if len(self._functionStack) < 1:
            exit(56)
        return self._functionStack.pop()
    def setLabels(self, labels: dict):
        self.labels = labels
        #print(labels)

    def getLabel(self, label_name):
        if(label_name not in self.labels):
            exit(52)
        return self.labels[label_name]

    def stackPush(self, val):
        self._stack.append(val)
    def stackPop(self):
        if(len(self._stack) < 1):
            exit(56)
        return self._stack.pop()