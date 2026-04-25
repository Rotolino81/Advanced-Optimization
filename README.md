# Advanced Optimization

Repository for the **Advanced Optimization** course at UDLAP.

The project collects different optimization models and algorithms developed during the course, with a focus on:

- Integer Programming
- Linear Programming
- Greedy Algorithms
- Heuristics
- Metaheuristics

Most of the implementations are written in **Xpress Mosel**, together with input files and supporting material used to model and solve the optimization problems.

---

## Project Overview

The repository is divided into three main optimization modules, plus an additional assignment section.

Each folder contains a specific set of problems, models or algorithms. The objective of the repository is to show how different optimization techniques can be applied to solve classical problems such as transportation, production planning, assignment, graph coloring, maximum clique, knapsack and routing-related problems.

---

## Repository Structure

```text
Advanced-Optimization/
│
├── Assignment/
│   ├── Trial12.mos
│   ├── Trial12.bim
│   ├── Trial12.bdg
│   └── chlond-toase-2003-ip-modeling-and-the-logical-puzzles-of-raymond-smullyan.pdf
│
├── Opti I/
│   ├── Oil Problem/
│   ├── Production Problem/
│   └── Vagon Problem/
│
├── Opti II/
│   ├── ColoringGraphGreedy-RLF/
│   ├── KruskalGreedy/
│   ├── MaxCiqueModel/
│   ├── MaxCliqueGreedy/
│   └── MochillaGready/
│
├── Opti III/
│   ├── AntColony/
│   ├── AntColoringGraph/
│   ├── KrusaklVoraz/
│   ├── KruskalGRASP/
│   ├── KruskalSemiVoraz/
│   └── kColoringTABU/
│
└── README.md
