# Mystery Delivery System – Python Assignment

## 📦 Overview
This project simulates one day of operations for a fictional logistics company called **FastBox**.  
The system assigns packages to delivery agents based on proximity, simulates deliveries, and generates a performance report.

The solution prioritizes **correctness, simplicity, and robustness**, and includes one optional bonus feature.

---

## 🧩 Problem Description
The system is provided with:
- A set of **warehouses**, each with a 2D coordinate
- A set of **delivery agents**, each with a starting location
- A list of **packages**, where each package belongs to a warehouse and has a delivery destination

The goal is to simulate deliveries for a single day and determine:
- How many packages each agent delivers
- The total distance traveled by each agent
- The most efficient delivery agent

---

## ✅ Solution Approach
1. Parse input data from a JSON file
2. Assign each package to the **nearest delivery agent** based on Euclidean distance from the agent to the package’s warehouse
3. Simulate delivery as:
   - Agent → Warehouse → Destination
4. Accumulate total distance traveled per agent
5. Compute agent efficiency as:
   ```
   efficiency = total_distance / packages_delivered
   ```
6. Identify the **best-performing agent** (lowest efficiency)
7. Generate output reports

---

## ⭐ Features Implemented

### Core Features
- JSON parsing with support for multiple input formats
- Euclidean distance calculation
- Nearest-agent assignment logic
- Delivery simulation
- Agent performance reporting
- Best agent identification
- Output written to `report.json`

### Bonus Feature
- **Export top-performing agent to CSV** (`top_performer.csv`)

---

## 📂 Project Structure
```
delivery.py
README.md
base_case.json
test_case_1.json
test_case_2.json
test_case_3.json
test_case_4.json
test_case_5.json
test_case_6.json
test_case_7.json
test_case_8.json
test_case_9.json
test_case_10.json
```

---

## ▶️ How to Run

### Requirements
- Python 3.x
- No external dependencies

### Command
```bash
python delivery.py <input_json_file>
```

### Example
```bash
python delivery.py base_case.json
```

---

## 📤 Output Files

### Output Files

For each input JSON file, the program generates:

#### `report_<input_file>.json`
Contains performance details for each agent, including:
- Packages delivered
- Total distance traveled
- Efficiency
- Best-performing agent

#### `top_performer_<input_file>.csv` (Bonus)
Exports the top-performing agent’s performance in CSV format.

---

## 📌 Assumptions
- Agent locations remain fixed throughout the day
- Each package is delivered independently
- All distances are calculated using Euclidean distance
- Input JSON files are valid and correctly formatted

---

## 🧪 Testing
The solution was tested against:
- `base_case.json`
- 10 additional test cases with varied agent and warehouse distributions

All test cases executed successfully without errors.

---

