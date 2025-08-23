import yaml
import os
folder_path = "tmp_sample3/sample"
errors = validate_yaml_files(
    value_folder="tmp_sample3/.batch.generate/",
    value_yaml_fields_file="tmp_sample3/fields.yaml",
    value_yaml_live_folder="tmp_sample3/live",
    value_yaml_sample_folder=folder_path
)

# Required fields for each signal entry
REQUIRED_FIELDS = ['signal', 'direction', 'pin']

def validate_yaml_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return [f"YAML error in {filepath}: {e}"]

    errors = []
    for i, entry in enumerate(data):
        for field in REQUIRED_FIELDS:
            if field not in entry or entry[field] in [None, '', ' ']:
                errors.append(f"{os.path.basename(filepath)} → Entry {i+1}: Missing or empty '{field}'")

    return errors
def validate_yaml_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return [f"YAML error in {filepath}: {e}"]

    if not isinstance(data, list):
        return [f"{os.path.basename(filepath)}: Expected a list of entries, got {type(data).__name__}"]

    errors = []
    for i, entry in enumerate(data):
        if not isinstance(entry, dict):
            errors.append(f"{os.path.basename(filepath)} → Entry {i+1}: Expected dict, got {type(entry).__name__}")
            continue
        for field in REQUIRED_FIELDS:
            if field not in entry or str(entry[field]).strip() == "":
                errors.append(f"{os.path.basename(filepath)} → Entry {i+1}: Missing or empty '{field}'")

    return errors

def validate_folder(folder_path):
    all_errors = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.yaml'):
            filepath = os.path.join(folder_path, filename)
            errors = validate_yaml_file(filepath)
            all_errors.extend(errors)

    if all_errors:
        print("⚠️ Validation Issues Found:")
        for err in all_errors:
            print(" -", err)
    else:
        print("✅ All YAML files passed validation.")

# Example usage
if __name__ == "__main__":
    validate_folder("log-samples/1-batch_generate")
if __name__ == "__main__":
    folder_path = "img-samples/batch_generate"  # Or wherever your YAMLs live
    errors = validate_folder(folder_path)

    if errors:
        print("⚠️ Validation Issues Found:")
        for err in errors:
            print(" -", err)
    else:
        print("✅ All YAML files passed validation.")
