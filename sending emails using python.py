import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

plt.fill(x, y, 'r')
plt.grid(True)

plt.savefig("C:/Users/Yifeng/Desktop/haha.jpeg")



from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

plot = figure()
plot.circle([1,2], [3,4],[4,1],[2,3])

htmlplot = file_html(plot, CDN, "my plot")



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

me = "songyifn@gmail.com" # me == my email address
you = "ys8mz@virginia.edu" # you == recipient's email address

# Create an instance of the class MIMEMultipart which contains all of the contents of the email
# - the MIME type can be multipart or alternative.
msg = MIMEMultipart('multipart') #msg will cover everything
msg['Subject'] = "Email sent via Python" #Title of the email
msg['From'] = me
msg['To'] = you

msg_sub = MIMEMultipart('multipart') #this instance contains all of the instance 
msg.attach(msg_sub)

# Create the body of the message (a plain-text and an HTML version).
text="How are you?"
html = """
  <html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">{}</a> you want.
    </p>
  </body>
  </html>
""".format("haha")
# Record the MIME types of both parts - text/plain and text/html.

part_txt = MIMEText(text, 'plain')
msg_sub.attach(part_txt)

part_html = MIMEText(html, 'html')
msg_sub.attach(part_html)

fp = open('haha.jpeg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

msg_sub = MIMEMultipart('multipart') #this instance contains all of the instance 
msg.attach(msg_sub)

part_txt=MIMEText(text,'plain')
msg_sub.attach(part_txt)

part_html = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
msg_sub.attach(part_html)

msgImage.add_header("Content-ID","<image1>")
msg_sub.attach(msgImage)

msg_sub = MIMEMultipart('multipart')
msg.attach(msg_sub) 

part4 = MIMEText(html, 'html')
msg_sub.attach(part4)


attachment1=MIMEText(htmlplot,'html')
attachment1.add_header('Content-Disposition', 'attachment; filename="new.html"')
msg.attach(attachment1)


# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.

# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('songyifn@gmail.com', 'wkj198991')
mail.sendmail(me, you, msg.as_string())
mail.quit()