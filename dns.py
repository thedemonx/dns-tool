import tkinter as tk
from tkinter import messagebox
import socket

def ip_solver():
    domain = entry.get()
    if domain:
        try:
            ip_address = socket.gethostbyname(domain)
            result_label.config(text=f"IP result for {domain}: {ip_address}")
        except socket.gaierror:
            messagebox.showerror("Error", "Invalid or unresolvable domain")
    else:
        messagebox.showerror("Error", "Please enter a valid domain")

root = tk.Tk()
root.title("DNS Tool")

domain_label = tk.Label(root, text="Enter your domain:")
domain_label.grid(row=1, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=1, column=1, padx=10, pady=10)

enter_button = tk.Button(root, text="Enter", command=ip_solver)
enter_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

credit_label = tk.Label(root, text="Revenant Leakers")
credit_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()