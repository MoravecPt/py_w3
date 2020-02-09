color_list = ["Red","Green","White" ,"Black"]
print(color_list)
print( "%s %s"%(color_list[1],color_list[-3]))
print( "%s %s"%(color_list[0],color_list[-1]))

#pomoci %s rikam kolik vypisuju prvku, pak pres zavorku rikam, ktere to maji byt (kdyz predcislem je minus, beru poradi zprava, kdyz je tam plus jdu klasickytleva)
#viz to, ze na zelenou se dostanu jako %(color_list[1],color_list[-3]) -> jdu ze dvou smeru