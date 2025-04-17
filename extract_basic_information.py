import re

# Input: A plain text sample of a resume
resume_text = """
Amin Veisi
Email: amin.veisi@example.com
Phone: +98-912-123-4567
Education: Master’s degree in Engineering at Amirkabir University of Technology
"""

# Function to extract name
def extract_name(resume_text):
    name_pattern = r"^[A-Z][a-z]+\s[A-Z][a-z]+"  # Match "First Last" with capitalization
    name = re.search(name_pattern, resume_text)
    return name.group(0) if name else "Name not found"

# Function to extract email address
def extract_email(resume_text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    email = re.search(email_pattern, resume_text)
    return email.group(0) if email else "Email not found"

# Function to extract phone number
def extract_phone(resume_text):
    phone_pattern = r"\+?\d{1,3}-?\d{3}-?\d{3}-?\d{4}"
    phone = re.search(phone_pattern, resume_text)
    return phone.group(0) if phone else "Phone not found"

# Extract details
name = extract_name(resume_text)
email = extract_email(resume_text)
phone = extract_phone(resume_text)

# Print extracted details
print("Extracted Information:")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
