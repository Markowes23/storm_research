"""Utility functions for recommending plants and watering schedules."""

import argparse
import json
from pathlib import Path


PLANT_DATA = Path(__file__).parent / "plant_data.json"


def load_plants():
    with open(PLANT_DATA, "r", encoding="utf-8") as f:
        return json.load(f)


def recommend_plants(plants, climate, sunlight, soil):
    """Return plants matching climate, sunlight, and soil preferences."""
    matches = []
    for plant in plants:
        if climate and climate not in plant["climate"]:
            continue
        if soil and plant["soil"] != soil:
            continue
        if sunlight and not plant["sunlight"].startswith(sunlight.split()[0]):
            continue
        matches.append(plant)
    return matches


def watering_schedule(plant, rainfall):
    """Return weekly water requirement and number of waterings."""
    required = max(plant["water_mm_per_week"] - rainfall, 0)
    if required == 0:
        times = 0
    elif required < 10:
        times = 1
    elif required < 20:
        times = 2
    else:
        times = 3
    return required, times


def watering_string(plant, rainfall):
    required, times = watering_schedule(plant, rainfall)
    if times == 0:
        return "no extra watering needed"
    plural = "time" if times == 1 else "times"
    return f"water {required}mm/week ({times} {plural})"


def main():
    parser = argparse.ArgumentParser(description="Simple garden planner")
    parser.add_argument("--climate", required=True, help="Local climate zone")
    parser.add_argument("--sunlight", required=True, help="Sunlight exposure")
    parser.add_argument("--soil", required=True, help="Soil type")
    parser.add_argument(
        "--rainfall",
        type=float,
        default=0.0,
        help="Weekly rainfall in millimeters",
    )
    args = parser.parse_args()

    plants = load_plants()
    matches = recommend_plants(plants, args.climate, args.sunlight, args.soil)

    if not matches:
        print("No matching plants found for the specified conditions.")
        return

    print("Recommended plants:")
    for plant in matches:
        required, times = watering_schedule(plant, args.rainfall)
        print(f"- {plant['name']}: water {required}mm/week ({times}x)")


if __name__ == "__main__":
    main()
