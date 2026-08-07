class Solution:
    def simplifyParentheses(self,s: str) -> str:
        count = 0
        ans = ""
        for  i in s:
            if i == "(":
                if count > 0:
                    ans += i
                count += 1
            elif i == ")":
                if count > 1:
                    ans += i
                count -= 1

        return ans


obj = Solution()
print(obj.simplifyParentheses("(()())(())"))