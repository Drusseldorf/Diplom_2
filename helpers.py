from faker import Faker


class Generate:

    @staticmethod
    def name():
        return Faker().name()

    @staticmethod
    def email():
        return Faker().email()

    @staticmethod
    def password():
        return Faker().password()
