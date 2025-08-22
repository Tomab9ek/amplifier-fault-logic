import sys
from pathlib import Path
import yaml

def yaml_to_markdown_table(yaml_path: Path, output_path: Path):
    if not yaml_path.exists():
        print(f"❌ YAML file not found: {yaml_path.name}")
        return

    try:
        with yaml_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        headers = ["Signal", "Source", "Destination", "Notes"]
        rows = data.get("wires", [])

        md_lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
        for row in rows:
            md_lines.append("| " + " | ".join(str(row.get(h.lower(), "")) for h in headers) + " |")

        output_path.write_text("\n".join(md_lines), encoding="utf-8")
        print(f"✅ Markdown table written: {output_path.name}")

    except Exception as e:
        print(f"❌ Error converting {yaml_path.name}:\n{e}")

def batch_convert_yaml_to_md(harness_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n📁 Writing Markdown tables to: {output_dir.resolve()}")
    for yaml_file in harness_dir.glob("*.yaml"):
        md_file = output_dir / f"{yaml_file.stem}.md"
        yaml_to_markdown_table(yaml_file, md_file)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        yaml_file = Path(sys.argv[1])
        output_md = Path(sys.argv[2])
        yaml_to_markdown_table(yaml_file, output_md)
    else:
        harness_dir = Path("harness")
        output_dir = Path("docs/wiring_tables")
        batch_convert_yaml_to_md(harness_dir, output_dir)
