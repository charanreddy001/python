class binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # this is done to remove duplicate data
        # binary tree doesn't have duplicate values

        if data < self.data:
            # helps to add left side data bcz it is less
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binary_tree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binary_tree(data)

    def in_order_traversal(self):
        elements = []

        # for left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # for right tree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    @classmethod
    def build_tree(cls, elements):
        root = cls(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])
        return root

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right.delete(min_val)
        return self



if __name__ == "__main__":
    numbers = [50, 30, 70, 20, 40, 60, 80]
    num_tree = binary_tree.build_tree(numbers)  # Use the class method
    print(num_tree.in_order_traversal())
    print(num_tree.search(30))  # Should print True or False
    print(num_tree.delete(20))
    print("after deleting 20 -",num_tree.in_order_traversal())