import csv

CfD_actuals_historic_values = {
    "Advanced Conversion Technology": ["null", "null"],
    "Biomass Conversion": ["1816435.796", "163300.341"],
    "Dedicated Biomass with CHP": ["269725.626", "28680.39"],
    "Energy from Waste with CHP": ["38689.443", "2531.256"],
    "Offshore Wind": ["7039091.399", "773975.067"],
    "Onshore Wind": ["404579.543", "27407.522"],
    "Solar PV": ["2295.431", "132.673"]
}

def data_from_csv(csv_name):
    with open(csv_name) as csvfile:
        reader = csv.DictReader(csvfile)
        data_values = []
        for row in reader:
            data_values.append(row)
    return data_values
