import numpy as np
import pandas as pd
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from IPython.core.display import display, HTML

df = pd.DataFrame({'DATE': [1.458315, 1.576704, 1.629253, 1.6693310000000001, 1.705139, 1.740447, 1.77598, 1.812037, 1.85313, 1.9439849999999999],
          'PRIORITY': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],
          'ALERT_MESSAGE': [-0.0057090000000000005, -0.005122, -0.0047539999999999995, -0.003525, -0.003134, -0.0012230000000000001, -0.0017230000000000001, -0.002013, -0.001396, 0.005732]})

me = "deepakr6242@gmail.com"
you = "xxxxxx"

# Create message container - the correct MIME type is multipart/alternative.
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
password = "xxxxxx"
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you
def color(val):
    if val == 1 :
        color = 'red'
    if  val == 2:
        color= 'green'
    if val == 3:
        color= 'blue'
    if val==4:
        color='yellow'
    return 'background-color: %s' % color

df1 = df.style.applymap(color, subset=['PRIORITY']).hide_index().render()

html =  """\
<html>
  <head></head>
  <style> 
  table, th, td {{
        border: 1px solid black;
        border-collapse: collapse;
    }}
    
    h2 {{
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
    }}
    table {{ 
        margin-left: auto;
        margin-right: auto;
    }}
    table, th, td {{
        border: 1px solid black;
        border-collapse: collapse;
    }}
    th, td {{
        padding: 5px;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
    }}
    table tbody tr:hover {{
        background-color: #dddddd;
    }}
    .wide {{
        width: 90%; 
    }}
    </style>
  <body>
    {}
  </body>
</html>
""".format(df1)
 
x = display(HTML(html))
print('x is ',html)

context = ssl.create_default_context()

part1 = MIMEText(html, "html")
msg.attach(part1)


try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(me, password)
    server.sendmail(me, you,msg.as_string())
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
