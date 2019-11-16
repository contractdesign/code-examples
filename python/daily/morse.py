#!/usr/bin/env python3

# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

# list of Morse codes a - z, separated by spaces
l_codes='.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()

def smorse(s):
    result = ''
    for c in s:
        result += l_codes[ord(c) - ord('a')]
    return result


assert smorse("sos") == "...---..."
assert smorse("daily") == "-...-...-..-.--"
assert smorse("programmer") == ".--..-.-----..-..-----..-."
assert smorse("bits") == "-.....-..."
assert smorse("three") == "-.....-..."




