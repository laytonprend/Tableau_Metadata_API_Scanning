import pandas as pd
import numpy as np
from tableau_api_lib import TableauServerConnection
from pathlib import Path

def load_api_key(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read().strip()  # Read and remove any surrounding whitespace
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
        raise
    except IOError as e:
        print(f"Error: An IOError occurred. Details: {e}")
        raise
    
    
# Credentials and configuration
HOST = 'https://10ax.online.tableau.com'#/api/metadata/graphql'  # Tableau Cloud URL (example)
TOKENNAME = 'DevMetadata'  # Personal Access Token Name
TOKENID =  load_api_key(r"C:\Users\layto\OneDrive\Documents\GitHub\Tableau_Metadata_API_Scanning\api_key.txt")
  # Personal Access Token Secret
SITE = ''  # Use '' for default site or provide the site ID if not using the default


tableau_server_auth = {
    'environment': {
        'server': HOST,
        'api_version': '3.22',  # Ensure this is the correct version for Tableau Cloud
        'personal_access_token_name': TOKENNAME,
        'personal_access_token_secret': TOKENID,
        'site_name': SITE,  # For Tableau Cloud, this is the site ID or '' for default site
        'site_url': SITE  # For Tableau Cloud, this is the site ID or '' for default site
    }
}

def sign_in():
    connection = TableauServerConnection(tableau_server_auth, env='environment')
    connection.sign_in()
    return connection

def execute_query(connection, query):
    response = connection.metadata_graphql_query(query=query)
    print(response)
    return response.json()['data']

def main():
    connection = sign_in()

    try:
        # Queries
        queries = {
            "data_gov_data_to_columns": """
            query data_gov_data_to_columns{ datasources{ name

fields {
  name
  #downstreamSheetsConnection {
  #  totalCount
  #}
}
} }
            """ #can do multi query
        }

        # Execute queries
        data = {}
        for key, query in queries.items():
            print(f"Executing {key} query...")
            data[key] = execute_query(connection, query)
            print('got here')
            print(data[key])
        combined_df = pd.json_normalize(data['data_gov_data_to_columns']['datasources'])

        # Export to JSON file
        json_file_path = Path(r"C:\Users\layto\OneDrive\Documents\GitHub\Tableau_Metadata_API_Scanning\exported_data.json")
        combined_df.to_json(json_file_path, orient='records', lines=True)  # Adjust 'orient' and 'lines' as needed

        print(f"Data successfully written to {json_file_path}")



        # Convert pandas DataFrame to Hyper
        #pantab.frame_to_hyper(combined_df, FILE, table="Extract")

        #print(f"Data successfully written to {FILE}")

    finally:
        connection.sign_out()
        
        #download code on https://community.tableau.com/s/question/0D58b0000C6UFQmCQO/need-help-getting-the-metadata-for-data-dictionary
        #can add this for multiple queries

if __name__ == '__main__':
    main()
