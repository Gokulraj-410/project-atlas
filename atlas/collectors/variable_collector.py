class  variable_collector:
    def visit_variable_declaration(self, current_method, source, node):

        type_node = node.child_by_field_name("type")
        variable_type = source[
            type_node.start_byte:type_node.end_byte
        ].decode("utf-8")

        for child in node.named_children:
            if child.type == "variable_declarator":
                name_node = child.child_by_field_name("name")

                variable = {
                    "name": source[
                        name_node.start_byte:name_node.end_byte
                    ].decode("utf-8"),
                    "type": variable_type,
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

                current_method["localVariables"].append(variable)