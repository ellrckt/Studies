#pragma once
#include<iostream>
#include<string>
#include<vector>

using namespace std;


class Shedule
{
public:
	
	string GetSubject(int id);

	void SetShedule(string subject);

	void GetShedule();

private:

	vector<string> shedule;


};