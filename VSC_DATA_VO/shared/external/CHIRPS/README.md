# CHIRPS v3.0 Monthly Precipitation

High-resolution quasi-global precipitation dataset from 1981 to present.

## Quick Access

```python
import xarray as xr
import os

chirps_path = os.path.join(os.environ['VSC_DATA_VO'],
                           'shared/external/CHIRPS/v3.0/monthly')
pr = xr.open_mfdataset(f'{chirps_path}/chirps_*.nc')
```

## Citation

Funk, C., et al. (2015). The climate hazards infrared precipitation with
stations—a new environmental record for monitoring extremes. Scientific Data,
2(1), 1-21. https://doi.org/10.1038/sdata.2015.66
