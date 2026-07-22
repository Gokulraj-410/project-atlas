from dataclasses import dataclass

@dataclass
class SyntaxTree:
    tree: object
    source: str
    file_path: str
    language: str