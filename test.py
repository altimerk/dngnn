r"""
    Given a binary tree, not a search tree.
    All node values are unique.

                10
             /      \
            8          3
          /    \         \
         13     15        11
        /      /   \
       14     6      1
                    /  \
                  7      5

    Given value X and value R, find all node values
    on distance R steps (any direction) from the value X,
    if X is presented in the tree.

"""

from typing import Any, Optional, List


class BinaryTreeNode:
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None

    def find_node(self, elem, radius):
        if elem == self.value:
            return [self.value]
        if self.left is None and self.right is None:
            return []
        result_left = []
        result_right = []
        result = None
        if self.left and radius > 0:
            result_left = self.left.find_node(elem, radius - 1)
        if result is not None:
            return result
        if self.right and radius > 0:
            result_right = self.right.find_node(elem, radius - 1)
        return result_left + result_right

    def find_node_global(self, elem):
        if elem == self.value:
            return self
        if self.left is None and self.right is None:
            return None
        result = None

        if self.left:
            result = self.left.find_node_global(elem)
        if result is not None:
            return result
        if self.right:
            result = self.right.find_node_global(elem)

        return result
    def find_nodes_by_radius(self, radius):
        if radius == 0:
            return [self.value]
        nodes_left = []
        nodes_right = []
        if self.left and radius>0:
            nodes_left = self.left.find_nodes_by_radius(radius-1)
        if self.right and radius>0:
            nodes_right = self.right.find_nodes_by_radius(radius-1)
        return nodes_left+nodes_right

class BinaryTree:


    def __init__(self):
        self.root: Optional[BinaryTreeNode] = None

    def find_radius(self, elem: Any, radius: int = 0) -> List[Any]:
        node = self.root.find_node_global(elem)
        node_list = []
        if node is not None:
            node_list = node.find_nodes_by_radius(radius)
        return node_list

    def find_node(self, elem):

        return self.root.find_node_global(elem)



if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = BinaryTreeNode(10)
    tree.root.left = BinaryTreeNode(8)
    tree.root.left.left = BinaryTreeNode(13)
    tree.root.left.left.left = BinaryTreeNode(14)
    tree.root.left.right = BinaryTreeNode(15)
    tree.root.left.right.left = BinaryTreeNode(6)
    tree.root.left.right.right = BinaryTreeNode(1)
    tree.root.left.right.right.left = BinaryTreeNode(7)
    tree.root.left.right.right.right = BinaryTreeNode(5)
    tree.root.right = BinaryTreeNode(3)
    tree.root.right.right = BinaryTreeNode(11)
    node = tree.find_node(10)
    if node:
        print(node.value)
    else:
        print("not found")
    print("v = 15, r = 0 -> " + str(tree.find_radius(15, 0)))  # [15]
    print("v = 15, r = 1 -> " + str(tree.find_radius(15, 1)))  # [6, 1, 8]
    print("v = 15, r = 2 -> " + str(tree.find_radius(15, 2)))  # [7, 5, 13, 10]