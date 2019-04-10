import collections

def flatit_list(inp):
    result = list()

    for item in inp:
        if isinstance(item, collections.Iterable):
            if not (isinstance(item, str) and len(item) == 1):
                result += flatit(item)
            else:
                result.append(item)
        else:
            result.append(item)

    return result

def flatit(inp):
    ans = flatit_list(inp)
    for item in ans:
        yield item

