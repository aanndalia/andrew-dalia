#include <iostream>
#include <vector>
#include <map>
#include <memory>

/* The Employee class has the attributes and actions common to a Zoo employee. 
   It has a mix of non-virtual and virtual functions depending on what actions 
   a manager may do differently to demonstrate polymorphism. */

class Employee
{
protected:
	std::string name;
	int employeeId;
	int yearHired;
	std::string title;
	int managerId; // -1 means employee has no manager
	double salary;
public:
	Employee(const std::string& name, int empId, const std::string& title, int yearHired, double startingSalary, int managerId = -1) : 
		name(name), employeeId(empId), title(title), yearHired(yearHired), salary(startingSalary), managerId(managerId) {

	}

	int getEmployeeId() const {
		return employeeId;
	}

	std::string getEmployeeName() const {
		return name;
	}

	int getYearEmployeeWasHired() const {
		return yearHired;
	}

	std::string getEmployeeTitle() const {
		return title;
	}

	void changeEmployeeTitle(const std::string& newTitle) {
		title = newTitle;
	}

	int getManagerEmployeeId() const {
		return managerId;
	}

	void changeManager(int newManagerId){
		managerId = newManagerId;
	}

	double getSalary() const {
		return salary;
	}

	void changeSalary(double newSalary) {
		salary = newSalary;
	}

	// Shows work that employee is doing
	virtual void doWork(){
		std::cout << "Employee " << name << " (" << employeeId << ") is working on a project\n";
	}

	virtual bool removeTeamMember(int removableTeamMemberId){
		std::cout << "Employee must be a manager to remove members\n";
		return false;
	}

	virtual bool addTeamMember(std::shared_ptr<Employee> newTeamMember) {
		std::cout << "Employee must be a manager to add members\n";
		return false;
	}

	// Shows information on this employee
	virtual void showInfo(){
		std::cout << getEmployeeName() << " (" << getEmployeeId() << ") was hired in " << getYearEmployeeWasHired() << " as the " << getEmployeeTitle() << "\n";
	}
 };

/* The Manager class inherits from Employee and polymorphically overrides some of the 
   member functions such as doWork and showInfo. It also contains a map containing the 
   Employee information for any employees that report to the manager. The manager can 
   also remove and add employees under him/her. */

class Manager : public Employee
{
private:
	std::map<int, std::shared_ptr<Employee>> teamMemberIdToEmployeeMap; // Maps each team member with their employee id

public:
	Manager(const std::string& name, int empId, const std::string& title, int yearHired, double startingSalary, int managerId = -1) :
		Employee(name, empId, title, yearHired, startingSalary, managerId) { }

	// Returns all the managers' direct reports
	std::map<int, std::shared_ptr<Employee>> getAllTeamMembers() const {
		return teamMemberIdToEmployeeMap;
	}

	// Removes a direct report under this manager
	virtual bool removeTeamMember(int removableTeamMemberId) {
		if(teamMemberIdToEmployeeMap.find(removableTeamMemberId) == teamMemberIdToEmployeeMap.end()){
			return false;
		}
		else{
			teamMemberIdToEmployeeMap.erase(removableTeamMemberId);
			return true;
		}
	} 

	// Adds a new direct report under this manager
	virtual bool addTeamMember(std::shared_ptr<Employee> newTeamMember) {
		int newTeamMemberId = newTeamMember->getEmployeeId();
		if(teamMemberIdToEmployeeMap.find(newTeamMemberId) == teamMemberIdToEmployeeMap.end()){
			teamMemberIdToEmployeeMap.insert(std::make_pair(newTeamMemberId, newTeamMember));
			return true;
		}
		else{
			return false;
		}
	}

	// The manager is doing some work
	virtual void doWork(){
		std::cout << "Manager " << name << " (" << employeeId << ") is managing several projects\n";
	}

	// Shows information of this manager and the direct reports (recursively)
	virtual void showInfo(){
		std::cout << "Manager " << getEmployeeName() << " (" << getEmployeeId() << ") was hired in " << getYearEmployeeWasHired() << " as the " << getEmployeeTitle() << "\n";
		std::cout << "Direct reports are:\n";
		for(std::map<int, std::shared_ptr<Employee>>::const_iterator it = teamMemberIdToEmployeeMap.begin(); it != teamMemberIdToEmployeeMap.end(); ++it){
			(it->second)->showInfo();
		}
		std::cout << "\n";
	}
};