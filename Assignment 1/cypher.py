coded_message = "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"
spaceless_message = coded_message.replace(" ", "")
decrypted_message_attempt_1 = spaceless_message

encoded_message_length = len(spaceless_message)
english_letter_frequency = {"A": 0.0817, "B": 0.0150, "C": 0.0278, "D": 0.0425, "E": 0.1270, "F": 0.0223, "G": 0.0202, "H": 0.0609, "I": 0.0697, "J": 0.0015, "K": 0.0077, "L": 0.0403, "M": 0.0241, "N": 0.0675, "O": 0.0751, "P": 0.0193, "Q": 0.0010, "R": 0.0599, "S": 0.0633, "T": 0.0906, "U": 0.0276, "V": 0.0098, "W": 0.0236, "X": 0.0015, "Y": 0.0197, "Z": 0.0007}
english_letter_frequency_keys = list(english_letter_frequency.keys())
english_letter_frequency_values = list(english_letter_frequency.values())
english_letter_frequency_values_sorted = sorted(english_letter_frequency_values, reverse=True)
english_letter_frequency_keys_sorted = sorted(english_letter_frequency, key=english_letter_frequency.get, reverse=True)
encoded_message_frequency = {}
count = 0
while count < encoded_message_length:
    encoded_letter = spaceless_message[count]
    match encoded_letter:
         case "a":
            encoded_message_frequency["A"] = encoded_message_frequency.get("A", 0) + 1
         case "b":
            encoded_message_frequency["B"] = encoded_message_frequency.get("B", 0) + 1
         case "c":
            encoded_message_frequency["C"] = encoded_message_frequency.get("C", 0) + 1
         case "d":
            encoded_message_frequency["D"] = encoded_message_frequency.get("D", 0) + 1
         case "e":
            encoded_message_frequency["E"] = encoded_message_frequency.get("E", 0) + 1
         case "f":
            encoded_message_frequency["F"] = encoded_message_frequency.get("F", 0) + 1
         case "g":
            encoded_message_frequency["G"] = encoded_message_frequency.get("G", 0) + 1
         case "h":
            encoded_message_frequency["H"] = encoded_message_frequency.get("H", 0) + 1
         case "i":
            encoded_message_frequency["I"] = encoded_message_frequency.get("I", 0) + 1
         case "j":
            encoded_message_frequency["J"] = encoded_message_frequency.get("J", 0) + 1
         case "k":
            encoded_message_frequency["K"] = encoded_message_frequency.get("K", 0) + 1
         case "l":
            encoded_message_frequency["L"] = encoded_message_frequency.get("L", 0) + 1
         case "m":
            encoded_message_frequency["M"] = encoded_message_frequency.get("M", 0) + 1
         case "n":
            encoded_message_frequency["N"] = encoded_message_frequency.get("N", 0) + 1
         case "o":
            encoded_message_frequency["O"] = encoded_message_frequency.get("O", 0) + 1
         case "p":
            encoded_message_frequency["P"] = encoded_message_frequency.get("P", 0) + 1
         case "q":
            encoded_message_frequency["Q"] = encoded_message_frequency.get("Q", 0) + 1
         case "r":
            encoded_message_frequency["R"] = encoded_message_frequency.get("R", 0) + 1
         case "s":
            encoded_message_frequency["S"] = encoded_message_frequency.get("S", 0) + 1
         case "t":
            encoded_message_frequency["T"] = encoded_message_frequency.get("T", 0) + 1
         case "u":
            encoded_message_frequency["U"] = encoded_message_frequency.get("U", 0) + 1
         case "v":
            encoded_message_frequency["V"] = encoded_message_frequency.get("V", 0) + 1
         case "w":
            encoded_message_frequency["W"] = encoded_message_frequency.get("W", 0) + 1
         case "x":
            encoded_message_frequency["X"] = encoded_message_frequency.get("X", 0) + 1
         case "y": 
            encoded_message_frequency["Y"] = encoded_message_frequency.get("Y", 0) + 1
         case "z":
            encoded_message_frequency["Z"] = encoded_message_frequency.get("Z", 0) + 1
    count += 1

for key in list(encoded_message_frequency.keys()):
    new_value = encoded_message_frequency[key] / encoded_message_length
    new_value = round(new_value, 4)  
    encoded_message_frequency[key] = new_value  
encoded_message_frequency_keys_sorted = sorted(encoded_message_frequency, key=encoded_message_frequency.get, reverse=True)

for letter in spaceless_message:
    if letter == "r":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "E")
    elif letter == "b":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "T")
    elif letter == "m":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "A")
    elif letter == "k":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "O")
    elif letter == "j":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "I")
    elif letter == "w":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "N")
    elif letter == "i":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "S")
    elif letter == "p":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "H")
    elif letter == "u":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "R")
    elif letter == "d":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "D")
    elif letter == "h":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "L")
    elif letter == "v":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "C")
    elif letter == "x":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "U")
    elif letter == "y":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "M")
    elif letter == "n":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "W")
    elif letter == "s":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "F")
    elif letter == "t":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "G")
    elif letter == "l":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "Y")
    elif letter == "q":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "P")
    elif letter == "o":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "B")
    elif letter == "e": 
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "V")
    elif letter == "a":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "K")
    elif letter == "c":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "J")
    elif letter == "f":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "X")
    elif letter == "g":
        decrypted_message_attempt_1 = decrypted_message_attempt_1.replace(letter, "Q")
    else:
        print("something went wrong")
print(decrypted_message_attempt_1)
print("----------------------------------------------------------")
decrypted_message_attempt_2 = decrypted_message_attempt_1.replace("Y", "@")
decrypted_message_attempt_2 = decrypted_message_attempt_2.replace("B", "Y")
decrypted_message_attempt_2 = decrypted_message_attempt_2.replace("@", "B")
decrypted_message_attempt_2 = decrypted_message_attempt_2.replace("W", "@")
decrypted_message_attempt_2 = decrypted_message_attempt_2.replace("U", "W")
decrypted_message_attempt_2 = decrypted_message_attempt_2.replace("@", "U")
print(decrypted_message_attempt_2)
print("----------------------------------------------------------")
decrypted_message_attempt_3 = decrypted_message_attempt_2.replace("N", "@")
decrypted_message_attempt_3 = decrypted_message_attempt_3.replace("I", "N")
decrypted_message_attempt_3 = decrypted_message_attempt_3.replace("@", "I")
decrypted_message_attempt_3 = decrypted_message_attempt_3.replace("O", "@")
decrypted_message_attempt_3 = decrypted_message_attempt_3.replace("N", "O")
decrypted_message_attempt_3 = decrypted_message_attempt_3.replace("@", "N")
print(decrypted_message_attempt_3)
print("----------------------------------------------------------")
decrypted_message_attempt_4 = decrypted_message_attempt_3.replace("F", "@")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("P", "F")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("@", "P")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("J", "@")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("W", "J")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("@", "W")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("W", "@")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("F", "W")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("@", "F")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("I", "@")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("O", "I")
decrypted_message_attempt_4 = decrypted_message_attempt_4.replace("@", "O")
print(decrypted_message_attempt_4)
print("----------------------------------------------------------")
decrypted_message_attempt_5 = spaceless_message

for letter in spaceless_message:
    if letter == "r":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "E") # Done
    elif letter == "b":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "T") # Done
    elif letter == "m":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "A") # Done
    elif letter == "k":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "N") # Done
    elif letter == "j":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "O") # Done
    elif letter == "w":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "I") # Done
    elif letter == "i":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "S") # Done
    elif letter == "p":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "H") # Done
    elif letter == "u":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "R") # Done
    elif letter == "d":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "D")
    elif letter == "h":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "L")
    elif letter == "v":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "C") # Done
    elif letter == "x":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "F") # Done
    elif letter == "y":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "M") # Done
    elif letter == "n":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "U") # Done
    elif letter == "s":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "P") # Done
    elif letter == "t":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "G")
    elif letter == "l":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "B") # Done 
    elif letter == "q":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "D") # Done
    elif letter == "o":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "B")
    elif letter == "e": 
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "V") # Done
    elif letter == "a":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "K")
    elif letter == "c":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "J")
    elif letter == "f":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "X")
    elif letter == "g":
        decrypted_message_attempt_5 = decrypted_message_attempt_5.replace(letter, "Q")
    else:
        print("something went wrong")
print(decrypted_message_attempt_5)
print("----------------------------------------------------------")
decrypted_message_attempt_6 = spaceless_message

for letter in spaceless_message:
    if letter == "r":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "E") # Done
    elif letter == "b":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "T") # Done
    elif letter == "m":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "A") # Done
    elif letter == "k":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "N") # Done
    elif letter == "j":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "O") # Done
    elif letter == "w":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "I") # Done
    elif letter == "i":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "S") # Done
    elif letter == "p":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "H") # Done
    elif letter == "u":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "R") # Done
    elif letter == "d":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "D") # Done
    elif letter == "h":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "L") # Done
    elif letter == "v":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "C") # Done
    elif letter == "x":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "F") # Done
    elif letter == "y":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "M") # Done
    elif letter == "n":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "U") # Done
    elif letter == "s":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "P") # Done
    elif letter == "t":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "Y") # Done
    elif letter == "l":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "B") # Done 
    elif letter == "q":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "K") # Done
    elif letter == "o":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "G") # Done
    elif letter == "e": 
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "V") # Done
    elif letter == "a":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "X") # Done
    elif letter == "c":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "W") # Done
    elif letter == "f":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "Q") # Done
    elif letter == "g":
        decrypted_message_attempt_6 = decrypted_message_attempt_6.replace(letter, "Z") # Done
    else:
        print("something went wrong")
print(decrypted_message_attempt_6)
