class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        current_node = self._root_node
        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            self._root_node = new_node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        """
        Detach a node from the tree.
        Node can have at most one child.
        """

        if node is None:
            return

        # If node has two children, raise error
        if node._left_child is not None and node._right_child is not None:
            raise ValueError("Cannot detach node with two children")

        parent = node._parent

        # Get child (if any)
        if node._left_child is not None:
            child = node._left_child
        else:
            child = node._right_child

        # If node is root
        if parent is None:
            self._root_node = child
            if child is not None:
                child._parent = None
            return

        # If node is left child
        if parent._left_child == node:
            parent._left_child = child
        else:
            parent._right_child = child

        # Update child's parent
        if child is not None:
            child._parent = parent

        # Fully detach node
        node._parent = None
        node._left_child = None
        node._right_child = None