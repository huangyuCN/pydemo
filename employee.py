class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmplouee(self):
        print "Name:", self.name, ",Salary:", self.salary


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmplouee()
emp2.displayEmplouee()
print "Total Employee %d" % Employee.empCount

print "__doc__:", Employee.__doc__
print "__name__:", Employee.__name__
print "__module__:", Employee.__module__
print "__basse__:", Employee.__bases__
print "__dict__:", Employee.__dict__
