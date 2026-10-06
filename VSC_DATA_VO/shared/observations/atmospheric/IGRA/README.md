# IGRA Paired Radiosonde Soundings

Global radiosonde observations with matched temporal pairs for boundary layer analysis.

## Data Organization

```
IGRA/
└── v20190515/
    └── pairs/
        ├── station_00001/
        ├── station_00002/
        └── ...
```

## Usage Example

```python
import pandas as pd
import os

igra_path = os.path.join(os.environ['VSC_DATA_VO'],
                         'shared/observations/atmospheric/IGRA/v20190515/pairs')

# Load station data
station_data = pd.read_csv(f'{igra_path}/station_00001/soundings.csv')
```

## Migration Notes

**Old paths (deprecated):**
- `/data/gent/vo/000/gvo00090/D2D/data/IGRA_PAIRS_20190515/`
- `/data/gent/vo/000/gvo00090/FLEXPART/observations/IGRA_PAIRS_20190515/`

**New path:**
- `$VSC_DATA_VO/shared/observations/atmospheric/IGRA/v20190515/`

Projects D2D and FLEXPART now have symlinks pointing to this consolidated location.

## Citation

Durre, I., Vose, R.S., & Wuertz, D.B. (2006). Overview of the Integrated Global
Radiosonde Archive. Journal of Climate, 19(1), 53-68.
https://doi.org/10.1175/JCLI3594.1
