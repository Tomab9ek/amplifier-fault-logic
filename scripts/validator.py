from pathlib import Path
import yaml

class YAMLValidator:
    def __init__(self, yaml_path: Path):
        self.yaml_path = yaml_path

    def validate(self):
        if not self.yaml_path.exists():
            print(f"❌ File not found: {self.yaml_path}")
            return False

        try:
            with open(self.yaml_path, 'r') as f:
                yaml.safe_load(f)
            print(f"✅ YAML is valid: {self.yaml_path}")
            return True
        except yaml.YAMLError as e:
            print(f"❌ YAML validation error:\n{e}")
            return False
