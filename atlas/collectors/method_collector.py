class method_collector:
    def visit_method_declaration(self,current_class,source,node):
        print("inside")

        name_node = node.child_by_field_name("name")
        method_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")

        return_node= node.child_by_field_name("type")
        return_type = source[return_node.start_byte:return_node.end_byte].decode("utf-8")
        
        method = {
        "name": method_name,
        "returnType": return_type,
        "parameters": [],
        "localVariables": []
        }
        current_class["methods"].append(method)