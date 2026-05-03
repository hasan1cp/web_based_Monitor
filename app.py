from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    total = None
    status_count = {}
    ip_count = {}
    sorted_ip = {}
    top_ips = []
    if request.method == "POST":
        file = request.files["logfile"]
        content = file.read().decode("utf-8")
        lines = [line for line in content.split("\n") if line.strip()]
        total = len(lines)
        
        status_pattern = r'"\s(\d{3})'
        for p in lines:
            status = re.search(status_pattern, p)
            if status:
                status = status.group(1)
                status_count[status] = status_count.get(status, 0) + 1
        for a in lines:
            ip = a.split()[0]
            ip_count[ip] = ip_count.get(ip, 0) + 1

        sorted_ip = sorted(ip_count.items(), key = lambda x: x[1], reverse=True)
        top_ips = sorted_ip[:5]
        
    return render_template("hello.html", total= total, status_count = status_count, ips = top_ips)





if __name__ == "__main__":
    app.run(debug=True)