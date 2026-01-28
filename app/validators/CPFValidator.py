import re
from validators.IValidator import IValidator

class CPFValidator(IValidator):
    def handle(self, text: str) -> str:
        # Matches XXX.XXX.XXX-XX or XXXXXXXXXXX
        cpf_pattern = r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b'
        
        if re.search(cpf_pattern, text):
            text = re.sub(cpf_pattern, "[CPF_REDACTED]", text)
        
        if self._IValidator__next_handler:
            return self._IValidator__next_handler.handle(text)
        
        return text