from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from helper import *
from db import *
import bcrypt
import logging


class FindSurah(Resource):
    def post(self):
        # STEP 1: GET POSTED DATA AND CHECK THE DATA
        postedData = request.get_json()
        statusCode = checkPostedData(postedData, "FindSurah")

        if(statusCode != 200):
            response = {
                "responseMessage": "An Error Happened",
                "responseCode": statusCode
            }
            return jsonify(response)
        else:
            surahNumber = postedData["surahNumber"]
            surahNumber = int(surahNumber)
            response = {
                "responseMessage": "Success",
                "responseCode": 200
            }
            return jsonify(response)


class Register(Resource):
    def post(self):
        # STEP 1: GET POSTED DATA
        postedData = request.get_json()

        # STEP 2: GET SPECIFIC DATA FROM POSTED DATA AND CHECK DATA
        username = postedData["username"]
        password = postedData["password"]

        if(users.count() > 0 and "users" in db.list_collection_names()):
            findUsers = users.find({
                "username": str(username)
            })[0]["username"]
            if(username == findUsers):
                response = {
                    "responseCode": 200,
                    "responseMessage": "Your Register Is Failed, Because Username Taken"
                    }
                return jsonify(response)

            else:
                # STEP 3: HASH PASSWORD
                hashedPassword = bcrypt.hashpw(
                    password.encode("utf8"), bcrypt.gensalt())

                # STEP 4: STORE USERNAME AND PASSWORD TO DB
                users.insert({
                    "username": username,
                    "password": hashedPassword,
                })

                # STEP 5: GIVE RESPONSE
                response = {
                    "responseCode": 200,
                    "responseMessage": "Your Register Is Success"
                }
                return jsonify(response)
        else:
            # STEP 3: HASH PASSWORD
            hashedPassword = bcrypt.hashpw(
                password.encode("utf8"), bcrypt.gensalt())

            # STEP 4: STORE USERNAME AND PASSWORD TO DB
            users.insert({
                "username": username,
                "password": hashedPassword,
            })

            # STEP 5: GIVE RESPONSE
            response = {
                "responseCode": 200,
                "responseMessage": "Your Register Is Success"
            }
            return jsonify(response)


class StorePosition(Resource):
    def post(self):
        # STEP 1: GET POSTED DATA
        postedData = request.get_json()

        # STEP 2: GET SPECIFIC DATA FROM POSTED DATA AND CHECK DATA
        username = postedData["username"]
        startPosition = postedData["storePosition"]
        endPosition = postedData["endPosition"]

        # STEP 3: STORE POSITION
        anotation.insert({
            "username": username,
            "startPosition": startPosition,
            "endPosition": endPosition
        })

        # STEP 4: GIVE RESPONSE
        response = {
            "responseCode": 200,
            "responseMessage": "Your Annotation Saved"
        }
        return jsonify(response)


class Login(Resource):
    def post(self):
        # STEP 1: GET POSTED DATA
        postedData = request.get_json()

        # STEP 2: GET SPECIFIC DATA FROM POSTED DATA AND CHECK DATA
        username = postedData["username"]
        password = postedData["password"]

        hashedPassword = users.find({
            "username": username
        })[0]["password"]

        if bcrypt.hashpw(password.encode('utf8'), hashedPassword) == hashedPassword:
            return True
        else:
            # STEP 3: GIVE RESPONSE
            reponse = {
                "responseCode": 407,
                "responseMessage": "Your Username Or Password Didn't Match"
            }
            return jsonify(response)


class DumpCorpusToDB(Resource):
    def post(self):
        # STEP 1: GET POSTED DATA
        postedData = request.get_json()

        # STEP 2: RUN METHOD
        storeCorpusToDB()

        # STEP 3: GIVE RESPONSE
        response = {
            "responseCode": 200,
            "responseMessage": "Dump Data Success"
        }
        return jsonify(response)
