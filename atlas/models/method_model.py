from dataclasses import dataclass, field
from .parameter_model import ParameterModel
from .variable_model import VariableModel
from .modifier import Modifier
from .source_location import SourceLocation

@dataclass
class MethodModel:
    name: str
    return_type: str
    location: SourceLocation
    modifier: Modifier
    parameters: list[ParameterModel] = field(default_factory=list)
    local_variables: list[VariableModel] = field(default_factory=list)