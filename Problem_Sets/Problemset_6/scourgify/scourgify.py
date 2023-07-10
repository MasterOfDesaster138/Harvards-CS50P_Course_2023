"""
    Title: Problemset_6 - scourgify

    Author: Emely Benke

    Created: 2023-06-28

    Version: 0.1

    Summary:
            “Ah, well,” said Tonks, slamming the trunk’s lid shut, “at least it’s all in.
            That could do with a bit of cleaning, too.” She pointed her wand at Hedwig’s cage.
            “Scourgify.” A few feathers and droppings vanished.
                        — Harry Potter and the Order of the Phoenix

            Data, too, often needs to be “cleaned,” as by reformatting it,
            so that values are in a consistent, if not more convenient, format.
            Consider, for instance, this CSV file of students, before.csv, below:

                            name,house
                            "Abbott, Hannah",Hufflepuff
                            "Bell, Katie",Gryffindor
                            "Bones, Susan",Hufflepuff
                            "Boot, Terry",Ravenclaw
                            "Brown, Lavender",Gryffindor
                            "Bulstrode, Millicent",Slytherin
                            "Chang, Cho",Ravenclaw
                            "Clearwater, Penelope",Ravenclaw
                            "Crabbe, Vincent",Slytherin
                            "Creevey, Colin",Gryffindor
                            "Creevey, Dennis",Gryffindor
                            "Diggory, Cedric",Hufflepuff
                            "Edgecombe, Marietta",Ravenclaw
                            "Finch-Fletchley, Justin",Hufflepuff
                            "Finnigan, Seamus",Gryffindor
                            "Goldstein, Anthony",Ravenclaw
                            "Goyle, Gregory",Slytherin
                            "Granger, Hermione",Gryffindor
                            "Johnson, Angelina",Gryffindor
                            "Jordan, Lee",Gryffindor
                            "Longbottom, Neville",Gryffindor
                            "Lovegood, Luna",Ravenclaw
                            "Lupin, Remus",Gryffindor
                            "Malfoy, Draco",Slytherin
                            "Malfoy, Scorpius",Slytherin
                            "Macmillan, Ernie",Hufflepuff
                            "McGonagall, Minerva",Gryffindor
                            "Midgen, Eloise",Gryffindor
                            "McLaggen, Cormac",Gryffindor
                            "Montague, Graham",Slytherin
                            "Nott, Theodore",Slytherin
                            "Parkinson, Pansy",Slytherin
                            "Patil, Padma",Gryffindor
                            "Patil, Parvati",Gryffindor
                            "Potter, Harry",Gryffindor
                            "Riddle, Tom",Slytherin

            Even though each “row” in the file has three values (last name, first name, and house),
            the first two are combined into one “column” (name), escaped with double quotes,
            with last name and first name separated by a comma and space.
            Not ideal if Hogwarts wants to send a form letter to each student, as via mail merge,
            since it’d be strange to start a letter with:

            Dear Potter, Harry,

            Rather than with, for instance:

            Dear Harry,


            In a file called scourgify.py, implement a program that:

            Expects the user to provide two command-line arguments:
            the name of an existing CSV file to read as input,
            whose columns are assumed to be, in order, name and house, and
            the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
            Converts that input to that output, splitting each name into a first name and last name.
            Assume that each student will have both a first name and last name.
            If the user does not provide exactly two command-line arguments,
            or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

""" Hints:
Note that csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are DictReader,
per docs.python.org/3/library/csv.html#csv.DictReader and DictWriter, per docs.python.org/3/library/csv.html#csv.DictWriter.

Note that you can tell a DictWriter to write its fieldnames to a file using writeheader with no arguments,
per docs.python.org/3/library/csv.html#csv.DictWriter.writeheader."""
##### Imports: #####
import sys  # for handling command-line arguments and exiting the program
import csv  # for reading the CSV file and usage of the DictReader and DictWriter


##### Functions: #####

def main():
    # Validate the inputted command-line paramters specified from the user
    if validate_user_input(sys.argv):
        # unpack the required file names from user input
        input_file, output_file = sys.argv[1:3]

        # Collects data from csv file into a list
        input_data = input_file_reader(input_file)

        # Tranforms the data from input file into the proper schema for the output file
        tranformed_data = tranformate_data_schema(input_data)

        # Now we want to write the tranformed datacollection to the specified output file
        output_file_writer(tranformed_data, output_file)

        # After writing the data to the file, we can close the program
        quit()



def validate_user_input(cl_parameters: list) -> bool:
    """validate_user_input

    Args:
        cl_parameters (list): inputted command-line arguments from sys.argv

    Returns:
        bool: indicates if the validation was succesfull or not

    Raises:
        SystemExit:  If the user does not provide exactly two command-line arguments, or the first parameter is not a CSV file.
    """
    # the user must provide exactly two command-line arguments
    if len(cl_parameters) < 3:
        sys.exit("Too few command-line arguments")
    elif len(cl_parameters) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if cl_parameters[1].strip().endswith(".csv"):
            return True
        else:
            sys.exit("Not a CSV file")


def input_file_reader(input_file: str) -> list:
    """input_file_reader opens a csv file in readmode and returns the collected data,
    or handles the exception with sys.exit + Errormessage, if the File cannot be read / found.

    Args:
        input_file (str): spefified file name from user for data collecting

    Returns:
        list: returns the collected data, each row represented as a dictionary
    """
    # initialize an empty list to collect the csv_data
    csv_data = []

    # Try to open the given file, for reading and collecting the containing csv data
    try:
        # open the given input file in read-mode
        with open(input_file, 'r') as file:
            # DictReader parses each line as an Dictionary
            csv_reader = csv.DictReader(file)
            # iterate through each line and collect the data into a list
            for row in csv_reader:
                # column_order: Name | House
                csv_data.append({"name": row["name"], "house": row["house"]})

        return csv_data

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    except csv.Error as e:
        raise e


def tranformate_data_schema(input_data: list) -> list:
    """tranformate_data_schema from [name, house] to new schema [firstname, lastname, house] and returns converted data collection.

    Args:
        input_data (list): collected data from inputted file, specified by the user

    Returns:
        list: returns the tranformed data, where first and last name will be separate elements
    """
    # initialize a empty list for collecting the tranformated data
    tranformed_data = []

    # we need to loop through all elements of the list
    for row in input_data:
        # Separate first and last name
        lastname, firstname = row["name"].split(', ')
        # Collects new dataschema into a prepared list
        tranformed_data.append({"first": firstname, "last": lastname, "house": row["house"]})

    return tranformed_data


def output_file_writer(datacollection: list, output_file: str):

    # prepare a list with the fieldnames for the output file
    new_fieldnames = ("first", "last", "house")

    # opens the specified output file in append mode for writing operations
    with open(output_file, 'a', newline="") as file:
        # DictWriter parses every row of the collection as an dictionary
        csv_writer = csv.DictWriter(file, fieldnames=new_fieldnames)
        csv_writer.writeheader()
        # Loop through each element of the collection and write the data to the file
        for row in datacollection:
            csv_writer.writerow({"firstname": row["first"], "lastname": row["last"], "house": row["house"]})



if __name__ == '__main__':
    main()
