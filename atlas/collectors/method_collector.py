from atlas.collectors.parameter_collector import  parameter_collector as pc
from atlas.collectors.variable_collector import  variable_collector as vc
from atlas.models.method_model import MethodModel
from atlas.models.modifier import Modifier
from atlas.models.source_location import SourceLocation, Position
class method_collector:
    def visit_method_declaration(self,current_class,source,node):

        name_node = node.child_by_field_name("name")
        method_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")

        return_node= node.child_by_field_name("type")
        return_type = source[return_node.start_byte:return_node.end_byte].decode("utf-8")

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
        
        modifier = Modifier(
            visibility=is_visible,
            static=is_static,
            final=is_final
        )
        method = MethodModel(
            name=method_name,
            return_type=return_type,
            modifier=modifier,
            location=SourceLocation(
                start=Position(
                    line=node.start_point[0] + 1,
                    column=node.start_point[1]
                ),
                end=Position(
                    line=node.end_point[0] + 1,
                    column=node.end_point[1]
                )
            ),
            parameters=[],
            local_variables=[]
        )

        
        current_class.methods.append(method)
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

            