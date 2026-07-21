import os
class FilterPipeline:

    def filterFiles(self,discovered_files, extensions):
        filtered_files = []
        print(f"Filtering files with extensions: {extensions}")
        for file in discovered_files:
            if file.endswith(extensions):
                filtered_files.append(file)
        print(f"Total files filtered: {len(filtered_files)}")        
        print(f"Filtered files: {filtered_files}")        
        return filtered_files
     
        
        
