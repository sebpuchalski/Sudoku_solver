class Sudoku():

    '''
    15 Available methods:
    
    Nonet verifying methods:
    - nonet_row_info_____________(Provides square occupancy parameters for a given vertical row and nonet the function)
    - nonet_sum__________________(Sums numbers in an indicated nonet)
    - nonet_fill_situation_______(Sums 1s for each number in an indicated nonet)
    - nonet_isin_________________(Checks if an indicated digit is in a nonet)
    - nonet_row_empty_space______(Checks for zeroes in a given vertical row of a nonet)
    
    Nonet augmenting methods:
    - nonet_almost_full__________(Fills in last missing space in a nonet)
    - nonet_row_fill_single_vertical_empty_space (Enters a digit into a nonet)
    - nonet_fill_________________(Enters a digit into a none)
    - nonet_row_single_val_empty_space (Enters a digit into a nonet)

    Row methods:
    - row_location_______________(Returns a location of occupied square in a nonet in an indicated vertical row
        assuming that the row has only one occupied square and the other squares are empty)
    - row_sum____________________(Sums all digits in a horizontal or vertical row)
    - row_isin___________________(Checks if digit is in indicated (vertical/horizontal) row)
    - row_isin_nonet_specific____(Checks if digit is in indicated row for an indicated nonet height)
    - rowisin_indexed_horizontal_(Checks if digit is in indicated horizontal row given nonet and nonet vertical row index)
    
    Matrix methods
    - rotate_matrix______________(Rotates the matrix clockwise by the indicated no. of rotations)
   
    '''    
    
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.nonets = {1:[0,3,0,3],2:[3,6,0,3],3:[6,9,0,3],
     4:[0,3,3,6], 5:[3,6,3,6], 6:[6,9,3,6],
     7:[0,3,6,9],8:[3,6,6,9],9:[6,9,6,9]} #dictionary with nonet coordinates
        
        self.horizontal_nonet_index = {1:{0:1,1:1,2:2},
                                       2:{0:1,1:1,2:2},
                                       3:{0:1,1:1,2:2},
                                       4:{0:3,1:4,2:5},
                                       5:{0:3,1:4,2:5},
                                       6:{0:3,1:4,2:5},
                                       7:{0:6,1:7,2:8},
                                       8:{0:6,1:7,2:8},
                                       9:{0:6,1:7,2:8}}
        
#NONET VERIFYING METHODS:___________________________________________________________________________:        
        
    def nonet_row_info(self, row_number, nonet):
        '''For a given vertical row and nonet the function provides square
        occupancy parameters:
        
        Args:
        row_number - vertical row number [int]
        nonet - nonet number [int]
        
        
        Returns:
        nonzero_location - indeces of occupied squares [list]
        zero_location - indeces of empty squares [list]
        suma_2- total number of occupied squares out of three [int]'''


        coordinates = self.nonets[nonet] #pulls nonet specific coordinates from the init function

        suma = [] #variable storing numbers from a vertical row in a digit
        suma_2 = 0 #variable used to determine vertical row occupancy, indicates number of occupied squares in a vertical row

        for row in self.matrix[coordinates[2]:coordinates[3]]: #iterates over matrix horizontal rows related to the nonet
            suma.append(row[row_number]) #appends numbers specific to the selected nonet vertical row

        nonzero_location = []  #placeholder variable non-zero square locations
        zero_location = [] #placeholder variable empty square locations
        coord = [0,1,2] #index coordinates

        for item, no in zip(suma, coord):
            if item != 0:
                nonzero_location.append(no)
                suma_2 +=1
            else:
                zero_location.append(no)
        return(nonzero_location, zero_location, suma_2)        
        
        
    def nonet_sum(self, nonet_number):
        '''Sums numbers in an indicated nonet.

        Args:
        nonet_number - [int]
        
        Returns:
        sum of numbers in the nonet [int]
        '''

        coord = self.nonets[nonet_number] #dynamic variable

        suma = 0 #adds each number in the nonet together
        for row in self.matrix[coord[2]:coord[3]]:
            x  = sum(row[coord[0]:coord[1]])
            suma += x

        return(suma)
    
    
    
    def nonet_fill_situation(self, nonet_number):
#          '''Sums 1s for each number in an indicated nonet.

#         Args:
#         nonet_number - [int]
        
#         Returns:
#         sum of numbers in the nonet [int]
#         '''
        coord = self.nonets[nonet_number] #dynamic variable

        suma = 0 #adds 1 for each number in the nonet
        for row in self.matrix[coord[2]:coord[3]]:
            for item in row[coord[0]:coord[1]]:
                if item != 0:
                    suma += 1
                else:
                    pass
        return(suma)  
    
    
    
    def nonet_isin(self, nonet_number, digit):
        '''Checks if an indicated digit is in a nonet.

        Args:
        nonet_number - [int]
        digit - indicated digit [int]
        
        Returns:
        Boolean value (True/False).    
        '''
        coord = self.nonets[nonet_number] #selects coordinates of an indicated nonet

        check = [] #appends all digits in the indicated matrix to this list
        for row in self.matrix[coord[2]:coord[3]]:
            x  = row[coord[0]:coord[1]]
            for dig in x:
                check.append(dig)

        if digit in check: #checks if the indicated digit is in the check list
            return(True)
        else:
            return(False)    
    
    
    def nonet_row_empty_space(self, empty_nonet, empty_row):
        '''Checks for zeroes in a given vertical row of a nonet.

        Args:
        empty_nonet - nonet in question [integer]
        empty_row -indicated vertical row [integer]

        Returns:
        number_of_zeroes - number of empty spaces [integer]
        zero_coord - coordinates of zeros [list]

        '''
        try:
            coord = self.nonets[empty_nonet] #selects coordinates of an indicated nonet

            numbers = [] # returns a list of numbers for the vertical row in the indicated nonet
            for row in self.matrix[coord[2]:coord[3]]:
                x  = row[empty_row]
                numbers.append(x)
  
            number_of_zeroes = 0
            zeroes = []   #checks how many zeroes are in the list
            for numb in numbers:
                if numb == 0:
                    zeroes.append(1)
                    number_of_zeroes +=1
                else:
                    zeroes.append(0)
                    
            
            indeces = [0,1,2] #records the index of empty rows
            zero_coord = []

            for item, ind in zip(zeroes, indeces):
                if item == 1:
                    zero_coord.append(ind)
                
            return number_of_zeroes, zero_coord
            
                
        except KeyError: #handles errors associated with empty spaces
            pass
        
#NONET AUGMENTING METHODS:___________________________________________________________________________:        
        
    def nonet_almost_full(self, nonet):
        '''Fills in last missing space in a nonet
        
        Args:
        nonet - nonet in question[integer]

        Returns:
        Updated matrix
        
        '''
        
        coord = self.nonets[nonet] #gets nonet's coordinates

        numbrs = [] #list of numbers in the nonet
        current_set = [] # set of numbers that are currently in the matrix
        revised_set = [] 
        
        for row in self.matrix[coord[2]:coord[3]]: #loops over horizontal rows in the nonet
            x  = row[coord[0]:coord[1]]
            for y in x: #loops over items in horizontal rows in the nonet
                current_set.append(y) #appends the current numbers (including 0) in the nonet to "current_set" list
                if y != 0:
                    numbrs.append(y) #appends the current numbers (excluding 0) in the nonet to "numbrs" list
        
        
        if len(numbrs) == 8: #this statement captures a special case where there is only one number missing in a nonet
            full_set = [1,2,3,4,5,6,7,8,9]
            for item in numbrs:
                full_set.remove(item)        
            missing_number = full_set[0] #this statement finds a number that is missing 

            
            for item in current_set:  #this loop creates a complete list of elements that should be placed in a nonet in correct order
                if item == 0:
                    revised_set.append(missing_number)
                else:
                    revised_set.append(item)
                    
            #these three lists split the numbers to be filled into a nonet by the three horizontal rows:
            r_1 = revised_set[0:3]
            r_2 = revised_set[3:6]
            r_3 = revised_set[6:9]
            full_revised = [r_1, r_2, r_3]
            
                        
            for row, revised_set in zip(self.matrix[coord[2]:coord[3]], full_revised): #the new list is used to generate a revised matrix
                row[coord[0]:coord[1]] = revised_set


        
    def nonet_row_fill_single_vertical_empty_space(self, nonet_number, row_no, digit):
        '''Enters a digit into a nonet.

        Args:
        nonet_number - nonet in question[integer]
        row_no -indicated vertical row [integer]
        digit - number for entry [integer]

        Returns:
        Updated matrix

        '''
        
        
        dic = {0:0,
                1:1,
                2:2,
                3:0,
                4:1,
                5:2,
                6:0,
                7:1,
                8:2
         }      
        
        
        
        try:
            coord = self.nonets[nonet_number] #selects coordinates of an indicated nonet

            numbers = [] # returns a list of numbers for the vertical row in the indicated nonet
            for row in self.matrix[coord[2]:coord[3]]:
                x  = row[row_no]
                numbers.append(x)

            zeroes = 0   #checks how many zeroes are in the list, must be uniquely 1 for this case to work (one empty space)
            for numb in numbers:
                if numb == 0:
                    zeroes +=1

            if zeroes == 1: #if there is only one zero then that zero is substituted with the sub number in a new list
                new_numbers =[]
                for numb in numbers:
                    if numb == 0:
                        new_numbers.append(digit)
                    else:
                        new_numbers.append(numb)

                        
        except KeyError: #handles errors associated with empty spaces
            pass
        
    
    def nonet_fill(self, nonet_number, vert_row, hori_row, digit):
        '''Enters a digit into a nonet.

        Args:
        nonet_number - nonet in question[integer]
        vert_row -indicated vertical row [0-8] [integer]
        hori_row -indicated hori row [0-2] [integer]
        digit - number for entry [integer]


        #variables: empty_nonet, space_to_fill (hori_row), empty_row (veri_row), investigated_number
        
        Returns:
        Updated matrix

        '''
        try:
            coord = self.nonets[nonet_number] #selects coordinates of an indicated nonet

            numbers = [] # returns a list of numbers for the vertical row in the indicated nonet
            for row in self.matrix[coord[2]:coord[3]]:
                x  = row[vert_row]
                numbers.append(x)
            numbers[hori_row] = digit    
                
            for row, numb in zip(self.matrix[coord[2]:coord[3]], numbers): #the new list is used to generate a revised matrix
                row[vert_row] = numb
                                
        except KeyError: #handles errors associated with empty spaces
            pass


    def nonet_row_single_val_empty_space(self, nonet_number, row_no, digit):
        '''Enters a digit into a nonet.

        Args:
        nonet_number - nonet in question[integer]
        row_no -indicated vertical row [integer]
        digit - number for entry [integer]

        Returns:
        Updated matrix

        '''
        try:
            coord = self.nonets[nonet_number] #selects coordinates of an indicated nonet

            numbers = [] # returns a list of numbers for the vertical row in the indicated nonet
            for row in self.matrix[coord[2]:coord[3]]:
                x  = row[row_no]
                numbers.append(x)

            zeroes = 0   #checks how many zeroes are in the list, must be uniquely 1 for this case to work (one empty space)
            for numb in numbers:
                if numb == 0:
                    zeroes +=1

            if zeroes == 1: #if there is only one zero then that zero is substituted with the sub number in a new list
                new_numbers =[]
                for numb in numbers:
                    if numb == 0:
                        new_numbers.append(digit)
                    else:
                        new_numbers.append(numb)

                for row, new_numb in zip(self.matrix[coord[2]:coord[3]], new_numbers): #the new list is used to generate a revised matrix
                    row[row_no] = new_numb
                
        except KeyError: #handles errors associated with empty spaces
            pass
        
        
        
        
        
#ROW METHODS:___________________________________________________________________________:         
        
        
    def row_location(self, row_number, nonet):
        '''
        Returns a location of occupied square in a nonet in an indicated vertical row
        assuming that the row has only one occupied square and the other squares are empty.

        Args:
        row_number - [int] number of the empty vertical row
        nonet - [int] number of the nonet in question

        Returns:
        localization [int]
        '''

        coordinates = self.nonets[nonet] #pulls nonet specific coordinates from the init function
            
        suma = [] #variable used to sum all digits
 
        for row in self.matrix[coordinates[2]:coordinates[3]]:
            suma.append(row[row_number])
        location = 'x'    
        coord = [0,1,2]
        for item, no in zip(suma, coord):
            if item != 0:
                location = no
        return(location)        
        
        
    def row_sum(self, row_number, orientation='not indicated'):
        '''
        Sums all digits in a horizontal or vertical row.

        Args:
        row_number - [int]
        orientation - 'horizontal'/'vertical' [str]

        Returns:
        Sum [int]
        '''

        suma = 0 #variable used to sum all digits

        if orientation == 'vertical':
            for row in self.matrix:
                suma += row[row_number]
            return(suma)

        elif orientation == 'horizontal':
            suma = sum(self.matrix[row_number])
            return(suma)

        else:
            print("Please indicate the orientation!")        
        
    
    def row_isin(self, digit, row_number, orientation='def'):
        '''Checks if digit is in indicated (vertical/horizontal) row.

        Args:
        digit - digit of interest [int]
        row_number - row number [int]
        orientation - 'horizontal' or 'vertical' [string]

        Returns:
        1 if digit in the list
        0 if digit not in the list
        '''

        if orientation == 'horizontal':
            x = self.matrix[row_number]
            if digit in x:
                return(1)
            else:
                return(0)

        elif orientation == 'vertical':
            x=[]
            for row in self.matrix:
                x.append(row[row_number])
            if digit in x:
                return(1)
            else:
                return(0)
        else:
            print('Please indicate the orientation for the isin function.')
            

            
    def row_isin_nonet_specific(self, digit, row_number, nonet):
        '''Checks if digit is in indicated row for an indicated nonet height.

        Args:
        digit - digit of interest [int]
        row_number - row number [int]
        nonet - nonet number [int]

        Returns:
        1 if digit in the list
        0 if digit not in the list
        '''
        dic = {
            1:[0,1,2],
            2:[0,1,2],
            3:[0,1,2],
            4:[3,4,5],
            5:[3,4,5],
            6:[3,4,5],
            7:[6,7,8],
            8:[6,7,8],
            9:[6,7,8]
        }
        
        corresponding_rows = dic[nonet]
        
        if row_number == 0:
            x = self.matrix[corresponding_rows[0]]
            if digit in x:
                return(1)
            else:
                return(0)
     
        elif row_number == 1:
            x = self.matrix[corresponding_rows[1]]
            if digit in x:
                return(1)
            else:
                return(0)
            
        else:
            x = self.matrix[corresponding_rows[2]]
            if digit in x:
                return(1)
            else:
                return(0)
     
            
            
    def row_isin_indexed_horizontal(self, digit, row_index, nonet):
        '''Checks if digit is in indicated horizontal row given nonet and nonet vertical row index

        Args:
        digit - digit of interest [int]
        row_index [int]
        nonet [int]

        Returns:
        1 if digit in the list
        0 if digit not in the list
        '''

        a = self.horizontal_nonet_index[nonet][row_index]

        x = self.matrix[a]
        if digit in x:
            return(1)
        else:
            return(0)



#MATRIX METHODS:___________________________________________________________________________:                           
        
    def rotate_matrix(self, no_rot):
        '''Rotates the matrix clockwise by the indicated no. of rotations.

        Args:
        no_rot - number of rotations [int]

        Returns:
        Rotated Matrix [list of lists]
        '''
        rotated_matrix = self.matrix

        l = [i for i in range(1,no_rot+1)]

        for rot in l:

            numbers = [0,1,2,3,4,5,6,7,8] #number of rows in the matrix
            vert_dic = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]} #dictionary for each row

            for row in rotated_matrix:
                for num in numbers:
                    vert_dic[num].append(row[num])    


            rotated_matrix = []

            for num in numbers:
                x = vert_dic[num]
                x.reverse()
                rotated_matrix.append(x)
        self.matrix = rotated_matrix


#________________________________________END OF METHODS:______________________________________  


    


    
