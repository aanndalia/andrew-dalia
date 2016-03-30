#include <iostream>

/* The Animal class is set up as an abstract base class since it does not make sense to 
   define a general animal in the zoo because they can be specified by the type of animal 
   it is or species. To achieve this, Animal has some pure virtual functions such as makeSound 
   and eat that must be implemented by derived classes that are not abstract. The accessors 
   and modifiers are shared amongst animals so these are defined at the Animal level. The common 
   attributes defined here amongst animals are the name and cage (if in a cage) for each animal. */

class Animal
{
protected:
	std::string name;
	int cageId; // -1 if not in cage
	int animalId;
public:
	Animal(int animalId, const std::string& name, int cageId = -1) : name(name), cageId(cageId), animalId(animalId) {
	}

	virtual void makeSound() = 0;

	virtual void eat() = 0;

	virtual void move() = 0;

	int getCageId() const {
		return cageId;
	}

	void setCageId(int newCageId) {
		cageId = newCageId;
	}

	int getAnimalId() const {
		return animalId;
	}

	std::string getName() const {
		return name;
	}

};

/* The FlyingAnimal class inherits from Animal. It is abstract as it does not implement 
   the makeSound or eat functions which were pure virtual in the Animal class. It does 
   however implement the move behavior, since flying is common to all Animals that fall 
   under this class. Flying animals have an additional wing span attribute. */

class FlyingAnimal : public Animal
{
private:
	float wingSpan;
protected:
	FlyingAnimal(int animalId, const std::string& name, int cageId, float wingSpan) : Animal(animalId, name, cageId), wingSpan(wingSpan) { }

	virtual void move() {
		std::cout << name << " flies around\n";
	}
};

/* The LandAnimal class inherits from Animal. It is also abstract for the same reason as the 
   FlyingAnimal class. This makes sense since LandAnimal is still a relatively generic concept. 
   It does implement the move behavior so there is a default behavior to how LandAnimals move. 
   Land animals have an addition attribute for number of legs. */

class LandAnimal : public Animal
{
private:
	int numLegs;
protected:
	LandAnimal(int animalId, const std::string& name, int cageId, int numLegs) : Animal(animalId, name, cageId), numLegs(numLegs) { }

	virtual void move() {
		std::cout << name << " runs around\n";
	}
};

/* The Crow class inherits from FlyingAnimal. It directly defines the virtual makeSound and eat 
   functions so that it is not abstract and can be instantiated. */

class Crow : public FlyingAnimal
{
public:
	Crow(int animalId, const std::string& name, int wingSpan, int cageId = -1) : FlyingAnimal(animalId, name, cageId, wingSpan) { }

	virtual void makeSound() {
		std::cout << name << " says CAWWWW\n";
	}

	virtual void eat() {
		std::cout << name << " the crow is eating worms\n";
	}
};

/* The Parrot class inherits from FlyingAnimal. It defines the makeSound and eat functions making 
   it instantiable. In addition it also has another attribute not defined in any of the base 
   classes, which is its feather color. */

class Parrot: public FlyingAnimal
{
private:
	std::string featherColor;
public:
	Parrot(int animalId, const std::string& name, int wingSpan, const std::string& color, int cageId = -1) : FlyingAnimal(animalId, name, cageId, wingSpan), featherColor(color) { }

	virtual void makeSound() {
		std::cout << name << " says: Polly wants a cracker\n";
	}

	virtual void eat() {
		std::cout << name << " the parrot is eating insects\n";
	}

	std::string getFeatherColor() const {
		return featherColor;
	}
};

/* The Cheetah class inherits from LandAnimal. It defines the makeSound and eat function so that it 
   is instantiable. In addition, it overrides the move function defined in the LandAnimal class since 
   a cheetah moves much faster than a typical land animal. */

class Cheetah : public LandAnimal
{
public:
	Cheetah(int animalId, const std::string& name, int numLegs, int cageId = -1) : LandAnimal(animalId, name, cageId, numLegs) { }

	virtual void move() {
		std::cout << name << " the cheetah is sprinting very fast!\n";
	}

	virtual void makeSound() {
		std::cout << name << " purrs loudly\n";
	}

	virtual void eat() {
		std::cout << name << " the cheetah is eating gazelles\n";
	}

};

/* The Goat class inherits from LandAnimal. It also defines makeSound and eat so that we can instantiate 
   goats. It has an additional attribute not defined in its hierarchy which is its number of legs. */

class Goat : public LandAnimal
{
private:
	int numHorns;
public:
	Goat(int animalId, const std::string& name, int numLegs, int numHorns, int cageId = -1) : LandAnimal(animalId, name, cageId, numLegs), numHorns(numHorns) { }

	virtual void makeSound()  {
		std::cout << name << " says: Baaah!\n";
	}

	virtual void eat() {
		std::cout << name << " the goat is eating grass\n";
	}

	int getNumHorns() const {
		return numHorns;
	}
};
