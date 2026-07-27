from dataclasses import dataclass
from .source_location import SourceLocation

@dataclass
class SyntaxErrorModel:
    type: str
    text: str
    location: SourceLocation