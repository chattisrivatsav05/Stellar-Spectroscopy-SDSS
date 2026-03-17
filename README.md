# Stellar-Spectroscopy-SDSS
Computational Spectral analysis of an SDSS star using Python, including redshift estimation, temperature calculation, and spectral line identification. 

# Computational Spectral Analysis of an SDSS Star

This project presents a computational analysis of a stellar spectrum obtained from the Sloan Digital Sky Survey (SDSS). The objective is to extract physical parameters of a star using observational data and fundamental principles of stellar spectroscopy.

## Star Identification

- Plate: 2942  
- MJD: 54521  
- Fiber: 0124  

## Methodology

- Extracted FITS data using Astropy
- Converted logarithmic wavelength scale
- Plotted flux vs wavelength spectrum
- Identified absorption lines (Hα, Hβ, Na, Mg, Ca)
- Estimated redshift and radial velocity
- Applied Wien’s law to estimate surface temperature

## Results

- Radial Velocity ≈ 5 km/s (approaching Earth)
- Surface Temperature ≈ 5800 K
- Clear identification of hydrogen and metal absorption lines

## Figures

### Computed Spectrum
![Spectrum](spectrum_python.png)

## Files

- `spec-2942-54521-0124.fits` → Raw SDSS data  
- `spectral_analysis.py` → Python code  
- `Spectral_Analysis_on_Stars_SDSS__.pdf` → Full research paper  

## Tools Used

- Python  
- Astropy  
- NumPy  
- Matplotlib  

## Author

Chatti Srivatsav
B.Tech, Electronics and Communication Engineering.
Visakhapatnam, India
