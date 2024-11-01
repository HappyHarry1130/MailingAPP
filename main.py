import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Load the SendGrid API key from environment variables
sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

def send_email(message):
    # Create the email content
    msg = Mail(
        from_email=('codeexpert74@gmail.com', 'Hasan'),  # Set the sender's email and name
        to_emails=["kunda111222@gmail.com", "sean993993@gmail.com", "Andril.com@outlook.com", "firethunderbolt1991@gmail.com"],  # List of recipients
        subject="Hello World!",
        plain_text_content=message,
        html_content=f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>See our products!</title>
  <style>

    /* Your email styles here */
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>Hello World!</h1>
    </div>
    <div class="content">
      <h2>Dear, Michelle</h2>
      <p>We hope this email finds you well. We have some exciting news to share with you!</p>
      <img src="https://place-hold.it/600x275/666?text=Image+Placeholder!" alt="Placeholder image" width="600" height="275">
      <p>Here's a brief overview of what we want to tell you:</p>
      <p>We'd love to hear your thoughts on this. If you have any questions, please don't hesitate to reach out.</p>
      <a href="https://www.goo.com/learnmore" class="cta-button">Learn More</a>
    </div>
    <div class="footer">
      <p>© 2024 Your Company Name. All rights reserved.</p>
      <p>You're receiving this email because you signed up for our newsletter.</p>
      <p><a href="https://www.goo.com/unsubscribe">Unsubscribe</a> | <a href="https://www.goo.com">View in Browser</a></p>
    </div>
  </div>
</body>
</html>
"""
    )
    
    try:
        # Send the email and print the response status
        response = sg.send(msg)
        print(response.status_code)
        print(response.headers)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Call the function to send an email with a message
send_email("hello")