# test_api_py
git clone https://github.com/annabnn812/test_api_py.git

cd test_api_py

npm install

//TO start the unit test API server which is listening on port 3001

npm start &

//You con confirm the server is working by opening a browser and entering this URL - http://locahost:3001/users


You need to install python3, 

install requests library

install pip3 

install json

run the python from the linux(ubuntu) command prompt  : python3 scrubber.py


RESULT
=========================================================================================
INPUT:

{

  id: 123,
  
  name: 'Elsa',
  
  username: 'iugkio18',
  
  email: 'elsa@gmail.com',
  
  power: 'ice ray',
  
  friends: [
  
    { id: 234, username: 'Magic213' },
    
    { id: 456, username: 'call_me_anna' },
    
    { id: 222, username: 'Trololo' },
    
    { id: 8846, username: 'Just_Alice' }
    
  ]
  
}

OUTPUT:

{

  "id": 123,
  
  "name": "****",
  
  "username": "********",
  
  "email": "****@gmail.com",
  
  "age": 21,
  
  "power": "ice ray",
  
  "friends": "[{"id":234,"username":"********"},{"id":456,"username":"************"},{"id":222,"username":"*******"},{"id":8846,"username":"**********"}]"
  
}
