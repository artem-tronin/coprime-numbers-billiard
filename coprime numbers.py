

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
start = 20
end = 150
coprimeList = open('coprime numbers list.txt', 'w')

for i in range(start, end):
    for j in range(start, end):
        if gcd(i, j)==1:
            coprimeList.writelines(f'{i} {j}\n')
            print(i, j)
