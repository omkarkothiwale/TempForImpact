class Solution:
    def __init__(self):
        self.count = 0
        self.miss = 0

    def decToBinary(self, n):
        value = "{0:b}".format(int(n))
        if "1111" in value:
            self.count += 1
        elif value[-1:] == '1':
            self.miss += 1

    def solve(self, n):
        self.count = 0
        self.miss = 0
        for i in range(2 ** n):
            self.decToBinary(i)
        print((2 ** n) - self.count)
        print(str(self.miss) + "/" + str((2 ** n - self.count)))


s = Solution()
s.solve(5)
s.solve(10)
