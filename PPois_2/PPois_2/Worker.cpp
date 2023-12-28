#include"Worker.h"



using namespace std;

Worker::Worker() :JobTitle(""), Salary(0)
{

}

Worker::Worker(string JobTitle, int Salary):JobTitle(JobTitle), Salary(Salary)
{



}

void Worker::SetJobTitle(string JobTitle)
{
	this->JobTitle = JobTitle;
}
string Worker::GetJobTitle()
{
	return this->JobTitle;
}
void Worker::SetSalary(int Salary)
{
	this->Salary = Salary;
}
int Worker::GetSalary()
{
	return this->Salary;
}

string Worker::DoWork(string doingsmth)
{
	cout << doingsmth << endl;
	return doingsmth;
}

