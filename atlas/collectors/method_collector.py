from atlas.collectors.parameter_collector import  parameter_collector as pc
class method_collector:
    def visit_method_declaration(self,current_class,source,node):

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
        param = node.child_by_field_name("parameters")
        parameter_collector = pc()
        if param:
            for child in param.named_children:
                #print(child)
                if child.type == "formal_parameter":
                    parameter_collector.visit_parameter_declaration(method,source,child)
            