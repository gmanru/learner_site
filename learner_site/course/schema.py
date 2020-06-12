import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Course, City
from people.models import Student, Teacher



class CourseType(DjangoObjectType):

    class Meta:
        model = Course

class StudentType(DjangoObjectType):

    class Meta:
        model = Student

class CityType(DjangoObjectType):

    class Meta:
        model = City

class TeacherType(DjangoObjectType):

    class Meta:
        model = Teacher

class CourseFilteredType(DjangoObjectType):

    class Meta:
        model = Course
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )

class Query:
    all_courses = graphene.List(CourseType, limit=graphene.Int())
    filtered_courses = DjangoFilterConnectionField(CourseFilteredType)
    retrieve_course = graphene.Field(CourseType, id=graphene.Int())
    all_students = graphene.List(StudentType)
    all_teachers = graphene.List(TeacherType)

    def resolve_all_courses(self, *args, **kwargs):
        if 'limit' in kwargs:
            return Course.objects.all()[:kwargs['limit']]
        return Course.objects.all()

    def resolve_all_students(self, *args, **kwargs):
        return Student.objects.all()

    def resolve_all_teachers(self, *args, **kwargs):
        return Teacher.objects.all()

    def resolve_retrieve_course(self, info, **kwargs):
        if 'id' in kwargs:
            return Course.objects.get(id=kwargs['id'])

class CourseMutation(graphene.Mutation):

    class Arguments:
        course_id = graphene.Int(required=True)
        new_name = graphene.String(required=True)

    result = graphene.Boolean()
    course = graphene.Field(CourseType)

    def mutate(self, info, school_id, new_name):
        # TODO
        return {
            'result': True,
            'course': Course.objects.first()
        }

class Mutation:
    change_course_name = CourseMutation.Field()