from flask import Flask, render_template
import yaml

app = Flask(__name__)

my_dict = yaml.safe_load(open("links.yaml"))

@app.route("/") # info page
def info():
    return render_template(
    "info.html",
    nombre = my_dict["nombre"],
    short_bio = my_dict["short_bio"],
    imagen = my_dict["imagen"],

    fb_description = my_dict["links"][0]["facebook"]["description"],
    fb_link = my_dict["links"][0]["facebook"]["link"],
    fb_enable = my_dict["links"][0]["facebook"]["enable"],
    
    ig_description = my_dict["links"][1]["instagram"]["description"],
    ig_link = my_dict["links"][1]["instagram"]["link"],
    ig_enable = my_dict["links"][1]["instagram"]["enable"],
    
    bg_description = my_dict["links"][2]["blog"]["description"],
    bg_link = my_dict["links"][2]["blog"]["link"],
    bg_enable = my_dict["links"][2]["blog"]["enable"],
    
    gh_description = my_dict["links"][3]["github"]["description"],
    gh_link = my_dict["links"][3]["github"]["link"],
    gh_enable = my_dict["links"][3]["github"]["enable"],

    yt_description = my_dict["links"][4]["youtube"]["description"],
    yt_link = my_dict["links"][4]["youtube"]["link"],
    yt_enable = my_dict["links"][4]["youtube"]["enable"],

    al_description = my_dict["links"][5]["algo"]["description"],
    al_link = my_dict["links"][5]["algo"]["link"],
    al_enable = my_dict["links"][5]["algo"]["enable"],

    # yt_description = my_dict["links"][4]["youtube"]["description"],
    # yt_link = my_dict["links"][4]["youtube"]["link"],
    # yt_enable = my_dict["links"][4]["youtube"]["enable"],
    )
    
if __name__ == "__main__":
    app.run(debug=True)
