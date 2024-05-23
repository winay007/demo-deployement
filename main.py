import webapp2

html_form = """
<!DOCTYPE html>
<html>
<head>
<title>Calculator</title>
</head>
<body>
    <center>
    <form action = "/" method = "post">
    <label for = "weight"> weight: </label>
    <input type="number" id="weight" name="weight" required><br><br>
    <label for = "height"> height: </label>
    <input type="number" id="height" name="height" required><br><br>
    <input type="submit" value="Calculate">
    </form>
    </center>
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(html_form)
    
    def post(self):
        try:
            w = float(self.request.get("weight"))
            h = float(self.request.get("height"))
            bmi = (w / (h * h)) * 10000
            self.response.write("Your BMI is: " + str(bmi))
        except ValueError:
            self.response.write("<h2>Error! Invalid Input")

app = webapp2.WSGIApplication([('/',MainPage)],debug = True)            
