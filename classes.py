__author__ = 'vikram'


class Fruit(object):
    """A class that makes various tasty fruits."""

    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

    def how_big(self):
        if self.name == "lemon":
            print "%s is a medium sized fruit" % (self.name)
        elif self.name == "mango":
            print "Mango is a large fruit"
        else:
            print "I dont know how big a %s is" % self.name


lemon = Fruit("lemon", "yellow", "sour", False)
mango = Fruit("mango", "yellow", "sweet", False)
papaya = Fruit("papaya", "yellow", "sweet", False)
lemon.description()
lemon.is_edible()
mango.how_big()
lemon.how_big()
papaya.how_big()


class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!
    def description(self):
        print self.name
        print self.age


hippo = Animal("fatty", 3)
hippo.description()


class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."


my_cart = ShoppingCart("Vik")
my_cart.add_item("pant", 40)
my_cart.add_item("pant", 43)


class Shape(object):
    """Makes shapes!"""

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        assert isinstance(hours, int)
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)
print milton.calculate_wage(10)
