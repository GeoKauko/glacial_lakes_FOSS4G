# glacial_lakes_FOSS4G

Repository for the abstract "Representing spatiotemporal dynamics of glacial lakes with vector data cubes", submitted to FOSS4G Europe 2026, Timișoara, Romania.

---

## Contents

### Glacial Lake Mapping with Sentinel-1 and Sentinel-2 (2016–2025): [`1_OBIA_lakes_S1S2.ipynb`](1_OBIA_lakes_S1S2.ipynb)

Maps annual glacial lake extents for the Vatnajökull area in southeast Iceland using an object-based image analysis (OBIA).\
&rarr; For each year, retrieve summer median composites from the Copernicus Dataspace via OpenEO for both Sentinel-2 and Sentinel-1 data.\
&rarr; Compute spectral indices (NDWI, NDVI, NDSI) and SAR backscatter features and combine into a feature stack.\
&rarr; Segment feature stack using SLIC.\
&rarr; Classify water segments using S2 and S1 thresholds.\
&rarr; Export annual lake outlines as GeoPackages.\
Based on the OBIA workflow by Dabiri et al. (2021).

**Requirements:** OpenEO authentication

> **Note:** Manually review the lake outlines and remove poorly segmented polygons.

---

### Glacial Lake Mapping with Landsat via Google Earth Engine (1985–2015): [`2_OBIA_lakes_LS.ipynb`](2_OBIA_lakes_LS.ipynb)

Extends the lake time series back to 1985 using Landsat imagery, replicating the OBIA workflow from notebook 1 with adaptations for the lower resolution and different band availability of Landsat.\
&rarr; Build annual summer composites via Google Earth Engine, automatically selecting the appropriate Landsat mission (5, 7, 8, or 9) per year.\
&rarr; In place of SAR data, use thermal infrared (TIR), elevation (ArcticDEM V4), and an additional spectral index (NDDI) to improve water classification.\ 
&rarr; Classify segments using a combination of NDWI, NDVI, NDDI, brightness, and elevation thresholds.\
&rarr; Export annual lake outlines as GeoPackages.

**Requirements:** Google Earth Engine authentication

> **Note:** Manually review the lake outlines and remove poorly segmented polygons. Years 2003, 2007, 2008, and 2009 were excluded entirely due to insufficient outline quality.

---

### Vector Data Cube Construction and Feature Grouping (1985–2025): [`3_glacial_lakes_VDC.ipynb`](3_glacial_lakes_VDC.ipynb)

Combines the annual lake outlines produced by notebooks 1 and 2 into a vector data cube (VDC) and investigates five feature grouping methods for tracking individual lakes over time.\
&rarr; Load and validate GeoPackages.\
&rarr; Assign lake IDs using: 1) spatial overlap or proximity, 2) centroid of temporal union, 3) bounding box of temporal union, 4) automatic representative point, and 5) manual representative point.\
&rarr; Build a VDC for each method using `xvec`.\
&rarr; Analyse spatiotemporal dynamics (disappearing, reappearing, merging, splitting) across methods and compare their effect on lake area time series.\
Based on the VDC framework by Abad et al. (2024).

**Requires:** Output from notebooks 1 and 2 in `OBIA_DIR`

---

## Setup

### 1. Install the environment
```bash
conda env create -f env.yaml
```

### 2. Activate the environment
```bash
conda activate glacial_lakes
```

### 3. Register as a Jupyter kernel
```bash
python -m ipykernel install --user --name glacial_lakes --display-name "glacial_lakes"
```

### 4. Configure local paths
Copy the template and set your local project root:
```bash
cp config_template.py config.py
```
Then open `config.py` and set `ROOT_DIR` to your local project path.

### 5. Run the notebooks in order
> **Important:** Manually review the lake outlines produced by notebooks 1 and 2 before running notebook 3.

---

## References

- Dabiri, Z. et al. (2021). Comparing the Applicability of Sentinel-1 and Sentinel-2 for Mapping the Evolution of Ice-marginal Lakes in Southeast Iceland. [Paper](https://austriaca.at/0xc1aa5576%200x003c9b50.pdf)
- Abad, L. et al. (2024). Vector data cubes for features evolving in space and time (computational notebook). [GitHub](https://github.com/loreabad6/vdc-space-time-feats/blob/main/notebook/vdc-showcase.md)
