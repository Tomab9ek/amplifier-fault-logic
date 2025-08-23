from pathlib import Path
import sys

def generate_markdown_table(yaml_path: Path) -> str:
    try:
        with open(yaml_path, 'rt', encoding='utf-8') as f:
            return f.read().rstrip()
    except UnicodeDecodeError as e:
        print(f"[Decode Error] {yaml_path.name}: {e}", file=sys.stderr)
        return ""

def write_markdown_table(yaml_path: Path) -> None:
    text = generate_markdown_table(yaml_path)
    if not text:
        print(f"[Skipped] {yaml_path.name} — empty or unreadable.")
        return

    md_path = yaml_path.with_suffix('.md')
    try:
        with open(md_path, 'wt', encoding='utf-8') as f:
            f.write(text)
        print(f"[✓] Generated: {md_path.name}")
    except UnicodeEncodeError as e:
        print(f"[Encode Error] {md_path.name}: {e}", file=sys.stderr)

def batch_process_yaml(folder: Path) -> None:
    if not folder.exists():
        print(f"[Error] Folder not found: {folder}")
        return

    yaml_files = list(folder.glob('*.yaml'))
    if not yaml_files:
        print(f"[Info] No YAML files found in {folder}")
        return

    for yaml_file in yaml_files:
        write_markdown_table(yaml_file)

if __name__ == "__main__":
    target_folder = Path('log-samples/1-batch_generate')
    batch_process_yaml(target_folder)
