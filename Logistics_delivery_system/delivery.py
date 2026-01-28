import json
import math
import sys
import csv
import os

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def normalize_warehouses(warehouses):
    if isinstance(warehouses, list):
        return {w["id"]: w["location"] for w in warehouses}
    return warehouses


def normalize_agents(agents):
    if isinstance(agents, list):
        return {a["id"]: a["location"] for a in agents}
    return agents


def simulate_delivery(data):
    warehouses = normalize_warehouses(data["warehouses"])
    agents = normalize_agents(data["agents"])
    packages = data["packages"]

    report = {}
    for agent_id in agents:
        report[agent_id] = {
            "packages_delivered": 0,
            "total_distance": 0.0,
            "efficiency": 0.0
        }

    for pkg in packages:
        warehouse_id = pkg.get("warehouse") or pkg.get("warehouse_id")
        warehouse_loc = warehouses[warehouse_id]

        nearest_agent = None
        min_distance = float("inf")

        for agent_id, agent_loc in agents.items():
            dist = euclidean_distance(agent_loc, warehouse_loc)
            if dist < min_distance:
                min_distance = dist
                nearest_agent = agent_id

        agent_loc = agents[nearest_agent]
        destination = pkg["destination"]

        travel_distance = (
            euclidean_distance(agent_loc, warehouse_loc) +
            euclidean_distance(warehouse_loc, destination)
        )

        report[nearest_agent]["packages_delivered"] += 1
        report[nearest_agent]["total_distance"] += travel_distance

    best_agent = None
    best_efficiency = float("inf")

    for agent_id, stats in report.items():
        if stats["packages_delivered"] > 0:
            stats["total_distance"] = round(stats["total_distance"], 2)
            stats["efficiency"] = round(
                stats["total_distance"] / stats["packages_delivered"], 2
            )

            if stats["efficiency"] < best_efficiency:
                best_efficiency = stats["efficiency"]
                best_agent = agent_id
        else:
            stats["total_distance"] = 0.0
            stats["efficiency"] = 0.0

    report["best_agent"] = best_agent
    return report


def export_best_agent_to_csv(report, csv_filename):
    best_agent = report.get("best_agent")
    if not best_agent:
        return

    stats = report[best_agent]

    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["agent_id", "packages_delivered", "total_distance", "efficiency"])
        writer.writerow([
            best_agent,
            stats["packages_delivered"],
            stats["total_distance"],
            stats["efficiency"]
        ])


def main():
    if len(sys.argv) < 2:
        print("Usage: python delivery.py <input_json_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    report = simulate_delivery(data)

    # derive base name from input file
    base_name = os.path.splitext(os.path.basename(input_file))[0]


    report_file = f"report_{base_name}.json"
    csv_file = f"top_performer_{base_name}.csv"


    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)
    export_best_agent_to_csv(report, csv_file)

    print(f"Report generated: {report_file}")
    print(f"Top performer exported: {csv_file}")


if __name__ == "__main__":
    main()