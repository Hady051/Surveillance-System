import yagmail

password = ''

with open("/home/pi/.local/share/.email password", "r") as f:
    password = f.read()

# Simple Mail Transfer Protocol

yag = yagmail.SMTP('melonpi037@gmail.com', password)

yag.send(to = 'hadyfayez1@gmail.com',
         subject = 'first email',
         contents = 'Hello from Raspberry Pi \n to the mooooooon',
         attachments = '/home/pi/Pictures/b.jpg')

print('email sent')