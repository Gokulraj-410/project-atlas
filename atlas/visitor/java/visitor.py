

class JavaVisitor:
    def __init__(self,syntax_tree):
        self.tree = syntax_tree.tree
        self.source = syntax_tree.source

    def visit(self):
        root_node = self.tree.root_node
        self._visit_node(root_node)    

    def _visit_node(self, node):
        print(node.type)

        for child in node.named_children:
            self._visit_node(child)