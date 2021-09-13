from math import sqrt


class phuongtrinhbac2:
    def __init__(self, a=0.0, b=0.0, c=0.0):
        self.__a = a
        self.__b = b
        self.__c = c

    def nhap(self):
        self.__a = float(input("Nhập a: "))
        self.__b = float(input("Nhập b: "))
        self.__c = float(input("Nhập c: "))

    def xuat(self):
        print("{}x^2+{}x+{}".format(self.__a, self.__b, self.__c))

    def giai(self):
        if self.__a == 0:
            if self.__b == 0:
                if self.__c == 0:
                    print("Phương trình có vô số nghiệm")
                else:
                    print("Phương trình vô nghiệm")
            else:
                print("Phương trình có nghiệm duy nhất: x = {}".format(-self.__c / self.__b))
        else:
            __delta = self.__b * self.__b - 4 * self.__a * self.__c
            if __delta < 0:
                print("Phương trình vô nghiệm")
            elif __delta == 0:
                print("Phương trình có nghiêm kép: x = {}".format(-self.__b/2/self.__a))
            else:
                print("Phương trình có hai nghiệm phân biệt: x1 = {}, x2 = {}".
                      format(-(self.__b-sqrt(__delta))/2/self.__a, -(self.__b+sqrt(__delta))/2/self.__a))
