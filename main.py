import turtle
turtle.tracer(0,0)   
turtle.pu()
turtle.goto(-500,0)
turtle.screensize(2000,2000)
turtle.pd()

def dessiner (n, longueur, angle):    
    for caractere in n:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)

def PrinSierpinski (chaine):
    nouvelleChaine = ''
    for lettre in chaine:
        if lettre == 'F':
            nouvelleChaine = nouvelleChaine + 'F-G+F+G-F'
        elif lettre == 'G':
            nouvelleChaine = nouvelleChaine + 'GG'
        else :
            nouvelleChaine = nouvelleChaine + lettre
    return nouvelleChaine

def OptSierpinski (motifInitial, niter):
    n = motifInitial
    for i in range(niter):
        nouveauMotif = PrinSierpinski (n)
        n = nouveauMotif
    return n

def FinSierpinski (motifInitial, niter):
    c = OptSierpinski (motifInitial, niter)
    FinSierpinski = ''
    for _ in range(3):
        FinSierpinski += c
        FinSierpinski += '--' 
    return FinSierpinski

longueur = 4
angle = 120
niter = 8
dessiner(OptSierpinski('F', niter), longueur, angle)

turtle.update()
turtle.exitonclick() 

