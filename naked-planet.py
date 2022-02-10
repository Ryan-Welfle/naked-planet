#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:58:37 2021

@author: ryanwelfle
"""

import matplotlib.pyplot as plt

while True:
    print('\nWELCOME TO THE NAKED PLANET TEMPERATURE SIMULATOR!\n')
    nSteps = int(input("Enter # of time-steps here: ")) #assigns nSteps with a user-assigned integer, to be used as the integer that ends the "for loop"
    timeStep = int(input("Enter # of years per time-step here (leave blank to keep at default of 100 years): ") or '100') #years
    waterDepth = int(input("Enter water depth in meters (leave blank to keep at default of 4000 meters): ") or '4000') #meters

    L = 1350 #W/m2
    albedo = 0.3
    epsilon = 1
    sigma = 5.67E-8 #W/m2 K4

    heatCapacity = waterDepth * 4.2E6  #J/K m2, second number is the heat capacity of water, multiplied by density of water
    time_list = [0] #list of time-steps
    temperature_list = [0] #list of temperatures per time-step, in K
    heatContent = 0 #sets heat content at zero, since the zero timeStep has an earth temperature of 0
    heatIn = L * (1 - albedo)/4
    heatOut = 0 #set at zero, since the zero timeStep has an earth temperature of zero

    for steps in range (0, nSteps):
        time_list.append(timeStep + time_list[-1]) #time_list column, calculates each timeStep from the last timeStep amount, and adds it to the column/list
        heatContent = heatContent + (heatIn - heatOut) * 3.154e+7 * timeStep #last number equals seconds/year
        temperature_list.append(heatContent/heatCapacity) #temperature_list column, calculates temperature of each timeStep, and adds it to the column/list
        heatOut = epsilon * sigma * pow(temperature_list[-1],4) #last temperature in list, to power of 4

    print('\nTemperature of last time-step: ' + str(temperature_list[-1]) + ' ˚K \nOutgoing heat of last time-step: ' + str(heatOut) + ' W/m2') #prints last time-step's outgoing heat and temperature
    plt.plot(time_list, temperature_list)
    plt.title('Temperature of a "Naked Earth" over Time') #adds main title to graph
    plt.xlabel('Time (in years)') #adds title to x-axis
    plt.ylabel('Temperature (in K)') #adds title to y-axis
    plt.show()

   
    exit_or_not = input('\nWould you like to try again? (y/n) ')
    if exit_or_not == 'y' or exit_or_not == 'Y':
        continue
    else:
        print('\nSee you next time ... !\n')
        break
            
        
