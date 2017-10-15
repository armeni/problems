class brackets:
   def valid(self, s):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for p in s:
            if p in pchar:
                stack.append(p)
            elif len(stack) == 0 or pchar[stack.pop()] != p:
                return False
        return len(stack) == 0

s=str(input('Введите последовательность скобок: '))
print(brackets().valid(s))