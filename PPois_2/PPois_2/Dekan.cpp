#include"Dekan.h"
#include"Lecture.h"
#include"Student.h"



using namespace std;

Dekan::Dekan() :NumOfProtocols(0)
{
}

void Dekan::CheckLecture( Lecture& lecture)
{
	if (lecture.GetNumStudents() > lecture.GetNumStudentsOnLecture()) {

		WriteOutAProtocol(lecture);
	}

}

void Dekan::WriteOutAProtocol(Lecture& lecture)
{	
	int num_of_students = lecture.GetNumStudents();
	int num_of_students_on_lecture = lecture.GetNumStudentsOnLecture();
	int NumOfProtocols = lecture.GetNumStudents() - lecture.GetNumStudentsOnLecture();
	cout << " Number of writed protocols: " << NumOfProtocols << endl;
	
	WriteNumOFProtocols(NumOfProtocols);
}

int Dekan::WriteNumOFProtocols(int protocols)

{	

	this->NumOfProtocols += protocols;

	return this->NumOfProtocols;
}

void Dekan::ExpelAStudent(Student& student)
{
	if (student.GetIsGoodStudent() == true) {
		student.SetIsStudent(true);
	}
	else {
		
		student.SetIsStudent(false);
	}
}

int Dekan::GetNumOfProtocols()
{
	return this->NumOfProtocols;
}



