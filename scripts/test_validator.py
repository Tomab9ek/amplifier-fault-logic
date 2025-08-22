from pathlib import Path
from scripts.validator import YAMLValidator

def test_valid_yaml():
    path = Path("tests/valid_harness.yaml")
    validator = YAMLValidator(path)
    assert validator.validate() == True

def test_invalid_yaml():
    path = Path("tests/invalid_harness.yaml")
    validator = YAMLValidator(path)
    assert validator.validate() == False

if __name__ == "__main__":
    test_valid_yaml()
    test_invalid_yaml()
    print("✅ Manual tests passed.")
