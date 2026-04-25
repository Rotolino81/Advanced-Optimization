# Opti I — Integer Programming Models

This section contains the first part of the **Advanced Optimization** course project.

The focus of this module is on the formulation and implementation of mathematical optimization models, mainly based on **Linear Programming** and **Integer Programming**, applied to real-world decision-making problems.

The models are implemented using **Xpress Mosel** and are designed to solve practical optimization problems such as transportation planning, production scheduling and wagon loading.

---

## Overview

The objective of this section is to translate real-world problems into mathematical optimization models.

Each problem is formulated by defining:

- decision variables;
- objective function;
- operational constraints;
- input data;
- optimal solution and interpretation of the results.

The problems included in this section show how optimization can be used to support decisions in logistics, production and resource allocation.

---

## Repository Structure

```text
Opti I/
│
├── Oil Problem/
│   ├── ProblemaLP_TransportePetroleo.mos
│   ├── TransportePetroleo.txt
│   ├── ProblemaLP_TransportePetroleo.bim
│   └── ProblemaLP_TransportePetroleo.bdg
│
├── Production Problem/
│   ├── ProductionOpt.mos
│   ├── Produzione1.txt
│   ├── Proyecto de modelado.pdf
│   ├── ProductionOpt.bim
│   └── ProductionOpt.bdg
│
└── Vagon Problem/
    ├── ProblemaEP_Vagoni.mos
    ├── Vagoni.txt
    ├── Caso de clase - Asignación de cajas a vagones(1) (1).pdf
    ├── vagones(1).py
    ├── ProblemaEP_Vagoni.bim
    └── ProblemaEP_Vagoni.bdg
