from PIL import Image
import random
end = 100

def show_board():
    img = Image.open("/Users/aryanmandhana/Desktop/python nptel/i984_pimgpsh_fullsize_distr.webp")
    img.show()

def check_ladder(points):
    if points == 8:
        print("Ladder")
        return 26
    elif points == 21:
        print("Ladder")
        return 82
    elif points == 43:
        print("Ladder")
        return 77
    elif points == 50:
        print("Ladder")
        return 91
    elif points == 54:
        print("Ladder")
        return 93
    elif points == 62:
        print("Ladder")
        return 96
    elif points == 66:
        print("Ladder")
        return 87
    elif points == 80:
        print("Ladder")
        return 99
    else:
        return points
    
def check_snakes(points):
    if points == 44:
        print('snake')
        return 22
    elif points == 46:
        print('snake')
        return 5
    elif points == 48:
        print('snake')
        return 9
    elif points == 52:
        print('snake')
        return 11
    elif points == 59:
        print('snake')
        return 17
    elif points == 64:
        print('snake')
        return 36
    elif points == 69:
        print('snake')
        return 33
    elif points == 73:
        print('snake')
        return 1
    elif points == 83:
        print('snake')
        return 19
    elif points == 92:
        print('snake')
        return 51
    elif points == 95:
        print('snake')
        return 24
    elif points == 98:
        print('snake')
        return 28
    else:
        return points

def reached_end(points):
    if points == end:
        return True
    else:
        return False


show_board()
def play():
    p1_name = input("player 1, Please enter you name : ")
    p2_name = input("player 2, Please enter you name : ")
    pp1 = 0
    pp2 = 0

    turn = 0
    
    while(1):
        if turn%2 ==0:
            print("\n",p1_name,"\'s Turn\n")
            c = input("press 1 to continue and 0 to quit : ")
            if c==0:
                print(p1_name ,'scored : ', pp1)
                print(p2_name ,'scored : ', pp2)
                print("quitting the game")
                break
            dice = random.randint(1,6)
            print('you rolled a : '+ str(dice))

            pp1 = pp1+dice
            pp1 = check_ladder(pp1)
            pp1 = check_snakes(pp1)
            if pp1>end:
                pp1 = end

            print(p1_name, 'your score : ',pp1)
            if reached_end(pp1):
                print("Congratulations ",p1_name," You won!!!\n")
                break
        else:
            print("\n",p2_name,"\'s Turn\n")
            c = input("press 1 to continue and 0 to quit : ")
            if c==0:
                print(p1_name ,'scored : ', pp1)
                print(p2_name ,'scored : ', pp2)
                print("quitting the game")
                break
            dice = random.randint(1,6)
            print('you rolled a : '+str(dice))

            pp2 = pp2+dice
            pp2 = check_ladder(pp2)
            pp2 = check_snakes(pp2)
            if pp2>end:
                pp2 = end

            print(p2_name, 'your score : ',pp2)
            if reached_end(pp2):
                print("Congratulations ",p2_name," You won!!!\n")
                break
        turn = turn+1

show_board()
play()