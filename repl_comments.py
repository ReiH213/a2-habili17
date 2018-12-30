from hashlib import sha256

def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()



correctpassword_hash="544f75f0ad9e4d6da51d68fdf5299077f64284af4d50e9297af77cd78e494496"

comments=[]

while True:
    new_comment=input("Enter your comment:")
    entered_pass=input("Enter password:")
    entered_pass_hash=create_hash(entered_pass)
    if correctpassword_hash==entered_pass_hash:
        comments.append(new_comment)
        i=1
        print("Previously entered comments:")
        for comment in comments:
            print(i, ". ", comment)
            i=i+1
    else:
        print("I am sorry this is the wrong password")
        
    check=input("Do you want to add another comments:yes or no?")
    if check=="no":
        break
    else:
        continue