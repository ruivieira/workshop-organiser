# Group Formation Tool

This script assists in creating diverse and distinct groups from a list of individuals. The script reads a CSV file that contains details about individuals, their unit, topic, and known connections. The goal is to generate groups that contain a diverse mix of units and topics and minimize connections between individuals within the same group.

## Requirements

- Python 3.7 or later
- Pandas library (Install with `pip install pandas`)

## Usage

The script can be run from the command line with the following:

```shell
python group_formation_tool.py filename.csv num_groups group_size
```

Arguments:

- `filename.csv`: The CSV file containing the individuals data.
- `num_groups`: The number of groups to be created.
- `group_size`: The desired size of each group (the last group size will be the remainder).

The CSV file should be formatted as follows:

```csv
name,unit,topic,known
person1,unit1,topic1,person2,person3
person2,unit2,topic2,person1,person4
...
```

Where each row represents an individual, with the following columns:

- `name`: The name of the individual.
- `unit`: The unit that the individual belongs to.
- `topic`: The topic that the individual is involved in.
- `known`: A list of individuals that this person knows, separated by commas.

The script will output the groups as a printed list in the console and save it as an Excel spreadsheet. The spreadsheet will have one row per individual, with columns for their name, unit, topic, known connections, their group in the first set, and their group in the second set.

## Notes

This script uses a heuristic algorithm to generate the groups. It attempts to create diverse groups by varying the units and topics, and minimizing connections within the groups. The result may not always be the optimal solution, but in most cases, it should be a good approximation.

This script is best used as a starting point for manual group formation, and further manual adjustments can be made as needed.

## Limitations

The script assumes that the input CSV file is correctly formatted, and all provided names are unique. Any deviations from this assumption may result in incorrect group formation.

## License

This script is open-source software released under the GPL3 license.
