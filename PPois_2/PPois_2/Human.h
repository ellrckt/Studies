#pragma once

#include<iostream>
#include<string>

using namespace std;

class Human
{
public:
	Human(string name, int age,string gender);

	Human();

	void SetAge(int age);

	int GetAge();

	string BeBorn();

	string GetGender();

	void SetGender(string gender);

	void SetName(string name);

	string GetName();



private:
	string name;
	int age;
	string gender;


};
