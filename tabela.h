#ifndef TABELA_H_
#define TABELA_H_

#include <C:\Users\MM1\Documents\Atividade_03\lista.h>
#include <iostream>
#include <vector>

using namespace std;

class Tabela {
public:
	vector <Lista> linha;
	
	Tabela() {	}
	
	virtual ~Tabela() {	};
	
	// Adiciona uma nova lista l como última linha da tabela
	void addList(Lista lista) {
		linha.push_back(lista);
	}
	
	Lista * getList(int num_linha) {
		if(num_linha >= 0 && num_linha < numLines())
			return &(linha[num_linha]);
		else
			cout<<"Out of range.\n";
	}
	
	int numLines() {
		return linha.size();
	}
	
	int numColumns(int num_linha) {
		return linha[num_linha].length();
	}
	
	void numColumns() {
		for(int i=0; i<numLines(); i++)
			cout<<"Linha "<<i<<" = "<<linha[i].length()<<endl;
	}
	
	void newLine() {
		Lista l;
		this->linha.push_back(l);
		l.~Lista();
	}
	
	// Remove a última linha da tabela
	void dropLine() {
		this->linha[numLines()-1].~Lista();
		this->linha.pop_back();
	}
	
	// Adiciona um item ao final da linha l
	void pushItem(int lin, int item) {
		if(lin >=0 && lin < numLines()) {
			this->linha[lin].addEnd(item);
		}
		else
			cout<<"Out of range.\n";
	}
	
	// Adiciona um item ao final da última linha da tabela
	void pushItem(int item) {
		this->linha[numLines()-1].addEnd(item);
	}
	
	// Altera um item ou adiciona um novo ao final
	void setItemPosition(int lin, int col, int item) {
		if(lin >= 0 && lin<numLines()) {
			int colunas = this->linha[lin].length();
			if(col >=0 && col < colunas)
				this->linha[lin].setItem(item, col);
			else {
				if(col == colunas)
					this->linha[lin].addEnd(item);
				else
					cout<<"Out of range.\n";
			}
		}
		else {
			if(lin == numLines() && col == 0) {
				newLine();
				this->linha[lin].addBegin(item);
			}
			else
				cout<<"Out of range.\n";
		}
	}
	
	void addItemPosition(int lin, int col, int item) {
		if(lin >= 0 && lin<numLines())
			this->linha[lin].addPosition(col, item);
		else
			cout<<"Out of range.\n";
	}
	
	// Remove o último item da última linha
	void removeLastItem() {
		if(numLines() > 0) {
			if(this->linha[numLines()-1].isEmpty())
				dropLine();
			else
				this->linha[numLines()-1].removeLast();
		}
		else
			cout<<"Empty table.\n";
	}
	
	void removeLastItem(int lin) {
		if(numLines() > 0) {
			if(lin >= 0 && lin < numLines()) {
				if(this->linha[lin].isEmpty())
					dropLine();
				else
					this->linha[lin].removeLast();
			}
			else
				cout<<"Out of range.\n";
		}
		else
			cout<<"Empty table.\n";
	}
	
	void dropTable() {
		for(int i=this->numLines()-1; i>=0; i--)
			dropLine();
	}
	
	void print() {
		if(numLines() > 0) {
			//cout<<"TABLE:\n";
			for(int i=0; i<numLines(); i++) {
				this->linha[i].print();
				cout<<endl;
			}
			cout<<endl;
		}
		else
			cout<<"Empty table.\n";
	}
};

#endif
