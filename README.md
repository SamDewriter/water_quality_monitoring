# 💧 Water Quality Monitoring Project

This is a beginner-level Data Engineering project where you will build a simple pipeline using Python to process water sensor data and determine the safety of the water quality based on predefined thresholds.

---

## 🚀 Objectives

- Learn to structure a Python project.
- Use Git for version control and push to GitHub.
- Work with CSV files using `pandas`.
- Practice data cleaning and transformation.
- Implement logic using functions and classes.
- Understand how code modularity works.
- Collaborate via branches using Git.

---

## 🛠️ Getting Started

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/Water_Quality_Monitoring.git
cd Water_Quality_Monitoring
```

2. **Create a virtual environment and install dependencies**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate   #git-bash on windows: source venv/scripts/activate
pip install -r requirements.txt
```

---

## 🔧 Tasks to Complete

- `load_data.py`: Write a function to load a CSV file into a DataFrame.
- `clean_data.py`: Clean the data — handle missing values, fix invalid entries.
- `evaluate.py`: Write a class that checks if each row meets safe pH and turbidity ranges.
- `main.py`: Load, clean, evaluate, and print results — run your full pipeline here.

---

## 📊 Sample Data (`sensor_data.csv`)

```csv
sensor_id,location,ph,turbidity,temperature
1,Lake A,7.2,0.9,25
2,Lake B,8.7,1.1,23
3,Lake C,,0.5,22
4,Lake D,7.1,,24
5,Lake E,6.4,0.8,20
```

---

## 📤 Expected Output

```bash
Sensor 1 at Lake A: ✅ Safe
Sensor 2 at Lake B: ❌ Unsafe (pH too high)
Sensor 3 at Lake C: ❌ Unsafe (missing pH)
Sensor 4 at Lake D: ❌ Unsafe (missing turbidity)
Sensor 5 at Lake E: ❌ Unsafe (pH too low)
```

---

## 💡 Bonus (Optional)

- Save the output to `results.csv`.
- Accept location name as an input from the terminal.
- Count how many lakes are safe vs unsafe.
- Use classes to model sensor readings.

---

## 🧱 Project Structure

```bash
Water_Quality_Monitoring/
├── README.md
├── .gitignore
├── requirements.txt
├── data/
│   └── sensor_data.csv          # Raw sample sensor data
├── notebooks/                   # For exploration (optional)
├── src/
│   ├── load_data.py             # TODO: Write logic to load CSV file
│   ├── clean_data.py            # TODO: Write logic to clean data
│   ├── evaluate.py              # TODO: Write logic to assess water safety
│   └── main.py                  # TODO: Combine everything to run the pipeline
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add something'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request
