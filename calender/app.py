from flask import Flask, render_template, request
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current month and year
    year = request.args.get('year', default=2023, type=int)
    month = request.args.get('month', default=10, type=int)

    # Create a calendar
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)

    # Get month names
    month_names = list(calendar.month_name)[1:]  # Skip the first empty string
    month_name = month_names[month - 1]  # Get the name of the selected month

    return render_template('calendar.html', month_calendar=month_calendar, year=year, month=month, month_name=month_name, months=month_names)

if __name__ == '__main__':
    app.run(debug=True)