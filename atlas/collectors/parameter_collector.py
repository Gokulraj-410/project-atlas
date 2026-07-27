from atlas.models.parameter_model import ParameterModel
from atlas.models.source_location import SourceLocation, Position
class parameter_collector:
    def visit_parameter_declaration(self,current_method,source,node):
        #print("here")
        name_node = node.child_by_field_name("name")
        param_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")

        type_node = node.child_by_field_name("type")
        type_name = source[type_node.start_byte:type_node.end_byte].decode("utf-8")
        
        param = ParameterModel(
            name=param_name,
            type=type_name,
            location=SourceLocation(
                start=Position(
                    line=name_node.start_point[0] + 1,
                    column=name_node.start_point[1]
                ),
                end=Position(
                    line=name_node.end_point[0] + 1,
                    column=name_node.end_point[1]
                )
            )
        )

        current_method.parameters.append(param)