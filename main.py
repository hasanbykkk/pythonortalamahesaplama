# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

ders=input("dersinizi giriniz")
not1=input("1.notunuzu giriniz")
not2=input("2.notunuzu giriniz")
not3=input("3.notunuzu giriniz")
ortalama=(float(not1)+float(not2)+float(not3))/3
print(ders," not ortalamanız",ortalama,)
if ortalama<50:
    print("üzgünüz dersten kaldınız.")
elif ortalama==50 :
    print("dersi sınırda geçtiniz.")
else:
    print("tebrikler dersi geçtiniz!!")





