# Les tests conditionnels retournent False ou True,
# donc un booléen
print( 10 == 8 + 2) # True
print( 9 <= 8 + 2)  # True
print( 9 != 2)      # True
print( 9 != '9')    # True

# A and B (noté aussi &) 
# => True si A et B sont True, sinon False
print ( 7 != 3 & 7 > 8) # False

# A or B (noté aussi |) 
# => True si au moins A ou B est True (sinon False)
print ( (7!= 3) or (7>8) ) # True

# not A (noté aussi !) 
# => True si A est False (inverse la valeur)
print ( not('re' == 'r'+'e')) # False  

print( bool('') == False )

# if test:
# elif test2:
# else:

