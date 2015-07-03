def first_non_repeat(string):
    char_count_arr = [0 for _ in range(26)]
    for letter in string:
        char_count_arr[ord(letter) - ord("A")] += 1
    
    for letter in string:
        if char_count_arr[ord(letter) - ord("A")] == 1:
            return letter
        
    return None

def main():
    string = "ABKADJAUVAEEAOAEMBKALCA"
    print first_non_repeat(string)
    print ord("C") - ord("A")
    
main()