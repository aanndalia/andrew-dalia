#include <iostream>
#include <vector>
#include <set>
#include <cstdlib>

using namespace std;

enum SHIP_STATE {EMPTY, SUBMARINE, CRUISER, BATTLESHIP, CARRIER};
enum ENEMY_CELL_STATE {UNSURE, HIT, MISS};

int getShipSize(int shipType){
	switch(shipType){
		case SUBMARINE:
			return 2;
		case CRUISER:
			return 3;
		case BATTLESHIP:
			return 4;
		case CARRIER:
			return 5;
		default:
			return 2;
	}
}

string shipTypeToString(int shipType){
	switch(shipType){
		case SUBMARINE:
			return "Submarine";
		case CRUISER:
			return "Cruiser";
		case BATTLESHIP:
			return "Battleship";
		case CARRIER:
			return "Carrier";
		default:
			return "Submarine";
	}
}

class Board 
{
private:
	//vector<vector<int> > ownBoard;
	//vector<vector<int> > enemyBoard;
	int** ownBoard;
	int** enemyBoard;
	//set<pair<int, int> > submarineSet, cruiserSet, battleshipSet, carrierSet;
	//map<int, vector< pair<int, int> > > shipToPoints;
	const int dimension;

public:
	Board(const int dim) : dimension(dim) {
		initialize();
	}

	~Board(){
		delete[] ownBoard;
		delete[] enemyBoard;
	}

	int getOwnBoardCell(int row, int col){
		return ownBoard[row][col];
	}

	void setOwnBoardCell(int row, int col, int newVal){
		ownBoard[row][col] = newVal;
	}

	int getEnemyBoardCell(int row, int col){
		return enemyBoard[row][col];
	}

	void setEnemyBoardCell(int row, int col, int newVal){
		enemyBoard[row][col] = newVal;
	}

	void printEnemyBoard(bool showAll=false){
		cout << "   ";
		for(int c = 0; c < dimension; c++){
			cout << c % 10 << " ";
		}
		cout << "\n";
		for(int r = 0; r < dimension; r++){
			cout << r % 10 << "  ";
			for(int c = 0; c < dimension; c++){
				if(enemyBoard[r][c] == UNSURE){
					cout << "X ";
				}
				else if(enemyBoard[r][c] == HIT){
					cout << "H ";
				}
				else if(enemyBoard[r][c] == MISS){
					cout << "M ";
				}
			}
			cout << "\n";
		}
		cout << "\n";
	}

	void printOwnBoard(){
		cout << "   ";
		for(int c = 0; c < dimension; c++){
			cout << c % 10 << " ";
		}
		cout << "\n";
		for(int r = 0; r < dimension; r++){
			cout << r % 10 << "  ";
			for(int c = 0; c < dimension; c++){
				if(ownBoard[r][c] == EMPTY){
					cout << "X ";
				}
				else if(ownBoard[r][c] == SUBMARINE){
					cout << "S ";
				}
				else if(ownBoard[r][c] == CRUISER){
					cout << "C ";
				}
				else if(ownBoard[r][c] == BATTLESHIP){
					cout << "B ";
				}
				else if(ownBoard[r][c] == CARRIER){
					cout << "R ";
				}
			}
			cout << "\n";
		}
		cout << "\n";
	}

	bool isValidMove(int row, int col){
		if(row >= 0 && row < dimension && col >= 0 && col < dimension){
			if(enemyBoard[row][col] == UNSURE){
				return true;
			}
			else{
				return false;
			}
		}
		return false;
	}

private:
	void initialize(){
		initializeOwnBoard();
		initializeEnemyBoard();
	}

	bool checkValidInput(int shipType, char horizOrVert, int alongRowOrCol, int rangeMinAxis, int rangeMaxAxis){
		if((rangeMaxAxis - rangeMinAxis == getShipSize(shipType) - 1) 
			&& (horizOrVert == 'H' || horizOrVert == 'V') 
			&& (alongRowOrCol >= 0 || alongRowOrCol < dimension) 
			&& (rangeMinAxis >= 0)
			&& (rangeMaxAxis < dimension)){
				for(int i = rangeMinAxis; i <= rangeMaxAxis; i++){
					if(horizOrVert == 'H'){
						if(ownBoard[alongRowOrCol][i] != EMPTY){
							return false;
						}
					}
					else {
						if(ownBoard[i][alongRowOrCol] != EMPTY){
							return false;
						}
					}
				}
			return true;
		}
		else{
			return false;
		}
	}

	void initializeByType(int shipType){
		char horizOrVert;
		int alongRowOrCol, rangeMinAxis, rangeMaxAxis;

		printOwnBoard();
		cout << "Initialize " << shipTypeToString(shipType) << " (H/V Row/Col RangeMin RangeMax): ";
		cin >> horizOrVert >> alongRowOrCol >> rangeMinAxis >> rangeMaxAxis;
		while(!checkValidInput(shipType, horizOrVert, alongRowOrCol, rangeMinAxis, rangeMaxAxis)){
			printOwnBoard();
			cout << shipTypeToString(shipType) << " not in range - please enter again (H/V Row/Col RangeMin RangeMax): ";
			cin >> horizOrVert >> alongRowOrCol >> rangeMinAxis >> rangeMaxAxis;
		}

		for(int i = rangeMinAxis; i <= rangeMaxAxis; i++){
			if(horizOrVert == 'H'){
				ownBoard[alongRowOrCol][i] = shipType;
				//submarineSet.insert(new pair<int, int>(alongRowOrCol, i));
				//shipToPoints[shipType].push_back(make_pair(alongRowOrCol, i));
			}
			else {
				ownBoard[i][alongRowOrCol] = shipType;
				//submarineSet.insert(new pair<int, int>(i, alongRowOrCol));
				//shipToPoints[shipType].push_back(make_pair(i, alongRowOrCol));
			}
		}
	}

	void initializeAllShips(){
		initializeByType(SUBMARINE);
		initializeByType(CRUISER);
		initializeByType(BATTLESHIP);
		initializeByType(CARRIER);
	}

	void initializeOwnBoard(){
		cout << "Initializing own board..." << endl;
		//ownBoard.reserve(dimension);
		ownBoard = new int*[dimension];
		for(int r = 0; r < dimension; r++){
			//ownBoard[r].reserve(dimension);
			ownBoard[r] = new int[dimension];
			for(int c = 0; c < dimension; c++){
				ownBoard[r][c] = EMPTY;
			}
		}

		initializeAllShips();

		cout << "Initial setup\n\n";
		printOwnBoard();
	}

	void initializeEnemyBoard(){
		cout << "Initializing enemy board..." << endl;
		//enemyBoard.reserve(dimension);
		enemyBoard = new int*[dimension];
		for(int r = 0; r < dimension; r++){
			//enemyBoard[r].reserve(dimension);
			enemyBoard[r] = new int[dimension];
			for(int c = 0; c < dimension; c++){
				enemyBoard[r][c] = UNSURE;
			}
		}
		cout << "Initial enemy setup\n\n";
		printEnemyBoard();
	}
};

class Player
{
private:
	string name;
	int submarineHits;
	int cruiserHits;
	int battleshipHits;
	int carrierHits;
	Board* b;
	int numMoves;
	Player* enemy;
public:
	Player(const string& pName, int dim) : name(pName), submarineHits(0), cruiserHits(0), battleshipHits(0), carrierHits(0), numMoves(0), enemy(NULL) {
		b = new Board(dim);
	}

	~Player(){
		delete b;
	}

	void setEnemy(Player* otherPlayer){
		enemy = otherPlayer;
	}

	int getCell(int row, int col){
		return b->getOwnBoardCell(row, col);
	}

	string getName() const {
		return name;
	}

	int getNumMoves() const {
		return numMoves;
	}

	bool shipSunkStatus(int shipType){
		int shipSize = getShipSize(shipType);
		if(shipType == SUBMARINE){
			return submarineHits == shipSize;
		}
		else if(shipType == CRUISER){
			return cruiserHits == shipSize;
		}
		else if(shipType == BATTLESHIP){
			return battleshipHits == shipSize;
		}
		else if(shipType == CARRIER){
			return carrierHits == shipSize;
		}
	}

	bool allShipsSunk(){
		return shipSunkStatus(SUBMARINE) && shipSunkStatus(CRUISER) && shipSunkStatus(BATTLESHIP) && shipSunkStatus(CARRIER);
	}

	void hitHandler(int shipType){
		switch(shipType){
			case SUBMARINE:
				submarineHits++;
				return;
			case CRUISER:
				cruiserHits++;
				return;
			case BATTLESHIP:
				battleshipHits++;
				return;
			case CARRIER:
				carrierHits++;
				return;
			default:
				return;
		}
	}

	string shipStatus(int shipType){
		bool isSunk = shipSunkStatus(shipType);
		return isSunk ? "Sunk" : "Active";
	}

	bool playTurn(){
		int row, col;
		bool gameOver = false;
		cout << "Turn: " << name << endl;
		cout << "Own Board" << endl;
		b->printOwnBoard();
		cout << "Enemy Board" << endl;
		b->printEnemyBoard();

		cout << "Number of moves so far: " << numMoves << endl;
		cout << "Your ships' status:\n";
		cout << "Submarine: " << shipStatus(SUBMARINE) << endl;
		cout << "Cruiser: " << shipStatus(CRUISER) << endl;
		cout << "Battleship: " << shipStatus(BATTLESHIP) << endl;
		cout << "Carrier: " << shipStatus(CARRIER) << endl;
		cout << "\n";

		cout << "Your enemies' status:\n";
		cout << "Submarine: " << enemy->shipStatus(SUBMARINE) << endl;
		cout << "Cruiser: " << enemy->shipStatus(CRUISER) << endl;
		cout << "Battleship: " << enemy->shipStatus(BATTLESHIP) << endl;
		cout << "Carrier: " << enemy->shipStatus(CARRIER) << endl;
		cout << "\n";

		do {
			cout << name << " - Enter row and column to strike: ";
			cin >> row >> col;
		} while (b->isValidMove(row,col) == false);

		int enemyCell = enemy->getCell(row, col);
		if(enemyCell == EMPTY){
			b->setEnemyBoardCell(row, col, MISS);
			cout << "You missed!\n" << endl;
		}
		else{
			b->setEnemyBoardCell(row, col, HIT);
			enemy->hitHandler(enemyCell);
			if(enemy->allShipsSunk())
				gameOver = true;
			cout << "You hit!\n" << endl;
		}

		numMoves++;

		//cout << "Enemy Board after move" << endl;
		//b->printEnemyBoard();
		return gameOver;
	}

};

class Game
{
private:
	Player* player1;
	Player* player2;

public:
	Game(int dim, const string& p1Name, const string& p2Name) {
		player1 = new Player(p1Name, dim);
		player2 = new Player(p2Name, dim);
		player1->setEnemy(player2);
		player2->setEnemy(player1);
	}

	~Game(){
		delete player1;
		delete player2;
	}

	void playGame(){
		while(true){
			if(player1->playTurn()){
				cout << player1->getName() << " wins! (in " << player1->getNumMoves() << " moves";
				return;
			}
			if(player2->playTurn()){
				cout << player2->getName() << " wins! (in " << player2->getNumMoves() << " moves";
				return;
			}
		}
	}
};

void startGame(){
	int dimension;
	string p1Name;
	string p2Name;
	cout << "Enter board dimension: ";
	cin >> dimension;
	while(dimension < 5 || dimension > 20){
		cout << "Re-enter the board dimension: ";
		cin >> dimension;
	}
	cout << "Enter player 1's name: ";
	cin >> p1Name;
	cout << "Enter player 2's name: ";
	cin >> p2Name;
	Game g(dimension, p1Name, p2Name);
	g.playGame();
}

int main()
{
	startGame();
}