class field_collector:

    def visit_field_declaration(self, current_class, source, node):
        type_node = node.child_by_field_name("type")
        field_type = source[
            type_node.start_byte:type_node.end_byte
        ].decode("utf-8")
        for child in node.named_children:

            if child.type == "variable_declarator":

                name_node = child.child_by_field_name("name")

                field_name = source[
                    name_node.start_byte:name_node.end_byte
                ].decode("utf-8")

                is_visible ="default" 
                is_static = False
                is_final = False

                modifiers_node = None

                for mod_child in node.children:
                    if mod_child.type == "modifiers":
                        modifiers_node = mod_child
                        break

                if modifiers_node is not None:
                    modifiers = source[
                        modifiers_node.start_byte:modifiers_node.end_byte
                    ].decode("utf-8").split()

                    if "public" in modifiers:
                        is_visible = "public"
                    elif "private" in modifiers:
                        is_visible = "private"
                    elif "protected" in modifiers:
                        is_visible = "protected"

                    is_static = "static" in modifiers
                    is_final = "final" in modifiers    

                field = {
                    "name": field_name,
                    "type": field_type,
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
                    "visibility": is_visible,
                    "static": is_static,
                    "final": is_final
                }

                current_class["fields"].append(field)