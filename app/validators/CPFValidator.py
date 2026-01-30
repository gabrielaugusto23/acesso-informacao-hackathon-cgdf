import re

from validate_docbr import CPF

from app.validators.IValidator import IValidator
from app.validators.ValidationResult import ValidationResult


class CPFValidator(IValidator):
    def __init__(self, next_handler=None):
        super().__init__(next_handler)
        self.cpf_validator = CPF()

    def handle(self, text: str):
        cpf_pattern = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"
        matches = re.findall(cpf_pattern, text)

        for match in matches:
            if self.cpf_validator.validate(match):
                return ValidationResult(
                    detected_value=f"CPF: {match}",
                    validators="CPFValidator",
                )

        if self._next_handler is not None:
            return self._next_handler.handle(text)

        return None
