import re

# Define your regular expression here
my_regex_pattern = r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
my_regex = re.compile(my_regex_pattern)

def fullmatch(string):
    return my_regex.fullmatch(string)

def findall(string):
    return my_regex.findall(string)
