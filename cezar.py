print("Developer: Alireza Hasanzadeh.")
print("-"*20)
text = str(input("Enter your text: ")).lower()

splited = []
for letter in text:
    splited.append(letter)

while True:
    try:
        mode = int(input("[1]: Encode , [2]: Decode : "))
        if mode > 2 or mode < 1:
            print("Wrong!?")
            continue
        else:
            break
    except:
        print("Just select a number.")
        continue

if mode == 1:
    encoded = ""
    for letter in splited:
        if letter == " ":
            encoded = encoded + letter
        else:
            encoded = encoded + (chr(ord(letter) + 1))
    print(f"Encoded: {encoded}")
elif mode == 2:
    decoded = ""
    for letter in splited:
        if letter == " ":
            decoded = decoded + letter
        else:
            decoded = decoded + (chr(ord(letter) - 1))
    print(f"Decoded: {decoded}")
print("-"*20)
