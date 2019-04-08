##API reference

### Endpoints

**api/user/login/**  
Method - POST. Accept json object in this format:  

```json
{  
    "username": "user_name",  
    "password": "user_password'"  
}
```
Returns either access token (something like this):  
```json
{  
    "token": "dfc8bdce962485b515b47e636ef628f30d134aff"  
} 
```
 
,and status __200__ or status __400__ if login failed

**api/user/create/**  
Method - POST. Accept json object in this format:  
```json
{  
    "username": "user_name",  
    "password": "user_password",  
    "confirm_password": "user_password",  
    "email": "user@email.com"  
}
```

Returns either status __201__ (if user successfully created), or status __400__ and json-object with errors list:  
```json
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
```

**api/user/activate/**  
Method GET. Accept activation token:  
```
api/user/activate/?t=<activation_token>
```
Returns either status __200__ if user successfully created or __400__ if activation fail

__api/user/reset/__  
Password reset endpoint.
Method GET: Accept user email
```
api/user/reset/?email=user@email.com
```
Returns status __200__ if user found. Link to reset form send to email.  
Or returns __400__ status if user not found  
Method POST. Accept json object with reset token, new password and password confirmation
```json
{
    "reset_token" :"98458407b0eb7edaa09528300bcbf46b22ad4846",
    "password": "new_password",
    "confirm_password": "new_password"
}
```
Returns status __200__ if password successfully changed, status __400__ and json-object with errors list:
```json
{
    "reset_token": "Invalid token"
}
```

__api/user/logout/__
Delete user auth token. Returns status __200__ in any case

__api/user/block/<user_id>__
User blocking endpoint. Require _IsAdminUser_ permissions. 
Returns either status __200__ if user successfully blocked, or status __400__ otherwise