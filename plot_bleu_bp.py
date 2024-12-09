import json
import matplotlib.pyplot as plt

# Initialize lists to store beam sizes, BLEU scores, and BP values
beam_sizes = []
bleu_scores = []
brevity_penalties = []

# Loop through the files bleu_output_k1.json to bleu_output_k25.json
for k in range(1, 26):
    file_name = f"translation_results/bleu_output_k{k}.json"
    try:
        # Open and load the JSON file
        with open(file_name, "r") as f:
            data = json.load(f)
        
        # Extract BLEU score and BP from the file
        bleu_score = data.get("score", 0)
        verbose_score = data.get("verbose_score", "")
        
        # Extract BP from the verbose_score string
        bp = 1.0  # Default BP is 1.0 (no penalty)
        if verbose_score:
            bp = float(verbose_score.split("BP = ")[1].split()[0])
        
        # Append data to lists
        beam_sizes.append(k)
        bleu_scores.append(bleu_score)
        brevity_penalties.append(bp)
    
    except FileNotFoundError:
        print(f"Warning: {file_name} not found. Skipping...")
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

# Plot BLEU Score and Brevity Penalty
fig, ax1 = plt.subplots()

# Plot BLEU score on the left y-axis
ax1.set_xlabel("Beam Size (k)")
ax1.set_ylabel("BLEU Score", color="tab:blue")
ax1.plot(beam_sizes, bleu_scores, color="tab:blue", marker="o", label="BLEU Score")
ax1.tick_params(axis="y", labelcolor="tab:blue")

# Create a second y-axis for BP
ax2 = ax1.twinx()
ax2.set_ylabel("Brevity Penalty (BP)", color="tab:red")
ax2.plot(beam_sizes, brevity_penalties, color="tab:red", marker="x", label="BP")
ax2.tick_params(axis="y", labelcolor="tab:red")

# Title and grid
fig.suptitle("BLEU Score and Brevity Penalty vs Beam Size")
ax1.grid(True)

# Add legends
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.8))

# Save the plot
plt.savefig("bleu_bp_vs_beam_size.png")
plt.show()
