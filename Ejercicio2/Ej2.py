
sol={""}

def bactracking(letters, string, tam):
    global sol
    for x in letters:
        string.append(x)
        #print(letters)
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
print(letters)
bactracking(letters,[],len(data))
print(*sorted(sol), sep=' ')
