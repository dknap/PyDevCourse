class Func:
    def __init__(self, value):
        self.value = value

    def __call__(self, times):
        if type(self.value) == int:
            return self.value * times
        elif type(self.value) == str:
            return self.value * times
        else:
            return self.value

num = Func(4)
print(num(21))
txt = Func("_Dawid Knap_")
print(txt(3))