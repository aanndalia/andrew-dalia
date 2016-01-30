#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

const int BOMB = -1;
const int EMPTY = 0;
enum GameState { WIN, LOSE, INVALID, VALID};

class Board{
private:
	int** board;
	bool** hiddenBoard;
	const int dim;
	const int totalBombs;
public:
	Board(const int dimension, const int totalBombs) : dim(dimension), totalBombs(totalBombs){
		initialize();
	} 

	~Board(){
		delete[] board;
		delete[] hiddenBoard;
	}

	void printBoard(bool showHidden = false){
		cout << "   ";
		for(int c=0; c < dim; c++){
			cout << c % 10 << " ";
		}
		cout << endl;
		cout << endl;
		for(int r=0; r < dim; r++){
			cout << r % 10 << "  ";
			for(int c=0; c < dim; c++){
				if(!showHidden && hiddenBoard[r][c]){
					cout << "X" << " ";
				}
				else{
					if(board[r][c] == EMPTY){
						cout << "0" << " ";
					}
					else if(board[r][c] == BOMB){
						cout << "B" << " ";
					}
					else {
						cout << board[r][c] << " ";
					}
				}
			}
			cout << endl;
		}
		cout << endl;
	}

	int getBoardCell(int row, int col){
		return board[row][col];
	}

	bool isHiddenCell(int row, int col){
		return hiddenBoard[row][col];
	}

	void setHiddenCell(int row, int col, bool newValue){
		hiddenBoard[row][col] = newValue;
	}

	bool isWin(){
		for(int r=0; r < dim; r++){
			for(int c=0; c < dim; c++){
				if(isHiddenCell(r,c) && getBoardCell(r, c) != BOMB){
					return false;
				}
			}
		}
		cout << "You win!" << endl;
		return true;
	}

	void uncoverConnectedEmpties(int row, int col){
		if(!isInbounds(row, col) || !isHiddenCell(row, col)){
			return;
		}

		if(board[row][col] != EMPTY){
			setHiddenCell(row, col, false);
			return;
		}

		setHiddenCell(row, col, false);

		for(int r = row - 1; r <= row + 1; r++){
			for(int c = col - 1; c <= col + 1; c++){
				if(!(r == row && c == col)){
					uncoverConnectedEmpties(r, c);
				}
			}
		}
	}

	bool isInbounds(int row, int col){
		if(row < 0 || row >= dim || col < 0 || col >= dim)
			return false;
		return true;
	}

private:
	void initBoard(){
		board = new int*[dim];
		for(int i = 0; i < dim; i++){
			board[i] = new int[dim];

			for(int j = 0; j < dim; j++){
				board[i][j] = EMPTY;
			}
		}
	}

	void initHiddenBoard(){
		hiddenBoard = new bool*[dim];
		for(int i = 0; i < dim; i++){
			hiddenBoard[i] = new bool[dim];
			for(int j = 0; j < dim; j++){
				hiddenBoard[i][j] = true;
			}
		}
	}


	void initBombs(){
		srand(time(NULL));
		int bombsPlaced = 0;
		while(bombsPlaced < totalBombs){
			int randRow = rand() % dim;
			int randCol = rand() % dim;
			if(board[randRow][randCol] != BOMB){
				board[randRow][randCol] = BOMB;
				bombsPlaced++;
			}
		}
	}

	void initNumbers(){
		for(int r=0; r < dim; r++){
			for(int c=0; c < dim; c++){
				if(board[r][c] != BOMB){
					board[r][c] = getNeighboringBombsCount(r, c);
				}
			}
		}
	}

	int getNeighboringBombsCount(int row, int col){
		int count = 0;
		for(int r=row-1; r <= row+1; r++){
			for(int c=col-1; c <= col+1; c++){
				if(r >= 0 && r < dim && c >= 0 && c < dim && board[r][c] == BOMB){
					count++;
				}
			}
		}
		return count;
	}

	void initialize(){
		initBoard();
		initHiddenBoard();
		initBombs();
		initNumbers();
	}

};

class Game{
private:
	Board b;
	int numMoves;
public:
	Game(Board& board) : b(board), numMoves(0) {
		
	}

	void printBoard(bool showHidden = false){
		b.printBoard(showHidden);
	}

	void play(){
		printBoard();
		while(playTurn() != LOSE && b.isWin() == false){
			numMoves++;
		}
		cout << "Number of moves: " << numMoves + 1 << endl;
		printBoard(true);
		return;
	}

private:
	GameState playTurn(){
		int row, col;
		cout << "Enter a row and column (separated by a space): ";
		cin >> row >> col;

		if(b.isInbounds(row, col) == false){
			cout << "Invalid move, outside dimensions - try again" << endl;
			printBoard();
			return INVALID;
		}

		if(b.isHiddenCell(row, col) == false){
			cout << "Invalid move, cell is already uncovered - try again" << endl;
			printBoard();
			return INVALID;
		}
		else{
			if(b.getBoardCell(row, col) == BOMB){
				cout << "You lose!" << endl;
				return LOSE;
			}
			else if(b.getBoardCell(row, col) == EMPTY){
				b.uncoverConnectedEmpties(row, col);
			}
			else{
				b.setHiddenCell(row, col, false);
			}
		}
		printBoard();
		return VALID;
	}

};

int main(){
	int dim, totalBombs;
	cout << "What dimension should the board be? ";
	cin >> dim;
	cout << "How many bombs should there be? ";
	cin >> totalBombs;

	Board b = Board(dim, totalBombs);
	Game g = Game(b);
	g.printBoard(true); // for debugging
	g.play(); 
}