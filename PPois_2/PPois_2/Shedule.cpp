#include"Shedule.h"

string Shedule::GetSubject(int id)
{
	return this->shedule[id];
}

void Shedule::SetShedule(string subject)
{
	shedule.push_back(subject);
}


void Shedule::GetShedule() 
{
	for (auto it = shedule.cbegin(); it != shedule.cend(); it++) {
		cout << *it << ' ';
	}
}

