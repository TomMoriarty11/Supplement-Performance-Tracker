# How to Run the Supplement Performance Tracker

This guide walks you through running the Python script to analyze supplement effectiveness.

---

## Step 1: Clone or Download the Repository
git clone https://github.com/yourusername/supplement-performance-tracker.git
cd supplement-performance-tracker

# Step 2: Install Dependencies
pip install -r requirements.txt

# Step 3: Run the Script
python scripts/analyze_tracker.py

# Explanation
 This will load the CSV file from data/supplenment_log.csv
 Analyze average effectiveness per day
 Generate a graph saved to visuals/effectiveness_trend.png

 # Step 4: View the Output
 Open the image file in the visuals/ folder to see you supplement performance trend.
