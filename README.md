# learner_site
http://127.0.0.1:8000/all_courses/  - выводит все курсы

http://127.0.0.1:8000/course_create/ - создание курса, после создания делается редирект на   
страницу с информацией о курсе http://127.0.0.1:8000/course_detail/<int:pk>/ ,где <int:pk> - уникальный номер курса в бд

http://127.0.0.1:8000/course_update/<int:pk>/ - изменение конкретного курса по его уникальному номеру, выданому при создании. После изменния курса  делается редирект на страницу с информацией о курсе http://127.0.0.1:8000/course_detail/<int:pk>/

http://127.0.0.1:8000/course_delete/<int:pk>/ - удаление конкретного курса по его уникальному номеру, выданому при создании. После удаления курса делается редирект на страницу со всеми курсами в бд,тем самым показывая, что курс удалился с бд http://127.0.0.1:8000/all_courses/


