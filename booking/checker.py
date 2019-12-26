f1 = open("models.py", "r")
count = 0
count2 = 0
print(f1.read(), end="")
for line in f1:
    for letter in line:
        if ord(letter) > 127:
            print("ALERT! at line", count,"character", count2, ":", letter )
        count2+=1
    count+=1
    