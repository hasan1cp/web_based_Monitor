from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    total = None
    status_count = {}
    if request.method == "POST":
        file = request.files["logfile"]
        content = file.read().decode("utf-8")
        lines = content.split("\n")
        total = len(lines)
        
        status_pattern = r'"\s(\d{3})'
        for p in lines:
            status = re.search(status_pattern, p)
            if status:
                status = status.group(1)
                status_count[status] = status_count.get(status, 0) + 1


        
    return render_template("hello.html", total= total, status_count = status_count)





if __name__ == "__main__":
    app.run(debug=True)