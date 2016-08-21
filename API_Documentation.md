**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/login/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "password": {
            "type": "string"
        },
        "username": {
            "type": "string"
        }
    },
    "type": "object"
}
```


**Input Example**
```json
{
    "password": "12345",
    "username": "abc"
}
```


**Output Schema**
```json
{
    "properties": {
        "message": {
            "type": "string"
        }
    },
    "type": "object"
}
```


**Output Example**
```json
{
    "message": "login success"
}
```




<br>
<br>

# /api/register/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "password": {
            "type": "string"
        },
        "username": {
            "type": "string"
        }
    },
    "type": "object"
}
```


**Input Example**
```json
{
    "password": "12345",
    "username": "abc"
}
```


**Output Schema**
```json
{
    "properties": {
        "message": {
            "type": "string"
        }
    },
    "type": "object"
}
```


**Output Example**
```json
{
    "message": "register success"
}
```



