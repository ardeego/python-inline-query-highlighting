from azure.kusto.data.request import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.helpers import dataframe_from_result_table

cluster = "<insert here your cluster name>"

kcsb = KustoConnectionStringBuilder.with_aad_device_authentication(cluster)
client = KustoClient(kcsb)

db = "Samples"

query = """
//begin-kusto
StormEvents
| where StartTime > datetime(2007-02-01) and StartTime < datetime(2007-03-01)
| where EventType == 'Flood' and State == 'CALIFORNIA'
| project StartTime, EndTime, State, EventType, EpisodeNarrative
//end-kusto
"""

response = client.execute(db, query)
df = dataframe_from_result_table(response.primary_results[0])