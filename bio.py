from flask import Flask, render_template
import yaml

app = Flask(__name__)

# my_list = []
# with open("links.yaml", 'r') as f:
#     file = yaml.safe_load(f)
    # line = f.readline()
    # while line:
    #     my_list.append(line)
    #     line = f.readline()

# txt = file["links"]["facebook"]["link"]

my_dict = yaml.safe_load(open("links.yaml"))
# link_dict = {}
# for item in "links":
#   link_dict.append(item)

facebook = my_dict["links"][0]["facebook"]["link"]
print(facebook)

@app.route("/") # info page
def info():
    return render_template(
    "info.html",
    nombre = my_dict["nombre"],
    short_bio = my_dict["short_bio"],
    imagen = my_dict["imagen"],
    fb_description = my_dict["links"][0]["facebook"]["description"],
    fb_link = my_dict["links"][0]["facebook"]["link"],
    ig_description = my_dict["links"][1]["instagram"]["description"],
    ig_link = my_dict["links"][1]["instagram"]["link"],
    )
    
if __name__ == "__main__":
    app.run(debug=True)



# Ideas:
# Maybe use {{% if enable == True %}} before the whole div so that block only appears when 
# enable True. Or, create a variable like the teacher did with Developer. (Not sure how to 
# pass this for each website button though)
