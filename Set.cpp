#include"./../PPois_1/Set.h"

Set::Set(string str) {
	

	StrToSet(str);
}
Set::Set(){}


void Set::processSet(const std::string& set_example, int& i) {
	int l_bracket_counter = 1;
	int r_bracket_counter = 0;
	std::string auxiliary_str = "{";

	while (l_bracket_counter != r_bracket_counter) {
		++i;

		if (set_example[i] == '{') {
			l_bracket_counter++;
			auxiliary_str += set_example[i];
		}
		else if (set_example[i] == '}') {
			r_bracket_counter++;
			auxiliary_str += set_example[i];
		}
		else {
			auxiliary_str += set_example[i];
		}
	}

	elements.push_back(auxiliary_str);
}

std::string Set::extractSet(const std::string& set_example, int& i) {
	std::string auxiliary_str = "";

	while (i < set_example.size() && set_example[i] != ',' && set_example[i] != '}') {
		auxiliary_str += set_example[i];
		i++;
	}

	return auxiliary_str;
}

void Set::StrToSet(const std::string& set_example) {
	for (int i = 1; i < set_example.size() - 1; i++) {
		if (set_example[i] == '{') {
			processSet(set_example, i);
		}
		else if (set_example[i] == '}') {
			
		}
		else if (set_example[i] == ',') {
			
		}
		else {
			elements.push_back(extractSet(set_example, i));
		}
	}
}


//void Set::StrToSet(string set_example) {		 
//
//	int r_bracket_counter = 0;			
//	int l_bracket_counter = 0;
//	string help = "";					
//	for (int i = 1; i < set_example.size() - 1; i++) {
//		help = "";
//		l_bracket_counter = 0;
//		r_bracket_counter = 0;
//		if (set_example[i] == '{') {
//			l_bracket_counter++;
//			help = set_example[i];
//			i++;
//
//			while (l_bracket_counter != r_bracket_counter) {
//
//				if (set_example[i] == '{') {
//					l_bracket_counter++;
//					help += set_example[i];
//
//				}
//				else {
//					if (set_example[i] == '}') {
//						r_bracket_counter++;
//						help += set_example[i];
//
//					}
//					else {
//						help += set_example[i];
//						
//
//					}
//				}
//				i++;
//			}
//			elements.push_back(help);
//
//		}
//		else {
//			if (set_example[i] == '}') {
//				r_bracket_counter++;
//			}
//			else {
//				if (set_example[i] == ',') {
//
//				}
//				else {
//					help += set_example[i];
//					elements.push_back(help);
//				}
//			}
//		}
//
//
//
//
//	}
//
//
//}

bool Set::IsEmpty() {
	
	bool isEmpty;
	if (elements.size() != 0) {
		isEmpty = false;
	}
	else {
		isEmpty = true;
	}
	return isEmpty;
	


}

string Set::add(string str) {

	elements.push_back(str);
	return str;

}

string Set::add(char str) {
	string auxiliary_str = "";
	auxiliary_str += str;
	elements.push_back(auxiliary_str);
	return auxiliary_str;
}

string Set::del(int pos) {
	auto iter = elements.cbegin();
	string result = elements[pos - 1];
	elements.erase(iter + (pos - 1));
	return result;
}

int  Set::power() {
	return elements.size();
	
}
bool Set::contains(string str){
    return find(elements.begin(), elements.end(), str) != elements.end();
}

bool Set::contains(char ch)  {
	string str(1, ch); 
	return contains(str);
}

void Set::Print() {

	if (elements.size() == 0) {
		cout << "Set is empty!" << endl;
	}
	else {
		vector<string>::iterator it;
		for (it = elements.begin(); it != elements.end(); it++)
		{
			cout << *it << endl;
		}
	}
}
vector<Set> Set::powerSet() {
	vector<Set> result;

	int totalSets = pow(2, this->power());
	for (int i = 0; i < totalSets; i++) {
		Set subset;
		for (int j = 0; j < this->power(); j++) {
			if ((i & (1 << j)) != 0) {
				subset.add(elements[j]);
			}
		}
		result.push_back(subset);
	}
	return result;
}

bool Set::operator[](const string& element) const {
	for (const auto& el : elements) {
		if (el == element) {
			return true;
		}
	}
	return false;
}
Set Set::operator+(const Set& other) const {
	Set resultSet(*this);
	for (const string& el : other.elements) {
		if (!resultSet[el]) {
			resultSet.elements.push_back(el);
		}
	}
	return resultSet;
}


Set& Set::operator+=(const Set& other) {
	for (const string& el : other.elements) {
		if (!(*this)[el]) {
			elements.push_back(el);
		}
	}
	return *this;
}

Set Set::operator*(const Set& other) const {
	Set resultSet;
	for (const auto& el : elements) {
		if (other[el]) {
			resultSet.elements.push_back(el);
		}
	}
	return resultSet;
}


Set& Set::operator*=(const Set& other) {
	vector<string> intersection;
	for (const auto& el : elements) {
		if (other[el]) {
			intersection.push_back(el);
		}
	}
	elements = intersection;
	return *this;
}

Set Set::operator-(const Set& other) const {
	Set resultSet;
	for (const auto& el : elements) {
		if (!other[el]) {
			resultSet.elements.push_back(el);
		}
	}
	return resultSet;
}


Set& Set::operator-=(const Set& other) {
	vector<string> difference;
	for (const auto& el : elements) {
		if (!other[el]) {
			difference.push_back(el);
		}
	}
	elements = difference;
	return *this;
}


