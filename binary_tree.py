class Node:
    def __init__ (self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__ (self) -> None:
        self.root = None
    
    def insert(self,data) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left,data)
        
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right,data)
        
    def search(self,data):
        return self._search_recursive(self.root,data)

    def _search_recursive(self, node, data):
        if node is None:
            return False
        elif node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left,data)
        elif data > node.data:
            return self._search_recursive(node.right,data)
    
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left,result)
            self._preorder_recursive(node.right,result)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left,result)
            result.append(node.data)
            self._inorder_recursive(node.right,result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left,result)
            self._postorder_recursive(node.right,result)
            result.append(node.data)

def main():
    tree = BinaryTree()
    tree.insert(3)
    tree.insert(8)
    tree.insert(9)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(7)
    tree.insert(3)
    tree.insert(15)
    tree.insert(81)
    tree.insert(0)

    print(tree.search(4))
    print(tree.search(7))

    print("Preorder traversal:  ",tree.preorder_traversal())
    print("Inorder traversal:   ",tree.inorder_traversal())
    print("Postorder traversal: ",tree.postorder_traversal())

if __name__ == '__main__':
    main()

