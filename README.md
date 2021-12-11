[![Alohomora](https://circleci.com/gh/xiaomi388/comsw-4156-project/tree/master.svg?style=svg)](https://app.circleci.com/pipelines/github/xiaomi388/comsw-4156-project)
[![codecov](https://codecov.io/gh/xiaomi388/comsw-4156-project/branch/master/graph/badge.svg?token=W6R9U4E57A)](https://codecov.io/gh/xiaomi388/comsw-4156-project)

Course project for comsw4156

Team Name: Alohomora

## run and test Instructions

### Run

```
python
pip3 install -r requirements.txt
flask run
```

### Test

```
coverage run -m unittest discover
coverage html
```

The flake8 and coverage reports have been stored in the `report` folder.

## API

### **POST** - /register

This API is used for new user registration

#### Request

##### Body Parameters

- **body** should follow form-encoded request bodies (x-www-form-urlencoded):


- Example:

```
email:781@columbia.edu
password:123412345
name:testtestuser
mobile_phone:8148888477
zipcode:10026
```

##### Registered successfully

- status code: 201
- output:

    ```
    {"error": ""}
    ```
##### Input Invalid

- status code: 400
- output:

    ```
    {"Input error": form.errors}
    ```
- example:

    ```
    {"Input error": {"email": ["Invalid email address."]}}
    ```
##### Database Error

- status code: 500
- output:

    ```
    {"error": "db error: **"}
    ```
- example:

    ```
    {"error": "db error: UNIQUE constraint failed: User.email"}
   
    ```
    
#### Response

### **POST** - /furnitures

This API is used by user to post a new furniture on the platform.

#### Request

##### Body Parameters

- **body** should respect the following json schema:

```
{
    "type": "object",
    "required": ["title", "labels", "image_url", "description"],
    "properties": {
        "title": {"type": "string"},
        "labels": {"type": "string"},
        "image_url": {"type": "string"},
        "description": {"type": "string"},
    }
}
```

- Example:

```
{
  "title": "iPhone 12",
  "labels": "like new, phone",
  "image_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fiphone&psig=AOvVaw0_LC7YH4CTStenQE3A95aw&ust=1637075168411000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNi2n7HSmvQCFQAAAAAdAAAAABAG",
  "description": "This is a brand new iphone 12 with box"
}
```

#### Response

##### Created successfully

- status code: 200
- output:

    ```
    {"error": ""}
    ```

##### Input Invalid

- status code: 400
- output:

    ```
    {"error": "invalid input"}
    ```
    

##### Internal Error

- status code: 500
- output:

    ```
    {"error": "Internal error"}
    ```


### **GET** - /furniture?keyword=<userInput>

Search funiture items based on user input(furniture labels)

#### Request

- Example:
```
GET /furniture?keyword="monitor"
```

#### Response

```
{
  "furniture": [
      {
          "fid": 1,
          "owner": Bob,
          "title": "Alienware Gaming Monitors",
          "labels": "monitor",
          "status": "init",
          "image_url": "",
          "description": "This is a monitor"
      }
}
```

### **GET** - /profile?email=<userEmail>

Get user's profile page

#### Request

- Example:

```
GET /profile?keyword="test0@email.com"
```

#### Response
```
{
  "email": "test0@gmail.com",
  "name": "rick",
  "zipcode": 100000,
  "phone_number": 123123
}
```

##### Created successfully

- status code: 201
- output:

    ```
    {"error": ""}
    ```

##### Input Invalid

- status code: 400
- output:

    ```
    {"error": "input invalid."}
    ```

##### Internal Error

- status code: 500
- output:

    ```
    {"error": "internal error"}
    ```

### **GET** - /user/login?email=<userEmail>&password=<userPassword>

User login

#### Request

- Example:

```
GET /user/login?email=aabb@columbia.edu&password=1234
```
    
##### Created successfully

- status code: 200
- output:

    ```
    {"error": ""}
    ```

##### Input Invalid

- status code: 400
- output:

    ```
    {"error": "invalid input"}
    ```
    
##### No such user 

- status code: 400
- output:

    ```
    {"error": "No such email aabb@columbia.edu"}
    ```
    
##### Wrong password

- status code: 400
- output:

    ```
    {"error": "wrong password aabb@columbia.edu"}
    ```

##### Internal Error

- status code: 500
- output:

    ```
    {"error": "Internal error"}
    ```

### **POST** - /furnitures/\<fid\>/rate?rating=\<rating\>

Used by a buyer to rate the owner of a furniture with the id of <fid> after the transaction is completed. The rating
score is specified by \<rating\>.

\<rating\> should be between an integer between 0 and 5.

#### Request

- Example:
```
POST /furnitures/f123/rate?rating=5
```

#### Response

##### On Success:

- status code: 200
- output:

```
{
  "error": ""
}
```

##### Input Invalid or Other Client Errors:

- status: 400
- output:

```
{
  "error": "<specific reason>"
}
```

##### Internal Error:

- status: 500
- output:

```
{
  "error": "<specific reason>"
}
```
### **POST** - /furnitures/\<fid\>/buy

Used by a buyer to show the intention to buy a furniture.

#### Request

- Example:
```
POST /furnitures/1/buy
```

#### Response

##### On Success:

- status code: 200
- output:

```
{
  "error": ""
}
```

##### No such furniture:

- status: 400
- output:

```
{
  "error": ""furniture not existed"
}
```
    
##### The furniture is already pending or sold:

- status: 400
- output:

```
{
  "error": ""The item is already sold or in progress"
}
```

##### Internal Error:

- status: 500
- output:

```
{
  "error": "<specific reason>"
}
```
### **POST** - /furnitures/\<fid\>/confirm?confirm=\<true/false\>

Used by a furniture owner to confirm the pending transaction with the id of <fid> when the transaction is pending. 
Confirm/not confirm is true/false depend on params.
If confirm=False, the furniture status goes back to "init", and buyer is set to NULL.

#### Request

- Example:
```
POST /furnitures/1/confirm?confirm=True
```

#### Response

##### On Success:

- status code: 200
- output:

```
{
  "error": ""
}
```

##### Input Invalid(no such furniture/not owner/not pending):

- status: 400
- output:
```
{
"error": "fid not existed."
}
```
```
{
"error": "Only owner can confirm the transaction."
}
```
```
{
"error": "the owner can only confirm the pending transaction"
}
```
##### Internal Error:

- status: 500
- output:

```
{
  "error": "f'db error <specific reason>"
}
```