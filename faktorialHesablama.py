faktorialHesablama=int(input("Faktorialini istediyiniz reqemi girin: "))

faktorial=1
i=2

while i<=faktorialHesablama:
    faktorial*=i
    i+=1


print(f"{faktorialHesablama}!={faktorial}")

