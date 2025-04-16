import zipfile
from rasterio.windows import Window
from rasterio.io import MemoryFile
from pathlib import Path
from typing import Literal
import math

WATER_VALUE_TYPES = Literal['LAND', 'OCEAN', 'RIVER', 'LAKE', 'UNKNOWN']

def is_in_water(lat: float, lon: float, dataset_path: str = 'dataset') -> WATER_VALUE_TYPES:
    lat_prefix = 'N' if lat >= 0 else 'S'
    lon_prefix = 'E' if lon >= 0 else 'W'
    lat_str = f"{lat_prefix}{abs(math.floor(lat)):02d}"
    lon_str = f"{lon_prefix}{abs(math.floor(lon)):03d}"
    tile_id = f"ASTWBDV001_{lat_str}{lon_str}"

    zip_path = Path(dataset_path) / f"{tile_id}.zip"
    if not zip_path.exists():
        return 'UNKNOWN'

    tif_name = f"{tile_id}_att.tif"

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        if tif_name not in zip_ref.namelist():
            return 'UNKNOWN'

        data = zip_ref.read(tif_name)

    with MemoryFile(data) as memfile:
        with memfile.open() as dataset:
            bounds = dataset.bounds
            width = dataset.width
            height = dataset.height

            bbox_width = bounds.right - bounds.left
            bbox_height = bounds.top - bounds.bottom

            width_pct = (lon - bounds.left) / bbox_width
            height_pct = (lat - bounds.bottom) / bbox_height

            x = math.floor(width * width_pct)
            y = math.floor(height * (1 - height_pct))  # invert Y like in JS

            if x < 0 or x >= width or y < 0 or y >= height:
                return 'UNKNOWN'

            window = Window(x, y, 1, 1)
            data = dataset.read(1, window=window)

            value = data[0, 0]
            if value == 0:
                return 'LAND'
            elif value == 1:
                return 'OCEAN'
            elif value == 2:
                return 'RIVER'
            elif value == 3:
                return 'LAKE'
            else:
                return 'UNKNOWN'
