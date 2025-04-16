import pytest
import requests


BASE_URL = "http://localhost:8000/is-it-water"  

@pytest.mark.parametrize("lat, lon, expected_feature, expected_is_water", [
    (0, 0, "UNKNOWN", True),
    (9999, 9999, "UNKNOWN", True),
    (46.67, 103.3, "LAKE", True),
    (-10.47, 105.57, "LAND", False),
    (30.03, 31.22, "RIVER", True),
    (45.295504, 12.61337, "OCEAN", True),
    (44.35953, -2.765543, "UNKNOWN", True),
    (6.56, 0, "LAKE", True),
    (0, -69, "LAND", False),
])
def test_is_in_water(lat, lon, expected_feature, expected_is_water):
    
    response = requests.get(f"{BASE_URL}/{lat}/{lon}")
    
    assert response.status_code == 200
    
    data = response.json()

    feature = data.get('feature', 'UNKNOWN')
    is_water = data.get('isWater', False)

    print(f"\nTesting ({lat}, {lon})")
    print(f"→ Expected Feature: {expected_feature}, Actual Feature: {feature}")
    print(f"→ Expected isWater: {expected_is_water}, Actual isWater: {is_water}")
    
    assert feature == expected_feature
    assert is_water == expected_is_water
