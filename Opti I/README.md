# Integer Programming Models

This section contains the first part of the **Advanced Optimization** course project.

The focus of this module is on the formulation and implementation of exact optimization models, mainly based on **Linear Programming** and **Integer Programming**, applied to real-world decision-making problems.

The models are implemented in **Xpress Mosel**.

---

## Overview

This section presents three optimization problems inspired by practical applications in logistics, production planning and resource allocation.

Each problem is modeled by identifying the main elements of a mathematical optimization formulation:

- decision variables;
- objective function;
- constraints;
- input data;
- optimal solution.

The goal is to show how real-world operational problems can be translated into mathematical models and solved using an exact optimization solver.

---

## Problems Included

The problems described in this section cover different application areas:

### Oil Transportation Problem

The `Oil Problem` folder contains a **Linear Programming** model for an oil transportation problem.

The goal is to determine the optimal quantity of oil to transport between different ports while minimizing the total transportation cost and satisfying supply, demand and flow conservation constraints.

This problem is an example of a transportation and network flow model.

---

### Production Planning Problem

The `Production Problem` folder contains an **Integer Programming** model for a production planning problem.

The goal is to determine the optimal production schedule over a planning horizon of 7 days, while minimizing inventory costs and satisfying demand, production capacity and inventory requirements.

This problem is an example of production planning and inventory management using integer decision variables.

---

### Wagon Loading Problem

The `Vagon Problem` folder contains an **Integer Programming** model for a wagon loading problem.

The goal is to assign a set of boxes to a fixed number of wagons while respecting the maximum capacity of each wagon and balancing the total load among them.

This problem is an example of an assignment and load balancing model with binary decision variables.


---

## Repository Structure

```text
Opti I/
│
├── README.md
│
├── Oil Problem/
│   ├── README.md
│   ├── ProblemaLP_TransportePetroleo.mos
│   └── TransportePetroleo.txt
│
├── Production Problem/
│   ├── README.md
│   ├── ProductionOpt.mos
│   └── Produzione1.txt
│
└── Vagon Problem/
    ├── README.md
    ├── ProblemaEP_Vagoni.mos
    └── Vagoni.txt
```

---

## Content

The models in this section are implemented using:

```text
Xpress Mosel
```

The main file types are:

```text
.mos   Mosel source code
.txt   Input data files
.md    Project documentation
```

The `.mos` files contain the mathematical models, while the `.txt` files contain the input data required to run each model.

---

## Notes

Generated files such as `.bim` and `.bdg` are not included in the cleaned project structure because they are automatically created by Xpress Mosel.

The original PDF problem statements have been replaced by individual `README.md` files inside each problem folder, making the repository easier to read and navigate.

