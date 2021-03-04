'''
Magic methods in Python are the special methods that start and end with the double underscores. They are also called dunder methods.
Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action.

['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__',
'__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__',
'__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
'__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
'__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
'__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
'''

class magic:
    def __init__(self):
        self.l = []

    def input(self):
        no = int(input("enter number of ds"))
        if not no:
            print("invalid input")
        else:
            for i in range(0, no):
                ele = int(input("enter element"))
                self.l.append(ele)

    def __add__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]+other.l[i])
            print(ans)
        else:
            print("input not accepted")

    def __sub__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]-other.l[i])
            print(ans)
        else:
            print("input not accepted")

    def __mul__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]*other.l[i])
            print(ans)
        else:
            print("input not accepted")

    def __truediv__(self, other):
        ans = []
        if len(self.l) == len(other.l):
            for i in range(len(self.l)):
                ans.append(self.l[i]/other.l[i])
            print(ans)
        else:
            print("input not accepted")