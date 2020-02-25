def near_thousand (n):
    return(abs(1000-n)<=100) or (abs(2000-n)<=100)

print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))
print(near_thousand(899))
print(near_thousand(-899))
print(near_thousand(-901))
print(near_thousand(900.1))

#zjistuju, jestli je rozdil cisel do stovky -> jestli je cislo pobliz jednoho tisice nebo dvou tisicu