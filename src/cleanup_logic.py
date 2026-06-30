import pandas as pd
import os
from dotenv import load_dotenv

# Load local .env machine paths
load_dotenv()
master_path = os.getenv("MASTER_ROSTER_PATH")

def cross_reference_data():
    # 1. Load the messy master data
    # 2. Match names against Constant Contact ('Full Name') 
    # 3. Match names against Eventbrite ('Buyer first name' + 'Buyer last name')
    # 4. Programmatically standardize phone formatting (XXX-XXX-XXXX)
    # 5. Export clean profiles directly into Organized_Program_Data.xlsx
    pass