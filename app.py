from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Bengaluru ,India' ,
        'salary' : 'Rs.10,00,000'
    },
    {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Dehi,India',
        'salary' : 'Rs.15,50,000'
    },
    {
        'id' : 3,
        'title' : 'FrontEnd Developer',
        'location' : 'remote',
        'salary' : 'Rs.13,00,00'
    },
    {
        'id' : 4,
        'title' : 'BackEnd Developer',
        'location' : 'Sanfransisco',
        'salary' : '$1300'
    }
]

@app.route("/")
def hello_world():
    # return render_template('Home.html')
    return render_template('jobApplication.html',
                           jobs=JOBS,
                          company_name = 'Jovian')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
