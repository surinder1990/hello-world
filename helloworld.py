
class ABC(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        """Calculate the sum of two numbers"""
        return (self.a + self.b)

objA = ABC(20, 10)
print(objA.sum())
