"""Requirment -
qrcode libery
pillow libery"""

import qrcode

# taking upi id as input
upi_id = input("Enter your upi id = ")

# Defining the payment url based on the upi id and the payment app
# you can modify these urls based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# creat qr codes for each payment app
phonepe_url = qrcode.make(phonepe_url)
paytm_url = qrcode.make(paytm_url)
google_pay_url = qrcode.make(google_pay_url)

phonepe_url.save('phonepe_qr.png')
paytm_url.save('paytm_qr.png')
google_pay_url.save('google_pay_qr.png')
# display the qr code (you may need to install PIL/PILLOW library)
phonepe_url.show()
paytm_url.show()
google_pay_url.show()
