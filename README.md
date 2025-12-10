The project structure is as follow:

AI-for-SaO/
├── data/
│   └── cities.csv                    # City coordinates dataset
├── src/
│   ├── notebook.ipynb               # Main Jupyter notebook with implementations
├── results/
│   ├── All results    
├── report                            # Report for mor details
└── README.md                         # This file


# Overview

This project explores the Travelling Salesman Problem (TSP) using different AI search and optimisation techniques. The goal is to compare the performance of Iterated Local Search (ILS), Genetic Algorithms (GA), Simulated Annealing (SA), and Tabu Search (TS) on the same dataset.
The repository contains the dataset, the implementation notebook, experiment results, and the final report summarising findings.

# Setup

Follow these steps to set up the project:
1. Clone the repository
git clone https://github.com/Side941/AI-for-SaO.git
cd AI-for-SaO
2. Install required dependencies
Make sure you have Python 3.8+ installed. Then install the required packages:
pip install -r requirements.txt
3. Open the Jupyter notebook
jupyter notebook src/notebook.ipynb

# Usage
Running the algorithms
Open the notebook: src/notebook.ipynb and run all cells