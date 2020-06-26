import csv
import random
from faker import Faker
import abc


class Column(metaclass=abc.ABCMeta):
    def __init__(self, func, num_uniq_value: int):
        self.num_uniq_value = num_uniq_value
        self.list = [func() for _ in range(self.num_uniq_value)]

        # in case duplication has occurred
        if len(set(self.list)) < self.num_uniq_value:
            left = self.num_uniq_value - len(set(self.list))
            self.list.extend([func() for _ in range(left)])


class RandomValue:
    def __init__(self, fake: Faker, num_rows: int):
        self.num_rows = num_rows
        self.fake = fake

        columns = (
            '企業名',
            '担当名',
            '住所',
            '電話番号',
            '日付',
            '売上',
        )
        self.dataset = []
        self.dataset.append(columns)

    def set_company_name(self, func, num_uniq_value: int = 10):
        self.company_name = Column(func, num_uniq_value)

    def get_company_name(self):
        return random.choice(self.company_name.list)

    def set_personal_name(self, func, num_uniq_value: int = 10):
        self.personal_name = Column(func, num_uniq_value)

    def get_personal_name(self):
        return random.choice(self.personal_name.list)

    def set_address(self, func, num_uniq_value: int = 10):
        self.address = Column(func, num_uniq_value)

    def get_address(self):
        return random.choice(self.address.list)

    def set_phone_number(self, func, num_uniq_value: int = 10):
        self.phone_number = Column(func, num_uniq_value)

    def get_phone_number(self):
        return random.choice(self.phone_number.list)

    def set_date_between(self, func, num_uniq_value: int = 10):
        self.date_between = Column(func, num_uniq_value)

    def get_date_between(self):
        return random.choice(self.date_between.list)

    def generate_romdom_dataset(self):
        for _ in range(self.num_rows):
            self.dataset.append([
                self.get_company_name(),
                self.get_personal_name(),
                self.get_address(),
                self.get_phone_number(),
                self.get_date_between(),
                int(random.uniform(1000, 10000))
            ])
        return self.dataset


def generate_romdom_dataset(filename_to: str, num_rows=100):
    def __data_btw():
        return faker.date_between('-1y')

    faker = Faker('ja_JP')
    rv = RandomValue(faker, num_rows)
    rv.set_address(faker.address)
    rv.set_company_name(faker.company)
    rv.set_personal_name(faker.name)
    rv.set_phone_number(faker.phone_number)
    rv.set_date_between(__data_btw)

    dataset = rv.generate_romdom_dataset()

    with open(filename_to, 'w') as f:
        w = csv.writer(f)
        w.writerows(dataset)
