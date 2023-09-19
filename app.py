form flask import Flask, renter_template, request, jsonify
# take dictionary into a json to output

from ice_breaker import ice_break

app = Flask(__name__)

@app.route("/process", methods=["POST"])
# post request with name of person we request about
# invokes the process the function on call
def process():
    name = request.form["name"]
    # extract name from request
    # invoke ice_break function
    # person_info holds summary, ice_breaker, interesting topics, and fun facts
    # profile_pic_url is an image url
    person_info, profile_pic_url = ice_break(name=name)
    # takes a dictionary and makes our webserver return a json object.
    # filled values from pydantic personInfo object
    return jsonify(
        {"summary": person_info.summary, "interests": person_info.topics_of_interst, "facts": person_info.facts,
         "ice_breakers": person_info.ice_breakers, "picture_url": profile_pic_url})


if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)