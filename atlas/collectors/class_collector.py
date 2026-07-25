from atlas.collectors.method_collector import method_collector as mc
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
        body = node.child_by_field_name("body")
        if body:
            for child in body.named_children:
              print(child.type)
              if child.type == "method_declaration":
                  print("here")
                  method_collector.visit_method_declaration(cls,source,child)
       