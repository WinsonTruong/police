
# Load packages
from pygeocoder import Geocoder
import pandas as pd

## CREDITS TO https://medium.com/@alexeskinasy/reverse-geocoding-on-tableau-prep-python-8feee9d4ca43 
## I DID NOT WRITE ANY OF THIS ITS ALL FROM THIS

# This function returns the new dataframe, including a new column
# with the  postcodes, as returned by Google Geocoding API
def getPostalCode(df):
    postcodes = []
    for i in df.index:  
        results = Geocoder('<YOUR-API-KEY>').reverse_geocode(df['Latitude'][i], df['Longitude'][i])
        postcodes.append(results.postal_code)
    
    df['Postcode'] = postcodes
    return df

# This is a mandatory function required by Tableau Prep, in case we 
# are returning a dataframe with a different schema than the original one
def get_output_schema():
    return pd.DataFrame({
        'Booli Id' : prep_int(),
        'Latitude' : prep_decimal(),
        'Longitude' : prep_decimal(),
        'Postcode' : prep_string()     
        })