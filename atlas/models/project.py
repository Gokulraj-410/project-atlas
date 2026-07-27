from dataclasses import dataclass, field
from .source_file import SourceFile

@dataclass
class Project:
    files: list[SourceFile] = field(default_factory=list)