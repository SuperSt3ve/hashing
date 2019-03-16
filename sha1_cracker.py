import hashlib
import time

counter = 1

sha1_pass = input('Enter the SHA1 hash : ')
sha1_file = input('Enter your wordlist file location : ')

try:
    sha1_file = open(sha1_file, 'r')

except:
    print("Couldn't find such file!")
    quit()

for password in sha1_file:
    hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    print("[%d] Trying password : %s " % (counter, password.strip()))
    counter += 1
    t_time = time.time()

    if hash_obj == sha1_pass:
        print("\n[password] %s" % password)
        print("[time] ", t_time, "s")
        break

else:
    print("\n[password] Not found")
    print("[time] ", t_time, "s")
