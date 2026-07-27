from atlas.models.variable_model import VariableModel
from atlas.models.source_location import SourceLocation, Position


class variable_collector:

    def visit_variable_declaration(self, current_method, source, node):

        type_node = node.child_by_field_name("type")
        variable_type = source[
            type_node.start_byte:type_node.end_byte
        ].decode("utf-8")

        for child in node.named_children:

            if child.type == "variable_declarator":

                name_node = child.child_by_field_name("name")

                variable_name = source[
                    name_node.start_byte:name_node.end_byte
                ].decode("utf-8")

                location = SourceLocation(
                    start=Position(
                        line=name_node.start_point[0] + 1,
                        column=name_node.start_point[1]
                    ),
                    end=Position(
                        line=name_node.end_point[0] + 1,
                        column=name_node.end_point[1]
                    )
                )

                variable = VariableModel(
                    name=variable_name,
                    type=variable_type,
                    location=location
                )

                current_method.local_variables.append(variable)