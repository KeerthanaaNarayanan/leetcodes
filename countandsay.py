class Solution:
    def countAndSay(self, n: int) -> str:
        out = "1" 
        if n == 1:
            return out

        for i in range(n):
            out = self.rec_rle(out)
            print("out is: ", out)

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
S.countAndSay(4)