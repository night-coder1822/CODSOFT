import tkinter as tk
from tkinter import messagebox

contacts = {}  # Dictionary to store contacts

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    
    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Name and phone are required fields.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, name)

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def view_contact(selected_contact):
    if selected_contact in contacts:
        contact_info = contacts[selected_contact]
        messagebox.showinfo("Contact Information", f"Name: {selected_contact}\nPhone: {contact_info['Phone']}\nEmail: {contact_info['Email']}\nAddress: {contact_info['Address']}")
    else:
        messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    selected_contact = contact_list.get(tk.ACTIVE)
    if selected_contact in contacts:
        del contacts[selected_contact]
        update_contact_list()
    else:
        messagebox.showerror("Error", "Contact not found.")

root = tk.Tk()
root.title("Contact Management System")

label_name = tk.Label(root, text="Name:")
label_phone = tk.Label(root, text="Phone:")
label_email = tk.Label(root, text="Email:")
label_address = tk.Label(root, text="Address:")

entry_name = tk.Entry(root)
entry_phone = tk.Entry(root)
entry_email = tk.Entry(root)
entry_address = tk.Entry(root)

button_add = tk.Button(root, text="Add Contact", command=add_contact)
button_view = tk.Button(root, text="View Contact", command=lambda: view_contact(contact_list.get(tk.ACTIVE)))
button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)

contact_list = tk.Listbox(root)
update_contact_list()

label_name.grid(row=0, column=0)
label_phone.grid(row=1, column=0)
label_email.grid(row=2, column=0)
label_address.grid(row=3, column=0)

entry_name.grid(row=0, column=1)
entry_phone.grid(row=1, column=1)
entry_email.grid(row=2, column=1)
entry_address.grid(row=3, column=1)

button_add.grid(row=4, column=0, columnspan=2)
button_view.grid(row=5, column=0, columnspan=2)
button_delete.grid(row=6, column=0, columnspan=2)

contact_list.grid(row=0, column=2, rowspan=7)

root.mainloop()
