import sys
import math

def main():

    name = input("Input name")
    a = input("a = ")
    b = input("b = ")
    alpha = input("alpha = ")
    beta = input("beta = ")

    x = membershipCurves(name, a, b, alpha, beta)
    print(x[Name])

class membershipCurves:

    name = ""

    def __init__(self, name, a, b, alpha, beta):
        self.a = int(a)
        self.b = int(b)
        self.alpha = int(alpha)
        self.beta = int(beta)
        self.name = name

    def __str__(self):
        return str(self.membership)

    def name(self):
        return self.name

    def membership(self, value):

        value = int(value)

        if (value < (self.a - self.alpha)):
            return 0
        elif (value in range (self.a - self.alpha, self.a)):
            return (value - self.a + self.alpha) / self.alpha
        elif (value in range(self.a, self.b)):
            return 1
        elif (value in range(self.b, self.b + self.beta)):
            return (self.b + self.beta - value) / self.beta
        elif (value > (self.b + self.beta)):
            return 0

        return

if __name__ == '__main__':
    main()