from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder="templates")

todos = [{"task": "Sample todo", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods =["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task":todo, "done":False})
    return redirect(url_for("index"))

@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    todos[index]["done"] = "done" in request.form
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        todos[index]["task"] = request.form['todo']
        return redirect(url_for("index"))
    return render_template("edit.html", todo=todos[index], index=index)

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    del todos[index]
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)