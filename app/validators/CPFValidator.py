import re

from validators.IValidator import IValidator
from validators.ValidationResult import ValidationResult


class CPFValidator(IValidator):
    CPF_REGEX = re.compile(r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b")

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, text: str) -> ValidationResult:

        match = self.CPF_REGEX.search(text)

        if match:
            return ValidationResult(
                detected_value=match.group(),
                validators="CPFValidator",
            )

        if self._next_handler is not None:
            return self._next_handler.handle(text)

        return None
