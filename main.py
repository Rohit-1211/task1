import json
from datetime import datetime
import time

def convert_iso_to_ms(iso_timestamp):
    """
    Convert ISO format timestamp to milliseconds timestamp
    """
    # Parse the ISO timestamp string to datetime object
    dt = datetime.strptime(iso_timestamp, "%Y-%m-%dT%H:%M:%SZ")
    # Convert to milliseconds timestamp
    return int(dt.timestamp() * 1000)

def convert_format_1_to_unified(data):
    """
    Convert data from format 1 (ISO timestamps) to unified format
    """
    unified_data = {"unified_telemetry": []}
    
    for entry in data["telemetry"]:
        unified_entry = {
            "timestamp": convert_iso_to_ms(entry["timestamp"]),
            "temperature": entry["temperature"],
            "humidity": entry["humidity"],
            "pressure": entry["pressure"]
        }
        unified_data["unified_telemetry"].append(unified_entry)
    
    return unified_data

def convert_format_2_to_unified(data):
    """
    Convert data from format 2 (millisecond timestamps) to unified format
    """
    unified_data = {"unified_telemetry": []}
    
    for entry in data["sensor_data"]:
        unified_entry = {
            "timestamp": entry["ts"],
            "temperature": entry["temp"],
            "humidity": entry["hum"],
            "pressure": entry["press"]
        }
        unified_data["unified_telemetry"].append(unified_entry)
    
    return unified_data

def main():
    # Load the test data
    with open('data-1.json', 'r') as f:
        data1 = json.load(f)
    
    with open('data-2.json', 'r') as f:
        data2 = json.load(f)
    
    # Convert both formats to unified format
    unified1 = convert_format_1_to_unified(data1)
    unified2 = convert_format_2_to_unified(data2)
    
    # Load the expected result
    with open('data-result.json', 'r') as f:
        expected_result = json.load(f)
    
    # Compare the results
    print("Testing format 1 conversion:")
    print("Result matches expected:", unified1 == expected_result)
    
    print("\nTesting format 2 conversion:")
    print("Result matches expected:", unified2 == expected_result)

if __name__ == "__main__":
    main() 