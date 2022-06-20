import pandas as pd
import os



def city_compacter(csv):
    merged_df = pd.DataFrame(columns=['location', 'burn_in', 'long_term_degredation', 'initial_pce', 'module_cost', 'two_years_lcoe', 'five_years_lcoe', 'ten_years_lcoe', 'tw_five_years_lcoe'])
    original_csv_df = csv

    for index, row in original_csv_df.iterrows():
        burn_in = original_csv_df.iat[index, 1]
        long_term = original_csv_df.iat[index, 2]
        init_pce = original_csv_df.iat[index, 3]
        module_cost = original_csv_df.iat[index, 4]

        duplicate_checker_df = merged_df.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')

        if duplicate_checker_df.empty:
            entry_rows = original_csv_df.query('`Burn-in` == @burn_in and `Long-Term Degredation` == @long_term and `Initial PCE` == @init_pce and `Module Cost` == @module_cost')
            location = entry_rows.iat[0,0]
            lcoe2 = entry_rows.iat[0, 6]
            lcoe5 = entry_rows.iat[1,6]
            lcoe10 = entry_rows.iat[2,6]
            lcoe25 = entry_rows.iat[3,6]

            merged_df = merged_df.append({'location': location, 'burn_in': burn_in, 'long_term_degredation': long_term, 'initial_pce': init_pce, 'module_cost': module_cost, 'two_years_lcoe': lcoe2, 'five_years_lcoe': lcoe5, 'ten_years_lcoe': lcoe10, 'tw_five_years_lcoe': lcoe25}, ignore_index=True)

    return merged_df


# Comment in or out the city you want to compact

durham_og = pd.read_csv('Durham.csv')
durham_compact = city_compacter('Durham.csv')
durham_compact.to_csv('output_cities/durham_compact.csv')

copenhagen_og = pd.read_csv('Copenhagen.csv')
copenhagen_compact = city_compacter('Copenhagen.csv')
copenhagen_compact.to_csv('output_cities/copenhagen_compact.csv')

johanesberg_og = pd.read_csv('Johanesberg.csv')
johanesberg_compact = city_compacter('Johanesberg.csv')
johanesberg_compact.to_csv('output_cities/johanesberg_compact.csv')

madrid_og = pd.read_csv('Madrid.csv')
madrid_compact = city_compacter('Madrid.csv')
madrid_compact.to_csv('output_cities/madrid_compact.csv')

nairobi_og = pd.read_csv('Nairobi.csv')
nairobi_compact = city_compacter('Nairobi.csv')
nairobi_compact.to_csv('output_cities/nairobi_compact.csv')

paris_og = pd.read_csv('Paris.csv')
paris_compact = city_compacter('Paris.csv')
paris_compact.to_csv('output_cities/paris_compact.csv')

# confimration = len(copenhagen_og.index)/4
# print('Copenhagen OG length: ', len(copenhagen_og.index))
# print('Copenhagen Compact length: ', len(copenhagen_compact.index))
# print('Copenhagen OG/4: ', str(confimration))
# confimration = len(johanesberg_og.index)/4
# print('Johanesberg OG length: ', len(johanesberg_og.index))
# print('Johanesberg Compact length: ', len(johanesberg_compact.index))
# print('Johanesberg OG/4: ', str(confimration))
# confimration = len(madrid_og.index)/4
# print('Madrid OG length: ', len(madrid_og.index))
# print('Madrid Compact length: ', len(madrid_compact.index))
# print('Madrid OG/4: ', str(confimration))
# confimration = len(nairobi_og.index)/4
# print('Nairobi OG length: ', len(nairobi_og.index))
# print('Nairobi Compact length: ', len(nairobi_compact.index))
# print('Nairobi OG/4: ', str(confimration))
# confimration = len(paris_og.index)/4
# print('Paris OG length: ', len(paris_og.index))
# print('Paris Compact length: ', len(paris_compact.index))
# print('Paris OG/4: ', str(confimration))
