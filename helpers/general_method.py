import imaplib
import email
import traceback
import re
# FROM_PWD = "test1q2w3e4r"


class GeneralMethod:

    @staticmethod
    def read_last_email():
        try:
            mail = imaplib.IMAP4_SSL('imap.ukr.net')
            mail.login('smertrusni@ukr.net', 'HxFGJVU5dY6nAjb7')
            mail.list()
            mail.select("inbox")
            data = mail.search(None, 'ALL')
            ids = data[1]
            id_list = ids[0].split()
            __, data = mail.fetch(id_list[-1], "(RFC822)")
            return email.message_from_string(str(data[0][1], 'utf-8')).as_string()

        except Exception as e:
            traceback.print_exc()
            print(str(e))

    def get_email_code(self):
        msg = self.read_last_email()
        match = re.findall(r'>\d{2}-\d{2}<', msg)
        match = re.findall(r'\d{2}', match[0])
        return ''.join(match)
