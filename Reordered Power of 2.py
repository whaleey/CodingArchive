#From Leetcode Daily challenge
#https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3679/
###Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.
###Return true if and only if we can do this in a way such that the resulting number is a power of 2.

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        N = str(N)
        lst_two = [1]
        lst = []
        n=1
        v=2

        while n<=1000000000:
            if v<=1000000000:
                lst_two.append(v) #Get the list of integers that have the power of 2 and less than 10^9
            elif v>=1000000000:
                break
            v*=2

        tst_lst = []
        lst = []

        for i in N:
            tst_lst.append(i)
            tst_lst.sort()

        for n in lst_two:
            n = str(n)
            for i in n:
                lst.append(i)   #Turn the integer into a sorted list of stringed characters for comparison
                lst.sort()
            if tst_lst == lst:  #Compare between the power_of_two list and the testing number
                return True
                break
            lst = []
