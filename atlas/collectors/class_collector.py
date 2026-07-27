from atlas.collectors.method_collector import method_collector as mc
from atlas.collectors.constructor_collector import constructor_collector as cc
from atlas.collectors.field_collector import field_collector as fc


class class_collector:

    def visit_class_declaration(self, source, node):
        
        name_node = node.child_by_field_name("name")
        class_name = source[
            name_node.start_byte:name_node.end_byte
        ].decode("utf-8")

        visibility = "default"
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
                visibility = "public"
            elif "private" in modifiers:
                visibility = "private"
            elif "protected" in modifiers:
                visibility = "protected"

            is_static = "static" in modifiers
            is_final = "final" in modifiers
        cls = {
            "name": class_name,
            "visibility": visibility,
            "static": is_static,
            "final": is_final,
            "fields": [],
            "constructors": [],
            "methods": []
        }

        self.result["classes"].append(cls)
        method_collector = mc()
        constructor_collector = cc()
        field_collector = fc()

        body = node.child_by_field_name("body")

        if body:
            for child in body.named_children:

                if child.type == "field_declaration":
                    field_collector.visit_field_declaration(
                        cls,
                        source,
                        child
                    )

                elif child.type == "constructor_declaration":
                    constructor_collector.visit_constructor_declaration(
                        cls,
                        source,
                        child
                    )

                elif child.type == "method_declaration":
                    method_collector.visit_method_declaration(
                        cls,
                        source,
                        child
                    )