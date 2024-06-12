class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]

        for i in range(len(s)):
            if s[i] !="]":
                stack.append(s[i])
            else:
                substr=""
                while stack[-1] !="[":
                    substr=stack.pop()+substr
                stack.pop()

                l=""
                while stack and stack[-1].isdigit():
                    l=stack.pop()+l
                stack.append(int(l)*substr)
        return "".join(stack)
        