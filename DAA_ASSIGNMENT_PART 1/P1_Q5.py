def is_palindrome(s):
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same,
    # then check if the substring without the first and last characters is a palindrome
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the function
palindrome1 = "racecar"
palindrome2 = "gohangasalamiimalasagnahog"
non_palindrome = "hello"

print("Is '{}' a palindrome? {}".format(palindrome1, is_palindrome(palindrome1)))
print("Is '{}' a palindrome? {}".format(palindrome2, is_palindrome(palindrome2)))
print("Is '{}' a palindrome? {}".format(non_palindrome, is_palindrome(non_palindrome)))
