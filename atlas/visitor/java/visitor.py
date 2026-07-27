from atlas.collectors.class_collector import class_collector
from atlas.collectors.import_collector import import_collector
from atlas.models.source_file import SourceFile
from atlas.models.syntax_error import SyntaxErrorModel
from atlas.models.source_location import SourceLocation, Position


class JavaVisitor:

    def __init__(self, tree, source, path):
        self.tree = tree
        self.source = source

        self.result = SourceFile(
            path=str(path)
        )

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

            location = SourceLocation(
                start=Position(
                    line=node.start_point[0] + 1,
                    column=node.start_point[1]
                ),
                end=Position(
                    line=node.end_point[0] + 1,
                    column=node.end_point[1]
                )
            )

            error = SyntaxErrorModel(
                type="SyntaxError",
                text=error_text,
                location=location
            )

            self.result.errors.append(error)

        if node.is_missing:
            print("missing")

            location = SourceLocation(
                start=Position(
                    line=node.start_point[0] + 1,
                    column=node.start_point[1]
                ),
                end=Position(
                    line=node.end_point[0] + 1,
                    column=node.end_point[1]
                )
            )

            error = SyntaxErrorModel(
                type="MissingNode",
                text=node.type,
                location=location
            )

            self.result.errors.append(error)

        if node.type == "import_declaration":
            import_collector.visit_import_declaration(
                self,
                self.source,
                node
            )

        if node.type == "class_declaration":
            class_collector.visit_class_declaration(
                self,
                self.source,
                node
            )

        for child in node.named_children:
            self._visit_node(child)