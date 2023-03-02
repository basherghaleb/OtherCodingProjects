#include "main.h"
#include <iostream>
#include <fstream>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <vector>
#include <utility>
#include <stdexcept>

using std::cin; 
using std::cout; 
using std::endl;
using std::map;
using std::string;
using std::set;
using std::ifstream;
using std::istream_iterator;
using std::accumulate;
using std::transform;
using std::vector;
using std::make_pair;
using std::pair;
using std::ios_base;
using std::stoi;
using std::invalid_argument;
using std::copy_if;
using std::sort;



// This function returns a vector of all the cells on a given comma separated row
vector<string> GetTokens(string commaSeparatedLine) {
	vector<string> tokens;
	string partial_res = "";
	string last_token = accumulate(commaSeparatedLine.begin(), commaSeparatedLine.end(), partial_res, [&tokens](string partial_res, char ch) {
		if (ch == ',') {
			tokens.push_back(partial_res);
			partial_res = "";
			return partial_res;
		}
		else {
			partial_res += ch;
			return partial_res;
		}
		});
	tokens.push_back(last_token);
	return tokens;
}


// This function return a vector of all the lines in a given file
// Good processing one line of the file at a time
vector<string> GetAllLines(string filename) {
	ifstream input(filename);
	vector<string> allLines;
	input.unsetf(ios_base::skipws); // Doing this so our istream_iterator doesn't skip the eol char

	string partial = "";
	string last_line = accumulate(
		istream_iterator<char>(input), istream_iterator<char>(), partial, [&allLines](string partial, char ch) {

			if (ch == '\n') { // New line
				allLines.push_back(partial);
				partial = "";
				return partial;
			}
			else {
				partial += ch;
				return partial;
			}
		}
	);
	allLines.push_back(last_line);
	return allLines;
}


// This function converts a string to an int
// Any string which isn't convertible will yield 0
int customStoi(const string& str) {
	int val;
	try {
		val = stoi(str);
	}
	catch (invalid_argument) {
		val = 0;
	}
	return val;
}



std::map<std::string, std::map<std::string, std::string>> GetIDToInfoFromCSV(std::string filename)
{
	vector<string> allLines = GetAllLines(filename);
	vector<string> columnHeaders = GetTokens(allLines[0]);
	map<string, map<string, string>> result;

	transform(allLines.begin() + 1, allLines.end(), std::inserter(result, result.end()), [columnHeaders](string line)
		{
			vector<string> tokens = GetTokens(line);
			string studentId = tokens[1];
			map<string, string> studentInfo;
			transform(columnHeaders.begin(), columnHeaders.end(), tokens.begin(), std::inserter(studentInfo, studentInfo.end()), [](string a, string b)
				{
					return std::make_pair(a, b);
				});
			return make_pair(studentId, studentInfo);
		}
	);
	return result;
}



int GetPointTotalForStudent(std::map<std::string, std::string> studentInfo, std::string assignementCategory)
{
	return accumulate(studentInfo.begin(), studentInfo.end(), 0, [assignementCategory](int total, pair<string, string> p)
		{
			if (p.first.find(assignementCategory) != string::npos) {
				total += customStoi(p.second);
			}
			return total;
		}
	);
}


int GetTopNHomeworkTotalForStudent(std::map<std::string, std::string> studentInfo, int topNHomework)
{
	map<string, string> hwInfo;
	copy_if(studentInfo.begin(), studentInfo.end(), std::inserter(hwInfo, hwInfo.end()), [](pair<string, string> p)
		{
			return p.first.find("HW") != string::npos;
		}
	);

	// Get all the homework grades
	vector<int> hwGrades;
	transform(hwInfo.begin(), hwInfo.end(), std::inserter(hwGrades, hwGrades.end()), [](pair<string, string> p)
		{
			return customStoi(p.second);
		}
	);

	sort(hwGrades.begin(), hwGrades.end(), [](int a, int b) {return a > b; });
	int numHwGrades = hwGrades.size();
	topNHomework = topNHomework > numHwGrades ? numHwGrades : topNHomework;
	return accumulate(hwGrades.begin(), hwGrades.begin() + topNHomework, 0);
}

int GetNumberOfMissingLabsForStudent(std::map<std::string, std::string> studentInfo)
{
	return accumulate(studentInfo.begin(), studentInfo.end(), 0, [](int result, pair<string, string>p)
		{
			if (p.first.find("Lab") != string::npos) {
				if (p.second != "1") {
					result += 1;
				}
			}
			return result;
		}
	);
}



int GetPointTotalForStudent(std::map<std::string, std::string> studentInfo)
{
	int examsPoints = GetPointTotalForStudent(studentInfo, "Exam");
	int projectsPoints = GetPointTotalForStudent(studentInfo, "Project");
	int honorsPoints = GetPointTotalForStudent(studentInfo, "Honors");
	int hwsPoints = GetTopNHomeworkTotalForStudent(studentInfo, 15);

	return examsPoints + projectsPoints + hwsPoints - honorsPoints;
}



double GetStudentGrade(std::map<std::string, std::string> studentInfo) {
	int total_points = GetPointTotalForStudent(studentInfo);
	double netGpa;
	if (total_points <= 599) {
		netGpa = 0.0;
	}
	else if (total_points <= 649) {
		netGpa = 1.0;
	}
	else if (total_points <= 699) {
		netGpa = 1.5;
	}
	else if (total_points <= 749) {
		netGpa = 2.0;
	}
	else if (total_points <= 799) {
		netGpa = 2.5;
	}
	else if (total_points <= 849) {
		netGpa = 3.0;
	}
	else if (total_points <= 899) {
		netGpa = 3.5;
	}
	else {
		netGpa = 4;
	}

	// lab penalty adjustement
	int numberMissingLabs = GetNumberOfMissingLabsForStudent(studentInfo);

	netGpa -= numberMissingLabs > 2 ? (numberMissingLabs - 2) * 0.5 : 0;
	return  netGpa >= 0 ? netGpa : 0;

}

std::map<std::string, double> GetIDToGrade(std::map<std::string, std::map<std::string, std::string>> idToStudentInfoMap)
{
	map<string, double> result;

	transform(idToStudentInfoMap.begin(), idToStudentInfoMap.end(), std::inserter(result, result.end()), [](pair<string, map<string, string>> p) {
		double studentGrade = GetStudentGrade(p.second);
		return make_pair(p.first, studentGrade);
		});
	return result;
}



std::set<std::string> GetStudentsEligibleForHonorsCredit(std::map<std::string, std::map<std::string, std::string>> idToStudentInfoMap, int thresh)
{
	map<string, map<string, string>> honorsStudents;
	copy_if(idToStudentInfoMap.begin(), idToStudentInfoMap.end(), std::inserter(honorsStudents, honorsStudents.end()), [thresh](pair<string, map<string, string>> p) {
		int honorsPoints = GetPointTotalForStudent(p.second, "Honors");
		double studentGpa = GetStudentGrade(p.second);
		return (honorsPoints >= thresh) && (studentGpa >= 3.5);
	});

	set<string> result;
	transform(honorsStudents.begin(), honorsStudents.end(), std::inserter(result, result.end()), [](pair<string, map<string, string>>p) {
		return p.first;
	});
	return result;
}

