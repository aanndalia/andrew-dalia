def permute(s):
    if len(s) < 2:
        return s
    
    permutations = []
    for i in range(len(s)):
        rest = s.split(s[i])
        rest_str = ''.join(rest)
        s_permutes = permute(rest_str)
        for p in s_permutes:
            permutations.append(s[i] + p)
            
    return permutations

s = "bear"
print permute(s)