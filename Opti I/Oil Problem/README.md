# Oil Transportation Problem

This folder contains a **Linear Programming** model for an oil transportation problem.

The goal of the problem is to determine the optimal quantity of oil to transport between different ports while minimizing the total transportation cost and satisfying supply, demand and flow conservation constraints.

The model is implemented in **Xpress Mosel**.

---

## Problem Description

The problem considers:

- a set of origin ports;
- a set of destination ports;
- intermediate ports;
- the available supply at each origin;
- the required demand at each destination;
- transportation routes between ports;
- the unit transportation cost for each route.

The decision variables represent the quantity of oil transported from one port to another.

The objective is to minimize the total transportation cost over all available routes.

The model also includes flow conservation constraints for intermediate ports, ensuring that the amount of oil entering an intermediate node is equal to the amount leaving it.

This is an example of a **Linear Programming** problem applied to transportation and logistics.

---

## Files

```text
Oil Problem/
│
├── README.md
├── ProblemaLP_TransportePetroleo.mos
└── TransportePetroleo.txt
```

### File Description

- `ProblemaLP_TransportePetroleo.mos`  
  Main Xpress Mosel model. It defines the decision variables, constraints and objective function.

- `TransportePetroleo.txt`  
  Input data file containing the transportation network, supply values, demand values and transportation costs.

---

## How to Run

To run the model, open `ProblemaLP_TransportePetroleo.mos` in **FICO Xpress Mosel**.

Make sure that `TransportePetroleo.txt` is located in the same folder as the model file.
