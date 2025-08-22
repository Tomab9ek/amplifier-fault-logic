from pathlib import Path
import sys
import yaml

def find_repo_root():
    current = Path(__file__).resolve()
    while current.parent != current:
        if (current / ".git").exists():
            return current
        current = current.parent
    raise RuntimeError("Repo root not found")

def validate_yaml_file(file_path):
    try:
        with open(file_path, "r") as f:
            yaml.safe_load(f)
        print(f"✅ Valid YAML: {file_path.name}")
    except Exception as e:
        print(f"❌ Invalid YAML: {file_path.name}")
        print(f"   Error: {e}")

def main():
    repo_root = find_repo_root()
    harness_dir = repo_root / "harness"

    if len(sys.argv) > 1:
        file_path = harness_dir / sys.argv[1]
        if file_path.exists():
            validate_yaml_file(file_path)
        else:
            print(f"❌ File not found: {file_path}")
    else:
        yaml_files = harness_dir.glob("*.yaml")
        if not any(yaml_files):
            print("⚠️ No YAML files found in harness/")
        for file in harness_dir.glob("*.yaml"):
            validate_yaml_file(file)

if __name__ == "__main__":
    main()


