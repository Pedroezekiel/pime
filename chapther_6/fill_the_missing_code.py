# print({1, 2, 4, 8, 16} | {1, 4, 16, 64, 256})
# print({1, 2, 4, 8, 16} & {1, 4, 16, 64, 256})
# print({1, 2, 4, 8, 16} - {1, 4, 16, 64, 256})
# print({1, 2, 4, 8, 16} ^ {1, 4, 16, 64, 256})
# print({1, 2, 4, 8, 16} .isdisjoint({1, 4, 16, 64, 256}))
# names = ["bola pedro", "titi kola"]
# print([name for  name in names if name.split()[-1] == "kola"])
class Solution:
    def isPalindrome(self, head):
        if head == head[::-1]:
            print(True)
        else:
            print(False)


solution = Solution()
solution.isPalindrome([1, 2])
