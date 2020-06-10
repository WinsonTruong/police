import sys
sys.path.append('/TabPy')
from geocode import geocodeReverse

def prepGeo(input):
    prepData = geocodeReverse(input,"450b9ebd6f0105cfcbb1284ac8b87f97d25b11e4e0ce68bb0f4f6a2cdee39c18")
    return prepData

def get_output_schema():
    return pd.DataFrame(
        {
            "InitialQuery": prep_string(),
            "ReturnAddress": prep_string(),
            "Accuracy": prep_string(),
            "Relevance": prep_decimal()
        }
    )