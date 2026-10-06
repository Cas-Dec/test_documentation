# EXT/ Dataset Inventory

**Path:** `/data/gent/vo/000/gvo00090/EXT/`
**Total datasets:** 108
**Purpose:** Raw external datasets (to become `shared/external/`)

## Directory Structure

```
EXT/
├── archive/        # Archived/old datasets
├── data/           # 108 active datasets (see below)
├── scripts/        # Download/processing scripts
├── software/       # Related software/tools
└── EXT_scripts.tgz # Script archive (1.7M)
```

## Complete Dataset List

### Atmospheric Reanalysis & Meteorology (19 datasets)
- **ERA5** - ECMWF reanalysis (hourly, by_var_nc structure with 20+ variables)
- **ERA5_Land** - Land-focused ERA5
- **ERA5_back_extension** - Historical extension
- **ERA-INTERIM** - Older ECMWF reanalysis
- **JRA-55** - Japanese reanalysis
- **JRA-3Q** - Recent Japanese reanalysis
- **NCEP** - NCEP/NCAR & NCEP/DOE reanalyses
- **CAMS** - Copernicus Atmosphere Monitoring Service
- **GEFS_reforecast_v12** - Ensemble forecast reanalysis
- **CRU** - Climate Research Unit data
- **CRUv4.09** - Specific CRU version
- **CHELSAv2.1** - High-resolution climate data
- **TERRACLIMATE** - Monthly climate and water balance
- **KMI** - Royal Meteorological Institute of Belgium data
- **KOEPPEN** - Köppen climate classification
- **Climate_Indices** - Climate variability indices
- **CLIMDEX_CMIP5** - CMIP5 climate extremes
- **CLIMDEX_CMIP6** - CMIP6 climate extremes
- **CORDEX** - Coordinated regional climate downscaling

### Precipitation Products (11 datasets)
- **CHIRPS** - Climate Hazards Group InfraRed Precipitation with Station data (v3.0/monthly)
- **MSWEP** - Multi-Source Weighted-Ensemble Precipitation (v1.2, v2.2)
- **MSWEP_3H** - 3-hourly variant
- **MSWEP_v2.8** - Version 2.8
- **MSWEP_v3.16** - Version 3.16 (NRT, Past, Monthly)
- **MSWX** - Multi-Source Weather
- **MSWX_3H** - 3-hourly variant
- **CMORPH** - CPC MORPHing technique
- **CMORPH CDR v1** - Climate Data Record v1
- **GPM_IMERG** - Global Precipitation Measurement IMERG
- **IMERG** - IMERG variant
- **PERSIANN-CDR** - Precipitation Estimation from Remotely Sensed Information
- **GPCC** - Global Precipitation Climatology Centre
- **GPCP** - Global Precipitation Climatology Project
- **TMPA** - TRMM Multi-satellite Precipitation Analysis
- **PREC_L** - NOAA precipitation reconstruction

### Evapotranspiration & Water Cycle (12 datasets)
- **FLUXCOM** - Upscaled flux measurements (TER, NEE, GPP subdirs)
- **FLUXCOM_X_BASE** - FLUXCOM extended base product
- **ETMonitor** - Evapotranspiration monitoring
- **PML** - Penman-Monteith-Leuning ET
- **MOD16A2_evaporation** - MODIS ET 8-day
- **MOD16A3_evaporation_annual** - MODIS ET annual
- **WAPOR-3** - Water Productivity Open-access portal
- **DOLCE** - Database of global gridded evapotranspiration (v3)
- **WECANN** - Water, Energy, and Carbon with Artificial Neural Networks
- **P-LSH** - Priestley-Taylor Jet Propulsion Laboratory model
- **VODGPP** - VOD-based GPP estimates
- **BESSv2** - Breathing Earth System Simulator v2

### Land Surface & Hydrology (10 datasets)
- **GLDAS** - Global Land Data Assimilation System
- **FLDAS** - Famine Early Warning System Land Data Assimilation
- **WATERGAP** - Water Global Assessment and Prognosis
- **GRACE** - Gravity Recovery and Climate Experiment
- **GRDC-global** - Global Runoff Data Centre
- **C3S** - Copernicus Climate Change Service (soil_moisture subdir)
- **HR-GACD** - High-Resolution Global Assessment of Closed Depressions
- **hydrobasins** - HydroBASINS watershed boundaries
- **DSMW** - Digital Soil Map of the World
- **soilgrids** - SoilGrids global soil information

### Vegetation & Land Cover (20 datasets)
- **GIMMS** - Global Inventory Modeling and Mapping Studies NDVI (v1, v2)
- **AVHRR-LTDR_burned_area** - Long-term burned area
- **ESA_CCI** - ESA Climate Change Initiative
- **ESA_CCI_LC_PFT** - Land cover plant functional types
- **LC_MCD12Q1** - MODIS land cover type
- **MCD12Q1_land_cover** - MODIS land cover
- **MCD15A3** - MODIS LAI/FPAR 4-day
- **MCD15A3H_vegetation** - High-quality LAI/FPAR
- **MCD43A3_Albedo** - MODIS albedo
- **MOD43D51** - MODIS albedo daily
- **MOD44B** - MODIS vegetation continuous fields
- **MOD44B_tree_cover** - Tree cover from MOD44B
- **MOD44B_VCF** - Vegetation continuous fields
- **MEaSUREs_VCF** - Making Earth System Data Records VCF
- **VCF_measures** - Vegetation continuous fields
- **SNU_LAI_AVHRR** - Seoul National University LAI from AVHRR
- **GLASS** - Global Land Surface Satellite
- **Clumping_Index_GMVCI** - Vegetation clumping index
- **VODCA** - Vegetation Optical Depth Climate Archive
- **IGBP-DIS** - IGBP land cover classification

### Radiation & Energy (8 datasets)
- **CERES** - Clouds and Earth's Radiant Energy System
- **CERESv** - CERES variant
- **SRB** - Surface Radiation Budget
- **OAFlux** - Objectively Analyzed air-sea Fluxes
- **OAFlux_hao** - OAFlux variant
- **LSAF** - Land Surface Analysis Satellite Application Facility
- **SIF** - Solar-Induced Fluorescence
- **AIRS** - Atmospheric Infrared Sounder

### Remote Sensing & Satellite (7 datasets)
- **MODIS**: Multiple products (see above in relevant categories)
- **MOD11A1** - MODIS land surface temperature daily
- **LST_Planet** - Planet land surface temperature
- **AMSR-E** - Advanced Microwave Scanning Radiometer
- **GLAS** - Geoscience Laser Altimeter System
- **CopernicusDEM** - Copernicus Digital Elevation Model
- **3T** - Unknown satellite product

### Field Observations & In-Situ (5 datasets)
- **FLUXNET** - Eddy covariance flux tower network
- **SOUNDINGS** - Atmospheric soundings (HUMPPA, GOAMAZON, BLLAST, GLOBAL, old)
- **ITRDB** - International Tree-Ring Data Bank
- **CAMELE** - Unknown observational dataset
- **LIS_OTD_Lightning** - Lightning Imaging Sensor / Optical Transient Detector

### Specialized / Derived (8 datasets)
- **GLOBSNOW** - Snow water equivalent
- **EM_Earth_v1** - Earth Mover embeddings
- **alpha_earth_embeddings** - Alpha Earth ML embeddings
- **CAS-GLA** - Unknown specialized product
- **GPWv4_population** - Gridded Population of the World v4
- **yield** - Agricultural yield data
- **natural_earth** - Natural Earth geographic data
- **CESM_data_for_FLEXPART** - CESM model output for FLEXPART forcing

### Miscellaneous (2 items)
- **findlog** - Log file or utility (not a dataset)
- **globsnow.yml** - Configuration file (not a dataset)
- **siTH** - Unknown dataset

## Migration Strategy

### Priority Classification

**Tier 1 - Active, Well-Structured, Frequently Used:**
Migrate first with full metadata
- ERA5, ERA5_Land
- CHIRPS
- MSWEP (latest version)
- GLDAS
- FLUXCOM
- MOD16A2_evaporation
- GPM_IMERG

**Tier 2 - Active but Versioned:**
Keep latest version, archive old versions
- MSWEP (consolidate v1.2, v2.8, v3.16 → keep v3.16)
- GIMMS (v1 vs v2)
- CRU/CRUv4.09
- ERA5_back_extension (merge into ERA5?)

**Tier 3 - Specialized/Project-Specific:**
Verify if truly cross-team before migrating to shared/
- SOUNDINGS (seems project-specific)
- CESM_data_for_FLEXPART (might belong in projects/FLEXPART/)
- CAMELE, CAS-GLA, siTH (unknown - need clarification)

**Tier 4 - Legacy/Archived:**
Move to archive or document-only
- ERA-INTERIM (superseded by ERA5)
- Older MSWEP versions
- TMPA (superseded by IMERG)
- Old MODIS products (if superseded)

### Structure Standardization Needed

**Good candidates for CF-style reorganization:**
- **ERA5**: Currently `by_var_nc/t2m_1hourly/` → Propose `hourly/tas/tas_ERA5_1hr_YYYY*.nc`
- **CHIRPS**: Currently `v3.0/monthly/` → Propose `monthly/pr/pr_CHIRPS_mon_*.nc`
- **MODIS products**: Consolidate MOD16A2/MOD16A3, MOD44B variants with clear variable names

**Leave as-is initially (complex structure):**
- FLUXCOM (multiple products: TER, NEE, GPP)
- MSWEP_v3.16 (NRT, Past, Monthly - temporal divisions make sense)
- ESA_CCI (multiple products)

## Questions for Lab Discussion

1. **Version consolidation**: Which old versions can we archive vs. keep accessible?
2. **Unknown datasets**: What are CAMELE, CAS-GLA, siTH, 3T?
3. **Specialized products**: Should CESM_data_for_FLEXPART move to projects/FLEXPART/?
4. **SOUNDINGS**: Project-specific or truly shared resource?
5. **Scripting**: Keep scripts/ and software/ at EXT level or distribute per-dataset?
6. **Migration timeline**: Which datasets are actively used in current research?
7. **Ownership**: Who should be contact person for each dataset category?

## Next Steps

1. **Survey actual usage**: Check which datasets have recent file access
2. **Contact stakeholders**: Identify primary users of each dataset
3. **Pilot migration**: Start with 2-3 Tier 1 datasets to test workflow
4. **Create metadata templates**: Pre-fill what's known from filenames/structure
5. **Archive old versions**: Move superseded data to `archive/` before migration
