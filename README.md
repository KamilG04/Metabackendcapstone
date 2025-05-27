kamilglowacki@MacBook-Air-Kamil ~ % export TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ4MzczNjIyLCJpYXQiOjE3NDgzNzAwMjIsImp0aSI6IjJkMWM0NTcxNmYyODRlMzY4MzRmZWY0YzBhYjBiMGZjIiwidXNlcl9pZCI6Mn0.gr-bQsfAt9edROZIIB9VceGVBwoL37ktHje4U4vZvJ4"
kamilglowacki@MacBook-Air-Kamil ~ % curl -X GET http://127.0.0.1:8000/api/menu-items/ \
  -H "Authorization: Bearer $TOKEN"

# Test kategorii
curl -X GET http://127.0.0.1:8000/api/categories/ \
  -H "Authorization: Bearer $TOKEN"

# Test bookings
curl -X GET http://127.0.0.1:8000/api/bookings/ \
  -H "Authorization: Bearer $TOKEN"

# Dodaj nową rezerwację
curl -X POST http://127.0.0.1:8000/api/bookings/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jan Kowalski",
    "no_of_guests": 4,
    "booking_date": "2025-06-01T18:00:00Z"
  }'
[{"id":1,"title":"Bruschetta","price":"12.99","featured":true,"category":{"id":1,"title":"Appetizers","slug":"appetizers"},"description":""},{"id":2,"title":"Spaghetti Carbonara","price":"18.99","featured":true,"category":{"id":2,"title":"Main courses","slug":"main-courses"},"description":""},{"id":3,"title":"Tiramisu","price":"8.99","featured":true,"category":{"id":3,"title":"Desserts","slug":"desserts"},"description":""}]zsh: command not found: #
[{"id":1,"title":"Appetizers","slug":"appetizers"},{"id":2,"title":"Main courses","slug":"main-courses"},{"id":3,"title":"Desserts","slug":"desserts"}]zsh: command not found: #
[]zsh: command not found: #
{"id":1,"user":"testuser","name":"Jan Kowalski","no_of_guests":4,"booking_date":"2025-06-01T18:00:00Z"}%                                            kamilglowacki@MacBook-Air-Kamil ~ % 
i ve tested it with postman 
