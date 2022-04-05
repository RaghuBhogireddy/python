
class Employee:
    def __init__(self, empname, empdepartment, empaddress ):
        self.empname = empname
        self.empdepartment = empdepartment
        self.empaddress = empaddress

class Company:
    def __init__(self, sales, stockprice, employee=None):
        self.sales = sales
        self.stockprice = stockprice
        self.employee = employee

    def printdetails(self):
        return  f"{{ \"empName\" : \"{self.employee.empname}\", " \
                f"\"empdepartment\" : \"{self.employee.empdepartment}\", " \
                f"\"empaddress\" : \"{self.employee.empaddress}\", " \
                f"\"sales\" : \"{self.sales}\", " \
                f"\"stockprice\" : \"{self.stockprice}\"}}"


emp = Employee("Raghu", "R&D", "IN")
msc = Company("Product", "$234.56", emp)

print(msc.printdetails())