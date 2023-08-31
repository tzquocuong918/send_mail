import requests
import json
import smtplib
from email.mime.text import MIMEText

url = "https://csc-morpheus.anycloud.vn/api/budgets/7"

headers = {
    "accept": "application/json",
    "authorization": "Bearer 8330d41c-ee15-4520-a856-5f54cd172e33"
}

response = requests.get(url, headers=headers, verify=False)

# Load JSON data from the response content
data = json.loads(response.text)

# Extract intervals
intervals = data['budget']['stats']['intervals']

# Email configuration
smtp_server = "smtp.elasticemail.com"
smtp_port = 2525
smtp_username = "cuong.dq@csc-jsc.com"
smtp_password = "600B2AF577D63965F480D97CB8ABF1D162FE"
sender_email = "cuong.dq@csc-jsc.com"
recipient_email = "tzquocuong918@gmail.com"

# Create a text version of the email body
email_body = ""
for interval in intervals:
    budget = interval['budget']
    cost = interval['cost']
    interval_name = interval['month']
    
    if cost > budget:
        alert_message = f"Alert: Cost ({cost}) is greater than Budget ({budget}) for interval {interval_name}\n"
        email_body += alert_message

# If there are alerts, send an email
if email_body:
    msg = MIMEText(email_body)
    msg['Subject'] = "Budget Alert"
    msg['From'] = sender_email
    msg['To'] = recipient_email
    
    # Establish a secure session with the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, [recipient_email], msg.as_string())

# Print the JSON response content
print("JSON response:")
print(response.text)


# import requests
# import json
# # import smtplib
# # from email.mime.text import MIMEText

# url = "https://csc-morpheus.anycloud.vn/api/credentials?max=25&offset=0&sort=name&direction=asc"


# headers = {
#     "accept": "application/json",
#     "authorization": "Bearer 8330d41c-ee15-4520-a856-5f54cd172e33"
# }

# response = requests.get(url, headers=headers, verify=False)

# data = json.loads(response.text)
# print("JSON response:")
# print(response.text)