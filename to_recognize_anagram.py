#A="Buckethead "
#B="DeathCubeK"
def verify_anagrams(A,B):
    return "".join(sorted(A.lower())).strip() == "".join(sorted(B.lower())).strip()
print (verify_anagrams("Buckethead ","DeathCubeK"))    #True