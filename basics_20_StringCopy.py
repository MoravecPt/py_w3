def larger_string (str, n):
    result = ""
    for i in range (n):
        result = result + str
    return result

print(larger_string('abc',2))
print(larger_string('testik',5))
print(larger_string('.py',3))

#pomoci fce si definuju ze chci zadat nejaky text a kolikrat se ma opakovat, přes for cyklus pak přidávám do resultu požadovaný počet opakování
