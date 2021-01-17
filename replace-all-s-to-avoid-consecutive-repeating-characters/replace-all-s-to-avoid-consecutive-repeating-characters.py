class Solution:
    def modifyString(self, s: str) -> str:
        
        replace = []
        
        for x in range(len(s)):
            if s[x] == '?':
                replace.append(x)
                
        # Need to make input a char list because strings aren't assignable
        s = list(s)
        for ind in replace:
            for letter in ['a', 'b', 'c']:
                if ind == 0:
                    if len(s) == 1:
                        s[ind] = letter
                        break
                    elif s[ind + 1] != letter:
                        s[ind] = letter
                        break
                elif ind == len(s) - 1:
                    if s[ind - 1] != letter:
                        s[ind] = letter
                        break
                elif s[ind - 1] != letter and s[ind + 1] != letter:
                    s[ind] = letter
                    break
            
        # Join used essentially to cast back to a string
        return(''.join(s))
