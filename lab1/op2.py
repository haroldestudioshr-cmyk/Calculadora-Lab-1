import math as a


class op2:

        def __init__(self, num1, res):
                self.num1 = num1
                self.res = res
                pass

        def sen(self):
                self.res = a.sin(self.num1)
                return self.res

        def cos(self):
                self.res = a.cos(self.num1)
                return self.res

        def tan(self):
                self.res = a.tan(self.num1)
                return self.res

        def fact(self):
                n = self.num1 
                if n == 1 or n == 0:
                         self.res = 1 
                         return self.res 
                self.num1 = n - 1 
                self.res = n * self.fact() 
                self.num1 = n 
                return self.res

        def fibonachi(self):
                n = self.num1 
                if n == 0:
                          self.res = 0
                          return self.res
                if n == 1:
                    self.res = 1
                    return self.res
                self.num1 = n - 1
                res1 = self.fibonachi()
                self.num1 = n - 2
                res2 = self.fibonachi()
                self.num1 = n  
                self.res = res1 + res2
                return self.res
