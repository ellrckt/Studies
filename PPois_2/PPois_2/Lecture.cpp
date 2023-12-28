#include"Lecture.h"


using namespace std;



Lecture::Lecture() : IsThereTeacher(false)
{

	int start = 0;
	int end = 90;
	int num_students = 90;
	int num_students_onLecture= rand() % (end - start + 1) + start;
	this->NumStudents = num_students;
	this->NumStudentsOnLecture = num_students_onLecture;
	if (num_students_onLecture < 15) {
		this->IsThereTeacher = false;
	}
	else {
		this->IsThereTeacher = true;
	}

}

void Lecture::SetIsThereTeacher(bool IsThereTeacher)
{
	this->IsThereTeacher = IsThereTeacher;
}

bool Lecture::GetIsThereTeacher()
{
	return this->IsThereTeacher;
}


void Lecture::SetNumStudents(int NumStudents)

{
	this->NumStudents = NumStudents;

}
int Lecture::GetNumStudents()

{
	return this->NumStudents;

}
void Lecture::SetNumStudentsOnLecture(int NumStudentsOnLecture)

{
	this->NumStudentsOnLecture = NumStudentsOnLecture;

}
int Lecture::GetNumStudentsOnLecture()

{
	return this->NumStudentsOnLecture;


}