import hashlib

# File to check
file = r"C:\Users\tbmag\GitHub\PyClock\README.md"


# Open,close, read file and calculate MD5 on its contents
with open(file, 'rb') as file:
    data = file.read()

    md5 = hashlib.md5(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()


print(f"File's MD5 is:  {md5}")
print(f"File's SHA256 is: {sha256}")
print(f"File's SHA1 is: {sha1}")

