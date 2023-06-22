# gmail_user = "tugas.smtplib@gmail.com"
# gmail_pass = "jpqvzhoqujptemlv"

# gmail_user = "tugas.imaplib@gmail.com"
# gmail_pass = "htqtgddtcxeyxvdo"

# pass_asli = "tugas1234"

# Tambahan untuk menyertakan lampiran jika ada
# if email_ids:
#     for email_id in email_ids:
#         # Mengambil data email dengan format RFC822
#         result, data = mail.fetch(email_id, '(RFC822)')
#         raw_email = data[0][1]

#         # Parsing email
#         email_message = email.message_from_bytes(raw_email)

#         # Menampilkan informasi email
#         email_info = {
#             'From': email_message['From'],
#             'To': email_message['To'],
#             'Subject': email_message['Subject'],
#             'Body': '',
#             'Attachments': []  # Inisialisasi daftar lampiran
#         }

#         # Mengekstrak isi pesan
#         if email_message.is_multipart():
#             for part in email_message.walk():
#                 content_type = part.get_content_type()
#                 if content_type == 'text/plain':
#                     body = part.get_payload(decode=True).decode()
#                     email_info['Body'] = body
#                 elif content_type.startswith('application/'):  # Memeriksa tipe konten lampiran
#                     attachment = {
#                         'Filename': part.get_filename(),  # Nama file lampiran
#                         'Data': part.get_payload(decode=True)  # Data lampiran
#                     }
#                     email_info['Attachments'].append(attachment)
#         else:
#             body = email_message.get_payload(decode=True).decode()
#             email_info['Body'] = body

#         email_content.append(email_info)

#     mail.close()
#     mail.logout()

#     return render_template('received_emails.html', emails=email_content)
# else:
#     mail.close()
#     mail.logout()
#     return render_template('received_emails.html', emails=[])
# except Exception as e:
#     return render_template('error.html', error_message=f"Error: {e}")


# <form action="/login" method="POST">
# action="/login" menentukan URL tujuan atau lokasi di mana data formulir akan dikirimkan saat formulir tersebut dikirimkan.
# method="POST" menentukan metode HTTP yang akan digunakan untuk mengirimkan data formulir. Dalam hal ini, data akan 
# dikirimkan menggunakan metode POST, yang berarti data tersebut akan dikirimkan secara tersembunyi dari tampilan pengguna.

# Kode ini akan dijalankan saat perubahan terjadi pada checkbox. Pada bagian ini, kode memeriksa apakah checkbox tersebut 
# diceklis atau tidak dengan menggunakan properti checked pada showPasswordCheckbox.
# Jika checkbox diceklis (showPasswordCheckbox.checked bernilai true), maka tipe input dari elemen 
# kata sandi (passwordInput) akan diubah menjadi "text". Hal ini akan membuat teks yang dimasukkan ke dalam input 
# kata sandi terlihat sebagai teks biasa.
# Jika checkbox tidak diceklis (showPasswordCheckbox.checked bernilai false), maka tipe input dari elemen kata sandi 
# (passwordInput) akan diubah menjadi "password". 

# id dan name
# Jadi, atribut id dan name memiliki peran yang berbeda dalam konteks ini. id digunakan untuk mengidentifikasi elemen secara 
# unik dalam dokumen HTML, sementara name digunakan untuk mengirimkan nilai input saat formulir dikirimkan ke server.

# metode fetch() dari objek mail dalam modul imaplib pada Python. Metode ini digunakan untuk mengambil pesan email tertentu dari 
# server IMAP berdasarkan ID pesan.

# SSL adalah protokol keamanan yang mengenkripsi komunikasi antara client dan server. Port yang digunakan adalah 465, 
# yang merupakan port default untuk koneksi SSL pada server SMTP Gmail.

# Enkripsi adalah proses mengubah atau melindungi data agar tidak dapat dibaca 
# atau dimengerti oleh pihak yang tidak berwenang. 

# Fungsi IMAP4_SSL adalah konstruktor (constructor) yang disediakan oleh modul imaplib pada Python. 
# Fungsi ini digunakan untuk membuat objek koneksi ke server IMAP melalui koneksi SSL (Secure Sockets Layer) atau TLS (Transport Layer Security).