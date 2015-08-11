#Code that uses matplotlib to generate a jpeg image, which serves as an example of embedding
#an image in email
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

plt.fill(x, y, 'r')
plt.grid(True)

plt.savefig("C:/Users/Yifeng/Desktop/matplotlib_image.jpeg")
#====================================================================================================

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

me = "songyifn@gmail.com" # sender's email address
you = "songyifn@gmail.com" # you == recipient's email address

# Create an instance of the class MIMEMultipart which contains all of the contents of the email
# - the MIME type can be multipart or alternative.
msg = MIMEMultipart('multipart') #this main instance contains all of the other sub-instances
msg['Subject'] = "Email sent via Python" #Title of the email
msg['From'] = me
msg['To'] = you

n=5 # The number of text lines that need to be added (this is just an example!)
list_of_lines=["Here is the link{} you want.".format(str(i)) for i in range(1,6)]
# list_of_websites will be used in the hyperlinks
list_of_websites=["http://www.python.org","http://www.virginia.edu",\
"http://www.google.com","http://www.facebook.com","http://www.gmail.com"]

'''Create the body of the email (the HTML scripts).'''
#Add 5 lines of texts which are all hyperlinks
for i in range(5):
    #use triple quotation marks for the string which is to be converted into html format
    html="""<p>"""+\
         """
         <a href=\"{0}\">{1}</a>
         </p>
         """.format(list_of_websites[i],list_of_lines[i])
    msg_sub = MIMEMultipart('alternative') #creat a sub-instance which contains one line of texts
    msg.attach(msg_sub) #attach this sub-instance to the main instance msg
    msg_sub.attach(MIMEText(html, 'html')) #attach the html text to the sub-instance

#Embed an image in the email body
# Open the image file saved in previous steps, and bind it to a variable (Image)
fp = open('matplotlib_image.jpeg', 'rb')
Image = MIMEImage(fp.read())
fp.close()

msg_img = MIMEMultipart('alternative') #this instance is also a sub-instance of msg; it will contain the image and its title
msg.attach(msg_img) #attach this image sub-instance to the main instance

image_title = MIMEText('<p><b><i>"The title of the image"</i><b></p><br><img src="cid:image1"><br>', 'html')
msg_img.attach(image_title) #attach image title to the sub-instance

#assign the Content-ID "image1" to the Image, which will map it to the html code in the image_title ("cid:image1")
Image.add_header("Content-ID","<image1>") 
msg_img.attach(Image) #attach the actual Image to the sub-instance

# Send the email message via SMTP server of Gmail (587 is the unique code for Gmail).
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()
mail.starttls()

mail.login('songyifn@gmail.com','*********') #for Gmail, username for login should be the entire email address
mail.sendmail(me, you, msg.as_string())
mail.quit()