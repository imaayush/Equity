# Equity
   
   The repository provdides the following items:
   
   ## bhavcopy_script.py
      - Downloads the Equity bhavcopy zip from the above page
      - Extracts and parses the CSV file in it
      - Writes the records into Redis into appropriate data structures
        (Fields: code, name, open, high, low, close)
        
   ## CherryPy python web application
       - Renders an HTML5 + CSS3 page that lists the top 10 stock entries from the Redis DB in a table
       - Has a searchbox that lets you search the entries by the 'name' field in Redis and renders it in a table
        (Partial name search is not supported) 
       

  ## Setting Dev Enviornment

     
   #### Install basics
          This setup is for Ubuntu 14.10 or later
          sudo aptitude install git python-virtualenv python-dev

   #### Set up virtual environment, and install dependencies
          virtualenv env
          source env/bin/activate

   #### Clone repository and install requirements

          git clone https://github.com/imaayush/Equity.git
          cd Equity
          pip install -r requirements.txt
          
   #### Run script
          python bhavcopy_script.py
          
   #### Run cherrypy server
         python main.py

      
