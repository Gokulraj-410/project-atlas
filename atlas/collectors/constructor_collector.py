from atlas.collectors.parameter_collector import  parameter_collector as pc
from atlas.models.constructor_model import ConstructorModel
from atlas.models.modifier import Modifier
from atlas.models.source_location import SourceLocation, Position
class constructor_collector:
    def visit_constructor_declaration(self,current_class,source,node):
        name_node = node.child_by_field_name("name")
        method_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")
        is_visible = "default"
        is_static = False
        is_final = False
 
        modifiers_node = None
        for child in node.children:
            if child.type == "modifiers":
                modifiers_node = child
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

        modifier = Modifier(
            visibility=is_visible,
            static=is_static,
            final=is_final
        )
        constructor = ConstructorModel(
            name=method_name,
            modifier=modifier,
            location=SourceLocation(
            start=Position(
                line=name_node.start_point[0] + 1,
                column=name_node.start_point[1]
            ),
            end=Position(
                line=name_node.end_point[0] + 1,
                column=name_node.end_point[1]
            )
            ),
            parameters=[]
        )
        current_class.constructors.append(constructor)
        param = node.child_by_field_name("parameters")
        parameter_collector = pc()
        if param:
            for child in param.named_children:
                if child.type == "formal_parameter":
                    parameter_collector.visit_parameter_declaration(constructor,source,child)