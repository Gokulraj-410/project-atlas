# ATLAS - Phase 1 Summary

## Project Overview

**ATLAS** is a modular static code analysis platform designed to analyze source code repositories. The long-term goal is to perform semantic analysis, dependency analysis, relationship extraction, and provide a web-based visualization platform.

The project is intentionally designed like a compiler pipeline so that future phases can be added without changing the existing architecture.

---

# Long-Term Roadmap

## Phase 1

- Repository discovery
- File filtering
- Parsing using Tree-sitter
- AST traversal
- Symbol extraction
- Syntax error detection
- Project Model
- JSON Export

## Phase 2

- Database persistence
- Repository indexing
- Symbol tables

## Phase 3

- Semantic analysis
- Type resolution
- Method resolution
- Dependency graph
- Cross-file relationship resolution

## Phase 4

- REST API
- Web Interface
- Repository Visualization

---

# Current Project Architecture

```
Repository
      │
      ▼
Source Provider
      │
      ▼
Finder
      │
      ▼
Filter
      │
      ▼
Parser
      │
      ▼
SyntaxTree
      │
      ▼
Visitor
      │
      ▼
Collectors
      │
      ▼
ProjectModel
      │
 ┌────┴───────────┐
 ▼                ▼
JSON Export    Database (Phase 2)
```

---

# Current Folder Structure

```
atlas/

├── cli/
│   └── main.py

├── orchestrator/
│   └── orchestrator.py

├── discovery/
│   ├── finder.py
│   └── filter.py

├── parsers/
│   ├── base_parser.py
│   └─ parser.py
├── visitors/


├── collectors/
│   ├── class_collector.py
│   ├── method_collector.py
│   ├── constructor_collector.py
│   ├── field_collector.py
│   ├── parameter_collector.py
│   ├── variable_collector.py
│   ├── package_collector.py
│   ├── import_collector.py
│   └── syntax_error_collector.py

├── models/
│   ├── project.py
│   ├── source_file.py
│   ├── source_location.py
│   ├── class_model.py
│   ├── field_model.py
│   ├── constructor_model.py
│   ├── method_model.py
│   ├── parameter_model.py
│   ├── variable_model.py
│   ├── modifier.py
│   └── syntax_error.py

├── exporters/
│   └── json_exporter.py

├── db/
│   (Phase 2)

├── semantic/
│   (Phase 3)

└── utils/
```

---

# Technologies Used

- Python
- Tree-sitter
- tree-sitter-java
- MySQL (Phase 2)
- JSON
- Visitor Pattern
- Abstract Base Classes
- Object Oriented Design

---

# Parser Design

Tree-sitter is used only for syntax parsing.

Tree-sitter provides:

- Concrete Syntax Tree
- Error recovery
- Node locations

Tree-sitter DOES NOT provide:

- Semantic Analysis
- Type Resolution
- Symbol Resolution
- Dependency Graphs

Those will be implemented manually in later phases.

---

# Current Extraction

For every Java file ATLAS currently extracts:

## File

- Path
- Package
- Imports

## Class

- Name
- Visibility
- Static
- Final
- Source Location

## Field

- Name
- Type
- Modifiers
- Source Location

## Constructor

- Name
- Parameters
- Modifiers
- Source Location

## Method

- Name
- Return Type
- Parameters
- Local Variables
- Modifiers
- Source Location

## Parameter

- Name
- Type
- Source Location

## Local Variable

- Name
- Type
- Source Location

## Syntax Errors

Tree-sitter ERROR nodes

with

- line
- column
- text

---

# Current JSON Output

The exported JSON contains

```
Project
    Files
        Package
        Imports
        Classes
            Fields
            Constructors
            Methods
                Parameters
                Local Variables
        Syntax Errors
```

---

# Important Design Decisions

## Parser is isolated

Parser only converts

```
File

↓

SyntaxTree
```

It knows nothing about JSON, databases or semantic analysis.

---

## Visitor extracts symbols

Visitor walks the syntax tree.

Collectors extract specific declarations.

---

## Collectors

Each collector has a single responsibility.

Example

ClassCollector

- extracts class metadata

MethodCollector

- extracts method metadata

FieldCollector

- extracts fields

etc.

---

## Project Model

The internal representation of the repository.

Everything else should consume ProjectModel.

Not JSON.

Future outputs:

```
ProjectModel

↓

JSON Export

ProjectModel

↓

Database

ProjectModel

↓

REST API

ProjectModel

↓

Web UI
```

---

# Things intentionally NOT implemented yet

These belong to semantic analysis.

- Method calls
- Object creation
- Field access
- Type resolution
- Inheritance resolution
- Interface implementation
- Dependency graph
- Call graph
- Data Flow
- Control Flow

---

# Next Phase (Phase 2)

## Database

Design MySQL schema

Tables

- projects
- files
- classes
- fields
- methods
- constructors
- parameters
- variables
- syntax_errors

---

## Persistence Layer

ProjectModel

↓

Database Writer

↓

MySQL

---

## Repository Index

Store every declaration in MySQL.

Enable searching by

- Class
- Method
- Field
- File

---

# Future Semantic Analysis

Once repository indexing exists:

Extract

- Method invocations
- Variable references
- Field accesses
- Object creation
- extends
- implements
- annotations
- generic types

Then resolve them into relationships.

Example

```
emp.display()

↓

Variable

↓

Employee

↓

display()
```

---

# Future Input Sources

Current

```
Local Folder
```

Future

```
GitHub Repository

↓

Clone

↓

Temporary Directory

↓

Current Pipeline
```

Also

- ZIP Upload

Later

- Private GitHub Repositories
- GitHub OAuth

The parser should never know where the source came from.

Everything should eventually become

```
Source Provider

↓

Working Directory

↓

Finder

↓

Filter

↓

Parser
```

---

# Resume Summary

ATLAS is a modular static code analysis platform inspired by compiler architecture.

Current capabilities include

- Recursive repository traversal
- Java parsing using Tree-sitter
- AST traversal
- Symbol extraction
- Syntax error detection
- Project Model generation
- JSON export

The architecture is designed for future semantic analysis, dependency resolution, database indexing and web-based visualization.

---

# Immediate Next Tasks

1. Finish refactoring collectors to populate ProjectModel.
2. Implement JSON exporter using ProjectModel.
3. Design MySQL schema.
4. Implement Database Writer.
5. Persist ProjectModel into MySQL.
6. Build repository indexing layer.
7. Begin semantic analysis.

---

Project Status

Phase 1: ~95% Complete

Remaining:

- Complete ProjectModel integration
- Refactor JSON exporter to use models

After that, begin Phase 2 (Database & Repository Indexing).
