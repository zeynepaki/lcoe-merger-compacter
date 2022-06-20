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
