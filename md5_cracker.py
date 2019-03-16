import hashlib
import time

counter = 1

md5_pass = input('Enter the MD5 hash : ')
md5_file = input('Enter your wordlist file location : ')

o_time = time.time()

try:
    md5_file = open(md5_file, "r")

except:
    print("[!] Couldn't find such file!")
    quit()

for password in md5_file:
    hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    print("[%d] Trying password : %s " % (counter, password.strip()))
    counter += 1
    c_time = time.time()

    if hash_obj == md5_pass:
        t_time = c_time - o_time
        print("\n[+] Password Found : %s" % password)
        print("[time] ", t_time, "s")
        break

else:
    print("\n[-] Password Not Found")
    print("[time] ", t_time, "s")
