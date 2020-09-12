#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""author: !!! Moussa Ndiaye DIC1 TR !!!"""
from MesFonctionsMaths import *
from flask import *
from math import *



################ Début ###############################s

app = Flask(__name__)
app.secret_key = 'd66HR8dç"f_-àgjYYic*df'
#############PAGE D'ACCUEIL#################
@app.route('/')
def index():
    
    return render_template('Accueil/index.html.twig')




#############MOI#################
@app.route('/auteur')
def Auteur():
    
    return render_template('Accueil/auteur.html.twig')

###########GESTION DES ERREURS ###########

    #####  TAILLE INCORRECTE #####
@app.errorhandler(404)
def erreurTaille(error,vue,valeur):

    return render_template('Erreur/taille.html.twig',erreur=error,vue=vue,valeur=valeur)


##### URL INEXIATANT #####
@app.errorhandler(404)
def erreurPage(e):
    return render_template('Erreur/url.html.twig')


########## MODELISATION DE LA FILE D'ATTENTE #################

# route index
@app.route('/Dimensionnement')
def Dim():
    return render_template('Dim/index.html.twig')


@app.route('/Dim/getData/', methods=['GET', 'POST'])
def evaluerDim():
    error = None
    if request.method == 'POST':
        try:
            Lambda=int(request.form['lambda'])
            try:
                mu=int(request.form['mu'])
                try:
                    s = int(request.form['s'])
                    Po = calcul_Po(Lambda,mu,s)
                    nu = calcul_nu(Lambda,mu,s)
                    n = calcul_n(Lambda,mu,s)
                    tf = calcul_tf(Lambda,mu,s)
                    theta = float(Lambda) / float(mu)
                    rho = s - theta
                    return render_template('Dim/resultat.html.twig',s=s,Po=Po,nu=nu,n=n,tf=tf,rho=rho,theta=theta,val_lambda=Lambda,val_mu=mu,val_s=s)
                except ValueError:
                    return erreurTaille('taille incorrecte','/Dimensionnement',request.form['s'])
            except ValueError:
                return erreurTaille('taille incorrecte','/Dimensionnement',request.form['mu'])
        except ValueError:
            return erreurTaille('taille incorrecte','/Dimensionnement',request.form['lambda'])

################################## ******  Erlang B  ****** #################################

# route index
@app.route('/ErlangB')
def ErlangB():
    return render_template('ErlangB/index.html.twig')


@app.route('/erlangb/calculer', methods=['GET', 'POST'])
def CalculerErlangb():
    if request.method == 'POST':
        global toff,ndc,tdb
        a=request.form['toff']
        n=request.form['ndc']
        tdb=request.form['tdb']
        if tdb=='':
            a=float(request.form['toff'])
            n=int(request.form['ndc'])
            Pb=proba_echec(a, n)*100
            return render_template('ErlangB/resultat.html.twig',trafic=a,nbreCircuit=n,tauxBlocage=Pb)
        if a=='':
            proba = float(request.form['tdb'])
            nbcircuit = int(request.form['ndc'])
            resultat = Trafic( nbcircuit, proba)
            return render_template('ErlangB/resultat.html.twig',trafic=resultat,nbreCircuit=nbcircuit,tauxBlocage=proba)
        if n=='':
            proba = float(request.form['tdb'])
            traffic = int(request.form['toff'])
            resultat = nombrecanaux(A,p)
            return render_template('ErlangB/resultat.html.twig',trafic=traffic,nbreCircuit=resultat,tauxBlocage=proba )
    return render_template('ErlangB/resultat.html.twig')

################################## ******  Erlang C  ****** #################################
 
# route index
@app.route('/ErlangC')
def ErlangC():
    return render_template('ErlangC/index.html.twig')

@app.route('/erlangc/calcul', methods=['GET', 'POST'])
def CalculerErlangC():
    if request.method == 'POST':
        global toff,ndc,tdb
        chaine_a=request.form['a']
        chaine_n=request.form['n']
        chaine_prob=request.form['prob']
        if chaine_prob=='':
            try:
                a=float(request.form['a'])
                try:
                    n=int(request.form['n'])
                    if a<0 or n<0 or a<n:
                        return '''<b><center><font color="red" size="6">Mauvaise valeur</font></center></b>'''
                    o1=puissance(a,n)/factoriel(n)
                    o2=n/(n-a)
                    o3=o1*o2
                    B2 = 0
                    for k in range(n):
                        B2 = B2+puissance(a,k)/factoriel(k)
                    B = o3+B2
                    B=(o3/B2)/10
                    return render_template('ErlangC/resultat.html.twig',toff=a,ndc=n,tdb=abs(B))
                except ValueError:
                    return erreurTaille('taille incorrecte','/ErlangB',request.form['n'])
            except ValueError:
                return erreurTaille('taille incorrecte','/ErlangB',request.form['a'])
        if chaine_a=='':
            try:
                proba = float(request.form['prob'])
                try:
                    nbcircuit = int(request.form['n'])
                    A = list()
                    for k in range(9):
                        A.append([])
                        for l in range(51):
                            A[k].append([])
                    for k in range(5):
                        for l in range(51):
                            A[k][l] = 0
                    fich = open("erlangC.txt", "r")
                    for i in range(5):
                        for j in range(51):
                            A[i][j] = float(fich.readline())
                    traffic = traficB(A, nbcircuit, proba, 9)
                    resultat = str(round(traffic, 3))
                    return render_template('ErlangC/resultat.html.twig',toff=resultat,ndc=nbcircuit,tdb=proba)
                except ValueError:
                    return erreurTaille('taille incorrecte','/ErlangB',request.form['n'])
            except ValueError:
                return erreurTaille('taille incorrecte','/ErlangB',request.form['prob'])

        if chaine_n=='':
            try:
                proba = float(request.form['prob'])
                try:
                    traffic = int(request.form['a'])
                    A = list()
                    for k in range(9):
                        A.append([])
                        for l in range(51):
                            A[k].append([])
                    for k in range(9):
                        for l in range(51):
                            A[k][l] = 0
                    fich = open("erlangC.txt", "r")
                    for i in range(9):
                        for j in range(51):
                            A[i][j] = float(fich.readline())
                    nbCir = nbCircuitsC(A, traffic, proba, 9)
                    resultat = str(nbCir)
                    return render_template('ErlangC/resultat.html.twig',toff=traffic,ndc=resultat,tdb=proba)
                except ValueError:
                    return erreurTaille('taille incorrecte','/ErlangB',request.form['n'])
            except ValueError:
                return erreurTaille('taille incorrecte','/ErlangB',request.form['prob'])

        return render_template('ErlangC/resultat.html.twig')

######################################### Appel du programme #################################

if __name__ == '__main__':
#     app.run(host='0.0.0.0')
    app.run(debug='true')