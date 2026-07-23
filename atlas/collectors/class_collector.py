class class_collector:
    def cls_collector(source,node):
        name_node = node.child_by_field_name("name")
        class_name = source[name_node.start_byte+1:name_node.end_byte+1].decode("utf-8")
        print(class_name)  
       