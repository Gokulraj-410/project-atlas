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

                field = {
                    "name": field_name,
                    "type": field_type
                }

                current_class["fields"].append(field)