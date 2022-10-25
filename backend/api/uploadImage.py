from flask.wrappers import Request
from flask import request , session
from api.reply import Response
from flask_restful import reqparse, Resource
import time
import hashlib
import json
import time
from datetime import datetime
import time
from flask import session, request
# from flask.config import Config
from api.transfertos3 import img_to_url
m=hashlib.sha256()


#parsing the request data coming from the client side
login_post_arguments = reqparse.RequestParser()
# login_post_arguments.add_argument('icon_url', type=str, help='password is not there', required=False)

class Upload_Image(Resource):
    def post(self) :
        file = request.files['file']
        # filename = secure_filename(file.filename)
        # file.save(os.path.join('/home/user/images', filename))
        return Response(body={} , message="f=dine" , status="sucds").json() , 200

