import nbt
import io
import base64
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import json
from .backend import check, clear, missing
from .backend.get_data.mayor import mayor_json
from .backend.get_data.user_data import user_accessories
from .backend.get_data.news import news
from .backend.artificial_intelligence.chat import load_ai, ask_ai

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@views.route('/<username>')
def profile(username):
    uuid = check.username(username)
    if uuid == 'ERROR':
        flash("Username does not exist", category='error')
        return render_template("profile.html", username=username)
    else:
        profiles = check.stranded(uuid)
        if len(profiles) == 0:
            flash("No Stranded Profiles Found", category='error')
            return render_template("profile.html", username=username)
        return render_template("profile.html", username=username, available=True, profiles=profiles)


@views.route('/<username>/<profile_id>')
def profileID(username, profile_id):
    uuid = check.username(username)
    if uuid == 'ERROR':
        flash("Username does not exist", category='error')
        return render_template("profile.html", username=username)
    else:
        given_profile = check.profileID(uuid, profile_id)
        if given_profile == 'ERROR':
            flash("Profile not Found", category='error')
            return render_template("profile.html", username=username)
        accessories = given_profile['members'][uuid]['inventory']['bag_contents']['talisman_bag']['data']
        data = nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(accessories)))[0]
        bag = []
        for i in data:
            if 'tag' in i:
                bag.append(clear.item_name(i['tag']['ExtraAttributes']['id']))

        bag = list(set(bag))
        return render_template("accessories.html", bag=bag, username=username)


@views.route('/<username>/<profile_id>/chatbot')
def chatbot(username, profile_id):
    uuid = check.username(username)
    if uuid == 'ERROR':
        flash("Username does not exist", category='error')
        return render_template("profile.html", username=username)
    else:
        given_profile = check.profileID(uuid, profile_id)
        if given_profile == 'ERROR':
            flash("Profile not Found", category='error')
            return render_template("profile.html", username=username)

        mayor_json()
        news()
        missing.accessories()
        user_accessories(username, profile_id, save=True)

        return render_template("chatbot.html")


@views.route('/load')
def load():
    if request.args:
        question = request.args.get('q')
        loaded = int(request.args.get('l'))

        if loaded == 0:
            response = load_ai(question)
        else:
            response = ask_ai(question)

        answer = {
            'ans': response
        }

        return answer
