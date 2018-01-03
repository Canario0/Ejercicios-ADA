
sol={""}

def bactracking(letters, string, tam):
    global sol
    for x in letters:
        string.append(x)
        if len(string)==tam:
            sol.add(''.join(string))
        else:
            letters.remove(x)
            bactracking(letters.copy(), string.copy(), tam)
        letters.add(x)
        string.pop()




data= input("Introduzca una palabra: ")
data.upper()!=0
letters= set(data)
if(len(letters)< len(data)):
    print("Tiene letras repetidas.")
else:
    bactracking(letters,[],len(data))
    print(*sorted(sol), sep=' ')
