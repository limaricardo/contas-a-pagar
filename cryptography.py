
def encrypt(text):
  encrypted = ""
  for letter in text:
    if letter == " ":
      encrypted += " "
    else: 
      encrypted += chr(ord(letter) + 25)
  
  return encrypted


def decrypt(encrypted):
  decrypted = ""
  for letter in encrypted:
    if letter == " ":
      decrypted += " "
    else: 
      decrypted += chr(ord(letter) - 25)

  return decrypted


