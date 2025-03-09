import matplotlib.pyplot as plt
import json
from shapely.geometry import box

def draw_2d_model(ai_response):
    try:
        # Convert AI response to structured data
        data = json.loads(ai_response)
        width = data.get("width", 10)
        length = data.get("length", 30)

        # Create a figure
        fig, ax = plt.subplots()
        ax.set_xlim(0, length)
        ax.set_ylim(0, width)

        # Draw road (rectangle)
        road = box(0, 0, length, width)
        x, y = road.exterior.xy
        ax.fill(x, y, color="gray")

        # Save the model
        plt.savefig("2d_model.png")
        print("2D Model Generated: 2d_model.png")

    except Exception as e:
        print("Error generating 2D model:", str(e))

if __name__ == "__main__":
    sample_response = '{"width": 10, "length": 30}'
    draw_2d_model(sample_response)
