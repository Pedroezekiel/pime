class Calculate(object):
    def add(self, x, y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("please input number")
# if __name__ == '__main__':
#     calc  = Calculate()
#     result = calc.add(2,2)
#     print( result)
