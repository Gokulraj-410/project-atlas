from abc import ABC, abstractmethod

class BaseParser(ABC):

    @abstractmethod
    def parse(self, file_path):
        """Parse a source file and return a SyntaxTree."""
        pass