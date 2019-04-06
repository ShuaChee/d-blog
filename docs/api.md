##API reference

### Endpoints

**api/user/login/** Method - POST. Accept json object in this format:  
{  
    'username': 'user_name',  
    'password': 'user_password'  
}

Returns either access token (something like this):  
{
    "token": "dfc8bdce962485b515b47e636ef628f30d134aff"  
}  
,and status __200__ or status __400__ if login failed

**api/user/create/** Method - POST. Accept json object in this format:  
{  
    'username': 'user_name',  
    'password': 'user_password',  
    'confirm_password': 'user_password',  
    'email': 'user@email.com'  
}

Returns either status __201__ (if user successfully created), or status __400__ and json-object with errors list:  
{  
    "Errors":   {  
        "username": [  
            "This field may not be blank."  
        ],  
        "password": [  
            "This field may not be blank."  
        ],  
        "email": [  
            "user with this email already exists."  
        ]  
    }  
}  