import turtle
import math
import timeit
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze ing")
wn.setup(700,700)
wn.tracer(0)
gold = 0

f = open("PlayerInfo.txt", "a")


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(12)
        
class Player (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() -24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = player.xcor()-24
        move_to_y = player.ycor() 
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = player.xcor()+24
        move_to_y = player.ycor() 
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def is_collision(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+b**2)

        if distance<5:
            return True
        else:
            return False

class Player2 (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
    def go_up(self):
        move_to_x = player2.xcor()
        move_to_y = player2.ycor() + 24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player2.xcor()
        move_to_y = player2.ycor() -24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_left(self):
        move_to_x = player2.xcor()-24
        move_to_y = player2.ycor() 
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = player2.xcor()+24
        move_to_y = player2.ycor() 
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def is_collision(self,other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2)+b**2)

        if distance<5:
            return True
        else:
            return False
        
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

levels = [""]
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXXT XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX TX",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XXXXXXXXXX      2       X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXX    XXXXX",
    "XX     XXXXXXXXX    XXXXX",
    "XX        XXXX          X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X TXXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X    X    XXXXXXXXXXXXXXX",
    "XXX              XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXXX2XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XXXXXXXXXX    XXX  XX   X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXX    XXXXX",
    "XX     XXXXXXXXX    XXXXX",
    "XX        XXXX    XXX T X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XT XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX  P     XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X    X    XXXXXXXXXXXXXXX",
    "XXX              XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXXXXXXXXX  X",
    "XXX  XXXXXXXXXX       2 X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XXXXXXXXXX    XXXXXXX   X",
    "XXT  XXXXX              X",
    "XX   XXXXXXXXXXX    XXXXX",
    "XX     XXXXXXXXX    XXXXX",
    "XX        XXXX    XXX   X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_4 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XT XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX  P     XX",
    "XXXXXX  XX  XXX      XXXX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX  XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X    X    XXXXXXXXXXXXXXX",
    "XXX              XXXXXXXX",
    "XXXXXXXXXXXX     XXXXXT X",
    "XXXXXXXXXXXXXXXXXXXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX     XX       X",
    "XXXXXXXXXX    XXXXXXX   X",
    "XX  2XXXXX              X",
    "XX   XXXXXXXXXXX    XXXXX",
    "XX     XXXXXXXXX    XXXXX",
    "XX        XXXX    XXX   X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_5 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX    X   XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXX PXXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X              X XXXXXXXX",
    "XXXXXXXXXXXX   T XXXXX  X",
    "XXXXXXXXXXXXXXXXXXXXXX  X",
    "XXX  XXXXXXXXXX        XX",
    "XXX               XT    X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX      X       X",
    "XXXXXXXXXX      XXXXXX  X",
    "XX   XXXXX       X      X",
    "XX   XXXXXXXXXXX    XXXXX",
    "XX     XXXXXXXXX    XXXXX",
    "XX    2   XXXX          X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
level_6 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X   X   XX  XXXXX   XXXXX",
    "X      XXX  XXX    XX  XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX    XXX",
    "XXXXXX  XX    XXXX    XXX",
    "X  XXX        XXXX T  XXX",
    "X  XXX  XXXXXXXXXX    XXX",
    "X         XXXXXXXXXXXXXXX",
    "X    XXX       X XXXXXXXX",
    "XXXXXXXXXXXX   P XXXXX  X",
    "XX    XXXXXXXXXXXXXXXX  X",
    "XX T  XXXXXXXXX        XX",
    "XX    XXXX        X     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX      X2      X",
    "XXXXXXXXXX      XXXXXX  X",
    "XX   XXXXX       X      X",
    "XX   XXXXXXXXXXX    XXXXX",
    "XX     XXXXXXXXX    XXXXX",
    "XX        XXXX          X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]
treasures = []

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)
levels.append(level_6)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 +(x * 24)
            screen_y = 288 - (y *24)

            if character == "X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character == "P":
                player.goto(screen_x,screen_y)
            if character =="2":
                player2.goto(screen_x,screen_y)
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))
pen = Pen()
player = Player()
player2 = Player2()

walls = []
setup_maze(levels[1])

turtle.listen()
turtle.onkeypress(player.go_left,"a")
turtle.onkeypress(player.go_right,"d")
turtle.onkeypress(player.go_up,"w")
turtle.onkeypress(player.go_down,"s")

turtle.onkeypress(player2.go_left,"Left")
turtle.onkeypress(player2.go_right,"Right")
turtle.onkeypress(player2.go_up,"Up")
turtle.onkeypress(player2.go_down,"Down")
wn.tracer(0)

while True:
    start = timeit.timeit()
    for treasure in treasures:
        if player.is_collision(treasure):
            gold += 100
            print ("players Gold: {}".format(gold))
            treasure.destroy()
            treasures.remove(treasure)
            if gold == 200:
                end = timeit.timeit()
                setup_maze(levels[(2)])
                print(end-start)
                content = (end-start)
                f.write("players have completed level 1 ")
                f.write(str(content))
                start = timeit.timeit()
            if gold == 400:
                end = timeit.timeit()
                setup_maze(levels[(3)])
                print(end-start)
                content = (end-start)
                f.write("players have completed level 2")
                f.write(str(content))
                start = timeit.timeit()
            if gold == 600:
                end = timeit.timeit()
                setup_maze(levels[(4)]) 
                print(end-start)
                content = (end - start)
                f.write("players have completed level 3")
                f.write(str(content))
                start = timeit.timeit()
            if gold == 800:
                end = timeit.timeit()
                setup_maze(levels[(5)]) 
                print(end-start)
                content= (end-start)
                f.write("players have completed level 4 in ")
                f.write(str(content))
                start = timeit.timeit()
            if gold == 1000:
                end = timeit.timeit()
                setup_maze(levels[(6)])
                print(end-start)
                content = (end - start)
                f.write("players have completed level 5 in ")
                f.write(str(content))
                start = timeit.timeit()
            if gold == 1200:
                end = timeit.timeit()
                pen.goto(0,260)
                pen.clear()
                pen.write("Sorry no more levels" , align="center", font=("Courier", 20, "normal"))
                pen.hideturtle()
                f.write("players have completed level 6 in ")
                f.write("\n")
                f.close()
        if player2.is_collision(treasure):
            gold += 100
            print ("players Gold: {}".format(gold))
            treasure.destroy()
            treasures.remove(treasure)
            if gold == 200:
                end = timeit.timeit()
                setup_maze(levels[(2)])
                print(end-start)
                content = (end- start)
                f.write("players have completed level 1 in ")
                f.write(str(content))
                start = timeit.timeit()
            if gold == 400:
                end = timeit.timeit()
                setup_maze(levels[(3)]) 
                print(end-start)
                content = (end - start)
                f.write("players have completed level 2 in ")
                f.write(str(content))
                start = timeit.timeit() 
            if gold == 600:     
                end = timeit.timeit()
                setup_maze(levels[(4)]) 
                print(end-start)
                f.write("players have completed level 3 in ")
                start = timeit.timeit()
            if gold == 800:
                end = timeit.timeit()
                setup_maze(levels[(5)]) 
                print(end-start)
                content = (end - start)
                f.write("players have completed level 4 in ")
                f.write(content)
                start = timeit.timeit()
            if gold == 1000:
                end = timeit.timeit()
                setup_maze(levels[(6)])
                print(end-start)
                content = (end - start)
                f.write("players have completed level 5 in ")
                f.write(content)
                start = timeit.timeit()
            if gold == 1200:
                end = timeit.timeit()
                pen.goto(0,260)
                pen.clear()
                pen.write("Sorry no more levels" , align="center", font=("Courier", 20, "normal"))
                pen.hideturtle()
                content = (end - start)
                f.write("players have completed level 6 in ")
                f.write(content)
                f.write("\n")
                f.close()
    wn.update()