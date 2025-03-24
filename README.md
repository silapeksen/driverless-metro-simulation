# Driverless Metro Simulation (Route Optimization)

## About the Project  

This project was developed as part of the **Akbank & Turkish AI Hub "Python for AI" Bootcamp**. The goal is to simulate a **driverless metro system** by optimizing route selection using **graph algorithms**.  

The simulation determines:  
- **Least transfer route** using **Breadth-First Search (BFS)**
 **Fastest route** using **A* algorithm**  

By modeling the metro network as a **graph**, the program efficiently finds optimal routes between stations. This project provides hands-on experience in **graph theory, algorithm implementation, and real-world problem-solving**. It can be further extended with **visualization, real-world metro data, or additional features**.  

## Features  

- **Graph-Based Metro Network** – Models metro stations and connections  
- **BFS Algorithm** – Finds the route with **minimum transfers**  
- **A* Algorithm** – Determines the **fastest route** based on travel time  
- **Scalable & Customizable** – Supports real metro networks  
- **Tested & Verified** – Ensures correctness with multiple test cases   

## Algorithms  

### Breadth-First Search (BFS) – Least Transfer Route  
BFS algorithm is used to find the shortest path with the **least number of transfers**. It works by exploring all possible paths from the starting station, prioritizing direct connections and avoiding unnecessary detours.  

### A* Algorithm – Fastest Route  
The A* algorithm finds the **fastest route** by considering both the **travel time** and a **heuristic estimate** of the remaining distance. It uses a priority queue to efficiently determine the best path to the destination.  

## Future Improvements  

- Integration of **real-world metro networks** for more accurate simulations.  
- Development of a **graphical user interface (GUI)** for interactive visualization.  
- Implementation of **real-time metro movement simulation** to analyze different scenarios dynamically.  

## License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.  

## Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/driverless-metro-sim.git
   cd driverless-metro-sim

## Usage  

Run the simulation with a sample metro network:  

```python
from metro_simulation import find_least_transfer_route, find_fastest_route  

# Define a metro network  
metro_network = {  
    "A": {"B": 2, "C": 5},  
    "B": {"A": 2, "D": 3},  
    "C": {"A": 5, "D": 1},  
    "D": {"B": 3, "C": 1, "E": 4},  
    "E": {"D": 4}  
}  

# Find least transfer route  
route = find_least_transfer_route(metro_network, "A", "E")  
print("Least transfer route:", route)  

# Find fastest route  
route = find_fastest_route(metro_network, "A", "E")  
print("Fastest route:", route)  
