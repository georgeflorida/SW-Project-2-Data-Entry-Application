from GroceryDbEntry import GroceryDbEntry
from tkinter import filedialog
import json

class GroceryDb:

    def __init__(self, init=False, dbName='GroceryDb.csv'):
        self.dbName = dbName
        self.groceryList = []

        with open(self.dbName, 'r') as file:
            lines = file.readlines()
            lines = lines[:]  
        for line in lines:
            data = line.strip().split(',')
            entry = GroceryDbEntry(data[0], data[1], data[2], data[3], data[4])
            self.groceryList.append(entry)

    def get_grocery_list(self):
        tupleList = []
        for data in self.groceryList:
            entries = (data.item, data.allergen, data.name, data.quantity, data.price)
            tupleList.append(entries)
        return tupleList

    def insert_grocery(self, item, allergen, name, quantity, price):
        newEntry = GroceryDbEntry(item=item, allergen=allergen, name=name, quantity=quantity,price=price)
        self.groceryList.append(newEntry)

    def delete_grocery(self, name):
        for data in self.groceryList:
            if data.name == name:
                self.groceryList.remove(data)

    def update_grocery(self, name, new_item, new_allergen, new_quantity, new_price):
        for data in self.groceryList:
            if data.name == name:
                data.item = new_item
                data.allergen = new_allergen
                data.quantity = new_quantity
                data.price = new_price
    
    def export_csv(self):
        with open(self.dbName, 'w') as file:
            for data in self.groceryList:
                data_entry = data.item + "," + data.allergen + "," + data.name + "," + str(data.quantity) + "," + str(data.price) + "\n"
                file.write(data_entry)

    def export_json(self):
            json_list = []
            for data in self.groceryList:
                json_dict = {'item': data.item, 'allergen': data.allergen, 'name': data.name, 'quantity': data.quantity, 'price': data.price}
                json_list.append(json_dict)

            with open('GroceryDb.json', 'w') as json_file:
                json.dump(json_list, json_file, indent=4)

    def import_csv(self):
        import_file_name = filedialog.askopenfilename(title="Select CSV file to import", filetypes=[("CSV Files", "*.csv")])

        with open(import_file_name, 'r') as file:
            lines = file.readlines()
            lines = lines[:]  

        for line in lines:
            data = line.strip().split(',')
            entry = GroceryDbEntry(data[0], data[1], data[2], data[3], data[4])
            self.groceryList.append(entry)

    def name_exists(self, name):
        for data in self.groceryList:
            if data.name == name:
                return True
            else:
                    continue
        return False