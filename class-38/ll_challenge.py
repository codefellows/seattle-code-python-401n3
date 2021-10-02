# Given an list of linked-lists with values of single, positive integers, create a function to traverse the list and convert the list to a number, add the lists together and return the total value of all lists.

# The lists will be passed as parameters.

# ll1: [5]->[9]->[9] = 599
# ll2: [2]->[1]->[1] = 211
# ll3: [1]->[4]->[1] = 141

# Should return 951

# Algo

# define function taking in list
# variable to hold total sum
# loop through lists
# assign current node and temp variable to hold values(str)
# traverse through list add to hold value
# move to next current
# add hold value to sum
# return sum

# list_of_ll = [ll1, ll2]
#                     ^
# ll1 [5] -> [9] -> [9] -> None

# ll2 [2] -> [1] -> [1] -> None
#                           ^
# temp_list = '211'
# total_sum = 810

def add_ll(list_of_ll):
    if not list_of_ll:
        return 0
    total_sum = 0
    for potatoe in list_of_ll:
        temp_var = ''
        current = potatoe.head
        while current:
            temp_var =+ str(current.value)
            current = current.next
        total_sum += int(temp_var)
    return total_sum
         



# Big O

# o(1)
# cf_classes = [ ['Wond', 'Teacher', 'Student1', 'Student2'], [301, 'Teacher', 'Student1', 'Rog'] ]

# Where is Teacher?  list[0] o(1)

# Where is Wond in any classes at CF?
# o(n^2)
