from astropy.io import fits
import numpy as np

#il file al suo stesso livello hanno 1 .

from..helpers.logger import Logger

class FitsManager:
    #""""
    #class to manage FITS files, using astropy.io.fits module"
    #""""
    #define constructor (la prima cosa che succede quando crei un oggetto di tipo FitsManager)"
    #IN PYTHON ESISTE SOLO UN COSTRUTTORE"
    def __init__(self, input_file):         #(dare sempre self sennò non vede sé stessa)
        #""""
        #Constructor of the class
        #param input_file: The input file to be opened"
        #""""
        self.input_file = input_file
        self.hdulist = fits.open(input_file)

        self.logger = Logger("FitsManager")
        self.logger("Fits file opened succesfully")    

    def get_header(self, hdu_index):
        #dà l'header di un HDU
        #
        if hdu_index < 0 or hdu_index >= len(self.hdulist):
            raise ValueError("Invalid HDU index")
        
        return self.hdulist[hdu_index].header
    
    def get_data(self, hdu_index):
        #dà i dati di un HDU
        #
        if hdu_index < 0 or hdu_index >= len(self.hdulist):
            raise ValueError("Invalid HDU index")
        return self.hdulist[hdu_index].data
    
    def get_hdu_count(self):
        return len(self.hdulist)