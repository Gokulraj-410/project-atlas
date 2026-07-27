from dataclasses import dataclass
from .modifier import Modifier
from .source_location import SourceLocation

@dataclass
class FieldModel:
    name: str
    type: str
    location: SourceLocation
    modifier: Modifier