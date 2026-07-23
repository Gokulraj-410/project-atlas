from pathlib import  Path
from atlas.collectors.class_collector import class_collector
from atlas.collectors.method_collector import method_collector
class JavaVisitor:
    def __init__(self,syntax_tree):
        self.tree = syntax_tree.tree
        self.source =  Path(syntax_tree.file_path).read_bytes()

    def visit(self):
        root_node = self.tree.root_node
        self._visit_node(root_node)    

    def _visit_node(self, node):
        print(node.type)

        if node.type == "class_declaration":
            class_collector.cls_collector(self.source,node)
        if node.type == "method_declaration":
            print("here")
            method_collector.mtd_collector(self.source,node)     

        for child in node.named_children:
            self._visit_node(child)