from atlas.parsers.base_parser import BaseParser
from tree_sitter import Parser,Language
import tree_sitter_java
from pathlib import Path

class JavaParser(BaseParser):
    def __init__(self):
        self.parser = Parser()
        self.parser.language = Language(tree_sitter_java.language())

    def parse(self, path):
        source = Path(path).read_bytes()
        tree = self.parser.parse(source)
        return tree,source,path
        
           

    