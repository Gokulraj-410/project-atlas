from atlas.collectors.method_collector import method_collector
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
        print(node.named_children)
        method_collector = method_collector()
        for child in node.named_children:
          if child.type == "method_declaration":
              print("inside")
              method_collector.visit_method_declaration(self.source,child)
       