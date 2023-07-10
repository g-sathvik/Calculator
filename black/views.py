from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import scipy as scp
from scipy import stats
# Create your views here.


def home(request):
    return render(request, 'black/black.html')


def bs(request):
    S = float(request.GET["S"])
    K = float(request.GET["K"])
    T = float(request.GET["T"])
    r = float(request.GET["r"])
    sigma = float(request.GET["sigma"])
    cp = request.GET["CP"]
    if cp == 'Call':
        N = scp.stats.norm.cdf
        d1 = float((np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T)))
        d2 = float(d1 - sigma*np.sqrt(T))
        c = float(S*N(d1) - K*np.exp(-r*T)*N(d2))
        context = {'first': S, 'second': K, 'third': T, 'four': r, 'five': sigma,'sixth': c}
        return render(request, "black/black.html", context)
    else:
        N = scp.stats.norm.cdf
        d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma* np.sqrt(T)
        c = K*np.exp(-r*T)*N(-d2) - S*N(-d1)
        context = {'first': S, 'second': K, 'third': T, 'four': r, 'five': sigma,'sixth': c}
        return render(request, "black/black.html", context)
