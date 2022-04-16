"""
Name: Joshua Uys
hw11.py

Sales Person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sale = []

    def get_ID(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sale.append(sale)

    def total_sales(self):
        total = 0
        for i in range(len(self.sale)):
            total += self.sale[i]

        return total

    def get_sales(self):
        return self.sale

    def met_quota(self, quota):
        if total_sales() < quota:
            return False
        elif total_sales() >= quota:
            return True

    def compare_to(self, other):
        if total_sales(other) > total_sales():
            return -1
        elif total_sales(other) < total_sales():
            return 1
        elif total_sales(other) == total_sales():
            return 0

    def __str__():
        return self.employee_id, self.name, total_sales()



from sales_force.py import add_data()

add_data("sales_data.txt")

# SalesForce.add_data("sales_data.txt")
