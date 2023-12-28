#include "Human.h"


using namespace std;

Human::Human(string name,int age,string gender) :name(name),age(age),gender(gender)
{
}
Human::Human()
{
	this->age = 0;
	this->gender = "";
	this->name = "";

}

void Human::SetAge(int age)
{
	this->age = age;
}

int Human::GetAge()
{
	return this->age;
}

string Human::BeBorn()
{	
	string beBorn = "Was born!";
	cout << beBorn << endl;
	return beBorn;
}

string Human::GetGender()
{
	return this->gender;
}

void Human::SetGender(string gender)
{
	this->gender = gender;
}

void Human::SetName(string name)
{
	this->name = name;
}

string Human::GetName()
{
	return this->name;
}
