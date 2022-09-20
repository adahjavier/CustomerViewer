import csv


class Customer():
    def __init__(self, cust_id, fName, lName, company, address, city, state, zip):
        self.cust_id = cust_id
        self.first_name = fName
        self.last_name = lName
        self.company_name = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        str = ""
        if self.company_name == "":
            str += self.first_name + "" + self.last_name + "n" + self.address + "n" + self.city + ", " + self.state + " " + self.zip
        else:
            str += self.first_name + "" + self.last_name + "n" + self.company_name + "n" + self.address + "n" + self.city + "," + self.state + " " + self.zip
        return str


# csv file name
customerList = []
with open('/Users/adahjavier/Downloads/customers.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        customerList.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        customerList.pop(0)
        print('Customer Viwer')
    while True:
        id = input('nEnter customer id: ')
        flag = 0
        for customer in customerList:
            if (customer.cust_id == id):
                print()
                print(customer)
                print()
                flag = 1
                break
        if (flag == 0):
            print("nNo customer with that idn")
        choice = input("Continue? (Y/N): ")
        if (choice == "N" or choice == "n"):
            print()
            print("Bye!")
            break