def set_test_list():
    test_list = [[1,4],[2,6],[1,7],[3,2],[4,2],[4,4],[1,5],[2,3],[6,2],[5,1]]
    return test_list

def initial_menu(readable_list):

    '''
    this function outputs the UI for the initial menu
    '''

    if (len(readable_list) == 0):
        print("\nMenu:\n1 - Read a new sequence of complex numbers\n2 - Use a predefined list of complex numbers")

def check_if_valid(option):

    '''
    it makes sure that the introduced value comes out of the function valid
    '''

    while True:
        if (option == 1):
            return 1
        elif(option == 2):
            return 2
        else:
            option = int(input("please enter a valid number: "))

def set_real_part(mylist):
    real = 0

    real = int(input("The real part of the number: "))

    mylist.append(real)

def set_immaginary_part(mylist):
    immaginary = 0

    immaginary = int(input("The immaginary part of the number: "))

    mylist.append(immaginary)

def get_real_part(complex_list):
    return complex_list[0]

def get_immaginary_part(complex_list):
    return complex_list[1]

def set_complex_number():

    '''
    this function adds another complex number to the list, in a form of another list
    '''
    complex_number_list = []

    set_real_part(complex_number_list)
    set_immaginary_part(complex_number_list)

    return complex_number_list

def create_new_list():

    '''
    this function creates the new list of complex numbers
    '''

    n = int(input("How many numbers would you like your list to have: "))

    new_list = []

    i = 0
    for x in range(n):
        print("Number", str(i+1) + ":")
        new_list.append(set_complex_number())
        i += 1
    
    return new_list

def sequence_menu(created_list):
    if len(created_list) != 0:
        print("\nSequence Menu:\n1 - Print the longest sequence with the real part in form of a mountain\n2 - Print the longest sequence with real and immaginary parts that can both be written using the same base 10 digits\n3 - Print the whole list of complex numbers")

def search_mountain(new_list):
    '''
    input: a list of numbers
    output: the longest sequence with the numbers allignated in a mountain form
    '''
    mountain_list = []

    max_length = 0

    left = 0
    right = 0
    n = len(new_list) - 1

    while right <= n:
        ok = True

        while ok == True:
            if get_real_number(new_list[right+1]) >= get_real_number(new_list[right]):
                right += 1
            else:
                ok = False
        
        ok = True
        
        while ok == True:
            if get_real_number(new_list[right+1]) <= get_real_number(new_list[right]):
                right += 1
            else:
                ok = False

        if right-left+1 > max_length:
            max_length = right-left+1

            mountain_list.clear()

            for x in range (left, right):
                mountain_list.append(new_list[x])
        
        left = right + 1
        right = left + 1
    
    return mountain_list

def get_mountain_sequence(new_list):
    '''
    input: the list of complex numbers
    output: a new list made of the longest sequence of numbers in a mountain form
    '''
    mountain_list = []

    max_length = 0

    left = 0
    right = 0
    list_length = len(new_list) - 1

    while right <= list_length:
        ok = True

        while ok == True:
            if get_real_part(new_list[right+1]) >= get_real_part(new_list[right]):
                right += 1
            else:
                ok = False
        
        ok = True
        
        while ok == True:
            if right < list_length and get_real_part(new_list[right+1]) <= get_real_part(new_list[right]):
                right += 1
            else:
                ok = False

        if right-left+1 > max_length:
            max_length = right-left+1

            mountain_list.clear()

            for x in range (left, right):
                mountain_list.append(new_list[x])
        
        left = right + 1
        right = left
    
    return mountain_list

def get_frequence_vector(complex_list):
    frequence = []
    for i in range(10):
        frequence.append(0)

    a = get_real_part(complex_list)

    while a != 0:
        frequence[int(a%10)] = 1
        a /= 10
    
    b = get_immaginary_part(complex_list)
    
    while b != 0:
        frequence[int(b%10)] = 1
        b /= 10

    return frequence
    
def check_frequence_match(a, b):
    for i in range (10):
        if a[i] != b[i]:
            return False
    return True

def get_same_sequence(initial_list):
    max_length = 0

    max_sequence = []

    right = 0
    left = 0
    n = len(initial_list) - 1
    
    frequence_a = []
    frequence_b = []

    while right <= n:
        ok = True

        while ok == True:
            a = right + 1
            b = right

            frequence_a.append(get_frequence_vector(initial_list[a]))
            frequence_b.append(get_frequence_vector(initial_list[b]))

            if check_frequence_match(frequence_a, frequence_b):
                right += 1
            else:
                ok = False
        
        if right-left+1 > max_length:
            max_length = right-left+1

            max_sequence.clear()

            for x in range (left, right):
                max_sequence.append(initial_list[x])
        
        left = right + 1
        right = left

    return max_sequence

def ui():

    while True:
        created_list = []

        initial_menu(created_list)
        option = 0
        option = int(input())

        option = check_if_valid(option)

        if option == 1:
            created_list = create_new_list()
        if option == 2:
            created_list = set_test_list()
        
        sequence_menu(created_list)
        option = 0
        option = int(input())

        if option == 3:
            for x in created_list:
                print (str(get_real_part(x)) + "+" + str(get_immaginary_part(x)) + "i")
        else:
            option = check_if_valid(option)

            output_list = []

            if option == 1:
                output_list = get_mountain_sequence(created_list)
            if option == 2:
                output_list = get_same_sequence(created_list)
            
            for x in created_list:
                print (str(get_real_part(x)) + "+" + str(get_immaginary_part(x)) + "i")

        break

ui()