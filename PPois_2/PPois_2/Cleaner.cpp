#pragma once
#include"Cleaner.h"

bool Cleaner::IsCleaned()
{
	return this->cleaned;
}

void Cleaner::CleanHere()
{
	for (int i = 0; i < 2; i++) {

		if (i == 0) {

			cout << "Cleaned by " << instruments[0] << endl;
		}
		else {
			cout << "Cleaned by " << instruments[1] << endl;
		}

	}
	cout << "Cleanning proccess has been done!" << endl;
	this->cleaned = true;
}
