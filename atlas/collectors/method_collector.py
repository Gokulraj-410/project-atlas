class method_collector:
    def mtd_collector(source,node):
        name_node = node.child_by_field_name("name").decode("utf-8")
        return_node= node.child_by_field_name("type")
        temp = return_node.end_byte - return_node.start_byte
        return_type = source[return_node.start_byte+1:return_node.end_byte+5].decode("utf-8")
        method_name = source[name_node.start_byte+temp :name_node.end_byte+temp].decode("utf-8")
        print(node)
        print("return name :",return_type) 
        print("method name :",method_name) 
        print(name_node.start_byte,"  ",name_node.end_byte)
        for i in range(name_node.start_byte - 2, name_node.end_byte + 3):
           print(i, chr(source[i]))