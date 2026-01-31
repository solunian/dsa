from lib.generics import Comparable
from ds.node import BinaryNode


# naive, not self-balancing bst set
# add, contains, remove: worst case O(n)
class BSTSet[T: Comparable]:
    def __init__(self):
        self.root: BinaryNode[T] | None = None

    def __str__(self):
        if self.root is not None:
            return str(list(self.root))
        else:
            return str([])

    def add(self, x: T):
        def rec_add(curr: BinaryNode[T], node: BinaryNode[T]):
            if node.val == curr.val:
                return  # already exists
            if node.val < curr.val:
                if curr.left is None:
                    curr.left = node
                else:
                    rec_add(curr.left, node)
            else:
                if curr.right is None:
                    curr.right = node
                else:
                    rec_add(curr.right, node)

        new_node = BinaryNode(x, None, None)
        if self.root is None:
            self.root = new_node
        else:
            rec_add(self.root, new_node)

    def __contains__(self, x: T) -> bool:
        def find(root: BinaryNode[T] | None, val: T) -> BinaryNode[T] | None:
            if root is None:
                return None

            if val == root.val:
                return root
            elif val < root.val:
                return find(root.left, val)
            else:
                return find(root.right, val)

        node = find(self.root, x)
        return node is not None

    def remove(self, x: T):
        def rec_remove(root: BinaryNode[T] | None, val: T):
            if root is None:
                return None

            if val == root.val:
                # case: 0 or 1 children
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left

                # case: 2 children, in-order successor
                succ = root.right
                while succ.left is not None:
                    succ = succ.left

                root.val = succ.val  # set successor to value of the root
                root.right = rec_remove(root.right, succ.val)  # delete successor node

            elif val < root.val:
                root.left = rec_remove(root.left, val)
            else:
                root.right = rec_remove(root.right, val)

            return root

        self.root = rec_remove(self.root, x)
