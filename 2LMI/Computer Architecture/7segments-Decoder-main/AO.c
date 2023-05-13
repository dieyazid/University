#include <stdio.h>
#include <stdlib.h>
int e0,e1,e2,e3,a,b,c,d,e,f,g;
int s1,s2,choice;
char ans;
int en_a,en_b,inv_a,c_in,c_out,f0,f1,d1,d2,d3,d4,bl1,bl2,s,s3,s4;

void menu(){
do{
printf("----Choose one 1 2 or 3----\n");
printf("1-->incrementer\n");
printf("2-->7 Segments Decoder\n");
printf("3-->Arithmetic and logical unit\n");
printf("---------------------------\n");
scanf("%d",&choice);
}while(choice!=1 && choice !=2 && choice !=3);
}
void inc(){
do{
do{
printf("Donner A\n");
scanf("%d",&a);}while(a!=0 && a!=1);
do{
printf("Donner B\n");
scanf("%d",&b);}while(b!=0 && b!=1);
s1=!a;
s2=a & !b | !a & b;
printf("S1 = %d\n",s1);
printf("S2 = %d\n",s2);

do{
printf("Do you want to go back to menu? Y/N \n");
scanf("%s",&ans);}while(ans!='Y' && ans!='N');

}while(ans=='N');}
void seg(){
do{
do{
printf("Donner la valeur de A-->");
scanf("%d",&e3);}while(e3!=1 && e3!=0);
do{
printf("Donner la valeur de B-->");
scanf("%d",&e2);}while(e2!=1 && e2!=0);
do{
printf("Donner la valeur de C-->");
scanf("%d",&e1);}while(e1!=1 && e1!=0);
do{
printf("Donner la valeur de D-->");
scanf("%d",&e0);}while(e0!=1 && e0!=0);
//affectation
a=e3 | e1 | e2 & e0 | !e2 & !e0;
b=!e2 | e1 & e0 | !e1 & !e0;
c=e3 | e2 | !e1 | e0;
d=e3 | e1 & !e0 | e2 & !e1 & e0 | !e2 & e1 | !e2 & !e0;
e=!e2 & !e0 | e1 & !e0;
f=!e1 & !e0 | e3 | e2 & !e1 | e2 & !e0;
g=e2 & !e1 | e3 | e1 & !e0 | !e2 & e1;
//affichage
printf("|a = %d\n",a);
printf("|b = %d\n",b);
printf("|c = %d\n",c);
printf("|d = %d\n",d);
printf("|e = %d\n",e);
printf("|f = %d\n",f);
printf("|g = %d\n",g);
if(a==1){
printf("◼️ ◼️ ◼️\n");
}if(a==0){
printf("\n");}
if(f==1){
printf("◼️");
}if(f==0){
printf(" ");}
if(b==1){
printf("   ◼️\n");
}if(b==0){
printf("\n");}
if(g==1){
printf("◼️ ◼️ ◼️\n");
}if(g==0){
printf("\n");}
if(e==1){
printf("◼️");
}if(e==0){
printf(" ");}
if(c==1){
printf("   ◼️\n");
}if(c==0){
printf("\n");}
if(d==1){
printf("◼️ ◼️ ◼️\n");
}if(d==0){
printf("\n");}
do{
printf("Do you want to go back to menu? Y/N \n");
scanf("%s",&ans);}while(ans!='Y' && ans!='N');
}while(ans=='N');
}
void ual(){
do{
//lecture
do{
printf("Donner la valeur de A-->");
scanf("%d",&a);}while(a!=0 && a!=1);
do{
printf("Donner la valeur de B-->");
scanf("%d",&b);}while(b!=0 && b!=1);
//optionnel
do{
printf("Est tu veut entrer la valeur de En_A? Y/N\n");
scanf("%s",&ans);}while(ans !='Y' && ans!='N');
if(ans =='Y'){
do{
printf("Donner la valeur de En_A-->");
scanf("%d",&en_a);}while(en_a!=0 && en_a!=1);}else {en_a=0;}
do{
printf("Est tu veut entrer la valeur de En_B? Y/N\n");
scanf("%s",&ans);}while(ans !='Y' && ans!='N');
if(ans =='Y'){
do{
printf("Donner la valeur de En_B-->");
scanf("%d",&en_b);}while(en_b!=0 && en_b!=1);}else {en_b=0;}
//
do{
printf("Donner la valeur de F0-->");
scanf("%d",&f0);}while(f0!=0 && f0!=1);
do{
printf("Donner la valeur de F1-->");
scanf("%d",&f1);}while(f1!=0 && f1!=1);
do{
printf("Donner la valeur de C_in-->");
scanf("%d",&c_in);}while(c_in!=0 && c_in!=1);
inv_a=!a;
d1=!f0 & !f1;
d2=!f0 & f1;
d3=f0 & !f1;
d4=f0 & f1;
bl1=inv_a ^ (a & en_a);
bl2=en_b & b;
s1=(bl1 & bl2) & d1;
s2=(bl1 | bl2) & d2;
s3=!bl2 & d3;
s4=((bl1 ^ bl2) ^ c_in) & d4;
s=s1 | s2 | s3 | s4;
c_out=(d4 & (bl1 ^ bl2) & c_in) | (d4 & bl1 & bl2);
//afichage
printf("|S     = %d\n",s);
printf("|C_out = %d\n",c_out);

do{
printf("Do you want to go back to menu? Y/N \n");
scanf("%s",&ans);}while(ans!='Y' && ans!='N');
}while(ans =='N');}
int main(){
do{
menu();
switch (choice){
  case 1:inc();
  break;
  case 2:seg();
  break;
  case 3:ual();
  break;
}
do{
printf("Do you want to continue Y/N \n");
scanf("%s",&ans);}while(ans!='Y' && ans!='N');
}while(ans=='Y');

}
