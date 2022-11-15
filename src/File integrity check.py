import hashlib

# File to check
file = r"C:\Users\tbmag\GitHub\PyClock\README.md"

Expectedhash=input("insert expected md5, sha256 or sha1:")

# Open,close, read file and calculate MD5 on its contents
with open(file, 'rb') as file:
    data = file.read()

    md5 = hashlib.md5(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()

if Expectedhash == md5 or Expectedhash == sha256 or Expectedhash == sha1:
    print("The hash corresponds to the file")
else:
    print("The hash is wrong or the file is corrupted")