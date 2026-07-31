from atlas.database.connection import SessionLocal
from atlas.database.db_models import *
import os

class AtlasImporter:
    def import_project(self, project):
        session = SessionLocal()
        try:
            db_project = self._insert_project(session, project)

            for file in project.files:
                self._insert_file(session, file, db_project.id)

            session.commit()

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()         
         

    def _insert_project(self, session, project):
        db_project = Project(
        name="atlas_test",
        root_path="test",
        language = "java"
        )

        session.add(db_project)
        session.flush()  

        return db_project
        
 
    def _insert_file(self, session, file, project_id):
 
        db_file = File(
            project_id=project_id,
            path=file.path,
            file_name =os.path.basename(file.path),
            language = "java"
        )
    
        session.add(db_file)
        session.flush()
    
        for imp in file.imports:
            session.add(
                Import(
                    file_id=db_file.id,
                    import_name=imp
                )
            )
    
        for cls in file.classes:
            self._insert_class(session, cls, db_file.id)
    
        for err in file.errors:
            session.add(
                SyntaxError(
                    file_id=db_file.id,
                    error_type=err.type,
                    text=err.text,
                    start_line=err.location.start.line,
                    start_column=err.location.start.column,
                    end_line=err.location.end.line,
                    end_column=err.location.end.column
                )
            )
 
         
  
    def _insert_class(self, session, cls, file_id):
 
        db_class = Class(
            file_id=file_id,
            name=cls.name,
            visibility=cls.modifier.visibility,
            is_static=cls.modifier.static,
            is_final=cls.modifier.final,
            start_line=cls.location.start.line,
            start_column=cls.location.start.column,
            end_line=cls.location.end.line,
            end_column=cls.location.end.column

        )
    
        session.add(db_class)
        session.flush()
    
        for field in cls.fields:
            self._insert_field(session, field, db_class.id)
    
        for constructor in cls.constructors:
            self._insert_constructor(session, constructor, db_class.id)
    
        for method in cls.methods:
            self._insert_method(session, method, db_class.id)
          
  
    def _insert_method(self, session, method, class_id):
 
        db_method = Method(
            class_id=class_id,
            name=method.name,
            return_type=method.return_type,
            visibility=method.modifier.visibility,
            is_static=method.modifier.static,
            is_final=method.modifier.final,
            start_line=method.location.start.line,
            start_column=method.location.start.column,
            end_line=method.location.end.line,
            end_column=method.location.end.column
            
        )
    
        session.add(db_method)
        session.flush()
    
        for parameter in method.parameters:
            self._insert_parameter(
                session,
                parameter,
                "METHOD",
                db_method.id
            )
    
        for variable in method.local_variables:
            self._insert_local_variable(
                session,
                variable,
                db_method.id
            )
          
 
    def _insert_constructor(self, session, constructor, class_id):

        db_constructor = Constructor(
            class_id=class_id,
            visibility=constructor.modifier.visibility,
            start_line=constructor.location.start.line,
            start_column=constructor.location.start.column,
            end_line=constructor.location.end.line,
            end_column=constructor.location.end.column
        )
    
        session.add(db_constructor)
        session.flush()
    
        for parameter in constructor.parameters:
            self._insert_parameter(
                session,
                parameter,
                "CONSTRUCTOR",
                db_constructor.id
            )
        

    def _insert_field(self, session, field, class_id):

        db_field = Field(
            class_id=class_id,
            name=field.name,
            type=field.type,
            visibility=field.modifier.visibility,
            is_static=field.modifier.static,
            is_final=field.modifier.final,
            start_line=field.location.start.line,
            start_column=field.location.start.column,
            end_line=field.location.end.line,
            end_column=field.location.end.column
        )
    
        session.add(db_field)
     
 
    def _insert_parameter(self, session, parameter, owner_type, owner_id):
   
        db_parameter = Parameter(
            owner_type=owner_type,
            owner_id=owner_id,
            name=parameter.name,
            type=parameter.type,
            start_line=parameter.location.start.line,
            start_column=parameter.location.start.column,
            end_line=parameter.location.end.line,
            end_column=parameter.location.end.column
            
        )
    
        session.add(db_parameter)
           
   
    def _insert_local_variable(self, session, variable, method_id):
   
        db_variable = LocalVariable(
            method_id=method_id,
            name=variable.name,
            type=variable.type,
            start_line=variable.location.start.line,
            start_column=variable.location.start.column,
            end_line=variable.location.end.line,
            end_column=variable.location.end.column
        )
    
        session.add(db_variable)
            