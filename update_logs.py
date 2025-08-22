from pathlib import Path
from datetime import datetime

def prepend_header_to_logs(base_dir):
    for log_path in Path(base_dir).rglob("annotation_log.txt"):
        block_name = log_path.parent.name
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = (
            f"# annotation_log.txt\n"
            f"Block: {block_name}\n"
            f"Timestamp: {timestamp}\n"
            f"Description: Pin mappings and signal annotations for this block\n---\n"
        )
        original = log_path.read_text()
        updated = f"{header}\n{original}"
        log_path.write_text(updated)
        print(f"Updated: {log_path}")

if __name__ == "__main__":
    prepend_header_to_logs("schematics")
