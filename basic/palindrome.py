def is_palindrome(teststr):
    i = 0
    j = len(teststr) - 1

    while i < j:
        if not teststr[i].isalnum():
            i += 1
            continue

        if not teststr[j].isalnum():
            j -= 1
            continue

        if teststr[i].lower() != teststr[j].lower():
            return False

        i += 1
        j -= 1

    return True


print(is_palindrome("A man, a plan, a canal, Panama!")) 
print(is_palindrome("This is not a palindrome"))