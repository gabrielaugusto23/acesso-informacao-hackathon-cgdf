from validators.PhoneValidator import PhoneValidator


class DataValidationPipeline:
    @staticmethod
    def build():
        phone = PhoneValidator()
        return phone

    # @staticmethod
    # def build():
    #     cpf = CPFHandler()
    #     email = EmailHandler()
    #     phone = PhoneHandler()
    #
    #     cpf.set_next(email).set_next(phone)
    #     return cpf
