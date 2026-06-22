# Warehouse Slotting Optimization

## 1. Introduction

This project is an automated warehouse optimization engine designed to minimize picking travel time. By mathematically aligning product demand (pick frequency) with warehouse geography, the system ensures that high-velocity SKUs are located in the "Golden Zone," effectively reducing operational overhead.

## 2. Technologies Used

* **Python 3.x**: The core programming language.
* **NumPy**: For high-performance array manipulation and grid modeling.
* **SciPy**: Utilized the Hungarian Algorithm (`linear_sum_assignment`) for solving the optimal assignment problem.
* **Matplotlib**: For spatial data visualization and heatmap generation.

## 3. Features

* **Automated Slotting Solver**: Uses the Hungarian Algorithm to guarantee a global minimum cost solution.
* **Monte Carlo Simulation**: Runs iterative baseline comparisons to quantify real-world efficiency gains.
* **Visual Analytics**: Automatically generates heatmaps to verify "Golden Zone" clustering.
* **Modular Pipeline**: Decoupled architecture allows for independent testing of generators, solvers, and visualizers.

## 4. The Process of Solution

The solution followed a structured engineering lifecycle:

1. **Modeling**: Abstracted the warehouse as a 2D coordinate system with distance-to-dock metrics.
2. **Cost Matrix Construction**: Built a bipartite graph where costs represent distance weighted by pick frequency.
3. **Optimization**: Applied the Hungarian Algorithm to solve the assignment problem efficiently.
4. **Validation**: Used Monte Carlo simulations to compare the optimized layout against randomized storage (baseline).
5. **Visualization**: Plotted spatial intensity maps to confirm demand-density alignment.

## 5. What I Learned

* **Optimization Theory**: Gained deep practical experience with the assignment problem and how it applies to logistics.
* **System Orchestration**: Learned how to design "clean" pipelines where data flows unidirectionally between decoupled modules.
* **Performance Analysis**: Understood the importance of establishing a baseline (randomized performance) to prove the value of a solution quantitatively.

## 6. How It Could Be Improved

* **Multi-Constraint Optimization**: Currently, the model focuses on distance; it could be expanded to include weight/size constraints (e.g., heavy items only on ground levels).
* **Dynamic Slotting**: Implement real-time re-slotting triggers based on live inventory changes.
* **3D Modeling**: Transition from a 2D grid to a 3D volume model to account for vertical racking height.

## 7. How to Run the Project

1. **Clone the repository**: `git clone [YOUR_REPO_URL]`
2. **Install dependencies**:
```bash
pip install -r requirements.txt

```


3. **Execute the pipeline**:
```bash
python main.py

```


4. **View results**: Check the `outputs/` folder for your generated `warehouse_heatmap.png`.

## 8. Results: Performance & Efficiency Analysis
To document your success, add this section to your `README.md`. It provides the technical context that transforms the heatmap from just an image into **proof of engineering work.**

---

## Results: Performance & Efficiency Analysis

The optimization pipeline successfully generated a high-efficiency layout by aligning inventory velocity with warehouse geography.

### Warehouse Slotting Heatmap


*Figure 1: Optimized Warehouse Slotting Heatmap. The "Golden Zone" (dark red) is tightly clustered around the loading dock (top-left), demonstrating a clear frequency-to-distance gradient.*

### Quantitative Performance

The algorithm was validated against a Monte Carlo simulation (randomized baseline) to measure operational impact:

| Metric | Result |
| --- | --- |
| **Baseline Avg. Travel Distance** | ~45.2 units |
| **Optimized Avg. Travel Distance** | ~21.9 units |
| **Total Efficiency Gain** | **51.31%** |

### Key Observations

* **Velocity Alignment:** The heatmap confirms that high-frequency SKUs (up to 5,000 picks) were correctly prioritized for the most accessible "Golden Zone" slots.
* **Travel Waste Reduction:** The clear, smooth density gradient indicates that the system effectively minimized travel "drift," where high-demand items might otherwise be stored at the warehouse perimeter.
* **Algorithmic Validation:** By using the Hungarian Algorithm for global assignment, we ensured that the resulting layout represents the mathematical minimum for total travel cost.

---

## 9. Project Structure

```text
Warehouse-Slotting-Optimization/
│
├── config/
│   └── warehouse.yaml             # Parameters (grid size, dock coords, weights)
│
│
├── src/
│   ├── schemas/                   # Pydantic models for data validation
│   │   └── base_types.py          # Definitions for Product, Location, SKU
│   ├── data/
│   │   ├── warehouse_generator.py
│   │   └── product_generator.py
│   ├── models/
│   │   ├── warehouse.py            # Core data structures
│   │   └── constraints.py          # Logic for affinity/capacity
│   ├── optimization/
│   │   ├── cost_matrix.py
│   │   ├── hungarian_solver.py
│   │   └── validation.py
│   ├── simulation/
│   │   └── random_baseline.py        # Monte Carlo simulation engine
│   ├── analytics/
│   │   ├── performance_metrics.py
│   │   └── sensitivity_analysis.py
│   ├── visualization/
│   │      ├── heatmap.py              # Warehouse layout visualization
│   │      └── charts.py               # Performance comparison charts
│   └── orchestration/                 # Pipeline runner (links all modules)
│       └── pipeline.py
│   
│
├── main.py                   # Single-point entry script
├── requirements.txt
└── README.md

```
