from atlas.parsers.base_parser import BaseParser
from atlas.models.syntax_tree import SyntaxTree
from tree_sitter import Parser,Language
import tree_sitter_java

class JavaParser(BaseParser):
    def __init__(self):
        self.parser = Parser()
        self.parser.language = Language(tree_sitter_java.language())

    def parse(self, path):
        with open(path, "r", encoding="utf-8") as f:
            source = f.read()

        tree = self.parser.parse(source.encode("utf-8"))
        return SyntaxTree(
        tree=tree,
        source=source,
        file_path=path,
        language="java"
        )
           

    