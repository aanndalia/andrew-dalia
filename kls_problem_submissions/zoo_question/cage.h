#include <iostream>
#include <set>

/* The Cage class is simple as each cage simply contains dimensions and a function to compute its volume. */ 

class Cage
{
private:
	int cageId;
	float height;
	float width;
	float length;
public:
	Cage(int cageId, float height, float width, float length) : cageId(cageId), height(height), width(width), length(length){

	}

	int getCageId() const {
		return cageId;
	}

	float getHeight() const {
		return height;
	}

	float getWidth() const {
		return width;
	}

	float getLength() const {
		return length;
	}

	float getVolume() const {
		return height * width * length;
	}

};
