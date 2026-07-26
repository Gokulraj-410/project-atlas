from atlas.collectors.parameter_collector import  parameter_collector as pc
from atlas.collectors.variable_collector import  variable_collector as vc
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
        var = node.child_by_field_name("body")
        parameter_collector = pc()
        variable_collector = vc()
        if param:
            for child in param.named_children:
                #print(child)
                if child.type == "formal_parameter":
                    parameter_collector.visit_parameter_declaration(method,source,child)
        if var:
            for child in var.named_children: 
                if child.type == "local_variable_declaration":
                    variable_collector.visit_variable_declaration(method,source,child)        

            