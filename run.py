from app import create_app

app=create_app() ##^ By calling the function we are creating the one app

if __name__ =="__main__":  ## ^ app going to run only when it directly going to execute .
    app.run(debug=True)  #^ Here we are running that app.
    