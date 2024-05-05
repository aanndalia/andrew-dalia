from typing import *

"""
Hi,  how are
you    doing
today?
a   a   a  a
"""


#     3 // 2 = 1
#     3 % 2 = 1
#     (12 - 4) // 3 = 2
#     8 % 3 = 2
# (12 - 9) // 2 = 1 space between words
# (12 - 8) // 1


# split by words
# sum(len(words)) + (len(words))  < width + 1
# (width - sum(len(words))) // (len(words) - 1)
# (width - sum(len(words))) % (len(words) - 1)

# sum(len(words)) characters

def justify_text(text: str, width: int) -> List[str]:
    if not text:
        return text

    word_list = text.split(' ')
    print(word_list)
    res = []
    cur_words_length = 0
    cur_num_words = 0
    for i, word in enumerate(word_list):
        print(i, word)
        if cur_words_length + len(word) + cur_num_words - 1 < width:
            cur_words_length += len(word)
            cur_num_words += 1
            print(cur_words_length, cur_num_words)
        else:
            floor_spaces_between = (width - cur_words_length) // (cur_num_words - 1)
            extra_spaces_allocate = (width - cur_words_length) % (cur_num_words - 1)
            print(floor_spaces_between, extra_spaces_allocate)
            cur_words = word_list[i - cur_num_words: i + 1]
            extra_spaces_left = extra_spaces_allocate
            cur_line = ''
            for w in cur_words:
                cur_line += w
                cur_line += ' ' * floor_spaces_between
                if extra_spaces_left:
                    cur_line += ' '
                    extra_spaces_left -= 1

            res.append(cur_line)

            cur_words_length = 0
            cur_num_words = 0

    return res


def full_justify(words: List[str], maxWidth: int) -> List[str]:
    if not words:
        return words

    if maxWidth < 1:
        return ''

    # inc_chars = # of chars in included words
    # inc_num_words = # of included words
    # if inc_chars + inc_num_words - 1 <= maxWidth
    # include new word by incrementing inc_chars by chars in new words
    # and inc_num_words by 1
    # else
    # add existing words string as an entry the list
    # -> add at least num_spaces = (maxWidth - inc_chars) // (inc_num_words - 1)
    # -> greedily add leftover_spaces = (maxWidth - inc_chars) % (inc_num_words - 1)
    # inc_chars = # of chars in new word
    # inc_num_words = 1

    inc_chars = len(words[0])
    inc_num_words = 1
    result = []
    for i in range(1, len(words)):
        word = words[i]
        temp_inc_chars = inc_chars + len(word)
        temp_inc_num_words = inc_num_words + 1
        print(word, inc_chars, inc_num_words, i)
        if temp_inc_chars + temp_inc_num_words - 1 <= maxWidth:
            inc_chars = temp_inc_chars
            inc_num_words = temp_inc_num_words
        else:
            if inc_num_words == 1:
                num_end_spaces = maxWidth - inc_chars
                cur_line_str = words[i - 1] + ' ' * num_end_spaces
            else:
                cur_words = words[i - inc_num_words: i]
                min_num_spaces = (maxWidth - inc_chars) // (inc_num_words - 1)
                remaining_spaces = (maxWidth - inc_chars) % (inc_num_words - 1)
                cur_line = []
                for j in range(len(cur_words) - 1):
                    w = cur_words[j]
                    cur_line.append(w)
                    cur_line.append(' ' * min_num_spaces)
                    if remaining_spaces:
                        cur_line.append(' ')
                        remaining_spaces -= 1

                cur_line.append(cur_words[-1])
                cur_line_str = ''.join(cur_line)

            print(cur_line_str)
            result.append(cur_line_str)
            inc_chars = len(word)
            inc_num_words = 1

    print(inc_num_words, inc_chars)
    last_line = ' '.join(words[-inc_num_words:])
    num_end_spaces = maxWidth - len(last_line)
    cur_line_str = last_line + ' ' * num_end_spaces
    result.append(cur_line_str)

    return result


width = 12
text = "Hi, how are you doing today?"
res1 = justify_text(text, width)
print(res1)

