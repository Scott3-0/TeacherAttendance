import imaplib

login = 'testingtester465@gmail.com'
password = ''

imap = imaplib.IMAP4_SSL("imap.gmail.com",995)
imap.login(login, password)
imap.starttls()
imap.select()
for num in data[0].split():
    typ, data = imap.fetch(num, '(RFC822)')
    print('Message %s\n%s\n' % (num, data[0][1]))
imap.close()
imap.logout()

input()
