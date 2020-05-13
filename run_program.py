class test4:
    def __init__(self, x1=None, x2=None):
        self.x1 = x1
        self.x2 = x2
    def getTest(self,x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.y = 0*x1 + 3*x2
        if self.y > 10:
            self.y = 0.25*x1 + 2.75*x2
        else:
            self.y
        print('Result : ', self.y)

cal4 = test4()
cal4.getTest(3, 5)