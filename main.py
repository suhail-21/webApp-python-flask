#websites acts as a pythonPackage so that create_app() can be imported.
from websites import create_app

app = create_app()


#Defining the main function
if __name__ == '__main__':

    #Run the flask application, and everytime there is a change in python code,
    #it's going to automatically rerun the webServer, avoiding to manually rerun
    #the server for every change.
    app.run(debug=True)