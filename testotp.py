import random
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pytest
from unittest.mock import patch


# OTP Code Implementation (for testing)
def generate_otp(length=6):
    """Generates a random OTP with the specified length (4 to 8 digits)."""
    if length < 4 or length > 8:
        raise ValueError("OTP length must be between 4 and 8 digits.")
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def send_email(otp, recipient_email):
    """Sends the OTP to the recipient's email address."""
    # Replace with your email credentials
    sender_email = "sagurbhai420@gmail.com"
    sender_password = "mffu cjyk kvgp nywf"
    smtp_server = "smtp.gmail.com"  # Adjust for your email provider
    smtp_port = 587
    
    # Compose the email
    subject = "Your One-Time Password (OTP)"
    body = f"Your one-time password (OTP) is: {otp}"
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Encrypt the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"OTP sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def is_valid_email(email):
    """Validate email using regex."""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None


# Test Cases for OTP Functions
# Test OTP Generation
def test_generate_otp_valid_length():
    """Test OTP generation with valid length"""
    otp = generate_otp(6)
    assert len(otp) == 6
    assert otp.isdigit()  # OTP should be numeric


def test_generate_otp_invalid_length():
    """Test OTP generation with invalid length"""
    with pytest.raises(ValueError):
        generate_otp(3)  # Length should be between 4 and 8

    with pytest.raises(ValueError):
        generate_otp(9)  # Length should be between 4 and 8


# Test Email Validation
def test_is_valid_email_valid():
    """Test valid email addresses"""
    valid_email = "test@example.com"
    assert is_valid_email(valid_email) is True


def test_is_valid_email_invalid():
    """Test invalid email addresses"""
    invalid_emails = [
        "test@com",        # Missing domain part
        "test.com",        # Missing @ symbol
        "test@.com",       # Domain starts with dot
        "test@com.",       # Domain ends with dot
        "test@com.c",      # Invalid domain TLD
        "test@com@com.com" # Extra @ symbol
    ]
    
    for email in invalid_emails:
        assert is_valid_email(email) is False


# Test Email Sending (mocking the send_email function)
@patch("builtins.print")
@patch("otp.send_email")
def test_send_email(mock_send_email, mock_print):
    """Test send_email without actually sending an email."""
    mock_send_email.return_value = None  # Mocking the actual send_email function
    
    otp = "123456"
    email = "test@example.com"
    
    send_email(otp, email)  # Should not raise any exceptions
    
    # Check if the send_email function was called
    mock_send_email.assert_called_once_with(otp, email)
    mock_print.assert_any_call(f"OTP sent successfully to {email}")


# Test OTP Verification in `main`
@patch("otp.send_email")
@patch("builtins.input", side_effect=["test@example.com", "6", "123456", "123456"])
@patch("builtins.print")
def test_main(mock_input, mock_send_email, mock_print):
    """Test the main OTP verification flow."""
    mock_send_email.return_value = None  # Mock sending email
    
    # Call the main function, it should run through without errors
    import otp  # Import the main module
    otp.main()

    # Check if OTP was verified successfully
    mock_print.assert_any_call("OTP verified successfully.")


# Running the tests with pytest
if __name__ == "__main__":
    pytest.main()
