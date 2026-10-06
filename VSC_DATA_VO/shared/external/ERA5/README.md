# ERA5 Hourly Reanalysis

ECMWF's ERA5 atmospheric reanalysis dataset at 0.25° resolution from 1940 to present.

## Data Organization

```
ERA5/
└── by_var_nc/
    ├── t2m_1hourly/
    │   ├── t2m_1940.nc
    │   ├── t2m_1941.nc
    │   └── ...
    ├── tp_1hourly/
    ├── ssrd_1hourly/
    └── [20+ other variables]/
```

## Usage Example

```python
import xarray as xr
import os

# Load temperature data
base_path = os.path.join(os.environ['VSC_DATA_VO'], 'shared/external/ERA5')
t2m = xr.open_mfdataset(f'{base_path}/by_var_nc/t2m_1hourly/t2m_*.nc')
```

## Notes

- **Updated regularly:** New data added monthly
- **Used by:** HEAT, FLEXPART, D2D, and other projects
- **Duplication alert:** If you need ERA5 for your project, link to this location instead of downloading separately
- **See also:** ERA5-Land for higher resolution land-only data
