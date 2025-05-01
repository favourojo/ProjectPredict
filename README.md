# DonarsChoose Project Funding Predictions

ProjectPredict is a a machine learning project that utilizes data from DonorsChoose to identify projects that are least likely to be funded before they exprire. This tool aims to assist educators and donors by highlighting projects that may need additional support.
--- 

## Data Processing
The project merges datasets containing project details, donation history, and funding outcomes. It includes:
- Data cleaning and preprocessing (handling missing values, timestamp conversions)
- Feature engineering (interaction terms between state, poverty level, and donations)
- One-hot encoding categorical features

## Model Training
# Combining Random Forest & Logistic Regression for Optimized Ranking

Our ranking model leverages both **Random Forest and Logistic Regression** to balance **feature discovery and precision optimization**.

### Why Use Both Models?
1. **Random Forest** was initially employed to capture **nonlinear interactions** and assess broad feature importance. It effectively identified key drivers of funding success, such as `"days_since_posted"`, `"resource_type"`, and `"students_reached"`. However, while its classification was useful, **precision needed improvement**, particularly in minimizing false positives.
2. **Logistic Regression** was introduced to refine **ranking precision** by adjusting probability thresholds, ensuring more accurate prioritization of projects likely to remain unfunded. Unlike Random Forest, Logistic Regression provides **clear feature coefficient interpretations**, allowing for structured adjustments to ranking decisions. This transition significantly **reduced false positives**, ensuring expert reviewers could **focus on truly high-risk projects** while maintaining transparency in decision-making.

### Results & Precision Improvement
By using **both models strategically**, we balanced **feature discovery** (via Random Forest) with **precision enhancement** (via Logistic Regression). The final model achieved **higher precision**, enabling more effective donor prioritization while ensuring expert reviewers allocate resources efficiently.

### Key Features Driving Improvements
- **Time-Based Influences:** `"days_since_posted"`, `"month_posted"`, `"year_posted"`
- **Donation Metrics:** `"donation_total"`, `"donation_per_student"`
- **Subject & Resource Preferences:** `"primary_focus_subject"`, `"resource_type"`
- **Fairness Considerations:** `"state_poverty_interaction"`

### Conclusion
The **integration of Logistic Regression** greatly enhanced the ranking system, **boosting precision** and improving funding allocation. Future iterations can explore **bias audits, fairness-aware ranking adjustments, and additional feature engineering** to refine funding prioritization even further.


## Usage
Run the Jupyter notebook (`Rank.ipynb`) to:
1. Load and preprocess data
2. Train the ranking model
3. Evaluate predictions and ranking output

## Future Enhancements
- Investigate alternative models like XGBoost and CatBoost for better handling of categorical features
- Experiment with additional interaction terms for improved prediction accuracy
- Optimize dataset chunking for large-scale processing

## Installation & Setup 

### 1. Clone the repository 
```bash
git clone https://github.com/favourojo/ProjectPredict.git
cd ProjectPredict
```

### 2. Create a virtual environment 
```bash
jupyter lab
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```






