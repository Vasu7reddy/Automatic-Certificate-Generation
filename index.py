import pdfkit
from sys import argv
from lib.Argument import Argument
from lib.Certificate import Generate
import os

# options = {
#     'page-size': 'A4',
#     'orientation': 'Landscape',
#     "enable-local-file-access": ""
# }

# css = "main.css"

# main_file = open("index.html", "r")
# main_file_contents = main_file.read()
# main_file_contents = main_file_contents.replace('{{name}}', "sudharshan")

# temp_file_name = "index_temp.html"
# temp_file = open(temp_file_name, "w+")
# temp_file.write(main_file_contents)
# pdfkit.from_file("index.html", "sdf.pdf", options=options, css=css)

def print_commands_help():
    print("Usage: " + argv[0] + " [participant|winner]")
    exit(-1)

def print_participant_help():
    print("Usage: " + argv[0] + " participant --name=<value> --degree=<value> --competition=<value> --year=<value> --p-sign=<value> --c-sign=<value> -h--sign=<value>")
    exit(-1)
    
def print_winner_help():
    print("Usage: " + argv[0] + " winner --name=<value> --degree=<value> --place=<value> --competition=<value> --year=<value> --p-sign=<value> --c-sign=<value> -h--sign=<value>")
    exit(-1)

a = Argument(argv)
generate = Generate(os.path.dirname(os.path.realpath(__file__)))

if (a.hasCommand("participant") or a.hasCommand("winner")) == False:
    print_commands_help()

if(a.hasCommand("participant")):
    reqoptions = ["--name", "--degree", "--competition", "--year", "--p-sign", "--c-sign", "--h-sign"]
    if not a.hasOptions(reqoptions):
        print_participant_help()

    reqoptionvalues = ["--name", "--degree", "--competition", "--year", "--p-sign", "--c-sign", "--h-sign"]
    is_values_found = True
    for op in reqoptionvalues:
        if a.hasOptionValue(op) == False:
            is_values_found = False
            break

    if is_values_found == False:
        print_participant_help()

    name = a.getOptionValue("--name")
    degree = a.getOptionValue("--degree")
    competition = a.getOptionValue("--competition")
    year = a.getOptionValue("--year")
    signatures = {
        "coordinator": a.getOptionValue("--c-sign"),
        "hod": a.getOptionValue("--h-sign"),
        "principal": a.getOptionValue("--p-sign")
    }

    generate.participant(name=name, degree=degree, competition=competition, year=year, signatures=signatures)
    exit(0)
else:
    reqoptions = ["--name", "--degree", "--place", "--competition", "--year", "--p-sign", "--c-sign", "--h-sign"]
    if not a.hasOptions(reqoptions):
        print_winner_help()

    reqoptionvalues = ["--name", "--degree", "--place", "--competition", "--year", "--p-sign", "--c-sign", "--h-sign"]
    is_values_found = True
    for op in reqoptionvalues:
        if a.hasOptionValue(op) == False:
            is_values_found = False
            break

    if is_values_found == False:
        print_winner_help()

    name = a.getOptionValue("--name")
    degree = a.getOptionValue("--degree")
    place = a.getOptionValue("--place")
    competition = a.getOptionValue("--competition")
    year = a.getOptionValue("--year")
    signatures = {
        "coordinator": a.getOptionValue("--c-sign"),
        "hod": a.getOptionValue("--h-sign"),
        "principal": a.getOptionValue("--p-sign")
    }

    generate.winner(name=name, degree=degree, place=place, competition=competition, year=year, signatures=signatures)
    exit(0)