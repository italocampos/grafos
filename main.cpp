#include <iostream>
#include <locale>
#include "lista.h"
#include "tabela.h"

using namespace std;

int main() {
	setlocale (LC_ALL, "portuguese");
	/*Lista lista;
	lista.addEnd(5);
	lista.addEnd(10);
	
	Lista listaA;
	listaA.addEnd(15);
	listaA.addEnd(20);
	listaA.addEnd(25);
	lista.append(listaA);
	lista.print();
	//lista.printNodes();
	lista.addPosition(2, 20);
	lista.addPosition(0, 0);
	lista.addPosition(6, 30);
	lista.addPosition(3, -5);
	//lista.printNodes();
	/*lista.removeFirst();
	lista.removeLast();
	//lista.printNodes();
	lista.removeAllItems(20);
	lista.printNodes();
	lista.removePosition(3);
	lista.print();
	lista.removePosition(0);
	lista.print();
	lista.removePosition(lista.length()-1);
	lista.printNodes();
	//lista.reverse();
	lista.print();
	cout<<"\nComprimento da lista: "<<lista.length();
	//lista.removePosition(1);
	//lista.print();*/
	
	/*Tabela table;
	table.addList(lista);
	cout<<"\nColunas: "<<table.numColumns(0);
	cout<<"\nLinhas: "<<table.numLines();
	cout<<"\nColunas: ";
	table.numColumns();
	table.print();
	table.pushItem(20);
	table.print();
	table.setItemPosition(1, 0, 25);
	table.print();
	table.removeLastItem();
	table.print();
	table.dropLine();
	table.print();
	table.addList(listaA);
	table.print();
	table.dropTable();
	table.print();*/
	
	Tabela fernoob;
	Lista italo;
	
	fernoob.print();
	
	for(int i=0; i<3; i++) {
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
	
	cout<<"\nGrau de saída do nó 1 = "<<fernoob.numColumns(1)-1;
	
	
	cout<<endl;
}
