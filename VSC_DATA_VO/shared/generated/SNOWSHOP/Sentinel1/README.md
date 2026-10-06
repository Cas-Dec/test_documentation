# SNOWSHOP Sentinel-1 Snow Products

High-resolution (100m) snow products derived from Sentinel-1 SAR for major mountain regions.

## Data Organization

```
Sentinel1/
├── g0_100m/               # Gamma-0 backscatter tiles (4949 tiles)
│   ├── tile_0001/
│   ├── tile_0002/
│   └── ...
├── SNAPPY/                # SNAP toolbox outputs
├── SD_RETRIEVAL/          # Snow depth retrieval algorithm outputs
└── README.md
```

## Usage Example

```python
import rasterio
import os

base = os.path.join(os.environ['VSC_DATA_VO'],
                    'shared/generated/SNOWSHOP/Sentinel1')

# Load a specific tile
with rasterio.open(f'{base}/g0_100m/tile_0001/g0_20250115.tif') as src:
    backscatter = src.read(1)
```

## Important Notes

- **Active processing:** Dataset updated regularly
- **Large scale:** 4949 tiles, ~2 TB total
- **Quality control:** See validation datasets in shared/observations/
- **Publication pending:** Please contact before using in publications
- **Processing code:** Available in SNOWSHOP project repository

## Regional Coverage

- **Alps:** Full coverage
- **Andes:** Major ranges
- **Nordic (NoSeFi):** Norway, Sweden, Finland
