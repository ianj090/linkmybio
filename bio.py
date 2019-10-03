from flask import Flask, render_template
from datetime import datetime
import yaml

app = Flask(__name__)

my_dict = yaml.safe_load(open("links.yaml"))
today = datetime.today()

@app.route("/") # info page
def info():
    return render_template(
    "info.html",
    nombre = my_dict["nombre"],
    short_bio = my_dict["short_bio"],
    short_bio2 = my_dict["short_bio2"],
    imagen = my_dict["imagen"],
    date = today.strftime("%d/%m/%Y %H:%M:%S"),

    fb_description = my_dict["links"][0]["facebook"]["description"],
    fb_link = my_dict["links"][0]["facebook"]["link"],
    fb_enable = my_dict["links"][0]["facebook"]["enable"],
    fb_timer = my_dict["links"][0]["facebook"]["until"],
    fb_background = my_dict["links"][0]["facebook"]["background"],
    
    ig_description = my_dict["links"][1]["instagram"]["description"],
    ig_link = my_dict["links"][1]["instagram"]["link"],
    ig_enable = my_dict["links"][1]["instagram"]["enable"],
    ig_timer = my_dict["links"][1]["instagram"]["until"],
    ig_background = my_dict["links"][1]["instagram"]["background"],
    
    bg_description = my_dict["links"][2]["blog"]["description"],
    bg_link = my_dict["links"][2]["blog"]["link"],
    bg_enable = my_dict["links"][2]["blog"]["enable"],
    bg_timer = my_dict["links"][2]["blog"]["until"],
    bg_background = my_dict["links"][2]["blog"]["background"],
    
    gh_description = my_dict["links"][3]["github"]["description"],
    gh_link = my_dict["links"][3]["github"]["link"],
    gh_enable = my_dict["links"][3]["github"]["enable"],
    gh_timer = my_dict["links"][3]["github"]["until"],
    gh_background = my_dict["links"][3]["github"]["background"],

    yt_description = my_dict["links"][4]["youtube"]["description"],
    yt_link = my_dict["links"][4]["youtube"]["link"],
    yt_enable = my_dict["links"][4]["youtube"]["enable"],
    yt_timer = my_dict["links"][4]["youtube"]["until"],
    yt_background = my_dict["links"][4]["youtube"]["background"],

    rd_description = my_dict["links"][5]["random"]["description"],
    rd_link = my_dict["links"][5]["random"]["link"],
    rd_enable = my_dict["links"][5]["random"]["enable"],
    rd_timer = my_dict["links"][5]["random"]["until"],
    rd_background = my_dict["links"][5]["random"]["background"],

    # yt_description = my_dict["links"][4]["youtube"]["description"],
    # yt_link = my_dict["links"][4]["youtube"]["link"],
    # yt_enable = my_dict["links"][4]["youtube"]["enable"],
    )
    
if __name__ == "__main__":
    app.run(debug=True)
