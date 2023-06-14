num_introdus = int(input("Introduceti numarul pana la care sa se creeze secventa Fibonacci:\n"))
if num_introdus == 0:
    print("[]")
# Printeaza restul elementelor
else:
    # Initializeaza primi 2 termeni
    secventa = [0]
    if num_introdus >= 2:
        secventa.append(1)
    # Genereaza ceilalti termeni
    count = 2
    while count < num_introdus:
        # Calculeaza numarul urmator
        urmatorul_term = secventa[count - 1] + secventa[count -2]
        #Adauga celalat element in secventa
        secventa.append(urmatorul_term)
        count += 1
    print(f"Aceasta este secventa Fibonacci \n{secventa}\npana la numarul {num_introdus}.\n")
