from dataclasses import dataclass
from .source_location import SourceLocation

@dataclass
class ParameterModel:
    name: str
    type: str
    location: SourceLocation