import smtplib
import imaplib
import email
<<<<<<< HEAD
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret_key"
=======
import os
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = os.urandom(24)
>>>>>>> 1ca7e381aa082206b13be333f4ddffbcbf516709

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    gmail_user = request.form['gmail_user']
    gmail_pass = request.form['gmail_pass']

    try:
        # Autentikasi SMTP (untuk mengirim email)
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.starttls()
        smtp_obj.login(gmail_user, gmail_pass)

        # Autentikasi IMAP (untuk membaca email)
        imap_obj = imaplib.IMAP4_SSL('imap.gmail.com')
        imap_obj.login(gmail_user, gmail_pass)

        # Simpan informasi autentikasi ke dalam sesi
        session['gmail_user'] = gmail_user
        session['gmail_pass'] = gmail_pass

        return render_template('home.html')

    except smtplib.SMTPAuthenticationError:
        # Tampilkan pesan error jika autentikasi gagal
        return render_template('login.html', error="Login gagal! Email atau password salah.")

@app.route('/received_emails')
def received_emails():
    try:
        gmail_user = session.get('gmail_user')
        gmail_pass = session.get('gmail_pass')

        if not gmail_user or not gmail_pass:
            return render_template('error.html', error_message="Please login to access emails.")

        # Mengakses email menggunakan IMAP
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(gmail_user, gmail_pass)
        mail.select('inbox')

        # Mencari semua email dalam kotak masuk
        result, data = mail.search(None, 'ALL')
        email_ids = data[0].split()
        email_ids = list(reversed(email_ids))  # Membalik urutan email_ids

        email_content = []  # Memindahkan inisialisasi list di luar loop

        if email_ids:
            for email_id in email_ids:
                result, data = mail.fetch(email_id, '(RFC822)')
                raw_email = data[0][1]

                # Parsing email
                email_message = email.message_from_bytes(raw_email)

                # Mendapatkan informasi pengirim
                from_address = email.utils.parseaddr(email_message['From'])[1]

                # Menampilkan informasi email
                email_info = {
                    'From': from_address,
                    'To': email_message['To'],
                    'Subject': email_message['Subject'],
                    'Body': ''
                }

                # Mengekstrak isi pesan
                if email_message.is_multipart():
                    for part in email_message.walk():
                        content_type = part.get_content_type()
                        if content_type == 'text/plain':
                            body = part.get_payload(decode=True).decode()
                            email_info['Body'] = body
                else:
                    body = email_message.get_payload(decode=True).decode()
                    email_info['Body'] = body

                email_content.append(email_info)

            mail.close()
            mail.logout()

            return render_template('received_emails.html', emails=email_content)
        else:
            mail.close()
            mail.logout()
            return render_template('received_emails.html', emails=[])
    except Exception as e:
        return render_template('error.html', error_message=f"Error: {e}")

@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        # Mengambil informasi pengguna dari session
        gmail_user = session.get('gmail_user')
        gmail_pass = session.get('gmail_pass')

        if not gmail_user or not gmail_pass:
            # Jika pengguna belum login, tampilkan pesan kesalahan
            return render_template('error.html', error_message="Please login to send emails.")

        # Mengambil informasi dari formulir yang dikirimkan pengguna
        sent_from = gmail_user
        sent_to = request.form['sent_to']
        sent_subject = request.form['sent_subject']
        sent_body = request.form['sent_body']

        # Membuat objek email_message dan mengatur pengirim, penerima, subjek, dan isi email
        email_message = email.message.EmailMessage()
        email_message['From'] = sent_from
        email_message['To'] = sent_to
        email_message['Subject'] = sent_subject
        email_message.set_content(sent_body)

        try:
            # Mengirim email menggunakan server SMTP Gmail
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_pass)
            server.send_message(email_message)
            server.quit()

            # Jika email berhasil dikirim, render template success.html
            return render_template('success.html')
        except Exception as exception:
            # Jika terjadi kesalahan saat mengirim email, tampilkan pesan kesalahan
            error_message = str(exception)
            return render_template('error.html', error_message=error_message)

    # Metode GET untuk mengakses halaman formulir
    return render_template('send_email.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
