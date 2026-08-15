class op3:
    def __init__(self, num1, num2, res):
        self.num1=num1
        self.num2=num2
        self.res=res
        pass
    def raiz (self):
        self.res=self.num1**(1/self.num2)
        return self.res

    def poten  (self):
            self.res=self.num1**self.num2
            return self.res
    def iva (self):
            self.res=self.num1*self.num2
            return self.res
