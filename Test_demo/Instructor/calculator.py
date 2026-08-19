class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def get_sum(self):
        return self.a + self.b
    
    def get_diff(self):
        return self.a - self.b
    
    def get_prod(self):
        return self.a * self.b
    
    def get_div(self):
        return self.a / self.b
    
if __name__ == "__main__":
    myCalc = Calculator(a=3,b=2)
    print(myCalc.get_prod())


        