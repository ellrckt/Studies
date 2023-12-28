#include"Student.h"

using namespace std;

Student::Student():FavSubject(""),IsGoodStudent(false),IsStudent(false),Course(0),University("")
{

}

Student::Student(string FavSubject, string University, bool IsStudent, bool IsGoodStudent,int Course): FavSubject(FavSubject),University(University),IsStudent(IsStudent),IsGoodStudent(IsGoodStudent),Course(Course)
{
}
void Student::Learning(string Subject)
{
	cout << "Learning " << Subject;
}

void Student::ChooseFavSub(string Subject)
{
	this->FavSubject = Subject;
}

string Student::GetFavSubject()
{
	return this->FavSubject;
}

string Student::GetUniversity()
{
	return this->University;
}

bool Student::GetIsStudent()
{
	return this->IsStudent;
}

void Student::SetIsStudent(bool IsStudent)
{
	this->IsStudent = IsStudent;
}

void Student::SetIsGoodStudent(bool IsGoodStudent)
{
	this->IsGoodStudent = IsGoodStudent;
}

bool Student::GetIsGoodStudent()
{
	return this->IsGoodStudent;
}

void Student::SetCourse(int course)
{
	this->Course = course;
}

int Student::GetCourse()
{
	return this->Course;
}

bool Student::PassExam(Student& student)
{
	bool PassEx;
	int g = rand();
	if (g % 2 == 0) {
		bool PassEx = true;
		student.SetIsStudent(PassEx);
		return PassEx;
	}
	else {
		bool PassEx = false;
		student.SetIsStudent(PassEx);
		return PassEx;
	}
	
}
