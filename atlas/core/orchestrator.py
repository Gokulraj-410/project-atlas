from atlas.discovery.finder import Finder
from atlas.discovery.filter import FilterPipeline
from atlas.parsers.java.parser import JavaParser
from atlas.models.project import Project
from atlas.visitor.java.visitor import JavaVisitor
from atlas.exporters.json_exporter import JsonExporter

class AnalysisPipeline:
    def analyze(self, path: str):
        print(f"Starting analysis of: {path}")

        # Step 1.1: Discover files
        print("Discovering files...")
        finder = Finder(path)
        all_files = finder.discoverFiles()
        # Step 1.2: Filter files
        print("Filtering files...")
        filter=FilterPipeline()
        java_files = filter.filterFiles(all_files,".java")  # later will add other exts

        project = Project()
        # Step 2: Parse files
        print("Parsing files...")
        for each_file in java_files:
            parser = JavaParser()
            tree,source,path = parser.parse(each_file)
            visitor = JavaVisitor(tree,source,path)
            result = visitor.visit(tree.root_node)
            project.files.append(result)

           
            # You can process the tree as needed, e.g., extract symbols, etc.
        
        
        

        # Step 3: Collect symbols
        print("Collecting symbols...")

        # Step 4: Store results
        print("Storing results...")

        # Step 5: Export JSON
        print("Exporting JSON...")
        JsonExporter.export(project, "atlas.json")

        print("Analysis completed.")