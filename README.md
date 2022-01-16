# Election_Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has requested information about the most recent election. We have already provided candidate calculations which include the total votes and the total votes per candidate along with the percentage of votes per candidate. Now they would like some information about votes by county. Their requests are below:

1. Calculate total votes for each county.
2. Calculate the percentage of votes for each county.
3. Determine the county with the largest turnout.

## Audit Election Results

- The total amount of votes cast in the election was 369,711.
- The county results were:
  - Jefferson county received 10.5% of the vote and 38,855 number of votes.
  - Denver county received 82.8% of the vote and 306,055 number of votes.
  - Arapahoe county received 6.7% of the vote and 24,801 number of votes.
- The largest county turnout was Denver.
- The candidate results were:
  - Charles Casper Stockham received 23% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Audit Election Summary

In this analysis we used Python code to calculate a breakdown of candidate votes and county votes. For future elections, if more information is gathered about voters we can provide an additional breakdown. If a gender column was provided for example, we could add the following code to create a tally:

```python
gender_options = []
voter_genders = {}

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

      voter_gender = row[3]

      if voter_gender not in gender_options:

            # Add the gender name to the gender list.
            gender_options.append(voter_gender)

            # And begin tracking that voter gender.
            voter_genders[voter_gender] = 0

        # Add a tally to that gender's count
        voter_genders[voter_gender] += 1
```

With the above, we would have everything needed in order to show detailed information about voter gender percentages. We could do the same for voter age, ethnicity, or any other information about voters that was collected.

For a countrywide election, this script can be reused simply by replacing all mentions of `county` with `state`. For example the following variables at the top of the file:

```python
county_list = []
county_votes = {}
```

The above would just need to be renamed like so:

```python
state_list = []
state_votes = {}
```

...and so on down the rest of the script.

There is a lot of potential for further analysis of voter data if more is collected. In addition this script can easily be expanded to handle nationwide elections. The reusability of this script makes it a great choice for your business.
