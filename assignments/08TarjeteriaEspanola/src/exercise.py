
def maximo(numpliegos,numplumones):
    pliegos = numpliegos*12
    plumones = numplumones*35

    if pliegos and plumones > 0:
        if pliegos > plumones:
            return plumones
        elif plumones > pliegos:
            return pliegos
    
def main():
    #escribe tu código abajo de esta línea
    pliegos = int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones = int(input('Dame la cantidad de plumones: '))
    tarjetas = maximo(pliegos, plumones)
    print('El número máximo de tarjetas que se pueden hacer es: ' + str(tarjetas))
if __name__=='__main__':
    main()
