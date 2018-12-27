def f(input):
    if not isinstance(input,int):
        return -1
    else:
        if (input%100)>10:
            return input%100
        else:
            return input%100+11