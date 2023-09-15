import pyqrcode
import datetime
import os

current_date_time = datetime.datetime.now()
format_current_date_time = current_date_time.strftime("%Y%m%d_%H%M%S")

directory_path = ".\\generated_qr_codes"
file_name = f"{directory_path}\\qrcode_{format_current_date_time}.png"

os.makedirs(directory_path, exist_ok=True)

qr = pyqrcode.create(input("Enter the desired URL:\n"))
qr.png(file_name, scale=6)

print("-------------------------------")
print("QR Code Generated successfully.")
print("-------------------------------")
