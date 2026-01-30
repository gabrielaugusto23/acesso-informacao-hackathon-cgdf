from app.validators.CPFValidator import CPFValidator
from app.validators.PhoneValidator import PhoneValidator
from app.validators.RGValidator import RGValidator


class DataValidationPipeline:
    @staticmethod
    def build():
        phone = PhoneValidator()
        rg = RGValidator(phone)
        cpf = CPFValidator(rg)
        return cpf
