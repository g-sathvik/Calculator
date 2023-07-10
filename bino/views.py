from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import numpy as np
import scipy as scp
from scipy import stats
import math 


def home(request):
	return render(request,'bino/bino.html')

def combos(n, i):
    return math.factorial(n) / (math.factorial(n-i)*math.factorial(i))


def bins(request):
	S = float(request.GET["S"])
	K = float(request.GET["K"])
	T = float(request.GET["T"])
	r = float(request.GET["r"])
	sigma = float(request.GET["sigma"])
	N = int(request.GET["n"])
	cp = request.GET["CP"]
	dt = T/N
	u = np.exp(sigma * np.sqrt(dt))
	d = np.exp(-sigma * np.sqrt(dt))
	if cp == 'Call':
		
		p = (  np.exp(r*dt) - d )  /  (  u - d )
		value = 0 
		for i in range(N+1):
			node_prob = combos(N, i)*p**i*(1-p)**(N-i)
			ST = S*(u)**i*(d)**(N-i)
			value += max(ST-K,0) * node_prob
		value = value*np.exp(-r*T)
		context = {'first': S, 'second': K, 'third': T, 'four': r,'five': N,'sixth': value,'sev': sigma}
		return render(request, 'bino/bino.html', context)
	else:
		
		p = (  np.exp(r*dt) - d )  /  (  u - d )
		value = 0 
		for i in range(N+1):
			node_prob = combos(N, i)*p**i*(1-p)**(N-i)
			ST = S*(u)**i*(d)**(N-i)
			value += max(K-ST,0) * node_prob
		value = value*np.exp(-r*T)
		context = {'first': S, 'second': K, 'third': T, 'four': r,'five': N,'sixth': value,'sev': sigma}
		return render(request, 'bino/bino.html', context)
