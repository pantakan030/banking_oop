class Bank:
    def __init__(self)
        self.client_info_list = []
        self.login = False
        self.amount = 500 ## First cash for bank-account opening

    def register(self, firstName, surName , contact, passwd): ## Register Pages
        amount = self.amount
        condition = True
        if len(str(contact)) > 10 or len(str(contact)) < 10:
            print('Invalid Phone number ! Please, provide it again'.)
            condition = False
        
        if len(str(passwd)) < 8:
            print('You password is too easy ! Please, enter password that greater than 8 characters.')
            condition = False
        
        if condition == True:
            print('Your account has been created successfully !')
            self.client_info_list = [firstName, surName, contact, passwd, amount]
            with open(f'{firstName}_{surName}.txt','w') as f:
                for details in self.client_info_list:
                    f.write(str(details) + ',')
    
    def login(self, firstName, surName,contact, passwd):
        with open(f'{firstName}_{surName}.txt', 'r') as input_:
            details = input_.read()
            self.client_info_list = details.split(',')
            if str(contact) in str(self.client_info_list):
                if str(passwd) in str(self.client_info_list):
                    self.login = True

            if self.login == True:
                print(f'{firstName}_{surName} loged in !')
                self.amount = self.client_info_list[4]
                self.firstName = firstName
            else:
                print('Wrong Details !!')

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.balance

    def transfer():
        pass

    def withdrawal():
        pass