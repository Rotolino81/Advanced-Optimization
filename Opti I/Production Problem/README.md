# Production Planning Problem

This folder contains an Integer Programming model for a production planning problem.

The goal of the problem is to determine the optimal production schedule over a planning horizon of 7 days, minimizing the total inventory cost while satisfying daily demand, production capacity and inventory requirements.

The model considers:

- a set of products;
- a set of production days;
- daily demand for each product;
- initial inventory levels;
- production rate for each product;
- inventory holding costs;
- setup/changeover times between products;
- final inventory requirements.

Each day, only one product can be produced.  
If the production changes from one product to another, the available production time is reduced according to the corresponding changeover time.

The decision variables determine:

- which product is produced on each day;
- the quantity produced of each product;
- the inventory level of each product at the end of each day;
- whether a changeover between two products occurs.

The objective function minimizes the total inventory cost over the planning horizon.

The model is implemented in **Xpress Mosel**.
