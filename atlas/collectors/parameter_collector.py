class parameter_collector:
    def visit_parameter_declaration(self,current_method,source,node):
        #print("here")
        name_node = node.child_by_field_name("name")
        param_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")

        type_node = node.child_by_field_name("type")
        type_name = source[type_node.start_byte:type_node.end_byte].decode("utf-8")
        
        param ={
            "name":param_name,
            "type":type_name,
            "location":{
            "start": {
                "line": node.start_point[0] + 1,
                "column": node.start_point[1]
            },
            "end": {
                "line": node.end_point[0] + 1,
                "column": node.end_point[1]
            }
            },
        }

        current_method["parameters"].append(param)