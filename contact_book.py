import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    """Add a new contact to the list."""
    name = name_entry.get()
    phone = phone_entry.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone})
        refresh_contacts()
        clear_fields()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Error", "Name and Phone are required!")


def refresh_contacts():
    """Refresh the contact list display."""
    contact_listbox.delete(0, tk.END)
    for idx, contact in enumerate(contacts, start=1):
        contact_listbox.insert(tk.END, f"{idx}. {contact['name']} | {contact['phone']}")


def view_contact():
    """View the details of a selected contact."""
    try:
        selected_index = contact_listbox.curselection()[0]
        contact = contacts[selected_index]
        messagebox.showinfo("Contact Details", f"Name: {contact['name']}\nPhone: {contact['phone']}")
    except IndexError:
        messagebox.showwarning("Error", "Please select a contact to view.")


def delete_contact():
    """Delete the selected contact."""
    try:
        selected_index = contact_listbox.curselection()[0]
        contacts.pop(selected_index)
        refresh_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    except IndexError:
        messagebox.showwarning("Error", "Please select a contact to delete.")


def clear_fields():
    """Clear the input fields."""
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  # Light blue background

tk.Label(root, text="Name:", bg="#f0f8ff", fg="#00008b", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Phone:", bg="#f0f8ff", fg="#00008b", font=("Arial", 12)).pack(pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack(pady=5)

tk.Button(root, text="Add Contact", command=add_contact, bg="#32cd32", fg="white", font=("Arial", 10)).pack(pady=10)
tk.Button(root, text="View Contact", command=view_contact, bg="#1e90ff", fg="white", font=("Arial", 10)).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="#ff4500", fg="white", font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="Contact List:", bg="#f0f8ff", fg="#00008b", font=("Arial", 12, "bold")).pack(pady=10)
contact_listbox = tk.Listbox(root, width=50, height=10, bg="#ffffff", fg="#000000", font=("Arial", 10))
contact_listbox.pack(pady=10)

root.mainloop()
