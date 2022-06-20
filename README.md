# City compacter and merger for lcoe-web-app-database
## Requirements
- Pyhton 3.8
- Venv
- pandas
## Using the code
### Setting up the environment
```
python3.8 -m venv venv
source venv/bin/activate
```
### City compacter
Uses the base version of the csv files to generate a new csv file for each city in the output_cities directory. Comment in/out the cities for the csv files to be generated accordingly.
```
python compacter.py
```
### City merger
Uses the compacted csv files for each city to generate one big csv file with all the information available.
```
pyhton merger.py
```
## Sanity Checks
### Length Confirmations
Run:
```
python sanity_check/length-confirmation.py
```
To get terminal outputs relating to the lenght of the original and compacted csv files.
### Value Confirmations
Run:
```
python sanity_check/bug-fixing.py
```
To get lcoe values printed out for all cities in every document including the original, the compacted and the all_cities.csv files to compare if the values are set right in the final generated document.
