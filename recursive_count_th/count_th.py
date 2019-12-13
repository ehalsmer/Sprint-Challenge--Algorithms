'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    i = 0
    if len(word) < 2:
        return 0
    def inner(word):
        # If we've reached the end, return count
        nonlocal i
        nonlocal count
        if i == len(word)-1:
            return count
        else:
            # Check for 'th' at current index
            if word[i:i+2] == 'th':
                # print('th')
                count += 1
                # print(count)
                i += 1
                inner(word)
            else:
                i += 1
                inner(word)
    inner(word)
    return count

print(count_th("abcthefthghith"))