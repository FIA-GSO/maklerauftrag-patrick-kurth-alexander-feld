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
        Fläche = (Seite_A * Seite_B + Seite_C * Seite_D)
        Gesamt = Gesamt + Fläche
        Anzahl_Räume += 1
            
        weitere_Räume = str(input('Willst du einen weiteren Raum messen? j/n'))
            
        if weitere_Räume == ('j'):
            weitere_Räume = True
        else:
            durchschnittliche_Fläche = Gesamt/Anzahl_Räume
            print('Die Gesamtfläche beträgt ' + str(Gesamt) + ('m2. Die durchschnittliche Fläche beträgt: ') + str(durchschnittliche_Fläche))
        
    else:
        str(input('Raum ist rechteckig, bitte auf ENTER klicken um einen Schritt weiter zu kommen.'))
        Seite_A = int(input('Wie lang ist Seite A?'))
        Seite_B = int(input('Wie lang ist Seite B?'))
        Fläche = (Seite_A * Seite_B)
        Gesamt = Gesamt + Fläche
        Anzahl_Räume +=1
            
        weitere_Räume = str(input('Willst du einen weiteren Raum messen? j/n'))
            
        if weitere_Räume == ('j'):
            weitere_Räume = True
        else:
            durchschnittliche_Fläche = Gesamt/Anzahl_Räume
            print('Die Gesamtfläche beträgt ' + str(Gesamt) + (' m2. Die durchschnittliche Fläche beträgt: ') + str(durchschnittliche_Fläche) + ('m2.'))


