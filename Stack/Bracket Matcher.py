# Given a string `s` containing just the characters '(', ')', '{', '}', '\[' and '\]',
# determine if the input string is valid.
#
# An input string is valid if:
#
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

# s = "()[]{}"


s = "([)]"


stack = []
pairs = {
    "(":")",
    "[":"]",
    "{":"}"
}
valid = True
for ch in s:
    if ch in pairs:
        stack.append(ch)
    else:
        if not stack:
            valid = False
            # print("False")
            break
        top = stack[-1]
        if pairs[top] != ch:
            valid = False
            # print("False")
            break
        stack.pop()
        # print(top)
        # stack.pop()
if valid is True and len(stack) == 0:
    print("True")
else:
    print("False")


class Solution:
    def isValid(self, s: str) -> bool:
        valid = True
        stack = []
        pairs = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if not stack:
                    valid = False
                    return False
                top = stack[-1]
                if pairs[top] != ch:
                    valid = False
                    return False
                stack.pop()

        if valid and len(stack) == 0:
            return True
        else:
            return False



obj = Solution()
print(obj.isValid("([)]"))


class KSolution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for chr in s:
            if chr in pairs:
                if not stack or stack.pop() != pairs[chr]:
                    return False
            return True

        if not stack:
            return True
        return False

k = KSolution()
print(k.isValid("([)]"))