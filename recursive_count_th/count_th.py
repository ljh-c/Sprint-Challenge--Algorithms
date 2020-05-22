'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    elif "th" in word:
        start_index = word.find("th")

        subword_1 = word[:start_index]
        subword_2 = word[(start_index + 2):]

        return 1 + count_th(subword_1) + count_th(subword_2)
    
    return 0