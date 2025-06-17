import pandas as pd
from clean_data import clean_sensor_data
import os


class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        """
def evaluate_single_reading(self, row):
        """
        Evaluate a single water quality reading.
        
        Args:
            row (pd.Series): Single row of water quality data
            
        Returns:
            dict: Evaluation results with safety status and reasons
        """
        issues = []
        
        # Check for missing pH
        if row.get('missing_ph', False) or pd.isna(row.get('ph')):
            issues.append('missing pH')
        elif row['ph'] < self.ph_min:
            issues.append('pH too low')
        elif row['ph'] > self.ph_max:
            issues.append('pH too high')
        
        # Check for missing turbidity
        if row.get('missing_turbidity', False) or pd.isna(row.get('turbidity')):
            issues.append('missing turbidity')
        elif row['turbidity'] > self.turbidity_max:
            issues.append('turbidity too high')
        
        is_safe = len(issues) == 0
        
        return {
            'is_safe': is_safe,
            'issues': issues,
            'status': 'Safe' if is_safe else 'Unsafe',
            'reason': ', '.join(issues) if issues else 'All parameters within safe range'
        }
def evaluate_all_readings(self, df):
        """
        Evaluate all water quality readings in the DataFrame.
        
        Args:
            df (pd.DataFrame): Water quality data
            
        Returns:
            pd.DataFrame: Original data with evaluation results
        """
        results = []
        
        for _, row in df.iterrows():
            evaluation = self.evaluate_single_reading(row)
            results.append(evaluation)
        
        # Add evaluation results to DataFrame
        results_df = df.copy()
        results_df['is_safe'] = [r['is_safe'] for r in results]
        results_df['status'] = [r['status'] for r in results]
        results_df['reason'] = [r['reason'] for r in results]
        
        return results_df
