class import_collector:
    def visit_import_declaration(self,source,node):
        scoped_node = node.named_children[0]

        import_name = source[scoped_node.start_byte:scoped_node.end_byte].decode("utf-8")

    
        self.result["imports"].append(import_name)

    
   