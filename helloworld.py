
class ABC(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        """Calculate the sum of two numbers"""
        return (self.a + self.b)

objA = ABC(10, 30)
total = objA.sum()
print(total)
