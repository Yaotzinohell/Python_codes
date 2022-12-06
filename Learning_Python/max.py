def fuc(li):
    max = li[0]
    for i in li:
        if max < i:
            max = i
    return max