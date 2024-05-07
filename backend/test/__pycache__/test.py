import json
from datetime import datetime
import matplotlib.pyplot as plt

def save_plot_scores():
    file_path = "D:\\PROJECT\\Newfolder\\its\\backend\\database\\quiz_scores.json"  # Adjust path as necessary
    output_path = "quiz_scores_plot.png"  # Adjust path as necessary
    try:
        with open(file_path, "r") as file:
            scores = json.load(file)
    except FileNotFoundError:
        print("Score file not found. Please take some quizzes first.")
        return

    score_values = [score["score"] for score in scores]
    timestamps = [datetime.fromisoformat(score["timestamp"]).strftime('%Y-%m-%d %H:%M:%S') for score in scores]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, score_values, marker='o', linestyle='-', color='b')
    plt.title('Quiz Scores Over Time')
    plt.xlabel('Attempt Timestamp')
    plt.ylabel('Score (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# Call this function to generate and save the plot
save_plot_scores()
import os
print("Current working directory:", os.getcwd())


