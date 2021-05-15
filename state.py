data_state=open("exercise.txt","r")
# print(file_data)
for i in range(15):
    c=data_state.readline()
    print(c)
    if "delhi" in c:
        delhi=open("delhi.txt","a")
        delhi.write(c)
    elif "shimla" in c:
        d=open("simla.txt","a")
        d.write(c)
    else:
        o=open("other.txt","a")
        o.write(c)

