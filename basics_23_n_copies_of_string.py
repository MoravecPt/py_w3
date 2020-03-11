def slovo(str, n):
    delka = 3
    if delka > len(str):
        delka = len(str)
    substr = str[:delka]

    result = ""
    for i in range(n):
        result = result + substr
    return result

print(slovo('Peta', 2));
print(slovo('abcd', 8));

#kdyz je delka slova kratsi nebo rovna podmince delky, beru celou delku slova, jinak do substr ulozim prave pozadovanou delku slova