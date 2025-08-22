def generate_summary(docs_folder):
    summary = "# 🧪 YAML Validation Summary\n\n"
    for file in os.listdir(docs_folder):
        if file.endswith(".md"):
            with open(os.path.join(docs_folder, file), "r") as f:
                content = f.read()
                status = "✅" if "passed validation" in content else "❌"
                summary += f"- {status} `{file.replace('.md', '')}`\n"
    return summary
