import pdfkit
import requests

class Generate:

    def __init__(self, work_dir):
        self.options = {
            'page-size': 'A4',
            'orientation': 'Landscape',
            "enable-local-file-access": ""
        }
        self.css_file = work_dir + "/assets/main.css"
        self.main_participant_file = work_dir + "/assets/participant.html"
        self.main_winner_file = work_dir + "/assets/winner.html"
        self.output_file = work_dir + "/output.html"
        self.output_dir = work_dir + "/output/"
        self.certify_dir = "/var/www/certify/"

    def participant(self, name, degree, competition, year, competition_logo, signatures: dict, output = "output.pdf"):
        tempfile = open(self.main_participant_file, "r")
        tempfile = tempfile.read()
        placeholder = {
            "name": name,
            "degree": degree,
            "competition" : competition,
            "year": year,
            "competition_logo": self.certify_dir + requests.utils.unquote(competition_logo),
            "coordinator_sign": self.certify_dir + signatures['coordinator'],
            "hod_sign": self.certify_dir + signatures['hod'],
            "principal_sign": self.certify_dir + signatures['principal']
        }

        for k, v in placeholder.items():
            tempfile = tempfile.replace("{{" + k + "}}", v)

        output_file = open(self.output_file, "w+")
        output_file.write(tempfile)
        output_file.flush()
        pdfkit.from_file(self.output_file, output, options=self.options, css=self.css_file)

    def winner(self, name, degree, place, competition, year, competition_logo, signatures, output="output.pdf"):
        tempfile = open(self.main_winner_file, "r")
        tempfile = tempfile.read()
        placeholder = {
            "name": name,
            "degree": degree,
            "place": place,
            "competition" : competition,
            "year": year,
            "competition_logo": self.certify_dir + requests.utils.unquote(competition_logo),
            "coordinator_sign": self.certify_dir + signatures['coordinator'],
            "hod_sign": self.certify_dir + signatures['hod'],
            "principal_sign": self.certify_dir + signatures['principal']
        }

        for k, v in placeholder.items():
            tempfile = tempfile.replace("{{" + k + "}}", v)

        output_file = open(self.output_file, "w+")
        output_file.write(tempfile)
        output_file.flush()
        pdfkit.from_file(self.output_file, output, options=self.options, css=self.css_file)