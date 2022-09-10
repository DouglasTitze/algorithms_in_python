def ransom_note(magazine: str, note: str) -> bool:
    """Checks if the note can be writen using the words inside of the magazine.\n
    You can only use whole words from the magazine
    """
    mag_dic = {}
    note_dic = {}

    magazine = magazine.strip().split()
    note = note.strip().split()

    if len(magazine) < len(note):
        return False

    for word in magazine:
        mag_dic[word] = 1

    for word in note:
        note_dic[word] = 1

    for word in note_dic.keys():
        if mag_dic.get(word, 0):
            mag_dic[word] = 0
        else:
            return False

    return True


magazine = "Welcome to the bank where we just give money to everyone for free now"

print(ransom_note(magazine, "give me money now"))
print(ransom_note(magazine, "give the money now"))
