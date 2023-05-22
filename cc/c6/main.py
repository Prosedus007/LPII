import webapp2

class MainPage(webapp2.RequestHandler):
     def get(self):
          n = 8
          n1, n2 = 0, 1
          count = 0
          while count < n:
               self.response.write(n1)
               self.response.write("<br />")
               nth = n1 + n2
               n1 = n2
               n2 = nth
               count += 1
        
app = webapp2.WSGIApplication([('/',MainPage),], debug=True)