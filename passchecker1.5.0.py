import hashlib
import requests

if __name__ == "__main__":
    rawpw = input("enter password:   ")
    pwhash = hashlib.sha1(rawpw.encode()).hexdigest().upper()
    hashprefix = pwhash[:5]
    hashsuffix = pwhash[5:]

    r = requests.get('https://api.pwnedpasswords.com/range/' + hashprefix)
    hasharray = r.text.splitlines()

    for hash in hasharray:
        if hash.split(":")[0] == hashsuffix:
            quit("You have been pwned: " + hash.split(":")[1] + " times")

    print("Good news — no pwnage found!")