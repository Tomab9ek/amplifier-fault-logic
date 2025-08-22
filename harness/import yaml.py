import yaml

VALID_DIRECTIONS = {"input", "output", "bidirectional", "power"}
POWER_NETS = {"VCC", "GND", "5V", "3.3V"}

class YAMLValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.errors = []
        self.pin_numbers = set()
        self.data = self._load_yaml()

    def _load_yaml(self):
        with open(self.file_path, 'r') as f:
            return yaml.safe_load(f)

    def validate(self):
        for connector in self.data.get("connectors", []):
            name = connector.get("name", "Unnamed Connector")
            ctype = connector.get("type")

            if not ctype:
                self.errors.append(f"Connector '{name}' has no type defined.")

            for pin in connector.get("pins", []):
                self._validate_pin(pin, name)

        return self.errors

    def _validate_pin(self, pin, connector_name):
        number = pin.get("number")
        net = pin.get("net")
        direction = pin.get("direction")

        if not net:
            self.errors.append(f"Pin {number} on '{connector_name}' is missing a net name.")

        if direction not in VALID_DIRECTIONS:
            self.errors.append(f"Pin {number} on '{connector_name}' has invalid direction '{direction}'.")

        if net in POWER_NETS and direction != "power":
            self.errors.append(f"Pin {number} on '{connector_name}' uses power net '{net}' but direction is '{direction}'.")

        if number in self.pin_numbers:
            self.errors.append(f"Duplicate pin number {number} on connector '{connector_name}'.")
        else:
            self.pin_numbers.add(number)
if __name__ == "__main__":
    import sys
    from pathlib import Path

    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("harness")
    all_errors = {}

    for file in folder.glob("*.yaml"):
        validator = YAMLValidator(file)
        errors = validator.validate()
        if errors:
            all_errors[file.name] = errors

    if all_errors:
        print("\n🔍 Validation Errors Found:")
        for fname, errs in all_errors.items():
            print(f"\n📄 {fname}:")
            for err in errs:
                print(f"  - {err}")
    else:
        print("✅ All YAML files passed validation.")


