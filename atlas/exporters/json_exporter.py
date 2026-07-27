from dataclasses import asdict
import json


class JsonExporter:

    @staticmethod
    def export(project, output_path):
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                asdict(project),
                f,
                indent=4,
                ensure_ascii=False
            )