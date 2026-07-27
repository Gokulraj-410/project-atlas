from dataclasses import dataclass, field
from .field_model import FieldModel
from .constructor_model import ConstructorModel
from .method_model import MethodModel
from .modifier import Modifier
from .source_location import SourceLocation

@dataclass
class ClassModel:
    name: str
    location: SourceLocation
    modifier: Modifier
    fields: list[FieldModel] = field(default_factory=list)
    constructors: list[ConstructorModel] = field(default_factory=list)
    methods: list[MethodModel] = field(default_factory=list)