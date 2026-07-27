from dataclasses import dataclass

@dataclass
class Position:
    line: int
    column: int

@dataclass
class SourceLocation:
    start: Position
    end: Position