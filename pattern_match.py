import re

#
# re : pattern match handling module
#   - \b : border b/w string and string
#   - \w : first char of string
#   - |  : A|B means A or B
#
def first_char():
    text = "Hello 2025 new World trend for most top-trends"
    print (re.findall("Hello", text))
    print (re.findall(r"\b\w", text))
    print (re.findall("\b\w", text))
    print (re.findall("trend", text))

    # s? : s repeats 0 or more than 1 
    # so s ok without showing hence trend also matching as well as trends
    print (re.findall(r"\btrends?", text))
    print (re.findall("trends", text))
    print (re.findall("trends|trend", text))

first_char()
