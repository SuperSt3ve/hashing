import hashlib
import time

counter = 1

sha256_pass = input('Enter the SHA256 hash : ')
sha256_file = input('Enter your wordlist file location : ')

try:
    sha256_file = open(sha256_file, 'r')

except:
    print("Couldn't find such file!")
    quit()

for password in sha256_file:
    hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    print("[%d] Trying password : %s " % (counter, password.strip()))
    counter += 1
    t_time = time.time()

    if hash_obj == sha256_pass:
        print("\n[password] %s" % password)
        print("[time] ", t_time, "s")
        break

else:
    print("\n[password] Not found")
    print("[time] ", t_time, "s")
