#!/usr/bin/env python
import requests
import pandas as pd




def measurement_to_string(measurement):
    outputString=""
    if measurement==1:
        outputString+="Arrving to"
    elif measurement==2:
        outputString+="Departing from"
    elif measurement==3:
        outputString+="Net Migration to"
    return outputString


def process_immigration_per_year(framed_data,gender,region,measure):
    #data frame of Men into australia Net
    men_data=framed_data[(framed_data['Sex']==gender)]
    men_aus_data=men_data[men_data['Region']==region]
    men_aus_net_data= men_aus_data[men_aus_data['MEASURE']==measure]
    print(men_aus_net_data)

    #The young ages
    men_aus_net_20_data=men_aus_net_data[ men_aus_net_data["AGE"]=="A20" ]
    men_aus_net_25_data=men_aus_net_data[ men_aus_net_data["AGE"]=="A25"]
    men_aus_net_30_data=men_aus_net_data[ men_aus_net_data["AGE"]=="A30"]
    men_aus_net_35_data=men_aus_net_data[ men_aus_net_data["AGE"]=="A35"]

    men_aus_net_young_data= pd.concat([men_aus_net_20_data,men_aus_net_25_data,men_aus_net_30_data,men_aus_net_35_data])



    all_years=list(dict.fromkeys(list(men_aus_net_young_data['Time'])))

    migration_per_year=[]

    for i in range (len(all_years)):
        yearly_data=men_aus_net_young_data[men_aus_net_young_data['Time']==all_years[i]]
        migration_per_year.append(int(yearly_data['Value'].sum(axis=0,skipna=True)))

    return [all_years,migration_per_year]






