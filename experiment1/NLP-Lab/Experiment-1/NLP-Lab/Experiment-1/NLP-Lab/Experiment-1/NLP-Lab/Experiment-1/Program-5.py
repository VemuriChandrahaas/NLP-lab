import re

text = input("Enter text: ")

words = re.findall(r"[A-Za-z]+", text)
numbers = re.findall(r"\d+", text)
emails = re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", text)
phones = re.findall(r"\b\d{10}\b", text)

print("Words:", words)
print("Numbers:", numbers)
print("Email IDs:", emails)
print("Phone Numbers:", phones)


# Output 1:
# Enter text: Contact: student@gmail.com
# Words: ['Contact', 'student', 'gmail', 'com']
# Numbers: []
# Email IDs: ['student@gmail.com']
# Phone Numbers: []
#
# Output 2:
# Enter text: Call 9876543210 or mail lab2026@scsvmv.ac.in
# Words: ['Call', 'or', 'mail', 'lab', 'scsvmv', 'ac', 'in']
# Numbers: ['9876543210', '2026']
# Email IDs: ['lab2026@scsvmv.ac.in']
# Phone Numbers: ['9876543210']
