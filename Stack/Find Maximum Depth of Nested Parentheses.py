class Solution :
    def max_depth(self, s: str):
        max_deep = 0
        curr = 0
        # stack = []
        for i in s:
            if i == "(":
                # stack.insert(0,i)
                curr += 1
                if curr > max_deep:
                    max_deep = curr
            else:
                # if not stack:
                # return "Stack is Empty"
                if i == ")":
                    # stack.pop()
                    curr -= 1

        return int(max_deep)

obj = Solution()
print(obj.max_depth(
"()(())((()()))"))









