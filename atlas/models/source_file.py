from dataclasses import dataclass, field
from .class_model import ClassModel
from .syntax_error import SyntaxErrorModel

@dataclass
class SourceFile:
    path: str
    package: str | None = None
    imports: list[str] = field(default_factory=list)
    classes: list[ClassModel] = field(default_factory=list)
    errors: list[SyntaxErrorModel] = field(default_factory=list)