# Is On Water

A Python implementation of a geospatial service that determines whether a given latitude and longitude point is on water. This project is inspired by [is-on-water.balbona.me](https://is-on-water.balbona.me/) and provides a simple API to check if a geographic coordinate is over water, along with the type of water body (ocean, river, or lake).

## Features

- Fast and efficient water body detection using NASA's ASTER Global Water Bodies Database
- Supports multiple water body types: Ocean, River, Lake
- Simple REST API interface
- Lightweight and easy to integrate

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/is-on-water.git
   cd is-on-water
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn rasterio
   ```

## Dataset

This project includes a subset of the ASTER Global Water Bodies Database (ASTWBD) in the `dataset` directory. The dataset is pre-processed and ready to use with the following specifications:

- Source: NASA's ASTER Global Water Bodies Database
- Resolution: 1 arc-second (~30 meters at the equator)
- Coverage: Global
- Format: Pre-processed ZIP files organized by tile


## Usage

### Running the API Server

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### API Endpoints

#### Check if a Point is on Water

```
GET /is-it-water/{lat}/{lon}
```

**Parameters:**
- `lat`: Latitude (decimal degrees, -90 to 90)
- `lon`: Longitude (decimal degrees, -180 to 180)

**Example Request:**
```
GET /is-it-water/40.7128/-74.0060
```

**Example Response:**
```json
{
    "isWater": true,
    "feature": "OCEAN",
    "lat": 40.7128,
    "lon": -74.0060,
    "reqMs": 45
}
```

**Response Fields:**
- `isWater`: `true` if the point is on water, `false` otherwise
- `feature`: Type of water body (OCEAN, RIVER, LAKE) or LAND if not on water
- `lat`: The input latitude
- `lon`: The input longitude
- `reqMs`: Request processing time in milliseconds

### Using the Water Detection Function

You can also use the water detection function directly in your Python code:

```python
from water import is_in_water

# Check if a point is on water
result = is_in_water(40.7128, -74.0060)  # New York City
print(result)  # Returns: 'OCEAN', 'RIVER', 'LAKE', 'LAND', or 'UNKNOWN'
```

## Development

### Running Tests

Run the test suite with:

```bash
python test.py
```

### Project Structure

- `main.py`: FastAPI application and API endpoints
- `water.py`: Core water detection functionality
- `test.py`: Test cases for the water detection
- `dataset/`: Directory containing the ASTER Global Water Bodies Database

