import json

class JsonExporter:

    @staticmethod
    def export(data, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)