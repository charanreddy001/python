class treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|___" if self.parent else ""
        print(prefix + self.data)
       # print(self.data)  if you leave this and continue without down command it will just print "Electronics" as it main information it contains children
        if self.children:
            for child in self.children:
               child.print_tree()

def build_product_tree():
    root = treenode("Electronics")

    laptop = treenode("laptop")
    laptop.add_child(treenode("mac"))
    laptop.add_child(treenode("windows"))
    laptop.add_child(treenode("linux"))

    phone = treenode("phone")
    phone.add_child(treenode("realme"))
    phone.add_child(treenode("google pixel"))
    phone.add_child(treenode("samsung"))

    earphones = treenode('TWS')
    earphones.add_child(treenode("wings"))
    earphones.add_child(treenode("oneplus"))


    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(earphones)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
