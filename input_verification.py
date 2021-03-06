import webapp2

form="""
<form method="post">
    What is your birthday?
    <br>
    <label>month
        <input type="text" name="month">
    </label>

    <label>Day
        <input type="text" name="day">
    </label>

    <label>Year
        <input type="text" name="year">
    </label>
    <br>
    <br>
    <input type="submit">
</form>

"""

class MainPage(webapp2.RequestHandler):
    """docstring for MainPage"""
    def get(self):
        self.response.write(form)

    def post(self):
        user_month = valid_month(self.request.get("month"))
        user_day = valid_day(self.request.get("day"))
        user_year = valid_year(self.request.get("year"))

        if not (user_month and user_day and user_year)
            self.response.out.write(form)
        else:
            self.response.out.write("cool brah")

    months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

    months_abbvs = dict((m[:3].lower(),m)for m in months)

    def valid_month(month):
        if month:
            short_month = month[:3].lower()
            return months_abbcs.get(short_month)

    def valid_day(day):
        if day:
            day = int(day)
            if day >0 and day <= 31:
                return valid_day

    def valid_year(year):
        if year:
            year = int(year)
            if year >1899 and year <= 2020
                return valid_year

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
