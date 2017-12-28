

FIELDS_NAMES = ["SC_CODE", "SC_NAME", "OPEN", "HIGH", "LOW", "CLOSE"]
SHOW_NUMBER_COMPANIES = 10
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
START_URL = "http://www.bseindia.com/markets/equity/EQReports/BhavCopyDebt.aspx?expandable=3"
BASE_URL = "http://www.bseindia.com/markets/equity/EQReports/"

HTML_TEMPLTE = """<html>
              <head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous"></head>
              <body>
                <form method="get" action="companies" >
                   <div class="col-lg-6" style="padding-top: 15px">
                    <div class="input-group">
                      <input type="text" class="form-control" placeholder="Search by company name" aria-label="Search for..." name="company_name">
                      <span class="input-group-btn">
                        <button class="btn btn-secondary" type="button">Search!</button>
                      </span>
                    </div>
                  </div>
                </form>
                %s
              </body>
            </html> """
