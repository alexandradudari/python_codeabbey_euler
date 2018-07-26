from stack import Stack

def clean_string(string :str) -> str:
    brackets = ['(', ')', '[', ']', '{', '}', '<', '>']
    new_string = ''
    for char in string:
        if char in brackets:
            new_string += char
    return new_string

def is_reversed(a: int, b: int) -> bool:
    brackets = {'(': ')',
                '[': ']',
                '{': '}',
                '<': '>'}
    k = [key for key, value in brackets.items() if value == a][0]
    if b == k:
        return True
    else:
        return False
 

def matching_brackets(brackets : str) -> int:
    """Check, whether brackets are in correct sequence.
    I.e. any opening bracket should have closing bracket
    of the same type somewhere further by the string,
    and bracket pairs should not overlap, though they could be nested.
    """
    s = Stack()
    balanced = True
    index = 0
    length = len(brackets)

    while index < length and balanced:
        bracket = brackets[index]

        if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
            s.push(bracket)
        else:
            if s.isEmpty():
                balanced = False
            elif is_reversed(bracket, s.peek()):
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return 1
    else:
        return 0


n = input()
for i in range(int(n)):
    a = input()
    string = clean_string(a)
    print(matching_brackets(string), end=' ')
