from atlas.collectors.method_collector import method_collector as mc
from atlas.collectors.constructor_collector import constructor_collector as cc
class class_collector:
    def visit_class_declaration(self,source,node):

        name_node = node.child_by_field_name("name")

        class_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")

        cls = {
        "name": class_name,
        "fields": [],
        "constructors": [],
        "methods": []
        }
        
        self.result["classes"].append(cls)
        method_collector = mc()
        constructor_collector = cc()
        body = node.child_by_field_name("body")
        if body:
            for child in body.named_children:
              if child.type == "method_declaration":
                  method_collector.visit_method_declaration(cls,source,child)
              if child.type == "constructor_declaration":
                    constructor_collector.visit_constructor_declaration(cls,source,child)

       