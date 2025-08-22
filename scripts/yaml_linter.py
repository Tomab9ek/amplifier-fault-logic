import argparse
from pathlib import Path
from validator import YAMLValidator  # assuming validator.py is in the same folder or importable


def lint_yaml_filenames(harness_dir):
    issues_found = False
    for file in Path(harness_dir).glob("*.yaml"):
        name = file.stem
        issues = []

        if "-" in name:
            issues.append("❌ Uses hyphen instead of underscore")
        if not name.islower():
            issues.append("⚠️ Not lowercase")
        if "_" not in name:
            issues.append("⚠️ Missing underscore separator")

        if issues:
            issues_found = True
            print(f"{file.name}: {' | '.join(issues)}")
        else:
            print(f"{file.name}: ✅ OK")
    if not issues_found:
        print("🎉 All filenames passed linting!")

def fix_yaml_filenames(harness_dir):
    for file in Path(harness_dir).glob("*.yaml"):
        new_name = file.stem.replace("-", "_").lower() + ".yaml"
        if file.name != new_name:
            new_path = file.parent / new_name
            file.rename(new_path)
            print(f"🔧 Renamed: {file.name} → {new_name}")

def yaml_prefix_dashboard(harness_dir):
    prefix_map = defaultdict(list)
    for file in Path(harness_dir).glob("*.yaml"):
        parts = file.stem.split("_")
        if len(parts) > 1:
            prefix = parts[0]
            prefix_map[prefix].append(file.name)

    print("📦 YAML Block Prefix Summary:")
    for prefix, files in sorted(prefix_map.items()):
        print(f"  {prefix}: {len(files)} files")
        for f in files:
            print(f"    - {f}")

def main():
    parser = argparse.ArgumentParser(description="Lint and organize YAML harness files.")
    parser.add_argument("harness_dir", help="Path to harness directory")
    parser.add_argument("--lint", action="store_true", help="Lint YAML filenames")
    parser.add_argument("--fix", action="store_true", help="Fix filename issues")
    parser.add_argument("--dashboard", action="store_true", help="Show prefix summary")

    args = parser.parse_args()

    if args.lint:
        lint_yaml_filenames(args.harness_dir)
    if args.fix:
        fix_yaml_filenames(args.harness_dir)
    if args.dashboard:
        yaml_prefix_dashboard(args.harness_dir)

if __name__ == "__main__":
    main()
