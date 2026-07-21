from atlas.discovery.finder import Finder
from atlas.discovery.filter import FilterPipeline

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

        # Step 2: Parse files
        print("Parsing files...")

        # Step 3: Collect symbols
        print("Collecting symbols...")

        # Step 4: Store results
        print("Storing results...")

        # Step 5: Export JSON
        print("Exporting JSON...")

        print("Analysis completed.")