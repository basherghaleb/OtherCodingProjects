#include <iostream>
#include <string>
#include <sstream>
using std::ostringstream;
using std::istringstream;
using std::string;
using std::getline;
using std::cout; using std::cin; using std::endl;



string GetEnd(const string& str, int end_size) {
	//end_size should be less than or equal to the 
	//actual size of the string
	int str_size = str.size();
	return str.substr(str_size - end_size, end_size);
}


string GetStart(const string& str, int start_size) {
	//start size should be less than or equal to the 
	//to the size of the string
	return str.substr(0, start_size);
}



int NumberOfCharactersOverlap(const string& a, const string& b) {
	int size_a = a.size();
	int size_b = b.size();

	int overlap = 0;
	int sub_size = 1;
	while (sub_size <= size_a && sub_size <= size_b) {
		if (GetEnd(a, sub_size) == GetStart(b, sub_size)) {
			overlap = sub_size;
		}
		sub_size += 1;
		
	}
	return overlap ;
}


string MergeStrings(const string& a, const string& b) {
	int overlap = NumberOfCharactersOverlap(a, b);
	string merge = a;

	if (overlap == 0) {
		merge += " " + b;
	}
	else {
		merge += b.substr(overlap);
	}
	return merge;
}


string CompressLine(const string& line) {
	string new_line;
	string word;
	istringstream iss(line);

	iss >> word; //Extract the first word
	new_line = word;

	while (iss >> word) {
		new_line = MergeStrings(new_line, word);
	}
	return new_line;
}

int main() {
	string line;

	while (getline(cin, line)) {
		cout << CompressLine(line) << endl;
	}
	return 0;
}
