from pathlib import  Path
from atlas.collectors.class_collector import class_collector
from atlas.collectors.import_collector import import_collector
class JavaVisitor:
    def __init__(self,tree,source,path):
        self.tree = tree
        self.source =  source
        self.result = {
            "path": str(path),
            "package": None,
            "imports": [],
            "classes": []
        }
        self.current_class = None
        self.current_method = None

    def visit(self,root_node):
        root_node = self.tree.root_node
        self._visit_node(root_node) 
        return self.result   

    def _visit_node(self, node):
        
        if node.type == "import_declaration":
            import_collector.visit_import_declaration(self,self.source,node)
        
        if node.type == "class_declaration":
            class_collector.visit_class_declaration(self,self.source,node)
            

        for child in node.named_children:
            self._visit_node(child)
            