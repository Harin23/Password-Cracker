import hashlib

def crack_sha1_hash(hash, use_salts=False):
  with open('top-10000-passwords.txt', 'r') as passFile:
    if use_salts == False:
      for password in passFile:
        password=password.splitlines()[0]
        if hashlib.sha1(password.encode()).hexdigest() == hash:
          return(password)
      return('PASSWORD NOT IN DATABASE')
    else:
      with open('known-salts.txt', 'r') as saltsFile:
        for salt in saltsFile:
          salt = salt.splitlines()[0]
          for password in passFile:
            password=password.splitlines()[0]
            append = hashlib.sha1((password+salt).encode()).hexdigest()
            prepend = hashlib.sha1((salt+password).encode()).hexdigest()
            if append == hash or prepend == hash:
              return(password)
          passFile.seek(0)
      return('PASSWORD NOT IN DATABASE')
