def solve(n):
    liste_des_chiffres=[]
    while n > 10:
        chiffre=n%10
        liste_des_chiffres.append(chiffre)
        n=n-chiffre
        n//=10
    return sum(liste_des_chiffres)+n
assert solve(2**15)==26
print(solve(2**1000))

    
    
        