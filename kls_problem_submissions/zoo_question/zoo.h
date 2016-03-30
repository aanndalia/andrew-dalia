#include <iostream>
#include <vector>
#include <map>
#include <memory>

#include "animal.h"
#include "employee.h"
#include "cage.h"

/* The Zoo class maintains maps between each animal, cage, and employee (value) and their 
   respective numeric identifications (key). These maps store a shared pointer to these 
   objects so that the memory is managed by reference count automatically. This 
   is give a way to obtain the full information of each of these using just their 
   unique id. The functions called by zoo_main to add the different types of 
   objects and make modifications are contained here as well as operations common 
   to a zoo. */

class Zoo
{
private:
	std::map<int, std::shared_ptr<Animal>> animalIdToAnimal; // map of animal's id to any type of Animal object
	std::map<int, std::shared_ptr<Employee>> employeeIdToEmployee; // map of employee's id to any type of Employee object
	std::map<int, std::shared_ptr<Cage>> cageIdToCage; // map of cage's id to Cage object
	int maxEmployeeId; // keep record of the max employee id generated so far so we are guaranteed to create unique ids
	int maxCageId; // keep record of the max cage id generated so far so we are guaranteed to create unique ids

public:
	Zoo() : maxEmployeeId(0), maxCageId(0) {
	}

	// Gets map of all animals in the Zoo 
	std::map<int, std::shared_ptr<Animal>> getAllAnimals() const{
		return animalIdToAnimal;
	}

	// Gets map of all employees in the Zoo 
	std::map<int, std::shared_ptr<Employee>> getAllEmployees() const{
		return employeeIdToEmployee;
	}

	// Gets map of all cages in the zoo
	std::map<int, std::shared_ptr<Cage>> getAllCages() const{
		return cageIdToCage;
	}

	// Returns pointer to the animal with the given id
	std::shared_ptr<Animal> getAnimal(int animalId) const{
		if(animalId < 0){
			return nullptr;
		}
		return animalIdToAnimal.at(animalId);		
	}

	// Returns pointer to the cage with the given id
	std::shared_ptr<Cage> getCage(int cageId) const{
		if(cageId < 0){
			return nullptr;
		}
		return cageIdToCage.at(cageId); 
	}

	// Returns pointer to the employee with the given id
	std::shared_ptr<Employee> getEmployee(int employeeId) const{
		if(employeeId < 0){
			return nullptr;
		}
		return employeeIdToEmployee.at(employeeId);
	}

	// Adds new employee (could be a manager) to the zoo and associates employee as a direct report to the given manager id
	bool addEmployee(const std::string& name, const std::string& title, int yearHired, double startingSalary, int managerId, bool isManager = false){
		std::shared_ptr<Employee> newEmployee = nullptr;
		if(isManager){
			newEmployee = std::shared_ptr<Employee> (new Manager(name, maxEmployeeId, title, yearHired, startingSalary, managerId));
		}
		else {
			newEmployee = std::shared_ptr<Employee> (new Employee(name, maxEmployeeId, title, yearHired, startingSalary, managerId));
		}

		employeeIdToEmployee.insert(std::make_pair(maxEmployeeId++, newEmployee));
		std::shared_ptr<Employee> manager = getEmployee(managerId);
		if(manager){
			manager->addTeamMember(newEmployee);
			return true;
		}
		else{
			return false;
		}
	}

	// adds a new cage with given dimensions
	void addCage(float height, float width, float length){
		cageIdToCage.insert(std::make_pair(maxCageId++, std::shared_ptr<Cage> (new Cage(maxCageId, height, width, length))));
	}

	// adds a new animal to the zoo
	bool addAnimal(Animal* animalToAdd){
		int animalId = animalToAdd->getAnimalId();
		if(animalIdToAnimal.find(animalId) == animalIdToAnimal.end()){
			animalIdToAnimal.insert(std::make_pair(animalId, std::shared_ptr<Animal> (animalToAdd)));
			return true;
		}
		else{
			return false;
		}
	}

	// Associate a current employee with another current manager. Also, remove employee from the old managers direct reports and add
	// the employee the new managers direct reports
	bool assignEmployeeToNewManager(int empId, int newManagerId){
		if(employeeIdToEmployee.find(empId) == employeeIdToEmployee.end() || employeeIdToEmployee.find(newManagerId) == employeeIdToEmployee.end()){
			return false;
		}
		else {
			std::shared_ptr<Employee> thisEmployee = employeeIdToEmployee.at(empId);
			int oldManagerId = thisEmployee->getManagerEmployeeId();
			thisEmployee->changeManager(newManagerId);
			std::shared_ptr<Employee> newManager = employeeIdToEmployee.at(newManagerId);
			newManager->addTeamMember(thisEmployee);
			std::shared_ptr<Employee> oldManager = employeeIdToEmployee.at(oldManagerId);
			oldManager->removeTeamMember(empId);
			return true;
		}
	}

	// change the cage an animal is in
	bool changeAnimalCage(int animalId, int newCageId){
		if(animalIdToAnimal.find(animalId) == animalIdToAnimal.end()){
			return false;
		}
		else {
			animalIdToAnimal.at(animalId)->setCageId(newCageId);
			return true;
		}

	}

	// get the maximum employee id so far in order to guarantee unique ids when creating new Employees
	int getMaxEmployeeId() const {	
		return maxEmployeeId;
	}

	// get the maximum cage id so far in order to guarantee unique ids when creating new Cages
	int getMaxCageId() const {
		return maxCageId;
	}
};

