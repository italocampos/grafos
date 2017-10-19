#include <iostream>
#include <locale>
#include "lista.h"
#include "tabela.h"
#include "input.h"

using namespace std;

int main() {
	setlocale (LC_ALL, "portuguese");
	
	Tabela fernoob;
	Lista italo;
	
	//fernoob.print();
	
	readFromUser(fernoob);
	
	fernoob.print();
	
	/*for(int i=0; i<3; i++) {
		for(int j=0; j<2; j++) {
			printf("Informe a posicao [%d, %d]: ", i, j);
			int temp;
			cin>>temp;
			fernoob.setItemPosition(i, j, temp);
		}
	}
	
	italo.addEnd(0);
	italo.addEnd(1);
	italo.addEnd(2);
	//italo.print();
	
	fernoob.setItemPosition(3, 3, 100);
	fernoob.setItemPosition(0, 2, 200);
	fernoob.addList(italo);
	cout<< endl << "This is fernoob: \n"; fernoob.print(); cout << endl;
	
	Lista * leo = new Lista();
	leo = fernoob.getList(1);
	cout<< endl << "This is leo: "; leo->print(); cout << endl;
	leo->reverse();
	cout<< endl << "This is oel: "; leo->print(); cout << endl;
	
	cout<< endl << "This is an other fernoob: \n"; fernoob.print(); cout << endl;
	
	cout<<"\nGrau de saída do nó 1 = "<<fernoob.numColumns(1)-1;*/
	
	
	cout<<endl;
}