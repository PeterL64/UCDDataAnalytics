# Quick sample code on how to import SAS and Stata Files

# Importing SAS Files
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file: # urbanpop.sas7bdat is the file name
    df_sas = file.to_data_frame()



# Importing Stata Files
import pandas as pd
data = pd.read_stata('urbanpop.dta')    # urbanpop.dta is file name