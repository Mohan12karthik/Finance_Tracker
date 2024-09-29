from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collect the form data and perform some calculations (dummy for now)
    salary = request.form['salary']
    rent = request.form['rent']
    utilities = request.form['utilities']
    misc = request.form['miscellaneous']
    goal = request.form['goal']
    
    # Calculate total expenses and other financial insights
    total_expense = float(rent) + float(utilities) + float(misc)
    necessary_savings = float(salary) - total_expense
    report = {
        'total_income': salary,
        'total_expense': total_expense,
        'necessary_savings': necessary_savings
    }
    
    # Placeholder for generated plots (dummy)
    plots = {
        'expense_plot': '/static/expense_plot.png',
        'savings_plot': '/static/savings_plot.png'
    }
    return render_template('summary.html', report=report, plots=plots)

if __name__ == '__main__':
    app.run(debug=True)
