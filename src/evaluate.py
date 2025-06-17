import pandas as pd


class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.min_ph, self.max_ph = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.

        Args:
            row (pd.Series): A row from the sensor data DataFrame.

        Returns:
            tuple: A tuple containing a boolean (True if safe, False if not)
                   and a string describing the status.
        """
        ph = row.get("pH")
        turbidity = row.get('turbidity')

        # Check for missing values first
        if pd.isnull(ph):
            return False, "Unsafe (missing pH)"
        if pd.isnull(turbidity):
            return False, "Unsafe (missing turbidity)"

        # Check against thresholds
        if not (self.min_ph <= ph <= self.max_ph):
            reason = "high" if ph > self.max_ph else "low"
            return False, f"Unsafe (pH too {reason})"

        if turbidity > self.turbidity_threshold:
            return False, "Unsafe (turbidity too high)"

        return True, "Safe"

    def evaluate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the evaluation logic to an entire DataFrame.

        Args:
            df (pd.DataFrame): The cleaned sensor data DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with a new 'status' column containing
                          the evaluation result string.
        """
        if df is None:
            return None
        
        print("Evaluating data...")
        # The apply function passes each row to our evaluate_row method
        results = df.apply(self.is_safe, axis=1, result_type='expand')
        
        # Rename the new columns created by the apply function
        results.columns = ['is_safe', 'status_message']

        # Join the results back to the original DataFrame
        evaluated_df = df.join(results)
        print("Evaluation complete.")
        print(evaluated_df)
        return evaluated_df