class My():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def task3(self):
        num1 = float(self.num1)
        num2 = float(self.num2)
        temp = []
        def rek(num1):
            if(num1 <= num2):
                temp.append(float(num1))
                rek(num1 + 0.5)

        rek(num1)
        print(temp)
        print(type(temp[1]))

my = My(2.0, 5.5)
my.task3()