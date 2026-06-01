# glacial_lakes_FOSS4G

Repository for the abstract "Representing spatiotemporal dynamics of glacial lakes with vector data cubes", submitted to FOSS4G Europe 2026, Timișoara, Romania.

---

## Contents

### [`1_OBIA_lakes_S1S2.ipynb`](1_OBIA_lakes_S1S2.ipynb) — Glacial Lake Mapping with Sentinel-1 and Sentinel-2 (2016–2025)

Maps annual glacial lake extents for the Vatnajökull area in southeast Iceland using an Object-Based Image Analysis (OBIA) workflow. For each year (2016–2025), summer median composites are retrieved from the Copernicus Dataspace via OpenEO for both Sentinel-2 (optical) and Sentinel-1 (SAR) data. Spectral indices (NDWI, NDVI, NDSI) and SAR backscatter features are computed and combined into a feature stack, which is segmented using SLIC. Water segments are classified using a configurable fusion of S2 and S1 thresholds. Annual lake outlines are exported as GeoPackages to `OBIA_DIR`. Based on the OBIA workflow by Dabiri et al. (2021).

**Requires:** OpenEO authentication (Copernicus Dataspace account)

> **Note:** Annual lake outlines were manually reviewed and poorly segmented polygons removed.

---

### [`2_OBIA_lakes_LS.ipynb`](2_OBIA_lakes_LS.ipynb) — Glacial Lake Mapping with Landsat via Google Earth Engine (1985–2015)

Extends the lake time series back to 1985 using Landsat imagery, replicating the OBIA workflow from notebook 1 with adaptations for the lower resolution and different band availability of Landsat. Summer composites are built annually via Google Earth Engine, automatically selecting the appropriate Landsat mission (5, 7, 8, or 9) per year. In place of SAR data, thermal infrared (TIR), elevation (ArcticDEM V4), and an additional spectral index (NDDI) are used to improve water classification. Segments are classified using a combination of NDWI, NDVI, NDDI, brightness, and elevation thresholds. Annual lake outlines are exported as GeoPackages to `OBIA_DIR`. Based on the OBIA workflow by Dabiri et al. (2021).

**Requires:** Google Earth Engine authentication (GEE account)

> **Note:** Annual lake outlines were manually reviewed and poorly segmented polygons removed. Years 2003, 2007, 2008, and 2009 were excluded entirely due to insufficient outline quality.

---

### [`3_glacial_lakes_VDC.ipynb`](3_glacial_lakes_VDC.ipynb) — Vector Data Cube Construction and Feature Grouping (1985–2025)

Combines the annual lake outlines produced by notebooks 1 and 2 into a vector data cube (VDC) and investigates five feature grouping methods for tracking individual lakes consistently over time. Annual GeoPackages are loaded, validated, and assigned lake IDs using: 1) spatial overlap or proximity, 2) centroid, 3) bounding box, 4) automatic representative point, and 5) manual representative point — each built into a separate VDC using `xvec`. The notebook then analyses spatiotemporal dynamics (disappearing, reappearing, merging, splitting) across methods and compares their effect on lake area time series. Based on the VDC framework by Abad et al. (2024).

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
