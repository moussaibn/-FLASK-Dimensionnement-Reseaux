###################################################################
##################################################Premier Semestre
# !/usr/bin/python3
# -*-coding:Utf-8 -*
"""author:Moussa Ndiaye DIC1 TR"""
################Fonction Python###################


def puissance(p, n):
	res = 1
	for i in range(n):
		res = res * p
	return res


def calcul_Po(Lambda, mu, S):
	po1 = 0
	theta = float(Lambda) / float(mu)
	for i in range(S + 1):
		po1 = po1 + puissance(theta, i) / factoriel(i)
	po2 = puissance(theta, S + 1) / (factoriel(S) * (S - theta))

	Po = 1 / (po1 + po2)
	return Po


def calcul_nu(Lambda, mu, S):
	theta = float(Lambda) / float(mu)
	m1 = puissance(theta, S + 1) * calcul_Po(Lambda, mu, S)
	m2 = S * factoriel(S) * puissance(1 - theta / S, 2)
	m = m1 / m2
	return m


def calcul_n(Lambda, mu, S):
	theta = float(Lambda) / float(mu)
	n1 = calcul_nu(Lambda, mu, S) + theta
	return n1


def calcul_tf(Lambda, mu, S):
	tf = calcul_nu(Lambda, mu, S) / Lambda
	return tf



##############Fin fonction Python ################
def factoriel(n):
	x = 1
	if n >= 0:
		i = 1 
		while i <= n:
			x = x * i
			i = i + 1
	return x

def proba_echec(A, n):
	num, den, i = 0.0, 0.0, 0
	num = pow(A,n)/factoriel(n)
	while i <= n:
		den = den + pow(A, i)/factoriel(i)
		i = i + 1
	Pe = num / den
	return Pe

def nombrecanaux(A, Pe):
	n = 1
	while proba_echec(A,n) > Pe:
		n = n + 1
	return n
	

def Trafic(n, p):
	a = 0
	while nombrecanaux(a / 100, p) != n:
		a = a + 2
		
def ProbaAttenteC(A, n):
	num, den, i = 0.0, 0.0, 0
	num = pow(A,n) / factoriel(n)
	num = num * (n / (n - A))
	while i <= n - 1:
		den = den + pow(A, i)/factoriel(i)
		i = i + 1
	som = (pow(A,n) / factoriel(n)) * (n / (n - A))
	den = den + som
	Pe = num / den
	return Pe

def NombreCanauxC(A, Pe):
	n = 0
	while ProbaAttenteC(A,n) > Pe:
		n = n + 1
	return n

def TraficC(n, Pe):
	a = 0
	while NombreCanauxC(a / 100, Pe) != n:
		a = a + 2
	return a / 100