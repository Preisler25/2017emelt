class Members:
    def __init__(self, list):
        self.rounds = list[0:-1]
        self.name = list[-1]        

def ImportFromTxt():
    temp = []
    f = open("egyszamjatek.txt", "r").read()
    lines = f.split("\n")
    for i in lines:
        temp.append(Members(i.split(" ")))
    return temp

def ötödik(list):
    for i in range(len(list)):
        if list[i].rounds[0] == "1":
            return "volt"
    return "nem volt"

def hatodik(list):
    temp = 0
    for i in range(len(list)):
        for j in range(len(list[i].rounds)):
            if int(list[i].rounds[j]) > temp:
                temp = int(list[i].rounds[j])
    return temp

def hetedik(max):
    temp = 0
    temp_inp = int(input())
    if temp_inp <= max and temp_inp > 0:
        temp = temp_inp-1
    return temp

def findAll(list, round):
    temp = []
    for i in range(len(list)):
        if int(list[i].rounds[round]) not in temp:
            temp.append([int(list[i].rounds[round]) , 0, 0])
    return temp

def findWinner(list, round):
    temp_num = 100
    id_winner = len(list)
    temp = findAll(list, round)

    for j in range(len(temp)):
        for i in range(len(list)):
            if temp[j][0] == int(list[i].rounds[round]):
                temp[j][1] += 1
                temp[j][2] = i

    for i in range(len(temp)):
        if temp[i][0] < temp_num and temp[i][1] == 1:
            temp_num = temp[i][0]
            id_winner = temp[i][2]
    
    return id_winner

def nyolcadik(list, round):
    id_winner = findWinner(list, round)
    if id_winner == len(list):
        return "Nem volt egyedi tipp a megadott fordulóban!"
    return f"A nyertes tipp a megadott fordulóban: {list[id_winner].rounds[round]}"
    
def kilencedik(list, round):
    id_winner = findWinner(list, round)
    if id_winner == len(list):
        return "Nem volt nyertes a megadott fordulóban!"
    return f"A megadott forduló nyertese: {list[id_winner].name}"

def tizedik(list, round):
    id_winner = findWinner(list, round)
    if id_winner != len(list):
        f = open('nyertes.txt', 'w', encoding='UTF8')
        f.write(f"Forduló sorszáma: {round}\nNyertes szám: {list[id_winner].rounds[round]}\nNyertes játékos: {list[id_winner].name}")

def main(): 
    main_list = ImportFromTxt()
    print(f"3. feladat: Játékosok száma: {len(main_list)}")
    print(f"4. feladat: Fordulók száma: {len(main_list[0].rounds)}")
    print(f"5. feladat: Az első fordulóban {ötödik(main_list)} egyes tipp")
    print(f"6. feladat: A legnagyobb tipp a fordulók során: {hatodik(main_list)}")
    print(f"7. feladat: A forduló sorszámát [1-{len(main_list[0].rounds)}]:", end=" ")
    user_round = hetedik(len(main_list[0].rounds))
    print(f"8. feladat: {nyolcadik(main_list, user_round)}")
    print(f"9. feladat: {kilencedik(main_list, user_round)}")
    tizedik(main_list, user_round)
main()