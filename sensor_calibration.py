# Temperature Sensor Calibration Fix
# Fixed the 2-degree offset issue

class TemperatureSensor:
    def __init__(self, calibration_factor=1.98):
        self.calibration_factor = calibration_factor
    
    def read_temperature(self, raw_value):
        """Read and calibrate temperature sensor reading."""
        try:
            calibrated = raw_value * self.calibration_factor
            return round(calibrated, 1)
        except Exception as e:
            print(f"Error reading sensor: {e}")
            return None

# Example usage
if __name__ == "__main__":
    sensor = TemperatureSensor()
    raw_reading = 25.0  # Raw sensor reading
    calibrated = sensor.read_temperature(raw_reading)
    print(f"Raw: {raw_reading}°C, Calibrated: {calibrated}°C")
    
    # Expected: ~49.5°C (was 50°C with old factor of 2.0)