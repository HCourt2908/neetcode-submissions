class Solution:
    def isValid(self, s: str) -> bool:

        unclosed = []
        n = 0


        for x in s:
            if x == "(":
                unclosed.append("(")
                n += 1
            elif x == "{":
                unclosed.append("{")
                n += 1
            elif x == "[":
                unclosed.append("[")
                n += 1
            elif x == ")":
                if n == 0:
                    return False
                elif unclosed[n-1] == "(":
                    unclosed.pop(n-1)
                    n -= 1
                else:
                    return False
            elif x == "}":
                if n == 0:
                    return False
                elif unclosed[n-1] == "{":
                    unclosed.pop(n-1)
                    n -= 1
                else:
                    return False
            elif x == "]":
                if n == 0:
                    return False
                elif unclosed [n-1] == "[":
                    unclosed.pop(n-1)
                    n -= 1
                else:
                    return False
            else:
                return False
        return len(unclosed)==0
        