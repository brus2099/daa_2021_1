#include<stdio.h>

int main() {
	
	printf("\n\t***Universidad Nacional Autonoma de Mexico***");
	printf("\n\t **Facultad de Estudios Superiores Aragon**");
	printf("\n\t        *Ingenieria en Computacion*\n");
	printf("\nAlumno: Bruno Cruz Granados ");
	printf("\nCatedratico: Juan Gastaldi Perez\n");
		
	int a[4][4],b[4][4],c[4][4],x,y;
	printf("\n\t**Programa que multiplica dos matrices**\n");
	
	printf("\nCaptura de la matriz de dimensiones 2x3\n");
      
	for(x=1;x<=2;x++)
		for(y=1;y<=3;y++) {
		    printf("\nIntroduce el valor (%i,%i) de la matriz :",x,y);
		    scanf("%i",&a[x][y]);
		   }

    printf("\n\nCaptura de la matriz con dimensiones 3x3\n");
      for(x=1;x<=3;x++)
		for(y=1;y<=3;y++) {
    		printf("\nIntroduce el valor (%i,%i) de la matriz :",x,y);
    		scanf("%d",&b[x][y]);
		}

	for(x=1;x<=2;x++)
	   for(y=1;y<=3;y++)
	    	c[x][y]=(a[x][1]*b[1][y])+(a[x][2]*b[2][y])+(a[x][3]*b[3][y]);

	printf ("\n\nEl resultado de multiplicar la matriz 2x3 con la matrizm 3x3 es el siguiente: \n");	
	for(x=1;x<=2;x++) {
		printf("\n\t");
		for(y=1;y<=3;y++) {
		    printf("%d ",c[x][y]);
			printf("\t");
		}
		printf("\n");
	}
	printf("\n\n");
	
}