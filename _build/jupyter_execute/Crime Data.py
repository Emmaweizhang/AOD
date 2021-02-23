# <span style = 'color: #00adee'> Crime Data

People living in high crime areas can be at higher risk of substance miss-use. This is evident in areas of lower socio-economic status where there is an increased rate of unemployment, poor support systems and low rates of school retention. 

import pandas as pd
import numpy as np
from IPython.display import IFrame

crimeData = 'https://app.powerbi.com/reportEmbed?reportId=f3d4ac41-8cc8-48e0-9096-5b4d7b256b5b&autoAuth=true&ctid=282e8c9e-daf7-4f9e-a238-0330c86cc7a4&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWF1c3RyYWxpYS1zb3V0aGVhc3QtcmVkaXJlY3QuYW5hbHlzaXMud2luZG93cy5uZXQvIn0%3D'
IFrame(crimeData, width = 1140, height = 541.25)

From 2019 to 2020, there are 13123 drug-related offences happened in NWMPHN region, accounting for 33.6% of drug-related offences in Victoria. Among these, 10844 are drug use and possession offences.   
In fact, the drug offence rate per LGA in NWMPHN is higher than the state average level in the past 10 years.    
The table above shows the rate per 100,000 population for all drug offences in 2019-2020. It is clear to see that Melbourne had the highest drug offence rate (1775.46 per 100k) than any other LGAs in NWMPHN. Yarra (1143.04 per 100k), Darebin (764.77 per 100k), Brimbank (671.74 per 100k) and Hume (657.37 per 100k) are above the NWMPHN average level. 616 offences happened out of 100,000 population in Maribyrnong, which placed Maribyrnong below the NWMPHN average but above the state average. 