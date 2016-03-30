#include <iostream>
#include <iterator>
#include <map>
#include <memory>

#include "zoo.h"

/* zoo_main.cpp runs through almost all the different actions that are defined for the zoo 
   such as creating animals, cages, employees, and managers. Also, it runs through examples 
   of animals taking actions such as eating, moving, and making sounds. Furthermore, it does 
   some changes such as modifying an animals cage, promoting an employee, and even changing 
   an employee’s manager. This can be used and modified to test the different parts of the 
   zoo design if needed. */

void createSomeCages(Zoo& zoo)
{
	zoo.addCage(15.0, 22.0, 13.0);
	zoo.addCage(12.0, 9.0, 4.0);
	zoo.addCage(20.0, 15.0, 13.0);
	zoo.addCage(10.0, 6.0, 8.0);
}

void createSomeAnimals(Zoo& zoo)
{
	zoo.addAnimal(new Crow(111, "Cary", 15, 1));
	zoo.addAnimal(new Parrot(112, "Patrick", 7, "green", 2));
	zoo.addAnimal(new Cheetah(113, "Chester", 3));
	zoo.addAnimal(new Goat(114, "Gary", 4, 2));
	zoo.addAnimal(new Parrot(115, "Peter", 8, "yellow", 2));
	zoo.addAnimal(new Parrot(116, "Paul", 9, "red", 2));
}

void makeAnimalsEatAndTalk(const Zoo& zoo){
	std::map<int, std::shared_ptr<Animal>> animals = zoo.getAllAnimals();
	for(std::map<int, std::shared_ptr<Animal>>::const_iterator it = animals.begin(); it != animals.end(); ++it){
		std::cout << "Animal id " << (it->second)->getAnimalId() << " is " << (it->second)->getName() << "\n";
		(it->second)->eat();
		(it->second)->makeSound();
	}
}

void calculateVolumeForAllCages(const Zoo& zoo){
	std::map<int, std::shared_ptr<Cage>> cages = zoo.getAllCages();
	for(std::map<int, std::shared_ptr<Cage>>::const_iterator it = cages.begin(); it != cages.end(); ++it){
		std::cout << "The volume of cage " << (it->second)->getCageId() << " is " << (it->second)->getVolume() << "\n";
	}
}

void createManagers(Zoo& zoo){
	zoo.addEmployee("Noah Arc", "Manager of Zoo", 2009, 75000.00, -1, true);
	zoo.addEmployee("Bob Adams", "Manager of Flying Animals", 2012, 45000.00, 0, true);
	zoo.addEmployee("Susan Smith", "Manager of Land Animals", 2009, 55000.00, 0, true);
}

void createEmployees(Zoo& zoo){
	zoo.addEmployee("Cheryl Fisher", "Zoo Keeper", 2010, 40000.00, 2);
	zoo.addEmployee("Lauren Jones", "Maintenance worker", 2013, 35000.00, 2);
	zoo.addEmployee("Albert Einstein", "Zoo Keeper", 2011, 40000.00, 1);
}

void makeAllEmployeesDoWork(const Zoo& zoo){
	std::map<int, std::shared_ptr<Employee>> employees = zoo.getAllEmployees();
	for(std::map<int, std::shared_ptr<Employee>>::const_iterator it = employees.begin(); it != employees.end(); ++it){
		(it->second)->doWork();
	}
}

void getAllEmployeeInfoForSusan(const Zoo& zoo){
	std::shared_ptr<Employee> susan = zoo.getEmployee(2); // Susan the manager
	susan->showInfo();
}

void getAllEmployeeInfoForLauren(const Zoo& zoo){
	std::shared_ptr<Employee> lauren = zoo.getEmployee(4); // Lauren the maintenance employee
	lauren->showInfo();
}

void changeCageForCary(Zoo& zoo){
	std::shared_ptr<Animal> cary = zoo.getAnimal(111); // Cary the crow
	std::cout << cary->getName() << "(" << cary->getAnimalId() << ") is in cage " << cary->getCageId() << "\n";
	zoo.changeAnimalCage(111, 0);
	std::cout << cary->getName() << "(" << cary->getAnimalId() << ") is in cage " << cary->getCageId() << " after change.\n";
}

void changeManagerForLauren(Zoo& zoo){
	std::shared_ptr<Employee> lauren = zoo.getEmployee(4); // Lauren the maintenance worker employee
	std::cout << lauren->getEmployeeName() << "(" << lauren->getEmployeeId() << ") has manger with id " << lauren->getManagerEmployeeId() << "\n";
	zoo.assignEmployeeToNewManager(4, 1);
	std::cout << lauren->getEmployeeName() << "(" << lauren->getEmployeeId() << ") has manger with id " << lauren->getManagerEmployeeId() << " after change.\n";
}

void promoteAlbert(Zoo& zoo){
	double raise = 3000.00;
	std::shared_ptr<Employee> albert = zoo.getEmployee(5); // Albert the zoo keeper employee
	std::cout << albert->getEmployeeName() << "(" << albert->getEmployeeId() << ") the " << albert->getEmployeeTitle() << " had salary " << albert->getSalary() << "\n";
	albert->changeSalary(albert->getSalary() + raise);
	albert->changeEmployeeTitle("Senior Zoo Keeper");
	std::cout << albert->getEmployeeName() << "(" << albert->getEmployeeId() << ") the " << albert->getEmployeeTitle() << " now has salary " << albert->getSalary() << " after promotion.\n";
}

int main()
{
	Zoo zoo;
	createSomeCages(zoo);
	createSomeAnimals(zoo);
	makeAnimalsEatAndTalk(zoo);
	std::shared_ptr<Animal> peter = zoo.getAnimal(115); // Peter the Parrot
	peter->move();
	std::cout << "Peter is in cage " << peter->getCageId() << "\n";
	std::shared_ptr<Animal> chester = zoo.getAnimal(113); // Chester the Cheetah
	chester->move();
	calculateVolumeForAllCages(zoo);
	createManagers(zoo);
	createEmployees(zoo);
	makeAllEmployeesDoWork(zoo);
	getAllEmployeeInfoForSusan(zoo);
	getAllEmployeeInfoForLauren(zoo);
	changeCageForCary(zoo);
	changeManagerForLauren(zoo);
	promoteAlbert(zoo);
}