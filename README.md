# Welcome to my Naked Planet Simulator

This is a program based on the "Time-Stepping Naked Planet Model" that is a part of the "Global Warming II: Create You Own Models in Python" Coursera course, provided by the University of Chicago.

This main output of this program is a line graph that charts a simulation of the change in planetary temperature of a "water-only" Earth throughout time. If enough time passes in the simulation, the planetary temperature (which is synonymous with water temperature in this simulation) will reach "equilibrium" and plateau.

The main point of this program is to show how water depth, as an isolated phenomenon, affects the overall temperature of Earth.

## How to use the program

The simulation starts from a temperature of 0° Kelvin, and increases in temperature as time moves forward. The program allows you to input a custom number of "steps" through time, a custom number of years per "time-step" (between 0-100), and a custom water depth in meters. If left blank, these values default to 20 (steps), 50 (years), and 4000 (meters) respectively.

## What the program does, in simple terms

After these values are inputted, they work in conjunction with a few constants to create:

1. Heat Capacity: the ability of the simulated water to retain incoming heat (sunlight) per second
2. Heat Content: the amount of heat present on the simulated Earth/water per second
3. Heat In: a fixed amount of incoming heat (based on constants of sunlight [L] and albedo values) per second
4. Heat Out: a growing amount of outgoing heat (based on constants of epsilon, sigma, as well as growing temperature values)

Along the way, temperature per time-step is appended to a temperature array, that grows in tandem with a time-step array, for the purposes of plotting them on the final simulation graph.

Have fun using the program!

