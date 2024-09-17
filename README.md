# Tableau_Metadata_API_Scanning
POC to show Metadata API can be queried using Python and scanned for fields of concern


1. Tableau developers programme for fake cloud site to experiment on personal laptop and trace URL's proved URL is already whitelisted on bridge VM
2. https://www.tableau.com/en-gb/developer
3. Use Python requests example: graphiql: https://gist.github.com/gbaman/b3137e18c739e0cf98539bf4ec4366ad Python Tableau auth: https://github.com/tableau/metadata-api-samples/blob/master/samples/metadata-api-with-python-and-TSC.py
  https://community.tableau.com/s/question/0D54T00000C5OjgSAF/query-the-metadata-api-from-python
5. Site name under work email was BentleyAPIDevelopment
Did not work so gmail and BentleyMetadataDev
https://10ax.online.tableau.com/#/site/bentleymetadatadev

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

 Key results:
 Working with a PA token to query multiple things at once
 Doesn't appear to need extra whitelist rules and encrypted in transit
 Need approval to configure PAT token on prod and use open source packages especially tableau_api_lib

Decisions: how to monitor which fields are PII


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 BentleyMetadataretried under gmail
7. 
