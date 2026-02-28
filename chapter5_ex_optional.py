def delete_node(self, data):
    # Step 1: find the node
    node = self._find(data)

    if node is None:
        return  # value not found

    # Step 2: if node has TWO children
    if node._left_child is not None and node._right_child is not None:
        # find inorder successor (smallest in right subtree)
        successor = node._right_child
        while successor._left_child is not None:
            successor = successor._left_child

        # copy successor data into node
        node.data = successor.data

        # now delete successor instead
        node = successor

    # Step 3: node has at most ONE child
    if node._left_child is not None:
        child = node._left_child
    else:
        child = node._right_child

    parent = node._parent

    # Step 4: if node is root
    if parent is None:
        self._root_node = child
        if child is not None:
            child._parent = None
        return

    # Step 5: reconnect parent to child
    if parent._left_child == node:
        parent._left_child = child
    else:
        parent._right_child = child

    if child is not None:
        child._parent = parent