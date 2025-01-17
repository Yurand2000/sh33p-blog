from flask import Blueprint, redirect, abort
from templates import *

amenities_bp = Blueprint("amenities_pages", __name__)

@amenities_bp.route("/amenity")
def amenity():
    amenity = get_todays_amenity()
    content = render_template("amenity.html", amenity = amenity)
    return render_skeleton("Amenity", content)

def get_todays_amenity():
    from datetime import datetime

    now = datetime.now()
    year = now.isocalendar()[0]
    weeknumber = now.isocalendar()[1]

    try:
        with open(f"/blog/data/amenities/year{year:4}week{weeknumber:02}.html", "r") as f:
            return f.read()
    except:
        return render_template("amenities/origin.html")