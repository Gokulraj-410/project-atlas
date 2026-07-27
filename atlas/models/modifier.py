from dataclasses import dataclass

@dataclass
class Modifier:
    visibility: str = "default"
    static: bool = False
    final: bool = False