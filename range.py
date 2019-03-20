

class Range:
    def __init__(self, *args):
        self.count_of_args = len(args)
        self.left = 0
        self.step = 1

        if len(args) == 1:
            self.right = args[0]
        elif len(args) == 2:
            self.left = args[0]
            self.right = args[1]
        else:
            self.left = args[0]
            self.right = args[1]
            self.step = args[2]

        self.range = range(self.left, self.right, self.step)
        # self.elems = [x for x in range(self.left, self.right, self.step)]

    def __repr__(self):
        repres = 'Range({})'

        if self.count_of_args == 1:
            return repres.format(self.right)
        elif self.count_of_args == 2:
            return repres.format('{0}, {1}'.format(self.left, self.right))
        else:
            return repres.format('{0}, {1}, {2}'.format(self.left, self.right, self.step))

        # return 'Range({0}, {1}, {2})' + str(self.left) + str(self.right) + str(self.step)

    def __call__(self, *args, **kwargs):
        for item in self.range:
            yield item

    def __getitem__(self, id):
        return self.range[id]

    # def __delitem__(self, index):
    #     self.elems.pop(index)
    #
    # def __setitem__(self, index, value):
    #     self.elems[index] = value

    def __contains__(self, item):
        return item in self.range

    def __len__(self):
        return len(self.range)
