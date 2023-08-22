# # LOCAL SCOPE and GLOBAL SCOPE
# monstax = 6 #global

# def members():
#     monstax = 1 #local
#     print(f"Inside: {monstax}")

# members()
# print(f'Outside: {monstax}')



# # MODIFYING A GLOBAL SCOPE
# monstax = 6 #global
# def members():
#     global monstax
#     monstax += 1 #local
#     print(monstax)

# members()



# # PYTHON DOESN'T SUPPORT BLOCK SCOPE
# monstax = 6
# if monstax == 6:
#     monstax += 1 #local
# print(monstax) #still can be accessed outside



# # GLOBAL CONSTANTS
# PI = 3.1415
# URL = 'https://www.google.com'