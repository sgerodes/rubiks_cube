from rubiks_cube import *

def test(cube):
    cube.set_element('F',0,'V')
    cube.set_element('B',0,'M')
    cube.set_element('U',6,'0')
    cube.set_element('U',7,'1')
    cube.set_element('U',8,'2')
    cube.set_element('R',0,'3')
    cube.set_element('R',3,'4')
    cube.set_element('R',6,'5')
    cube.set_element('D',0,'8')
    cube.set_element('D',1,'7')
    cube.set_element('D',2,'6')
    cube.set_element('L',8,'9')
    cube.set_element('L',5,'X')
    cube.set_element('L',2,'I')
    
scramble1="U2  R  D'  L  B  L'  U  D  R  F'  R  F2  U'  R  F'  D2  F  B  D  U  L2  D2  R2  F  L'"
#cube=Cube(scramble1)
cube=Rubiks_Cube();print(cube)
#test(cube)
turn="R";cube.rotate(turn);print(cube)






