# Wagon Loading Problem

This folder contains an Integer Programming model for a wagon loading problem.

The goal of the problem is to assign a set of boxes to a fixed number of wagons while respecting the maximum capacity of each wagon and balancing the total load among them.

The model is implemented in **Xpress Mosel**.

---

## Problem Description

The problem considers:

- a set of boxes;
- a set of available wagons;
- the weight of each box;
- the maximum loading capacity of each wagon.

Each box must be assigned to exactly one wagon.

The objective is to minimize the maximum total weight assigned to any wagon.  
In this way, the model tries to distribute the boxes as evenly as possible among the wagons, while ensuring that no wagon exceeds its capacity.

This is an example of an **Integer Programming** problem with binary decision variables.

---

## Files

```text
Vagon Problem/
│
├── README.md
├── ProblemaEP_Vagoni.mos
└── Vagoni.txt
