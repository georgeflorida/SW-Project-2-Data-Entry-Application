from GroceryDb import GroceryDb
from GroceryGuiCtk import GroceryGuiCtk

def main():
    db = GroceryDb(init=False, dbName='GroceryDb.csv')
    app = GroceryGuiCtk(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()