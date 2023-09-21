class BankAcc:

    def __init__(self, acc_no, acc_holder, branch, ifsc_code, email, phonenumber, atm_pin):
        self.account_no = acc_no
        self.account_holder = acc_holder
        self.branch = branch
        self.ifsc_code = ifsc_code
        self.email = email
        self.phonenumber = phonenumber
        self.__atm_pin = atm_pin

    def display_details(self):
        print(f"Account number is : {self.account_no}")
        print(f"Account holder name si: {self.account_holder}")
        print(f"branch name is : {self.branch}")
        print(f"IFSC code is : {self.ifsc_code}")
        print(f"Email ID is : {self.email}")
        print(f"Contact number is : {self.phonenumber}")
        print(f"ATM Pin is : {self.__atm_pin}")

bank_details1 = BankAcc("10001", "fathima", "fedral", "12344555676788", "ahfjadj@gmail.com", "56789032321", "3456")
print(bank_details1.account_no)
print(bank_details1.display_details())
print(bank_details1.__atm_pin)