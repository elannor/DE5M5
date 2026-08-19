from calculator import Calculator

class Scientific_Calc(Calculator):
    def __init__(self, a, b):
        super().__init__(a,b)

    def get_exp(self):
        return self.a**self.b
    
sci_calc = Scientific_Calc(a=2,b=3)
print(sci_calc.get_exp())