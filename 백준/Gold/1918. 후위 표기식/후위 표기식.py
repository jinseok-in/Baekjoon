import re

input_text = input()

input_text = re.findall('[A-Z]+|[()+*/-]', input_text)

mark_stack = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
result = ''

marks = []

for element in input_text :
    if element.isalpha() :
        result += element
    elif element == '(' :
        marks.append(element)
    elif element == ')' :
        while marks[-1] != '(' :
            result += marks.pop()
        marks.pop()
    else :
        while marks and marks[-1] != '(' and mark_stack[marks[-1]] >= mark_stack[element] :
            result += marks.pop()
        marks.append(element)

while marks :
    result += marks.pop()

print(result)