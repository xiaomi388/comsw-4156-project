[![Alohomora](https://circleci.com/gh/xiaomi388/comsw-4156-project/tree/master.svg?style=svg)](https://app.circleci.com/pipelines/github/xiaomi388/comsw-4156-project)
[![codecov](https://codecov.io/gh/xiaomi388/comsw-4156-project/branch/master/graph/badge.svg?token=W6R9U4E57A)](https://codecov.io/gh/xiaomi388/comsw-4156-project)

Course project for comsw4156

Team Name: Alohomora

## run and test Instructions

### Run

```python
pip install -r requirements.txt
flask run
```

### Test

```
coverage run -m unittest discover
coverage html
```

## API

### **POST** - /register

This API is used for new user registration

#### Request

##### Body Parameters

- **body** should respect the following json schema:

```
email, password, name, zipcode, phone_number
{
    "type": "object",
    "required": ["email", "labels", "image_url", "description"],
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

