def is_palindrome(s):
    i = 0
    j = len(s) - 1
    
    while i < len(s):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
        
    return True

def longest_palindrome(s):
    max_len = 1
    max_palindrome = s[0]
    for i in range(len(s) - 1):
        for j in range(i+1, len(s)):
            print "is palindrome:", s[i:j]
            if is_palindrome(s[i:j]):
                if len(s[i:j]) > max_len:
                    max_len = len(s[i:j])
                    max_palindrome = s[i:j]
            #else:
                #break
                
    return max_palindrome, max_len

def longest_palindrome2(s):
    max_pal = s[0]
    max_len = 1
    for i in range(len(s)):
        a = i
        b = i + 1
        while a >= 0 and b < len(s):
            print "i=", i, "a=", a, "b=", b, "s[a]=", s[a], "s[b]=", s[b]
            if s[a] == s[b]:
                #max_pal = s[a:b+1]
                if (b + 1 - a) > max_len:
                    max_len = b + 1 - a
                    max_pal = s[a:b+1]
                a -= 1
                b += 1
            else:
                break
                
    return max_pal, max_len
            
        

#s_rev = ""
#for idx in range(len(s) - 1, -1, -1):
#    s_rev += s[idx]
    

def main():
    s = "ccddcc"
    print is_palindrome(s)
    s = "abaccddccefe"
    #print longest_palindrome(s)
    s = "abaccddccefe"
    #s = "racecars"
    print longest_palindrome2(s)
    
main()