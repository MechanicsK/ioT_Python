import pyrebase


config = {
  "apiKey": "your_api_key",
  "authDomain": "appname.firebaseapp.com",
  "databaseURL": "https://project_name.firebaseio.com",
  "storageBucket":  "appname.appspot.com",
  "serviceAccount": "path_to_service_json"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password('yourmail', 'yourpassword')
user = auth.refresh(user['refreshToken'])
user['idToken']

database_reference = firebase.database()


#Set Value
data = {'name':'Alice', 'Age':23}
database_reference.child("child1").child("child2".set(data)

#Update Value

database_reference.child("child1").child("child2".update(updated_value)

#Fetch Value

Fetched_value = database_reference.child("child1").child("child2").get().val()

