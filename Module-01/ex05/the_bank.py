class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1
        if (not hasattr(self, 'value')):
            self.value = 0
        if (self.value < 0):
            raise AttributeError("Attribute value cannot be negative.")
        if (not isinstance(self.name, str)):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def __str__(self) -> str:
        txt = None
        id = None
        name = None
        value = None
        if (hasattr(self, 'id')):
            id = self.id
        if (hasattr(self, 'name')):
            name = self.name
        if (hasattr(self, 'value')):
            value = self.value
        txt = f"Account(name: {name}, id: {id}, value: {value})"
        return (txt)

    def __repr__(self):
        txt = f"Account({self.__dict__})"
        return (txt)


class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    @staticmethod
    def account_check(account: Account) -> bool:
        if (not isinstance(account, Account)):
            return False
        attr_list = dir(account)
        if (len(attr_list) % 2 == 0 or
            'name' not in attr_list or
            'id' not in attr_list or
            'value' not in attr_list or
            len(list(filter(
                lambda att: att.startswith('b'), attr_list))) != 0 or
            (len(list(filter(
                lambda att: att.startswith('zip'), attr_list))) == 0 and
            len(list(filter(
                lambda att: att.startswith('addr'), attr_list))) == 0)):
            return False
        return True
        # https://www.programiz.com/python-programming/methods/built-in/filter

    def get_account(self, identity) -> Account or None:
        if (not isinstance(identity, (int, str))):
            return None

        def find_account(account: Account):
            if (isinstance(identity, int) and
                    hasattr(account, 'id') and account.id == identity):
                return account
            elif (isinstance(identity, str) and
                    hasattr(account, 'name') and account.name == identity):
                return account
            return None
        # https://code-maven.com/python-find-first-element-in-list-matching-condition
        account = next(filter(find_account, self.accounts), None)
        return account

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return False
        self.accounts.append(new_account)

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        if (not isinstance(origin, (int, str)) or
                not isinstance(dest, (int, str)) or
                amount < 0):
            return False
        origin_account = self.get_account(origin)
        if (self.account_check(origin_account) is False or
                (origin_account.value < amount)):
            return False
        dest_account = self.get_account(dest)
        if (self.account_check(dest_account) is False):
            return False
        origin_account.transfer(-amount)
        dest_account.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if (not isinstance(name, str)):
            return False
        account = self.get_account(name)
        if (not isinstance(account, Account)):
            return False
        if (self.account_check(account) is True):
            return True
        acc_attributes = dir(account)
        # Fix b* attribute
        list_b_attr = list(filter(
            lambda att: att.startswith('b'), acc_attributes))
        if (len(list_b_attr) != 0):
            for attr_name in list_b_attr:
                delattr(account, attr_name)
        # Fix zip attribute
        list_zip_attr = list(filter(
            lambda att: att.startswith('zip'), acc_attributes))
        if (len(list_zip_attr) == 0):
            setattr(account, 'zip', None)
        # Fix addr attribute
        list_addr_attr = list(filter(
            lambda att: att.startswith('addr'), acc_attributes))
        if (len(list_addr_attr) == 0):
            setattr(account, 'addr', None)
        if ('name' not in acc_attributes):
            setattr(account, 'name', None)
        if ('id' not in acc_attributes):
            setattr(account, 'id', None)
        if ('value' not in acc_attributes):
            setattr(account, 'value', 0)
        # Fix even # of attr
        if (len(dir(account)) % 2 == 0):
            nb = 0
            while hasattr(account, f'value{nb}'):
                nb += 1
            setattr(account, f'value{nb}', None)
        return True


# if __name__ == "__main__":
#     bank = Bank()
#     try:
#         acc_valid_1 = Account('Sherlock Holmes',
#                             zip='NW1 6XE',
#                             addr='221B Baker street',
#                             value=10000.0)
#         acc_valid_2 = Account('James Watson',
#                             zip='NW1 6XE',
#                             addr='221B Baker street',
#                             value=25000.0,
#                             info=None)
#         acc_invalid_1 = Account("Adam",
#                                 value=4200,
#                                 addr='Somewhere')
#         acc_invalid_2 = Account("Bender Bending Rodríguez",
#                                 zip='1',
#                                 addr='Mexico',
#                                 value=42)
#         acc_invalid_3 = Account("Charlotte",
#                                 zip='2',
#                                 addr='Somewhere in the Milky Way',
#                                 value=42)
#         acc_invalid_4 = Account("Douglass",
#                                 zip='42',
#                                 addr='boulevard bessieres',
#                                 value=42)
#         acc_invalid_5 = Account("Edouard",
#                                 zip='3',
#                                 addr='France',
#                                 value=42)
#     except AttributeError as e:
#         print(e)
#         exit()

#     bank.add(acc_valid_1)
#     bank.add(acc_valid_2)
#     bank.add(acc_invalid_1)
#     bank.add(acc_invalid_4)
#     bank.add(acc_invalid_5)

#     if bank.transfer(acc_invalid_1.name, acc_valid_1.name, 1000.0) is False:
#         print('Failed')
#         bank.fix_account(acc_valid_1.name)
#         bank.fix_account(acc_invalid_1.name)
#     if bank.transfer(acc_invalid_1.name, acc_valid_1.name, 1000.0) is False:
#         print('Failed')
#     else:
#         print('Success')

#     bank.add(Account('Jane', zip='911-745', value=1000.0, ref='1044618427ff2782f0bbece0abd05f31'))

#     jhon = Account('Jhon', zip='911-745', value=1000.0, ref='1044618427ff2782f0bbece0abd05f31')

#     bank.add(jhon)

#     print("testing a valid transfer")
#     print(jhon.value)
#     print(bank.transfer("Jane", "Jhon", 500))
#     print(jhon.value)

#     print(bank.transfer("Jane", "Jhon", 1000))
#     print(jhon.value)