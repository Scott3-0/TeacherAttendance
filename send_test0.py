import outlook

mail = outlook.Outlook()
mail.login('testertesting465@gmail.com','Pps573551')
mail.sendEmail('bremmerscottw@gmail.com','subject','message body')
