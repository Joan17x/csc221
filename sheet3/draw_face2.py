from gasp import *

begin_graphics()


def drawFace(x,y):
    Circle((x,y),40, color="blue")



    Circle((x-20,y), 5, color="blue")
    Circle((x+20,y), 5, color="blue")

    Line((x,y+10),(x-10,y-10))
    Line((x-10,y-10),(x+10,y-10))

    Arc((x,y), 30, 225, 315, color="red", filled=True)


    Arc((x-40,y), 10, 90,270)
    Arc((x+40,y), 10, -90, 100)

    Line((75, 420),(80, 425))
    Line((80, 425), (90, 425))
    Line((125, 420), (120, 425))
    Line((120, 425), (110, 425))
    

for row in range(8):
    for col in range(9):
        x = col *100
        y = row *100
        drawFace(x,y)
update_when('key_pressed') 
end_graphics()