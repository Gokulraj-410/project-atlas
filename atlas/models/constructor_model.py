from dataclasses import dataclass, field
from .parameter_model import ParameterModel
from .modifier import Modifier
from .source_location import SourceLocation

@dataclass
class ConstructorModel:
    name: str
    location: SourceLocation
    modifier: Modifier
    parameters: list[ParameterModel] = field(default_factory=list)