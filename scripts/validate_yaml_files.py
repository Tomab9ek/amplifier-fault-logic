import os
import yaml
from datetime import datetime

REQUIRED_FIELDS = ['signal', 'direction', 'pin']
REPORT_PATH = "validation_report.md"

def validate_yaml_file(filepath):
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        errors.append(f"YAML parsing error → {e}")
        return errors

    if not isinstance(data, list):
        errors.append(f"Expected a list, got {type(data).__name__}")
        return errors

    for i, entry in enumerate(data):
        if not isinstance(entry, dict):
            errors.append(f"Entry {i+1}: Expected dict, got {type(entry).__name__}")
            continue
        for field in REQUIRED_FIELDS:
            if field not in entry or str(entry[field]).strip() == "":
                errors.append(f"Entry {i+1}: Missing or empty '{field}'")

    return errors

def validate_all_yaml(root_folder):
    total_errors = {}
    file_count = 0

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.yaml'):
                filepath = os.path.join(dirpath, filename)
                file_count += 1
                errors = validate_yaml_file(filepath)
                if errors:
                    total_errors[filepath] = errors

    # Write Markdown report
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(f"# YAML Validation Report\n\n")
        f.write(f"**Run Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Files Scanned:** {file_count}\n")
        f.write(f"**Files with Errors:** {len(total_errors)}\n\n")

        if total_errors:
            for path, errors in total_errors.items():
                f.write(f"## ❌ {path}\n")
                for err in errors:
                    f.write(f"- {err}\n")
                f.write("\n")
        else:
            f.write("✅ All YAML files passed validation.\n")

    print(f"\n📄 Validation report written to: {REPORT_PATH}")

if __name__ == "__main__":
    root_folder = "harness_blocks"  # Update to your repo root
    validate_all_yaml(root_folder)
- name: 📤 Upload validation report
  uses: actions/upload-artifact@v3
  with:
    name: validation-report
    path: validation_report.md
