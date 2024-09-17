# Tableau_Metadata_API_Scanning
POC to show Metadata API can be queried using Python and scanned for fields of concern


1. Tableau developers programme for fake cloud site to experiment on personal laptop and trace URL's needed
2. https://www.tableau.com/en-gb/developer
3. Use Python requests example: graphiql: https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad Python Tableau auth: https://github.com/tableau/metadata-api-samples/blob/master/samples/metadata-api-with-python-and-TSC.py
  https://community.tableau.com/s/question/0D54T00000C5OjgSAF/query-the-metadata-api-from-python
5. Site name under work email and BentleyAPIDevelopment
Did not work so gmail and BentleyMetadataDev
https://10ax.online.tableau.com/#/site/bentleymetadatadev?:isFromSaml=y

 query:
 query data_gov_data_to_columns{
  datasources{ 
    name
    
    fields {
      name
      #downstreamSheetsConnection {
      #  totalCount
      #}
    }
  }
}


 pip install tableau_api_lib

 https://community.tableau.com/s/question/0D58b0000C6UFQmCQO/need-help-getting-the-metadata-for-data-dictionary
 




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 BentleyMetadataretried under gmail
7. 
