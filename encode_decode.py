'''
659 · Encode and Decode Strings

Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Because the string may contain any of the 256 legal ASCII characters, your algorithm must be able to handle any character that may appear

Do not rely on any libraries, the purpose of this problem is to implement the "encode" and "decode" algorithms on your own

Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''


"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""


def encode(self, strs):
    # write your code here
    res = []
    for s in strs:
        res.append(f'{len(s)}#')
        res.append(s)

    res_str = ''.join(res)
    return res_str


"""
@param: str: A string
@return: decodes a single string to a list of strings
"""


def decode(self, s):
    # write your code here
    print(s)
    i = 0
    res = []
    while i < len(s):
        print(res)
        num_chars_str = ''
        while s[i] != '#':
            num_chars_str += s[i]
            i += 1

        num_chars = int(num_chars_str)
        i += 1
        last_char_at = i + num_chars
        cur_s = ''
        while i < last_char_at:
            cur_s += s[i]
            i += 1

        res.append(cur_s)

    return res