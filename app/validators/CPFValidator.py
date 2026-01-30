import re

from validators.IValidator import IValidator
from validators.ValidationResult import ValidationResult


class CPFValidator(IValidator):

    def __init__(self, next_handler=None):
        super().__init__(next_handler)

    def handle(self, text: str) -> str:

        cpf_pattern = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"

        if re.search(cpf_pattern, text):
            text = re.sub(cpf_pattern, "[CPF_REDACTED]", text)

            return ValidationResult(
                detected_value="VALOR CPF",
                validators="CPFValidator",
            )

        if self._next_handler is not None:
            return self._next_handler.handle(text)

        return None
