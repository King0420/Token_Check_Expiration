import jwt
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta


def get_expiration_and_issued_at():
    token = token_entry.get()

    try:
        decoded_payload = jwt.decode(token, options={"verify_signature": False})
        expiration_timestamp = decoded_payload['exp']
        expiration_datetime = datetime.fromtimestamp(expiration_timestamp)

        issued_at_timestamp = decoded_payload['iat']
        issued_at_datetime = datetime.fromtimestamp(issued_at_timestamp)

        valid_duration = timedelta(seconds=expiration_timestamp - issued_at_timestamp)

        result_label.config(text=f'Token issued at: {issued_at_datetime}\nToken expiration: {expiration_datetime}\nValid duration: {valid_duration}')
    except Exception as e:
        result_label.config(text=f'Error: {str(e)}')


def center_window():
    app.update_idletasks()
    width = app.winfo_width()
    height = app.winfo_height()

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    app.geometry(f'{width}x{height}+{x}+{y}')


app = tk.Tk()
app.title("JWT Expiration, Issued At, and Valid Duration Checker")
app.geometry("500x180")  # Adjust the height here
app.resizable(False, False)

style = ttk.Style()
style.configure(".", font=("Helvetica", 12))

input_label = ttk.Label(app, text="Enter your JWT Token:")
input_label.grid(row=0, column=0, padx=(15, 0), pady=(15, 10), sticky=tk.W)

token_entry = ttk.Entry(app, width=60)
token_entry.grid(row=1, column=0, padx=(15, 15), pady=(0, 10))

check_button = ttk.Button(app, text="Check Expiration, Issued At, and Valid Duration", command=get_expiration_and_issued_at)
check_button.grid(row=2, column=0, pady=(0, 10))

result_label = ttk.Label(app, text="", justify=tk.LEFT)
result_label.grid(row=3, column=0, padx=(15, 15), pady=(0, 15), sticky=tk.W)

center_window()
app.mainloop()
