class parameter_collector:
    def visit_parameter_declaration(self,current_method,source,node):
        #print("here")
        name_node = node.child_by_field_name("name")
        param_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")

        type_node = node.child_by_field_name("type")
        type_name = source[type_node.start_byte:type_node.end_byte].decode("utf-8")
        
        param ={
            "name":param_name,
            "type":type_name
        }

        current_method["parameters"].append(param)