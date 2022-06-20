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

def city_merger(durham, copenhagen, johanesberg, madrid, nairobi, paris):
    merged_df = pd.DataFrame(columns=['burn_in', 'long_term_degredation', 'initial_pce', 'module_cost', 'durham_two_years_lcoe', 'durham_five_years_lcoe', 'durham_ten_years_lcoe', 'durham_tw_five_years_lcoe', 'copenhagen_two_years_lcoe', 'copenhagen_five_years_lcoe', 'copenhagen_ten_years_lcoe', 'copenhagen_tw_five_years_lcoe', 'johanesberg_two_years_lcoe', 'johanesberg_five_years_lcoe', 'johanesberg_ten_years_lcoe', 'johanesberg_tw_five_years_lcoe', 'madrid_two_years_lcoe', 'madrid_five_years_lcoe', 'madrid_ten_years_lcoe', 'madrid_tw_five_years_lcoe', 'nairobi_two_years_lcoe', 'nairobi_five_years_lcoe', 'nairobi_ten_years_lcoe', 'nairobi_tw_five_years_lcoe', 'paris_two_years_lcoe', 'paris_five_years_lcoe', 'paris_ten_years_lcoe', 'paris_tw_five_years_lcoe'])
    for index, row in durham.iterrows():
        burn_in = durham.iat[index, 2]
        long_term = durham.iat[index, 3]
        init_pce = durham.iat[index, 4]
        module_cost = durham.iat[index, 5]

        duplicate_checker_df = merged_df.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')

        if duplicate_checker_df.empty:
            durham_entry_rows = durham.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')
            durham_lcoe2 = durham_entry_rows.iat[0, 6]
            durham_lcoe5 = durham_entry_rows.iat[0,7]
            durham_lcoe10 = durham_entry_rows.iat[0,8]
            durham_lcoe25 = durham_entry_rows.iat[0,9]

            copenhagen_entry_rows = copenhagen.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')
            copenhagen_lcoe2 = copenhagen_entry_rows.iat[0, 6]
            copenhagen_lcoe5 = copenhagen_entry_rows.iat[0,7]
            copenhagen_lcoe10 = copenhagen_entry_rows.iat[0,8]
            copenhagen_lcoe25 = copenhagen_entry_rows.iat[0,9]

            johanesberg_entry_rows = johanesberg.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')
            johanesberg_lcoe2 = johanesberg_entry_rows.iat[0, 6]
            johanesberg_lcoe5 = johanesberg_entry_rows.iat[0,7]
            johanesberg_lcoe10 = johanesberg_entry_rows.iat[0,8]
            johanesberg_lcoe25 = johanesberg_entry_rows.iat[0,9]

            madrid_entry_rows = madrid.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')
            madrid_lcoe2 = madrid_entry_rows.iat[0, 6]
            madrid_lcoe5 = madrid_entry_rows.iat[0,7]
            madrid_lcoe10 = madrid_entry_rows.iat[0,8]
            madrid_lcoe25 = madrid_entry_rows.iat[0,9]

            nairobi_entry_rows = nairobi.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')
            nairobi_lcoe2 = nairobi_entry_rows.iat[0, 6]
            nairobi_lcoe5 = nairobi_entry_rows.iat[0,7]
            nairobi_lcoe10 = nairobi_entry_rows.iat[0,8]
            nairobi_lcoe25 = nairobi_entry_rows.iat[0,9]

            paris_entry_rows = paris.query('`burn_in` == @burn_in and `long_term_degredation` == @long_term and `initial_pce` == @init_pce and `module_cost` == @module_cost')
            paris_lcoe2 = paris_entry_rows.iat[0, 6]
            paris_lcoe5 = paris_entry_rows.iat[0,7]
            paris_lcoe10 = paris_entry_rows.iat[0,8]
            paris_lcoe25 = paris_entry_rows.iat[0,9]

            merged_df = merged_df.append({'burn_in': burn_in, 'long_term_degredation': long_term, 'initial_pce': init_pce, 'module_cost': module_cost, 'durham_two_years_lcoe': durham_lcoe2, 'durham_five_years_lcoe': durham_lcoe5, 'durham_ten_years_lcoe': durham_lcoe10, 'durham_tw_five_years_lcoe': durham_lcoe25, 'copenhagen_two_years_lcoe': copenhagen_lcoe2, 'copenhagen_five_years_lcoe': copenhagen_lcoe5, 'copenhagen_ten_years_lcoe': copenhagen_lcoe10, 'copenhagen_tw_five_years_lcoe': copenhagen_lcoe25, 'johanesberg_two_years_lcoe': johanesberg_lcoe2, 'johanesberg_five_years_lcoe': johanesberg_lcoe5, 'johanesberg_ten_years_lcoe': johanesberg_lcoe10, 'johanesberg_tw_five_years_lcoe': johanesberg_lcoe25, 'madrid_two_years_lcoe': madrid_lcoe2, 'madrid_five_years_lcoe': madrid_lcoe5, 'madrid_ten_years_lcoe': madrid_lcoe10, 'madrid_tw_five_years_lcoe': madrid_lcoe25, 'nairobi_two_years_lcoe': nairobi_lcoe2, 'nairobi_five_years_lcoe': nairobi_lcoe5, 'nairobi_ten_years_lcoe': nairobi_lcoe10, 'nairobi_tw_five_years_lcoe': nairobi_lcoe25, 'paris_two_years_lcoe': paris_lcoe2, 'paris_five_years_lcoe': paris_lcoe5, 'paris_ten_years_lcoe': paris_lcoe10, 'paris_tw_five_years_lcoe': paris_lcoe25}, ignore_index=True)
    return merged_df

merged_cities = city_merger(durham_compact, copenhagen_compact, johanesberg_compact, madrid_compact, nairobi_compact, paris_compact)
merged_cities.to_csv('merged_files/all_cities.csv')
print(len(merged_cities.index))
