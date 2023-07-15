#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

f = open("Input/Names/invited_names.txt", "r")
tfile = open("Input/Letters/starting_letter.txt")
txt = tfile.read()
for name in f.readlines():
    x = name.strip("\n")
    t = txt
    new_t = t.replace("[name]",x)
    with open(f"Output/ReadyToSend/{x}.txt", "w") as letter:
        letter.write(new_t)