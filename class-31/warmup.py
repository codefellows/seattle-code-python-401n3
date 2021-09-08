# Write a script to produce the following output

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

n = 5

# for i in range(n): 
#     for j in range(0, i + 1): 
#         print("* ", end ="") 
#     print("\r")


print('\n'.join('* ' * i for i in range(n+1)))

