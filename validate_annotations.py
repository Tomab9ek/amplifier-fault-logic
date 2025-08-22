from pathlib import Path
import yaml
import re

# Load annotation log and build mapping
def parse_annotation_log(log_text):
    mapping = {}
    pattern = r"Updated (\S+) from (\S+) to (\S+)|Annotated (\S+) as (\S+)"
    for line in log_text.splitlines():
        match = re.search(pattern, line)
        if match:
            old_type, old_ref, new_ref, ann_type, ann_ref = match.groups()
            key = old_ref if old_ref else ann_type
            val = new_ref if new_ref else ann_ref
            mapping.setdefault(key, []).append(val)
    return mapping

# Load YAML harness files
def load_yaml_components(yaml_dir):
    components = set()
    for file in Path(yaml_dir).glob("*.yaml"):
        with open(file, "r") as f:
            data = yaml.safe_load(f)
            for wire in data.get("wires", []):
                for end in wire.get("ends", []):
                    ref = end.get("ref")
                    if ref:
                        components.add(ref)
    return components

# Load Markdown wiring tables
def load_markdown_components(md_dir):
    components = set()
    pattern = r"\b([A-Z]+\d+)\b"
    for file in Path(md_dir).glob("*.md"):
        with open(file, "r") as f:
            for line in f:
                matches = re.findall(pattern, line)
                components.update(matches)
    return components

# Compare and validate
def validate_components(mapping, yaml_refs, md_refs):
    all_mapped = {ref for refs in mapping.values() for ref in refs}
    missing_in_yaml = all_mapped - yaml_refs
    missing_in_md = all_mapped - md_refs
    print("🔍 Missing in YAML:", sorted(missing_in_yaml))
    print("📄 Missing in Markdown:", sorted(missing_in_md))

# Entry point
if __name__ == "__main__":
    with open("schematics/annotation_log.txt") as f:
        log_text = f.read()
    mapping = parse_annotation_log(log_text)
    yaml_refs = load_yaml_components("harness/")
    md_refs = load_markdown_components("wiring_tables/")
    validate_components(mapping, yaml_refs, md_refs)
