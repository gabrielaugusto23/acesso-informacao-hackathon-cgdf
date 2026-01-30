from validators.CPFValidator import CPFValidator
from validators.EmailValidator import EmailValidator
from validators.NameValidator import NameValidator
from validators.PhoneValidator import PhoneValidator
from validators.RGValidator import RGValidator


class DataValidationPipeline:
    @staticmethod
    def build():
        return PhoneValidator(
            RGValidator(CPFValidator(EmailValidator(NameValidator(None))))
        )
