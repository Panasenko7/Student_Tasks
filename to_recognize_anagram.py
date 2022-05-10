#A="Buckethead"
#B="DeathCubeK"
#def verify_anagrams(A,B):
    #return "".join(sorted(A.lower())).strip() == "".join(sorted(B.lower())).strip()
#print (verify_anagrams("Buckethead ","DeathCubeK"))    #True

is_anagram = lambda x1, x2: sorted(x1.lower()) == sorted(x2.lower())


#Results
print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram("elvise", "livees"))
print(is_anagram("elvis", "dead"))