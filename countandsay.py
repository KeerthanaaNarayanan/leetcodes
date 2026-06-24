class Solution:
    def countAndSay(self, n: int) -> str:
        out = "1" 
        for i in range(n-1):
            out = self.rec_rle(out)
        return out

    def rec_rle(self, input):
        if len(input) == 0:
            return ""

        count = 1
        result = ""
        for i in range(1, len(input)):
            if input[i] == input[i - 1]:
                count += 1
            else:
                result += str(count) + input[i - 1]
                count = 1

        result += str(count) + input[-1]
        return result
                    

S = Solution()
print(S.countAndSay(4))
print("****")
print(S.countAndSay(1))