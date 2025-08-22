from pathlib import Path
import yaml

VALID_DIRECTIONS = {"input", "output", "bidirectional", "power"}
POWER_NETS = {"VCC", "GND", "5V", "3.3V"}

def validate_yaml_file(file_path):
    errors = []
    pin_numbers = set()

    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        errors.append(f"YAML syntax error:\n{e}")
        return errors

    for connector in data.get("connectors", []):
        name = connector.get("name", "Unnamed Connector")
        ctype = connector.get("type")

        if not ctype:
            errors.append(f"Connector '{name}' has no type defined.")

        for pin in connector.get("pins", []):
            number = pin.get("number")
            net = pin.get("net")
            direction = pin.get("direction")

            if not net:
                errors.append(f"Pin {number} on '{name}' is missing a net name.")
            if direction not in VALID_DIRECTIONS:
                errors.append(f"Pin {number} on '{name}' has invalid direction '{direction}'.")
            if net in POWER_NETS and direction != "power":
                errors.append(f"Pin {number} on '{name}' uses power net '{net}' but direction is '{direction}'.")
            if number in pin_numbers:
                errors.append(f"Duplicate pin number {number} on connector '{name}'.")
            else:
                pin_numbers.add(number)

    return errors

# Run across all YAML files in harness/
harness_dir = Path("harness")
for file in harness_dir.glob("*.yaml"):
    print(f"\n🔍 Validating {file.name}")
    errors = validate_yaml_file(file)
    if errors:
        for err in errors:
            print(f"  - {err}")
    else:
        print("  ✅ No errors found.")
