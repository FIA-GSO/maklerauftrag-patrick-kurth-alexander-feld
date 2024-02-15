Fläche = 0 
Gesamt = 0
Anzahl_Räume = 0

weitere_Räume = True

while weitere_Räume == True:
    l_förmiger_Raum = str(input('Handelt es sich um einen L-förmigen Raum? j/n'));
    if l_förmiger_Raum == ('j'):
        Seite_A = int(input('Wie lang ist Seite A?'))
        Seite_B = int(input('Wie lang ist Seite B?'))
        Seite_C = int(input('Wie lang ist Seite C?'))
        Seite_D = int(input('Wie lang ist Seite D?'))
        Fläche=(Seite_A * Seite_B + Seite_C * Seite_D)
        Gesamt = Gesamt + Fläche

        else rechteckiger_raum:
        Seite_A = int(input('Wie lang ist Seite A?'))
        Seite_B = int(input('Wie lang ist Seite B?'))
        Fläche = (Seite_A * Seite_B)
        Gesamt = Gesamt + Fläche
        Anzahl_Räume +=1
     
