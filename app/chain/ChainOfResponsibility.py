from app.handlers.PhoneHandler import PhoneHandler


class PersonalDataChain:
    @staticmethod
    def build():
        phone = PhoneHandler()
        return phone

    # @staticmethod
    # def build():
    #     cpf = CPFHandler()
    #     email = EmailHandler()
    #     phone = PhoneHandler()
    #
    #     cpf.set_next(email).set_next(phone)
    #     return cpf
