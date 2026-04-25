# Production Planning Problem

This folder contains an **Integer Programming** model for a production planning problem.

The goal of the problem is to determine the optimal production schedule over a planning horizon of 7 days, while minimizing the total inventory cost and satisfying demand, production capacity and inventory requirements.

The model is implemented in **Xpress Mosel**.

---

## Problem Description

The problem considers:

- a set of products;
- a set of production days;
- the daily demand for each product;
- the initial inventory level of each product;
- the production rate for each product;
- the inventory holding cost for each product;
- the setup/changeover time between products;
- the required final inventory level.

Each day, only one product can be produced.

If the production changes from one product to another, the available production time is reduced according to the corresponding changeover time.

The decision variables determine which product is produced on each day, the quantity produced, the inventory level at the end of each day and whether a changeover between products occurs.

The objective is to minimize the total inventory holding cost over the entire planning horizon.

This is an example of an **Integer Programming** problem applied to production planning and inventory management.

---

## Files

```text
Production Problem/
│
├── README.md
├── ProductionOpt.mos
└── Produzione1.txt
```

### File Description

- `ProductionOpt.mos`  
  Main Xpress Mosel model. It defines the decision variables, constraints and objective function.

- `Produzione1.txt`  
  Input data file containing the products, days, demand values, initial inventory, production rates, inventory costs and changeover times.

---

## How to Run

To run the model, open `ProductionOpt.mos` in **FICO Xpress Mosel**.

Make sure that `Produzione1.txt` is located in the same folder as the model file.
