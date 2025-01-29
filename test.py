class Warehouse:
    def __init__(self, city, country, coordinates, stock):
        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.stock = stock

class Buyer:
    def __init__(self, name, city, country, coordinates):
        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates

class Order:
    def __init__(self, buyer, product, quantity):
        self.buyer = buyer
        self.product = product
        self.quantity = quantity

class Delivery:
    

    def same_country(self, warehouses, order):
        cities = []
        for warehouse in warehouses:
            if warehouse.country == order.buyer.country:
                cities.append(warehouse.city)
        return cities
    
    def stock_availability(self, warehouses, order):
        cities = []
        for warehouse in warehouses:
            if warehouse.stock >= order.quantity:
                cities.append(warehouse.city)
        return cities
        

      
   
warehouse = Warehouse("Toronto", "Canada", [2, 2], 1)
warehouse2 = Warehouse("Montreal", "Canada", [3, -1], 99)
warehouse3 = Warehouse("Seattle", "US", [-2, 1], 5)
warehouse4 = Warehouse("London", "UK", [10, 3], 10)


order = Order(Buyer("Tom", "Vancouver", "Canada", [-2, 5]), "laptop", 1)

order2 = Order(Buyer("Kevin", "New York", "US", [4,-3]), "laptop", 1)


order3 = Order(Buyer("Tom", "Vancouver", "Canada", [-2, 5]), "laptop", 5)

delivery = Delivery()
print(delivery.same_country([warehouse, warehouse2, warehouse3, warehouse4], order)) # ['Toronto', 'Montreal']

print(delivery.same_country([warehouse, warehouse2, warehouse3, warehouse4], order2)) # ['Seattle']

print(delivery.stock_availability([warehouse, warehouse2, warehouse3, warehouse4], order3)) # ['Montreal', 'Seattle', 'London']