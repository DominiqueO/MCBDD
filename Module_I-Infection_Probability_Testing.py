#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 22:17:05 2021

@author: dominique
"""
import matplotlib.pyplot as plt
import numpy as np

def infectionProb(prevalence, sensitivity=99, specificity=99):
    return (prevalence * sensitivity) / ((100 - specificity) * (100 - prevalence) + (prevalence * sensitivity))


specificityList = [99, 99.9, 99.999]

plt.figure('Infection Probability')
prevalence = np.arange(0.001, 50, 0.009)
plt.xlabel('Prevalence (%)')
plt.ylabel('Probability of True Positive (%)')
for specificity in specificityList:
    plt.plot(prevalence, infectionProb(prevalence, specificity=specificity), label='specificity = '+str(specificity)+'%')
plt.legend()
