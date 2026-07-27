from dataclasses import dataclass
from .source_location import SourceLocation

@dataclass
class VariableModel:
    name: str
    type: str
    location: SourceLocation