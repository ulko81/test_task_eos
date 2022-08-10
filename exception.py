class ElementNotClickAble(Exception):
    def __init__(self, item, step):
        super(ElementNotClickAble, self).__init__()
        self.item = item
        self.step = step

    def __str__(self):
        return '{0}. Not clickable el by {1} path {2} '.format(self.step, *self.item)


class ElementNotFoundException(Exception):
    def __init__(self, item, step):
        super(ElementNotFoundException, self).__init__()
        self.item = item
        self.step = step

    def __str__(self):
        return '{0}. Not found el by {1} path {2} '.format(self.step, *self.item)

