class Solution:
    def addBinary(self, a, b):
        if len(b) == 0:
            return a
        if len(a) == 0:
            return b
        if a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[0:-1], b[0:-1]) + "0"
        if a[-1] == "1" and b[-1] == "1":
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), "1") + "0"
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + "1"
