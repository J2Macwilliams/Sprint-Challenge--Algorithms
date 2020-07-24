'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Plan
    # only seeking the lower case
    # TBC - The Base Case
    if len(word) < 2:
        return 0
    else:
        # checking for the first 2 string items which contain 'th'
        if word[0:2] == "th":
            # recursive case after the first to string items
            return 1 + count_th(word[2:])
        else:
            # recursive case seeking first string item
            return count_th(word[1:])

