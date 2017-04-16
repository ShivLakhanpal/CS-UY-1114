'''class BankAccount(object):
    
    def __init__ (own, account, bal):
        own.account_number = account
        own.balance = bal
        
    def get_balance(own):
        return own.balance
    
    def deposit(own, x):
        own.balance += x
        
    def withdraw(own, x):
        if own.balance > x:
            own.balance -= x


my_account = BankAccount("BOA123", 1000)
print ('Current balance is: ', my_account.get_balance())
my_account.deposit(100)
print('Current balance is: ', my_account.get_balance())
my_account.withdraw(500)
print('Current balance is: ', my_account.get_balance())
my_account.withdraw(1000)'''

class Student(object):
    def __init__(self, first, last, studentID, gpa):
        self.first_name = first
        self.last_name = last
        self.student_id = studentID
        self.student_gpa = gpa
    def get_studentID(self):
        return self.student_id
    def set_gpa(self, new_gpa):
        self.student_gpa = new_gpa
    def get_studentGPA(self):
        return self.student_gpa
    def __str__(self):
        return "{}, {}:\t\t{}".format(self.last_name, self.first_name, self.student_id)
    
def main():
    s1 = Student("Jane","Jones","N012345678",3.5)
    s2 = Student("Sam", "Smith", "N123456789",3.0)
    print(s1.get_studentID()) #Line 1
    print(str(s1)) #Line 2
    s2.set_gpa(3.75)
    evaluation = ""
    if s1.get_studentGPA() > s2.get_studentGPA():
        evaluation = s1.get_studentID() + " has higher GPA than " +s2.get_studentID()

    else:
        evaluation = s2.get_studentID() + " has higher or equal GPA than " + s2.get_studentID()
        print(evaluation) # Line 3
main()
