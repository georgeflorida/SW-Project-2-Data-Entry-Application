import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from GroceryDb import GroceryDb

class GroceryGuiCtk(customtkinter.CTk):

    def __init__(self, dataBase=GroceryDb()):
        super().__init__()
        self.db = dataBase

        self.title('Grocery List')
        self.geometry('1355x735')
        self.config(bg='#D7C18F')
        self.resizable(False, False)

        self.bg_image = PhotoImage(file='background.png')
        windowsize = Canvas(self, width=1355, height=735)
        windowsize.pack()

        windowsize.create_image(0, -50, anchor=NW, image=self.bg_image)

        self.font1 = ('Comic Sans MS', 20, 'bold')
        self.font2 = ('Courier New', 12, 'bold')

        #item
        self.item_label = self.newCtkLabel('Item')
        self.item_label.place(x=110, y=500)
        self.item_cboxVar = StringVar()
        self.item_cboxOptions = ['Fresh Produce', 'Dairy', 'Meat/Seafood', 'Frozen', 'Bakery', 'Pantry', 'Beverage', 'Toiletries']
        self.item_cbox = self.newCtkComboBox(options=self.item_cboxOptions, entryVariable = self.item_cboxVar)
        self.item_cbox.place(x=17.5, y=540)

        #allergen
        self.allergen_label = self.newCtkLabel('Allergen')
        self.allergen_label.place(x=365, y=500)
        self.allergen_cboxVar = StringVar()
        self.allergen_cboxOptions = ['None', 'Milk', 'Eggs', 'Nuts', 'Soy', 'Gluten', 'Seafood']
        self.allergen_cbox = self.newCtkComboBox(options=self.allergen_cboxOptions, entryVariable = self.allergen_cboxVar)
        self.allergen_cbox.place(x=285, y=540)

        #name
        self.name_label = self.newCtkLabel('Name')
        self.name_label.place(x=645, y=500)
        self.name_entry = self.newCtkEntry()
        self.name_entry.place(x=552.5, y=540)

        #quantity
        self.quantity_label = self.newCtkLabel('Quantity')
        self.quantity_label.place(x=895, y=500)
        self.quantity_entry = self.newCtkEntry()
        self.quantity_entry.place(x=820, y=540)

        #price
        self.price_label = self.newCtkLabel('Price')
        self.price_label.place(x=1180, y=500)
        self.price_entry = self.newCtkEntry()
        self.price_entry.place(x=1087.5, y=540)


        self.add_button = self.newCtkButton(text='Add Grocery Item', onClickHandler=self.add_entry, fgColor='#56733c', hoverColor='#3b5722', borderColor='#56733c')
        self.add_button.place(x=17.5, y=600)

        self.new_button = self.newCtkButton(text='New Grocery Item', onClickHandler=lambda:self.clear_form(True))
        self.new_button.place(x=357.5, y=600)

        self.update_button = self.newCtkButton(text='Update Grocery Item', onClickHandler=self.update_entry)
        self.update_button.place(x=357.5,y=650)

        self.delete_button = self.newCtkButton(text='Remove Grocery Item', onClickHandler=self.delete_entry, fgColor='#90261c', hoverColor='#69170f', borderColor='#90261c')
        self.delete_button.place(x=17.5,y=650)

        self.export_button = self.newCtkButton(text='Export to CSV', onClickHandler=self.export_to_csv)
        self.export_button.place(x=697.5,y=600)

        self.export_button = self.newCtkButton(text='Export to JSON', onClickHandler=self.export_to_json)
        self.export_button.place(x=697.5,y=650)

        self.export_button = self.newCtkButton(text='Import CSV file', onClickHandler=self.import_csv_file)
        self.export_button.place(x=1037,y=625)

        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Treeview', font=self.font2, foreground='#ad4132', background='#f4ab2e', fieldbackground='#fdd0aa')
        
        self.style.map('Treeview', background=[('selected', '#56733c')])

        self.tree = ttk.Treeview(self, height=15)
        self.tree['columns'] = ('Item', 'Allergen', 'Name', 'Quantity', 'Price')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('Item', anchor=tk.CENTER, width=165)
        self.tree.column('Allergen', anchor=tk.CENTER, width=165)
        self.tree.column('Name', anchor=tk.CENTER, width=660)
        self.tree.column('Quantity', anchor=tk.CENTER, width=165)
        self.tree.column('Price', anchor=tk.CENTER, width=165)

        self.tree.heading('Item', text='Item')
        self.tree.heading('Allergen', text='Allergen')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')

        self.tree.place(x=17.5, y=20, width=1320, height=450)
        self.tree.bind('<ButtonRelease>', self.read_display_data)

        self.add_to_treeview()

    def newCtkLabel(self, text ='CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#725054'
        widget_BgColor='#D7C18F'

        widget = customtkinter.CTkLabel(self, text=text, font=widget_Font, text_color=widget_TextColor, bg_color=widget_BgColor)
        return widget
    
    def newCtkEntry(self, text = 'CTK Label'):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#e1af9f'
        widget_BorderColor='#a77c82'
        widget_BorderWidth=2
        widget_Width=250

        widget = customtkinter.CTkEntry(self,
                                    font=widget_Font,
                                    text_color=widget_TextColor,
                                    fg_color=widget_FgColor,
                                    border_color=widget_BorderColor,
                                    border_width=widget_BorderWidth,
                                    width=widget_Width)
        return widget
    
    def newCtkComboBox(self, options=['DEFAULT', 'OTHER'], entryVariable=None):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor='#e1af9f'
        widget_DropdownHoverColor='#56733c'
        widget_ButtonColor='#a77c82'
        widget_ButtonHoverColor='#fbcad1'
        widget_BorderColor='#a77c82'
        widget_BorderWidth=2
        widget_Width=250
        widget_Options=options

        widget = customtkinter.CTkComboBox(self,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        border_color=widget_BorderColor,
                                        width=widget_Width,
                                        variable=entryVariable,
                                        values=options,
                                        state='readonly')
        
        widget.set(options[0])
        return widget
    
    def newCtkButton(self, text = 'CTK Button', onClickHandler=None, fgColor='#9db9d1', hoverColor='#3b5884', bgColor='#D7C18F', borderColor='#0b1f3d'):
        widget_Font=self.font1
        widget_TextColor='#000'
        widget_FgColor=fgColor
        widget_HoverColor=hoverColor
        widget_BackgroundColor=bgColor
        widget_BorderColor=borderColor
        widget_BorderWidth=2
        widget_Cursor='hand2'
        widget_CornerRadius=15
        widget_Width=300
        widget_Function=onClickHandler

        widget = customtkinter.CTkButton(self,
                                        text=text,
                                        command=widget_Function,
                                        font=widget_Font,
                                        text_color=widget_TextColor,
                                        fg_color=widget_FgColor,
                                        hover_color=widget_HoverColor,
                                        bg_color=widget_BackgroundColor,
                                        border_color=widget_BorderColor,
                                        border_width=widget_BorderWidth,
                                        cursor=widget_Cursor,
                                        corner_radius=widget_CornerRadius,
                                        width=widget_Width)
       
        return widget
    
    def add_to_treeview(self):
        grocerylist = self.db.get_grocery_list()
        self.tree.delete(*self.tree.get_children())
        for grocery in grocerylist:
            print(grocery)
            self.tree.insert('', END, values=grocery)

    def clear_form(self, *clicked):
        if clicked:
            self.tree.selection_remove(self.tree.focus())
            self.tree.focus('')
        self.item_cboxVar.set('Produce')
        self.allergen_cboxVar.set('Soy')
        self.name_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.price_entry.delete(0, END)

    def read_display_data (self, event):
        selected_name = self.tree.focus()
        if selected_name:
            row = self.tree.item(selected_name)['values']
            self.clear_form()
            self.item_cboxVar.set(row[0])
            self.allergen_cboxVar.set(row[1])
            self.name_entry.insert(0, row[2])
            self.quantity_entry.insert(0, row[3])
            self.price_entry.insert(0, row[4])
        else:
            pass

    def add_entry(self):
        item = self.item_cboxVar.get()
        allergen = self.allergen_cboxVar.get()
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()

        if not (item and allergen and name and quantity and price):
            messagebox.showerror('Error', 'Enter all fields.')
        elif self.db.name_exists(name):
            messagebox.showerror('Error', 'Item already exists')
        else:
            self.db.insert_grocery(item, allergen, name, quantity, price)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Item has been added')

    def delete_entry(self):
        selected_name = self.tree.focus()
        if not selected_name:
            messagebox.showerror('Error', 'Choose an item to remove')
        else:
            name = self.name_entry.get()
            self.db.delete_grocery(name)
            self.add_to_treeview()
            self.clear_form()
            messagebox.showinfo('Success', 'Item was removed from the list')

    def update_entry(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showerror('Error', 'Choose an item to update')
        else:
            row_id = self.tree.index(selected_item)
            item = self.item_cboxVar.get()
            allergen = self.allergen_cboxVar.get()
            name = self.name_entry.get()
            quantity = self.quantity_entry.get()
            price = self.price_entry.get()

        
            selected_name = self.tree.item(selected_item)['values'][2]
            self.db.update_grocery(selected_name, item, allergen, quantity, price)
            self.tree.item(selected_item, values=(item, allergen, name, quantity, price))
            self.clear_form()
            messagebox.showinfo('Success', 'Grocery has been updated')

    def export_to_json(self):
        self.db.export_json()
        messagebox.showinfo('Success', f'Data exported to GroceryDb.json')

    def export_to_csv(self):
        self.db.export_csv()
        messagebox.showinfo('Success', f'Data exported to GroceryDb.csv')

    def import_csv_file(self):
        self.db.import_csv()
        self.add_to_treeview()
        messagebox.showinfo('Success', f'Data was imported from ImportGroceryDb.csv')
        

