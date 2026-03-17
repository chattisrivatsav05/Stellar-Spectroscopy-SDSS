import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.table import Table
import numpy as np

file_path = r'B:\CODING\ASTRONOMY\spec-2942-54521-0124.fits'

# Your identified lines with names for the legend
line_dict = {
    6563: 'H-alpha',
    4861: 'H-beta',
    4340: 'H-gamma',
    5890: 'Sodium (Na)',
    3933: 'Calcium (Ca II K)'
}

try:
    with fits.open(file_path) as hdul:
        spec_table = Table.read(hdul[1])
        flux = spec_table['flux']
        wavelength = 10**spec_table['loglam']

        plt.figure(figsize=(15, 7))
        plt.plot(wavelength, flux, color='black', lw=0.5, label='Stellar Spectrum')

        # Improved loop for your lines
        for line_wave, name in line_dict.items():
            if wavelength.min() < line_wave < wavelength.max():
                plt.axvline(line_wave, color='red', linestyle='--', alpha=0.5)
                # This adds the name of the element above the line
                plt.text(line_wave, plt.gca().get_ylim()[1]*0.9, name, 
                         color='red', rotation=90, va='top', fontsize=10)

        plt.xlabel(r'Wavelength ($\AA$)')
        plt.ylabel('Flux')
        plt.title('Absorption Line Identification')
        plt.show()

except Exception as e:
    print(f"Error: {e}")
