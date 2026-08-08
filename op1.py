class op1:
    def __init__(self, num1, num2, res):
        self.num1=num1
        self.num2=num2
        self.res=res
        pass
    def suma (self):
        self.res=self.num1+self.num2
        return self.res

    def rest (self):
            self.res=self.num1-self.num2
            return self.res
    def multi (self):
            self.res=self.num1*self.num2
            return self.res
    def divi (self):
                self.res=self.num1/self.num2
                return self.res
    def mcd (self):
                
          while self.num2 != 0:
            self.res = self.num2
            self.num2 = self.num1 % self.num2
            self.num1 = self.res
            return self.num2
    def mcm (self):
        num1=self.num1
        num2=self.num2
        mcd=self.mcd()
        return (num1 * num2) // mcd