# learner_site
http://127.0.0.1:8000/all_courses/  - выводит все курсы

http://127.0.0.1:8000/course_create/ - создание курса, после создания делается редирект на   
страницу с информацией о курсе http://127.0.0.1:8000/course_detail/<int:pk>/ ,где <int:pk> - уникальный номер курса в бд

http://127.0.0.1:8000/course_update/<int:pk>/ - изменение конкретного курса по его уникальному номеру, выданому при создании. После изменния курса  делается редирект на страницу с информацией о курсе http://127.0.0.1:8000/course_detail/<int:pk>/

http://127.0.0.1:8000/course_delete/<int:pk>/ - удаление конкретного курса по его уникальному номеру, выданому при создании. После удаления курса делается редирект на страницу со всеми курсами в бд,тем самым показывая, что курс удалился с бд http://127.0.0.1:8000/all_courses/

Для работы с авторизацией используйте приложение postman или Insomnia designer.

Для начала надо авторизовать свое приложение здесь http://127.0.0.1:8000/people/o/applications/

Далее скопипастить оттуда данные из полей Client id и Client server
и вставлять в запросы на генерацию токена в Insomnia.

Чтобы сгенерировать токен надо прописать поля grand_type (password), username, password,
Далее вставлять полученный access_token для пользователя в свои запросы.

Есть три юзера, admin, medium,user

admin имеет максимальные права

medium может создавать пользователей и видеть группы

user не видит группы и не может создать пользователей и не видет группы

работа с graphql по адресу http://127.0.0.1:8000/graphql/ 

запросы курсы+преподаватели, курсы+студенты
query {
  allCourses{
    name
  }
  allTeachers{
    lastName
    firstName
  }
}

query {
  allCourses{
    name
  }
  allStudents{
    lastName
    firstName
  }
}

запрос вида все курсы, преподаватели и все студенты, записанные на курсы


query {
  allCourses{
    name
    students{
      lastName
      firstName
    }
    teachers{
      lastName
      firstName
    }
  }
}

