# Amazon-Price-Tracker
This tracker will keep a track of the price of an item of your choice. If the price drops below your base price, it will send you an alert through email.

### **Python libraries used:** BeautifulSoup and smtplib

Some of the challenges I faced:
* ```smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted)``` : Earlier to solve this you could enable 'less secure apps' in your gmail settings. But Google has now changed its policy and as of 30th May 2022 you cannot use less secure apps to send emails without generating App password. You can follow the steps [here](https://support.google.com/mail/answer/185833?hl=en-GB) on how to generate an App password.
