import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from tkinterweb import HtmlFrame

content_texts = {}

def get_content(widget):
    if isinstance(widget, scrolledtext.ScrolledText) or isinstance(widget, tk.Text):
        return widget.get("1.0", tk.END).strip()
    else:
        return widget.get().strip()

def send_email():
    # Get the HTML content from the text area
    name = get_content(content_texts["Name"])
    subject_text = get_content(content_texts["Subject"])
    title = get_content(content_texts["Title"])
    main_content = get_content(content_texts["Content"])
    company_name = get_content(content_texts["Company"])

    # Create the email message
    message = Mail(
        from_email=('codeexpert74@gmail.com', 'Hasan'),
        to_emails=["kunda111222@gmail.com", "sean993993@gmail.com", "Andril.com@outlook.com", "firethunderbolt1991@gmail.com"],
        subject=subject_text,
        html_content=f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{subject_text}</title>
  <style>

    /* Your email styles here */
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>{title}</h1>
    </div>
    <div class="content">
      <h2>Dear, {name}</h2>
      {main_content}
    </div>
    <div class="footer">
      <p>© 2024 {company_name}. All rights reserved.</p>
      <p>You're receiving this email because you signed up for our newsletter.</p>
      <p><a href="https://www.salesup.com/unsubscribe">Unsubscribe</a> | <a href="https://www.salesup.com">View in Browser</a></p>
    </div>
  </div>
</body>
</html>
"""
    )

    try:
        sg = SendGridAPIClient("")
        response = sg.send(message)
        messagebox.showinfo("Success", f"Email sent successfully! Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

def preview():
    name = get_content(content_texts["Name"])
    subject_text = get_content(content_texts["Subject"])
    title = get_content(content_texts["Title"])
    main_content = get_content(content_texts["Content"])
    company_name = get_content(content_texts["Company"])

    frame.load_html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>{subject_text}</title>
  <style>

    /* Your email styles here */
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>{title}</h1>
    </div>
    <div class="content">
      <h2>Dear, {name}</h2>
      {main_content}
    </div>
    <div class="footer">
      <p>© 2024 {company_name}. All rights reserved.</p>
      <p>You're receiving this email because you signed up for our newsletter.</p>
      <p><a href="https://www.salesup.com/unsubscribe">Unsubscribe</a> | <a href="https://www.salesup.com">View in Browser</a></p>
    </div>
  </div>
</body>
</html>
""")

def load_template():
    try:
        with open('template.html', 'r') as file:
            return file.read()
    except FileNotFoundError:
        messagebox.showwarning("Warning", "template.html file not found. Starting with empty content.")
        return ""
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load template: {str(e)}")
        return ""

root = tk.Tk()
root.title("Email Sender")
root.geometry("1200x800")

# Create main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create left frame for input fields
left_frame = ttk.Frame(main_frame, padding="10")
left_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create right frame for preview
right_frame = ttk.Frame(main_frame, padding="10")
right_frame.grid(column=1, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input fields
fields = [
    ("Name", 1),
    ("Subject", 1),
    ("Title", 1),
    ("Content", 10),
    ("Company", 1)
]



for i, (text, height) in enumerate(fields):
    ttk.Label(left_frame, text=text).grid(column=0, row=i*2, sticky=tk.W, pady=(10, 0))
    if text == "Content":
        content_texts[text] = scrolledtext.ScrolledText(left_frame, height=height, width=50)
    else:
        content_texts[text] = ttk.Entry(left_frame, width=50)
    content_texts[text].grid(column=0, row=i*2+1, sticky=(tk.W, tk.E), pady=(0, 10))

# Buttons
button_frame = ttk.Frame(left_frame)
button_frame.grid(column=0, row=len(fields)*2, pady=10)

send_button = ttk.Button(button_frame, text="Send Email", command=send_email)
send_button.grid(column=0, row=0, padx=5)

preview_button = ttk.Button(button_frame, text="Preview", command=preview)
preview_button.grid(column=1, row=0, padx=5)

# Preview frame
preview_label = ttk.Label(right_frame, text="Preview")
preview_label.pack(pady=(0, 10))

frame = HtmlFrame(right_frame)
frame.load_html("<h1>Email Preview</h1>")
frame.pack(fill="both", expand=True)

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
left_frame.columnconfigure(0, weight=1)
right_frame.columnconfigure(0, weight=1)
right_frame.rowconfigure(1, weight=1)

# Start the GUI event loop
root.mainloop()


# Create and pack the send button
send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack(pady=5)

preview_button = tk.Button(root, text="Preview", command=preview)
preview_button.pack(pady=5)

frame = HtmlFrame(root)
frame.load_html("<h1>Hello, World!</h1>")
frame.pack(fill="both", expand=True)

# Start the GUI event loop
root.mainloop()