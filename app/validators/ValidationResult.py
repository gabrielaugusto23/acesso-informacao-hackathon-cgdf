from dataclasses import dataclass

@dataclass
class ValidationResult:
    detected_value: str
    validators: str