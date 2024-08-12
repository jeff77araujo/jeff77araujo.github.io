from rest_framework import serializers
from .models import Student, Professor, Classroom

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    teacher_name = serializers.ReadOnlyField(source='teacher.name')
    classroom_number = serializers.ReadOnlyField(source='classroom.number')

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'first_semester_grade', 'second_semester_grade', 'teacher', 'teacher_name', 'classroom', 'classroom_number']
