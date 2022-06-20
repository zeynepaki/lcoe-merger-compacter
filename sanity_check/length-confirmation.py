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

confimration = len(copenhagen_og.index)/4
print('Copenhagen OG length: ', len(copenhagen_og.index))
print('Copenhagen Compact length: ', len(copenhagen_compact.index))
print('Copenhagen OG/4: ', str(confimration))
confimration = len(johanesberg_og.index)/4
print('Johanesberg OG length: ', len(johanesberg_og.index))
print('Johanesberg Compact length: ', len(johanesberg_compact.index))
print('Johanesberg OG/4: ', str(confimration))
confimration = len(madrid_og.index)/4
print('Madrid OG length: ', len(madrid_og.index))
print('Madrid Compact length: ', len(madrid_compact.index))
print('Madrid OG/4: ', str(confimration))
confimration = len(nairobi_og.index)/4
print('Nairobi OG length: ', len(nairobi_og.index))
print('Nairobi Compact length: ', len(nairobi_compact.index))
print('Nairobi OG/4: ', str(confimration))
confimration = len(paris_og.index)/4
print('Paris OG length: ', len(paris_og.index))
print('Paris Compact length: ', len(paris_og.index))
