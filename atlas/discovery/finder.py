import os 

class Finder:

    def __init__(self,path):
        self.path = path

    def discoverFiles(self):
        discovered_files = []
    
        print(f"Discovering files in: {self.path}")
    
        for root, dirs, files in os.walk(self.path):
            for file in files:
                discovered_files.append(os.path.join(root, file))
        print(f"Total files discovered: {len(discovered_files)}")        
        #print(f"Discovered files: {discovered_files}")
        return discovered_files   

