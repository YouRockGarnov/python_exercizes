import itertools
import operator

def transpose(lst):
    return list(zip(*lst))

def uniq(lst):
    st = set()
    for item in lst:
        st.add(item)

    return list(st)

def product(vec1, vec2):
    return sum(itertools.starmap(operator.mul, zip(vec1, vec2)))

def dict_merge(*args):
    # chain = itertools.chain.from_iterable(args)
    # print(itertools.starmap(operator.mul, chain))
    #return itertools.chain.from_iterable(args)

    res = dict()
    for arg in args:
        # for key, val in list(zip(arg.keys(), arg.values())):
        res.update(arg)

    return res

# print(dict_merge({1:2}, {2: 2}, {1: 1}))
