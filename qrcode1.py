import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr_code():
    # Get user input from the entry box
    text = text_entry.get()
    if not text:
        messagebox.showerror("Error", "Please enter text or a URL!")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    # Save the image
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", f"QR Code saved to {file_path}")

        # Display the QR code in the GUI
        img.thumbnail((200, 200))  # Resize for displaying in the app
        img_display = ImageTk.PhotoImage(img)
        qr_label.config(image=img_display)
        qr_label.image = img_display

# Set up the main window
root = tk.Tk()
root.title("QR Code Generator")

# Set up input field
text_label = tk.Label(root, text="Enter text or URL:")
text_label.pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

# Label to display QR code image
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Run the application
root.mainloop()
