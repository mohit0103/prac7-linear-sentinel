#LINEAR SEARCH
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

n=int(input("enter no to search: "))

for i in range(len(p)):
  if p[i]==n:
    print("Number found")
    break
else:
  print("Number not found")
  
#SENTINEL SEARCH
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

key=int(input("enter no to search: "))

def sentinel_Search(p, n, key):
    last = p[n - 1]
    p[n-1] = key
    i=0
 
    while (p[i] != key):
        i+=1
    p[n-1]=last
 
    if ((i<n-1) or (p[n-1] == key)):
        print("Number found")
    else:
        print("Number not found")

sentinel_Search(p, n, key)
#include<iostream>
using namespace std;
 struct node{
 int value;
  node* next;
}*HashTable[10];
class hashing{
public:

 hashing(){

  for(int i=0 ; i<10 ; i++){
   HashTable[i]=NULL;
  }
 }


 int HashFunction(int value){
  return (value%10);
 }

 node* create_node(int x){
  node* temp=new node;
  temp->next=NULL;
  temp->value=x;
  return temp;
 }

 void display(){
  for(int i=0 ; i< 10; i++){
   node * temp=new node;
   temp=HashTable[i];
   cout<<"a["<<i<<"] : ";
   while(temp !=NULL){
    cout<<" ->"<<temp->value;
    temp=temp->next;
   }
   cout<<"\n";
  }
 }
 void insertElement(int value){
   int hash_val = HashFunction(value);
             // node* prev = NULL;
              //node* entry = HashTable[hash_val];
              node* temp=new node;
              node* head=new node;
              head = create_node(value);
              temp=HashTable[hash_val];
              if (temp == NULL)
                           {

                              HashTable[hash_val] =head;
                               }
              else{
               while (temp->next != NULL)

              {
                  temp = temp->next;
              }

                      temp->next =head;

              }


 }
};

int main(){
 int ch;
 int data,search,del;
 hashing h;
 do{
  cout<<"\nTelephone : \n1.Insert \n2.Display";
  cin>>ch;
  switch(ch){
  case 1:cout<<"\nEnter phone no. to be inserted : ";
    cin>>data;
    h.insertElement(data);
    break;
  case 2:h.display();
    break;
  }
 }while(ch!=5);
 return 0;
}

