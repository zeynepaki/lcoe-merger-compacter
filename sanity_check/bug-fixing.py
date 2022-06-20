import pandas as pd
import os

durham_og = pd.read_csv('Durham.csv')
durham_compact = pd.read_csv('output_cities/durham_compact.csv')
copenhagen_og = pd.read_csv('Copenhagen.csv')
copenhagen_compact = pd.read_csv('output_cities/copenhagen_compact.csv')
johanesberg_og = pd.read_csv('Johanesberg.csv')
johanesberg_compact = pd.read_csv('output_cities/johanesberg_compact.csv')
madrid_og = pd.read_csv('Madrid.csv')
madrid_compact = pd.read_csv('output_cities/madrid_compact.csv')
nairobi_og = pd.read_csv('Nairobi.csv')
nairobi_compact = pd.read_csv('output_cities/nairobi_compact.csv')
paris_og = pd.read_csv('Paris.csv')
paris_compact = pd.read_csv('output_cities/paris_compact.csv')

all_cities_merged = pd.read_csv('merged_files/all_cities.csv')

def og_query(df, burn_in, long_term, init_pce, module_cost):
    results = df.query('`Burn-in` == @burn_in and `Long-Term Degredation` == @long_term and `Initial PCE` == @init_pce and `Module Cost` == @module_cost')
    return results
def compact_query(df, burn_in, long_term, init_pce, module_cost):
    results = df.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')
    return results
def all_cities_query(city, burn_in, long_term, init_pce, module_cost):
    results = all_cities_merged.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')

    if city == 'Durham':
        result = results[['durham_two_years_lcoe', 'durham_five_years_lcoe', 'durham_ten_years_lcoe', 'durham_tw_five_years_lcoe']]
    elif city == 'Copenhagen':
        result = results[['copenhagen_two_years_lcoe', 'copenhagen_five_years_lcoe', 'copenhagen_ten_years_lcoe', 'copenhagen_tw_five_years_lcoe']]
    elif city == 'Johanesberg':
        result = results[['johanesberg_two_years_lcoe', 'johanesberg_five_years_lcoe', 'johanesberg_ten_years_lcoe', 'johanesberg_tw_five_years_lcoe']]
    elif city == 'Madrid':
        result = results[['madrid_two_years_lcoe', 'madrid_five_years_lcoe', 'madrid_ten_years_lcoe', 'madrid_tw_five_years_lcoe']]
    elif city == 'Nairobi':
        result = results[['nairobi_two_years_lcoe', 'nairobi_five_years_lcoe', 'nairobi_ten_years_lcoe', 'nairobi_tw_five_years_lcoe']]
    elif city == 'Paris':
        result = results[['paris_two_years_lcoe', 'paris_five_years_lcoe', 'paris_ten_years_lcoe', 'paris_tw_five_years_lcoe']]
    else:
        print('City not in database.')

    return result
    
print(og_query(durham_og, 0, 0, 0.01, 1.225))
print(compact_query(durham_compact, 0, 0, 0.01, 1.225))
print(all_cities_query('Durham', 0, 0, 0.01, 1.225))

print(og_query(copenhagen_og, 0, 0, 0.01, 1.225))
print(compact_query(copenhagen_compact, 0, 0, 0.01, 1.225))
print(all_cities_query('Copenhagen', 0, 0, 0.01, 1.225))

print(og_query(johanesberg_og, 0, 0, 0.01, 1.225))
print(compact_query(johanesberg_compact, 0, 0, 0.01, 1.225))
print(all_cities_query('Johanesberg', 0, 0, 0.01, 1.225))

print(og_query(madrid_og, 0, 0, 0.01, 1.225))
print(compact_query(madrid_compact, 0, 0, 0.01, 1.225))
print(all_cities_query('Madrid', 0, 0, 0.01, 1.225))

print(og_query(nairobi_og, 0, 0, 0.01, 1.225))
print(compact_query(nairobi_compact, 0, 0, 0.01, 1.225))
print(all_cities_query('Nairobi', 0, 0, 0.01, 1.225))

print(og_query(paris_og, 0, 0, 0.01, 1.225))
print(compact_query(paris_compact, 0, 0, 0.01, 1.225))
print(all_cities_query('Paris', 0, 0, 0.01, 1.225))
