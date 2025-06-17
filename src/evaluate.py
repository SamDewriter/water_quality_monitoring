from typing import Dict, Optional

class WaterQualityEvaluator:
    """
    Evaluates water quality based on sensor readings.
    """
    
    # Safe ranges
    SAFE_PH_MIN = 6.5
    SAFE_PH_MAX = 7.5
    SAFE_TURBIDITY_MAX = 1.0
    
    def evaluate_sensor(self, sensor_data: Dict) -> Dict:
        """
        Evaluate a single sensor's water quality.
        
        Args:
            sensor_data: Dictionary containing sensor readings
            
        Returns:
            Dictionary with evaluation results
        """
        result = {
            'sensor_id': sensor_data.get('sensor_id'),
            'location': sensor_data.get('location'),
            'is_safe': True,
            'issues': []
        }
        
        # Check pH
        ph = sensor_data.get('ph')
        if ph is None:
            result['is_safe'] = False
            result['issues'].append('missing pH')
        elif ph < self.SAFE_PH_MIN:
            result['is_safe'] = False
            result['issues'].append('pH too low')
        elif ph > self.SAFE_PH_MAX:
            result['is_safe'] = False
            result['issues'].append('pH too high')
            
        # Check turbidity
        turbidity = sensor_data.get('turbidity')
        if turbidity is None:
            result['is_safe'] = False
            result['issues'].append('missing turbidity')
        elif turbidity > self.SAFE_TURBIDITY_MAX:
            result['is_safe'] = False
            result['issues'].append('turbidity too high')
            
        return result
    
    def format_result(self, evaluation: Dict) -> str:
        """
        Format the evaluation result as a readable string.
        
        Args:
            evaluation: Dictionary with evaluation results
            
        Returns:
            Formatted string with the evaluation
        """
        sensor_id = evaluation.get('sensor_id', 'Unknown')
        location = evaluation.get('location', 'Unknown location')
        status = "✅ Safe" if evaluation['is_safe'] else "❌ Unsafe"
        
        if evaluation['issues']:
            issues = " (" + ", ".join(evaluation['issues']) + ")"
        else:
            issues = ""
            
        return f"Sensor {sensor_id} at {location}: {status}{issues}"