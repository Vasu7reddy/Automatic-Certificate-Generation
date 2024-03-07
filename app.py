from flask import Flask, request, abort
import json
app = Flask(__name__)
from lib.Certificate import Generate
import os
import shutil
import time
import hashlib

@app.route("/api/generate/winner", methods=["GET"])
def winner():
    name = request.args.get("name")
    degree = request.args.get("degree")
    place = request.args.get("place")
    competition = request.args.get("competition")
    year = request.args.get("year")

    principal_sign = request.args.get("p_sign")
    hod_sign = request.args.get("h_sign")
    coordinator_sign = request.args.get("c_sign")
    
    competition_logo = request.args.get("competition_logo")

    if name and degree and place and competition and year and principal_sign and hod_sign and coordinator_sign and competition_logo:
        generate = Generate(os.path.dirname(os.path.realpath(__file__)))
        sigantures = {
            "coordinator": request.args.get("c_sign"),
            "hod": request.args.get("h_sign"),
            "principal": request.args.get("p_sign")
        }
        generate.winner(name=name, degree=degree, place=place, competition=competition, competition_logo=competition_logo, year=year, signatures=sigantures)
        output_file = get_file_name() + ".pdf"
        shutil.copy(os.path.dirname(os.path.realpath(__file__)) + "/output.pdf", "/var/www/certify/assets/certificates/%s" % output_file)
        return json.dumps({
            "result": True,
            "output_file": "/assets/certificates/%s" % output_file
        })
    
    else:
        return json.dumps({
            "result": False,
            "message": "Invalid arguments"
        })

@app.route("/api/generate/participant", methods=["GET"])
def participant():
    name = request.args.get("name")
    degree = request.args.get("degree")
    competition = request.args.get("competition")
    year = request.args.get("year")

    principal_sign = request.args.get("p_sign")
    hod_sign = request.args.get("h_sign")
    coordinator_sign = request.args.get("c_sign")

    competition_logo = request.args.get("competition_logo")

    if name and degree and competition and year and competition_logo:
        generate = Generate(os.path.dirname(os.path.realpath(__file__)))
        sigantures = {
            "coordinator": request.args.get("c_sign"),
            "hod": request.args.get("h_sign"),
            "principal": request.args.get("p_sign")
        }
        generate.participant(name=name, degree=degree, competition=competition, competition_logo=competition_logo, year=year, signatures=sigantures)
        output_file = get_file_name() + ".pdf"
        shutil.copy(os.path.dirname(os.path.realpath(__file__)) + "/output.pdf", "/var/www/certify/assets/certificates/%s" % output_file)
        return json.dumps({
            "result": True,
            "output_file": "/assets/certificates/%s" % output_file
        })
    else:
        return json.dumps({
            "result": False,
            "message": "Invalid arguments"
        })
    
def get_file_name():
    currtime = round(time.time())
    hash = hashlib.md5(str(currtime).encode())
    return hash.hexdigest()

if __name__ == "__main__":
    app.run(debug=True)