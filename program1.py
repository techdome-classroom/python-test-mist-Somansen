class Solution:
def isValid(self, s: str) -> bool:
stack
o
lookup = (")":"",")":"(", "]":"[">

for p in S:
if p in lookup.values():
stack.append(p)
elif stack and lookup[p] == stack[-1]:
stack.pop()
else:
return False
return stack == []
    



  

