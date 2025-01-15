def get_todays_amenity():
    from datetime import datetime
    from flask import render_template

    now = datetime.now()
    year = now.isocalendar()[0]
    weeknumber = now.isocalendar()[1]

    try:
        with open(f"/blog/data/amenities/year{year:4}week{weeknumber:02}.html", "r") as f:
            return f.read()
    except:
        return render_template("amenities/origin.html")