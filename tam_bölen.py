def tambölen(sayı):
    liste = []
    for i in range(1,sayı+1):
        if sayı%i == 0:
            liste.append(i)
    return liste

while True:
    sayı = input("Sayı:")
    if sayı == "q":
        print("Sonlanıyor...")
        break
    else:
        sayı = int(sayı)
        print("Tam bölenler:",tambölen(sayı))