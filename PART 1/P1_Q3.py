def string_to_integer(s):
    # Base case: if the string is empty, return 0
    if len(s) == 0:
        return 0
    # Recursive case: convert the substring without the first character to an integer
    # and multiply it by 10, then add the integer value of the first character.
    return string_to_integer(s[:-1]) * 10 + int(s[-1])

# Test the function
input_string = "13531"
result = string_to_integer(input_string)
print("The integer representation of '{}' is: {}".format(input_string, result))
