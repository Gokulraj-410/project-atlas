from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    TIMESTAMP,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from atlas.database.connection import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    root_path = Column(Text, nullable=False)
    language = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    files = relationship(
        "File",
        back_populates="project",
        cascade="all, delete-orphan"
    )

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)

    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False
    )

    path = Column(Text, nullable=False)
    file_name = Column(String(255), nullable=False)
    language = Column(String(50))

    project = relationship("Project", back_populates="files")

    imports = relationship(
        "Import",
        back_populates="file",
        cascade="all, delete-orphan"
    )

    classes = relationship(
        "Class",
        back_populates="file",
        cascade="all, delete-orphan"
    )

    syntax_errors = relationship(
        "SyntaxError",
        back_populates="file",
        cascade="all, delete-orphan"
    )

class Import(Base):
    __tablename__ = "imports"

    id = Column(Integer, primary_key=True)

    file_id = Column(
        Integer,
        ForeignKey("files.id", ondelete="CASCADE"),
        nullable=False
    )

    import_name = Column(Text, nullable=False)

    file = relationship("File", back_populates="imports")

class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)

    file_id = Column(
        Integer,
        ForeignKey("files.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String(255), nullable=False)

    visibility = Column(String(20))
    is_static = Column(Boolean, default=False)
    is_final = Column(Boolean, default=False)

    start_line = Column(Integer)
    start_column = Column(Integer)
    end_line = Column(Integer)
    end_column = Column(Integer)

    __table_args__ = (
        CheckConstraint(
            "visibility IN ('public','private','protected','package')",
            name="chk_class_visibility"
        ),
    )

    file = relationship("File", back_populates="classes")

    fields = relationship(
        "Field",
        back_populates="class_",
        cascade="all, delete-orphan"
    )

    methods = relationship(
        "Method",
        back_populates="class_",
        cascade="all, delete-orphan"
    )

    constructors = relationship(
        "Constructor",
        back_populates="class_",
        cascade="all, delete-orphan"
    )

class Field(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True)

    class_id = Column(
        Integer,
        ForeignKey("classes.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String(255), nullable=False)
    type = Column(String(255))

    visibility = Column(String(20))
    is_static = Column(Boolean, default=False)
    is_final = Column(Boolean, default=False)

    start_line = Column(Integer)
    start_column = Column(Integer)
    end_line = Column(Integer)
    end_column = Column(Integer)

    class_ = relationship("Class", back_populates="fields")

class Constructor(Base):
    __tablename__ = "constructors"

    id = Column(Integer, primary_key=True)

    class_id = Column(
        Integer,
        ForeignKey("classes.id", ondelete="CASCADE"),
        nullable=False
    )

    visibility = Column(String(20))

    start_line = Column(Integer)
    start_column = Column(Integer)
    end_line = Column(Integer)
    end_column = Column(Integer)

    class_ = relationship("Class", back_populates="constructors")

class Method(Base):
    __tablename__ = "methods"

    id = Column(Integer, primary_key=True)

    class_id = Column(
        Integer,
        ForeignKey("classes.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String(255), nullable=False)
    signature = Column(String(500))
    return_type = Column(String(255))

    visibility = Column(String(20))
    is_static = Column(Boolean, default=False)
    is_final = Column(Boolean, default=False)

    start_line = Column(Integer)
    start_column = Column(Integer)
    end_line = Column(Integer)
    end_column = Column(Integer)

    class_ = relationship("Class", back_populates="methods")

    local_variables = relationship(
        "LocalVariable",
        back_populates="method",
        cascade="all, delete-orphan"
    )

class Parameter(Base):
    __tablename__ = "parameters"

    id = Column(Integer, primary_key=True)

    owner_type = Column(String(20), nullable=False)
    owner_id = Column(Integer, nullable=False)

    position = Column(Integer, nullable=False)

    name = Column(String(255), nullable=False)
    type = Column(String(255))

    start_line = Column(Integer)
    start_column = Column(Integer)
    end_line = Column(Integer)
    end_column = Column(Integer)

class LocalVariable(Base):
    __tablename__ = "local_variables"

    id = Column(Integer, primary_key=True)

    method_id = Column(
        Integer,
        ForeignKey("methods.id", ondelete="CASCADE"),
        nullable=False
    )

    name = Column(String(255), nullable=False)
    type = Column(String(255))

    start_line = Column(Integer)
    start_column = Column(Integer)
    end_line = Column(Integer)
    end_column = Column(Integer)

    method = relationship("Method", back_populates="local_variables")

class SyntaxError(Base):
    __tablename__ = "syntax_errors"

    id = Column(Integer, primary_key=True)

    file_id = Column(
        Integer,
        ForeignKey("files.id", ondelete="CASCADE"),
        nullable=False
    )

    error_type = Column(String(100))
    text = Column(Text)

    start_line = Column(Integer)
    start_column = Column(Integer)
    end_line = Column(Integer)
    end_column = Column(Integer)

    file = relationship("File", back_populates="syntax_errors")

class Relationship(Base):
    __tablename__ = "relationships"

    id = Column(Integer, primary_key=True)

    source_type = Column(String(50), nullable=False)
    source_id = Column(Integer, nullable=False)

    relationship = Column(String(50), nullable=False)

    target_type = Column(String(50), nullable=False)
    target_id = Column(Integer, nullable=False)
