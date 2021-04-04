#правильная скобочная последовательность
s='(([))[]{'
diction={'(':')','[':']','{':'}'}
def isCorrect(s):
  stack=[]
  for i in range(len(s)):
    if s[i] in diction:
      stack.append(s[i])
    else:
      if len(stack)>0 and diction[stack[-1]]==s[i]:
        stack.pop()
      else:
        return s[:i]
  if len(stack)==0:
    return 'CORRECT'
  else:
    return s
print(isCorrect(s))