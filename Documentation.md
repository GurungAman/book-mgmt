## Book Management System API Documentation

1. Get all Books:
- type: GET
- url: book_api/
- headers: {
    'X-CSRFToken': {csrf_token}
}

2. Get book by id:
- type: GET
- url: book_api/__id__/
- headers: {
    'X-CSRFToken': {csrf_token}
}
- body:
```
{
    'id': __id__
}
```

3. Add New Book:
- type: POST
- url: book_api/
- contentType: 'application/json'
- headers: {
    'X-CSRFToken': {csrf_token}
}
- body:
```
{
    'name': __str__,
    'ISBN': __str__
}
```

4. Update Book:
- type: PUT
- url: book_api/__id__/
- contentType: 'application/json'
- headers: {
    'X-CSRFToken': {csrf_token}
}
- body:
```
{
    'id': __id__,
    'name': __str__,
    'ISBN': __str__
}
```

5. Delete Book:
- type: DELETE
- url: book_api/__id__/
- headers: {
    'X-CSRFToken': {csrf_token}
}
- body:
```
{
    'id': __id__
}
```

