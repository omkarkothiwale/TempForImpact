class Solution:

    def solve(self, n):
        d = 4                       # since 4 or more consecutive days
        cons_miss = [0] * (n+1)
        # a0=0, a1=0, a2=0, a3=0, a4=0 , initialising respective indexs, representing 'n' values as indexes and value
        # of that particular index is "no of ways to miss ceremony because of not attending 4 or more consecutive days"

        if n >= d:
            cons_miss[d] = 1
        for i in range(d+1, n+1):
            cons_miss[i] = cons_miss[i-1] + cons_miss[i-2] + cons_miss[i-3] + cons_miss[i-4] + (2 ** (i - d))

        no_of_ways_to_attend = (2 ** n) - cons_miss[n]
        print(f"{no_of_ways_to_attend}")

        # no of combinations in which I'll not be able to attend the ceremony
        not_able_to_attend = (2 ** n) // 2 - (cons_miss[n] - cons_miss[n-1])

        # The probability that you will miss your graduation ceremony.
        print(f"{not_able_to_attend}/{no_of_ways_to_attend}")


s = Solution()
s.solve(5)
s.solve(10)
s.solve(4)









# class Solution:
#     def __init__(self):
#         self.count = 0
#         self.miss = 0
#         self.flag = False
#
#     def decToBinary(self, n):
#         value = "{0:b}".format(int(n))
#         if "1111" in value:
#             self.count += 1
#         elif value[-1:] == '1':
#             # print("value", value, n)
#             self.miss += 1
#         # if self.flag:
#         #     print("at half: ", self.miss)
#
#     def solve(self, n):
#         self.count = 0
#         self.miss = 0
#         self.flag = False
#         for i in range(2 ** n):
#             if i == ((2**n)//2 - 1) or i == (2 ** n)-1:
#                 # print("i", i)
#                 self.flag = True
#             else:
#                 self.flag = False
#             self.decToBinary(i)
#         # print(n, 2 ** n)
#         # print("miss", self.miss)
#         # print("cons", self.count)
#         print((2 ** n) - self.count)
#         print(str(self.miss) + "/" + str((2 ** n - self.count)))
#
#
# s = Solution()
# s.solve(5)
# s.solve(10)
