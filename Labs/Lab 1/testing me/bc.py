from stackLib import stack


def bc(formula):
    brackets_open = ['(', '[', '{']
    brackets_close = [')', ']', '}']
    bracket_list = stack()
    for i in range(0, len(formula), 1):
        if formula[i] in brackets_open:
            bracket_list.push(formula[i])
        elif formula[i] in brackets_close:
            popped = bracket_list.pop()
            compare = brackets_open[brackets_close.index(formula[i])]
            if compare != popped:
                return [False, i]
    return [True, 0]