from atlas.database.connection import SessionLocal
from atlas.database.db_models import *

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
        name="demo",
        root_path=project.path,
        language="java"
        )

        session.add(db_project)
        session.flush()  

        return db_project
       

    def _insert_file(self, session, file, project_id):
        

    def _insert_class(self, session, cls, file_id):
        

    def _insert_method(self, session, method, class_id):
        

    def _insert_constructor(self, session, constructor, class_id):
        

    def _insert_field(self, session, field, class_id):
    

    def _insert_parameter(self, session, parameter, owner_type, owner_id):
        

    def _insert_local_variable(self, session, variable, method_id):
        