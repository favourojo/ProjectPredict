# DonarsChoose Project Funding Predictions

ProjectPredict is a a machine learning project that utilizes data from DonorsChoose to identify projects that are least likely to be funded before they exprire. This tool aims to assist educators and donors by highlighting projects that may need additional support.
--- 

## Data Processing
The project merges datasets containing project details, donation history, and funding outcomes. It includes:
- Data cleaning and preprocessing (handling missing values, timestamp conversions)
- Feature engineering (interaction terms between state, poverty level, and donations)
- One-hot encoding categorical features

## Model Training
The ranking model is built using `RandomForestClassifier`:
- Features include subject focus, resource type, donations per student, and state interactions
- Training data is split, with iterative refinement to test precision improvements
- Performance evaluation is done using precision metrics

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






