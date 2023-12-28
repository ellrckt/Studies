#include "Security.h"

void Security::SetOutsiders(int outsiders)
{
	if (outsiders > 0) {
		this->IsAllAlright = false;
	}
	this->NumOfOutsiders = outsiders;
}

int Security::GetNumOfOutsiders()
{
	return this->NumOfOutsiders;
}
