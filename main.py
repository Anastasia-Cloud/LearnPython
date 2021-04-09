'''
Даны две строки S1 и S2 . Длины строк не превосходят 1000000. Найдите их наибольшую по длине общую подстроку.
'''
def fixSubstr(l,s1,s2):
  m=set()
  for i in range(len(s1)-l+1):
    m.add(s1[i:i+l])
  for i in range(len(s2)-l+1):
    if s2[i:i+l] in m:
      return s2[i:i+l]
  

def maxSubstr(s1,s2):
  l=min(len(s1),len(s2))
  for i in range(l,0,-1):
    res=fixSubstr(i,s1,s2)
    if res is not None:
      return res

print(maxSubstr('aabcdeabcdef','acdeabf'))
print(maxSubstr('aabcdeabcdef','aabcdea def'))
print(maxSubstr('qwerty','123'))

    