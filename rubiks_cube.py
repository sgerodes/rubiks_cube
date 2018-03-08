class Rubiks_Cube:
    solved_cube=[['y']*9,['b']*9,['r']*9,['g']*9,['o']*9,['w']*9]
    orientation={'U':0,'L':1,'F':2,'R':3,'B':4,'D':5}

    front_table={'D':'X','R':'Y','U':"X'",'L':"Y'",'B':'X2'}
    unfront_table={'D':"X'",'R':"Y'",'U':"X",'L':"Y",'B':'X2'}
    double_turns={'f':'B Z', 'r':'L X', 'u':'D Y', 'l':"R X'", 'd':"U Y'", 'b':"F Z'"}
    double_turns.update({"f'":"B' Z'", "r'":"L' X'", "u'":"D' Y'", "l'":"R' X", "d'":"U' Y", "b'":"F' Z"})
    slice_turns={"M":"R' L X", "M'":"R L' X'", "E":"U D' Y'", "E'":"U' D Y", "S":"F B' Z'", "S'":"F' B Z"}
    possible_orientation='XYZ'
    possible_double_turns='fruldb'
    possible_slice_turns='MES'
    
    def __init__(self,*scramble):
        self.state=self.solved_cube
        if scramble:
            self.scramble_cube(scramble[0])
    

    def scramble_cube(self,s):
        for turn in s.split():
            self.rotate(turn)

    def get_state(self):
        return ''.join([''.join(face) for face in self.state])
    
    
    def rotate(self,turn):
        if turn[0] in self.possible_orientation:
            self.orient(turn)
            return
        if turn[0] in self.possible_slice_turns:
            for subturn in self.slice_turns[turn].split(' '):
                self.rotate(subturn)
            return
        if turn in self.possible_double_turns:
            for subturn in self.double_turns[turn].split(' '):
                self.rotate(subturn)
            return
        if '2' in turn:
            self.rotate(turn[0])
            self.rotate(turn[0])
            return
        if "'" in turn:
            self.rotate(turn[0])
            self.rotate(turn[0])
            self.rotate(turn[0])
            return
        
        self.front(turn[0])
        
        state=self.state
        set=self.set_element
        get=self.get_element

        self.rotate90('F')
        u_line=self.get_side('U')[6:]
        set('U',6,get('L',8))
        set('U',7,get('L',5))
        set('U',8,get('L',2))
        set('L',8,get('D',2))
        set('L',5,get('D',1))
        set('L',2,get('D',0))
        set('D',0,get('R',6))
        set('D',1,get('R',3))
        set('D',2,get('R',0))
        set('R',6,u_line[2])
        set('R',3,u_line[1])
        set('R',0,u_line[0])

        self.unfront(turn[0])

    def rotate90(self,side):
        arr=self.get_side(side)
        original=[arr[:3] , arr[3:6] , arr[6:]]
        rotated=[item for sublist in zip(*original[::-1]) for item in sublist]
        self.set_side(side,rotated)

    def front(self,turn):
        if not turn == 'F':
            self.orient(self.front_table[turn])

    def unfront(self,turn):
        if not turn == 'F':
            self.orient(self.unfront_table[turn])

    
    def orient(self,turn):
        if '2' in turn:
            self.orient(turn[0])
            self.orient(turn[0])
        if "'" in turn:
            self.orient(turn[0])
            self.orient(turn[0])
            self.orient(turn[0])
        
        s=self.state
        set=self.set_side
        get=self.get_side
        
        if turn == 'X':
            #от себя
            self.rotate90('R')
            self.rotate90('U')
            self.rotate90('U')
            self.rotate90('L')
            self.rotate90('L')
            self.rotate90('L')
            self.rotate90('B')
            self.rotate90('B')
            f=get('F')
            set('F',get('D'))
            set('D',get('B'))
            set('B',get('U'))
            set('U',f)

        if turn == 'Y':
            #налево
            self.rotate90('U')
            self.rotate90('D')
            self.rotate90('D')
            self.rotate90('D')
            f=get('F')
            set('F',get('R'))
            set('R',get('B'))
            set('B',get('L'))
            set('L',f)

        if turn == 'Z':
            #по часовой
            self.rotate90('L')
            self.rotate90('U')
            self.rotate90('R')
            self.rotate90('D')
            self.rotate90('B')
            self.rotate90('B')
            self.rotate90('B')
            u=get('U')
            set('U',get('L'))
            set('L',get('D'))
            set('D',get('R'))
            set('R',u)
    
    
    def repr_side(self,side):
        arr=self.get_side(side)
        return ' '.join(arr[:3])+' \n' + ' '.join(arr[3:6])+' \n' + ' '.join(arr[6:])+' \n'
    
    
    def get_side(self,side):
        return self.state[self.orientation[side]]
    def set_side(self,side,arr):
        self.state[self.orientation[side]]=arr
    
    def get_element(self,side,n):
        return self.state[self.orientation[side]][n]
    def set_element(self,side,n,new_elem):
        self.state[self.orientation[side]][n]=new_elem
    
    def __repr__(self):
        indent=' '*6
        arr=self.get_side('U')
        up=indent+'+-----+' + '\n' +indent+'|'+' '.join(arr[:3])+'|\n' + indent+'|'+' '.join(arr[3:6])+'|\n' + indent+'|'+' '.join(arr[6:])+'|\n'
        arr=self.get_side('D')
        down=indent+'|'+' '.join(arr[:3])+'|\n' + indent+'|'+' '.join(arr[3:6])+'|\n' + indent+'|'+' '.join(arr[6:])+'|\n' + indent+'+-----+' + '\n' 
        
        middle=[self.get_side(x) for x in ['L','F','R','B']]
        upper_middle='|'+''.join([' '.join(side[:3]) + '|' for side in middle])
        middle_middle='|'+''.join([' '.join(side[3:6]) + '|' for side in middle])
        lower_middle='|'+''.join([' '.join(side[6:]) + '|' for side in middle])
        
        output=up + '+-----'*4+'+\n' + upper_middle+'\n' + middle_middle+'\n' + lower_middle+'\n' + '+-----'*4+'+\n'+ down
        return output
