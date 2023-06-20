import smtplib
from tkinter import Text, Tk, Label, Entry, Button, messagebox

def send_email():
    gmail_user = gmail_entry.get()
    gmail_pass = password_entry.get()
    sent_to = to_entry.get()
    sent_subject = subject_entry.get()
    sent_body = body_entry.get("1.0", "end-1c")

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (gmail_user, sent_to, sent_subject, sent_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_pass)
        server.sendmail(gmail_user, sent_to, email_text)
        server.close()

        messagebox.showinfo("Email Sent", "Email berhasil dikirim!")
    except Exception as exception:
        messagebox.showerror("Error", f"Error: {exception}")

# Membuat jendela aplikasi menggunakan Tkinter
window = Tk()
window.title("Aplikasi Pengiriman Email")
window.geometry("400x300")

# Label dan Entry untuk akun Gmail
gmail_label = Label(window, text="Akun Gmail:")
gmail_label.pack()
gmail_entry = Entry(window, width=30)
gmail_entry.pack()

# Label dan Entry untuk password Gmail
password_label = Label(window, text="Password Gmail:")
password_label.pack()
password_entry = Entry(window, show="*", width=30)
password_entry.pack()

# Label dan Entry untuk penerima email
to_label = Label(window, text="Gmail Penerima:")
to_label.pack()
to_entry = Entry(window, width=30)
to_entry.pack()

# Label dan Entry untuk subjek email
subject_label = Label(window, text="Subject:")
subject_label.pack()
subject_entry = Entry(window, width=30)
subject_entry.pack()

# Label dan Entry untuk isi pesan email
body_label = Label(window, text="Pesan:")
body_label.pack()
body_entry = Text(window)
body_entry.pack()

# Tombol Kirim Email
send_button = Button(window, text="Kirim", command=send_email)
send_button.pack()

# Menjalankan aplikasi
window.mainloop()

    # gmail_user = "tugas.smtplib@gmail.com"
    # gmail_pass = "jpqvzhoqujptemlv"

        # gmail_user = "tugas.imaplib@gmail.com"
        # gmail_pass = "htqtgddtcxeyxvdo"