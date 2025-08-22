from scripts.validate_yaml import YAMLValidator
from scripts.markdown_report import generate_markdown_report

validator = YAMLValidator("harness/mute-relay.yaml")
errors = validator.validate()
report = generate_markdown_report(errors, "mute-relay.yaml")
print(report)
