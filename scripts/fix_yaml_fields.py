import os
import yaml

REQUIRED_FIELDS = ['signal', 'direction', 'pin']
ROOT_FOLDER = "harness_blocks"  # Update to your repo root

def fix_yaml_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ Skipping {filepath}: YAML error → {e}")
        return

    if not isinstance(data, list):
        print(f"❌ Skipping {filepath}: Expected list, got {type(data).__name__}")
        return

    modified = False
    for i, entry in enumerate(data):
        if not isinstance(entry, dict):
            print(f"⚠️ Entry {i+1} in {filepath} is not a dict. Skipping.")
            continue
        for field in REQUIRED_FIELDS:
            if field not in entry or str(entry[field]).strip() == "":
                entry[field] = "TODO"
                modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, sort_keys=False)
        print(f"✅ Fixed missing fields in: {filepath}")
    else:
        print(f"✅ No changes needed: {filepath}")

def fix_all_yaml(root_folder):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.yaml'):
                filepath = os.path.join(dirpath, filename)
                fix_yaml_file(filepath)

if __name__ == "__main__":
    fix_all_yaml(ROOT_FOLDER)
