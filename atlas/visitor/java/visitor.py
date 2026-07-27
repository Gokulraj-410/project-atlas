from pathlib import Path
from atlas.collectors.class_collector import class_collector
from atlas.collectors.import_collector import import_collector

class JavaVisitor:
    def __init__(self, tree, source, path):
        self.tree = tree
        self.source = source
        self.result = {
            "path": str(path),
            "package": None,
            "imports": [],
            "classes": [],
            "errors": []
        }

    def visit(self, root_node):
        root_node = self.tree.root_node
        self._visit_node(root_node)
        return self.result

    def _visit_node(self, node):

        if node.type == "ERROR":
            print("error")
            error_text = self.source[
                node.start_byte:node.end_byte
            ].decode("utf-8", errors="ignore")

            self.result["errors"].append({
                "type": "SyntaxError",
                "text": error_text,
                "start": {
                    "line": node.start_point[0] + 1,
                    "column": node.start_point[1]
                },
                "end": {
                    "line": node.end_point[0] + 1,
                    "column": node.end_point[1]
                }
            })

        if node.is_missing:
            print("missing")
            self.result["errors"].append({
                "type": "MissingNode",
                "node": node.type,
                "line": node.start_point[0] + 1,
                "column": node.start_point[1]
            })
        if node.type == "import_declaration":
            import_collector.visit_import_declaration(self, self.source, node)

        if node.type == "class_declaration":
            class_collector.visit_class_declaration(self, self.source, node)

        for child in node.named_children:
            self._visit_node(child)