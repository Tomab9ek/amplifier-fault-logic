import yaml
from pathlib import Path


def generate_markdown_table(yaml_path_str):
    yaml_path = Path(yaml_path_str)
    if not yaml_path.exists():
        print(f"⚠️ File not found: {yaml_path}")
        return ""

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # continue processing...

def generate_markdown_table(yaml_path):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    block_name = data.get("name", yaml_path.stem)
    lines = [f"### Wiring Table: {block_name}", "", "| Signal | Ref | Pin |", "|--------|-----|-----|"]

    for wire in data.get("wires", []):
        signal = wire.get("signal")
        for end in wire.get("ends", []):
            ref = end.get("ref")
            pin = end.get("pin")
            lines.append(f"| {signal} | {ref} | {pin} |")

    return "\n".join(lines), block_name

def batch_generate(harness_dir, output_dir):
    Path(output_dir).mkdir(exist_ok=True)
    full_table_lines = ["# Full System Wiring Table", ""]

    for yaml_file in Path(harness_dir).glob("*.yaml"):
        md_content, block_name = generate_markdown_table(yaml_file)
        md_path = Path(output_dir) / f"{yaml_file.stem}.md"
        md_path.write_text(md_content)
        print(f"✅ Generated: {md_path}")

        # Add to full system table
        full_table_lines.append(f"## Block: {block_name}")
        full_table_lines += md_content.splitlines()[3:]  # skip title + headers
        full_table_lines.append("")  # spacing

    # Write full system table
        full_md_path = Path(output_dir) / "full-system.md"
        with open("gen_table.md", "w", encoding="utf-8") as f:
         f.write(table_text)

         


    print(f"🧩 Merged: {full_md_path}")
def generate_markdown_table(yaml_path):
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)

    block_name = data.get("name", yaml_path.stem)
    schematic_link = f"[📘 Schematic](/schematics/{block_name}.pdf)"
    lines = [f"### Wiring Table: {block_name} {schematic_link}", "", "| Signal | Ref | Pin |", "|--------|-----|-----|"]

    for wire in data.get("wires", []):
        signal = wire.get("signal")
        for end in wire.get("ends", []):
            ref = end.get("ref")
            pin = end.get("pin")
            lines.append(f"| {signal} | {ref} | {pin} |")

    return "\n".join(lines), block_name

if __name__ == "__main__":
    batch_generate("harness", "wiring_tables")
