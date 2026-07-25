from atlas.collectors.parameter_collector import  parameter_collector as pc
class constructor_collector:
    def visit_constructor_declaration(self,current_class,source,node):
        name_node = node.child_by_field_name("name")
        method_name = source[name_node.start_byte:name_node.end_byte].decode("utf-8")

        constructor ={
            "name":method_name,
            "parameters":[]
        }
        current_class["constructors"].append(constructor)
        param = node.child_by_field_name("parameters")
        parameter_collector = pc()
        if param:
            for child in param.named_children:
                if child.type == "formal_parameter":
                    parameter_collector.visit_parameter_declaration(constructor,source,child)