

class JavaVisitor:
    def __init__(self,syntax_tree):
        self.tree = syntax_tree.tree
        self.source = syntax_tree.source

    def _visit_node(self, node):
        print(node.type)

        for child in node.children:
            self._visit_node(child)