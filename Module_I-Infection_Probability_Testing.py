#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 22:17:05 2021

@author: dominique
"""
import matplotlib.pyplot as plt
import numpy as np

def infectionProb(prevalence, sensitivity=99, specifity=99):
    return (prevalence * sensitivity) / ((100 - specifity) * (100 - prevalence) + (prevalence * sensitivity))


specifityList = [99, 99.9, 99.999]

plt.figure('Infection Probability')
prevalence = np.arange(0.001, 50, 0.009)
plt.xlabel('Prevalence (%)')
plt.ylabel('Probability of True Positive (%)')
for specifity in specifityList:
    plt.plot(prevalence, infectionProb(prevalence, specifity=specifity), label='specifity = '+str(specifity)+'%')
plt.legend()
