# Oil Transportation Problem

This folder contains a Linear Programming model for an oil transportation problem.

The goal of the problem is to determine the optimal quantity of oil to transport between different ports, minimizing the total transportation cost while satisfying supply, demand and flow conservation constraints.

The model represents the transportation network through:

- origin ports, with available supply;
- destination ports, with required demand;
- intermediate ports, where flow conservation must be respected;
- transportation routes, each associated with a unit cost.

The decision variables represent the quantity of oil transported from one port to another.  
The objective function minimizes the total transportation cost over all available routes.

The model is implemented in **Xpress Mosel**.
