from swapper.pronounSwapper import caseParser

out = caseParser("hE", "they")
#print(out)
result = "Pass - Mixed case, len(oldPronoun)<len(newPronoun)" if out == "tHey" else "Fail - Mixed case, len(oldPronoun)<len(newPronoun)"
print(result)