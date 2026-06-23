class Solution:
    def countAndSay(self, n: int) -> str:
        out = "1" 
        if n == 1:
            return out

        for i in range(n):
            out = self.rec_rle(out)
            print("out is: ", out)

    def rec_rle(self, input):
        i = 0
        cur = input[i]
        val = ""
        while i < len(input):
            j = i + 1
            while j < len(input):
                print("I is ",i)
                print("J is: ", j)
                if input[i] == input[j]:
                    j += 1
                else:
                    i = j
                    cur = input[i]
                    j += 1
            val = val + str(j) + cur
            print("val is ", val)
            j += 1
            i = j
        return val
                    

S = Solution()
S.countAndSay(4)