import data
import county_demographics


#Part 1: a function that adds together all the populations from 2014 together
def population_total(lst: list[data.CountyDemographics]) -> int:
    total = 0
    for county in lst:
        total += county.population["2014 Population"]
    return total

#Part 2: a function that returns all the county demographics of a specified state
def filter_by_state(lst: list[data.CountyDemographics], state: str) -> list[data.CountyDemographics]:
    return [county for county in lst if county.state == state]


#Part 3:
def population_by_education(lst: list[data.CountyDemographics], education_level: str) -> float:
    total_population = 0
    for county in lst:
        if education_level in county.education:
            multiplier = county.education[education_level] / 100
            total_population += multiplier * county.population["2014 Population"]

    return total_population

def population_by_ethnicity(lst: list[data.CountyDemographics], ethnicity: str) -> float:
    total_population = 0
    for county in lst:
        if ethnicity in county.ethnicities:
            multiplier = county.ethnicities[ethnicity] / 100
            total_population += multiplier * county.population["2014 Population"]

    return total_population

def population_below_poverty_level(lst: list[data.CountyDemographics]) -> float:
    total_population = 0
    for county in lst:
        if 'Persons Below Poverty Level' in county.income:
            multiplier = county.income['Persons Below Poverty Level'] / 100
            total_population += multiplier * county.population["2014 Population"]

    return total_population


#Part 4:
def percent_by_education(lst: list[data.CountyDemographics], education_level: str) -> float:
    total_population = population_total(lst)
    percentage_population = 0
    if total_population == 0:
        return 0
    else:
        percentage_population = (population_by_education(lst, education_level) / total_population) * 100
        return percentage_population

def percent_by_ethnicity(lst: list[data.CountyDemographics], ethnicity: str) -> float:
    total_population = population_total(lst)
    percentage_population = 0
    if total_population == 0:
        return 0
    else:
        percentage_population = (population_by_ethnicity(lst, ethnicity) / total_population) * 100
        return percentage_population

def percent_below_poverty_level(lst: list[data.CountyDemographics]) -> float:
    total_population = population_total(lst)
    percentage_population = 0
    if total_population == 0:
        return 0
    else:
        percentage_population = (population_below_poverty_level(lst) / total_population) * 100





