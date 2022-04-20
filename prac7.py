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




#include<iostream>
using namespace std;

class hp
{
   int heap[20],heap1[20],x,n1,i;
   public:
   hp()
   { heap[0]=0;  heap1[0]=0;
   } 
   void getdata();
   void insert1(int heap[],int);
   void upadjust1(int heap[],int);
   void insert2(int heap1[],int);
   void upadjust2(int heap1[],int);
   void minmax();
};
void hp::getdata()
{  
   cout<<"\n enter the no. of students";
   cin>>n1;
   cout<<"\n enter the marks";
   for(i=0;i<n1;i++)
   {   cin>>x;
       insert1(heap,x);
       insert2(heap1,x);
   }
}
void hp::insert1(int heap[20],int x)
{
   int n;
   n=heap[0]; 
   heap[n+1]=x;
   heap[0]=n+1;
  
   upadjust1(heap,n+1);
}
void hp::upadjust1(int heap[20],int i)
{
    int temp;
    while(i>1&&heap[i]>heap[i/2])
    {
       temp=heap[i];
       heap[i]=heap[i/2];
       heap[i/2]=temp;
       i=i/2;
    }
}
void hp::insert2(int heap1[20],int x)
{
   int n;
   n=heap1[0]; 
   heap1[n+1]=x;
   heap1[0]=n+1;
  
   upadjust2(heap1,n+1);
}
void hp::upadjust2(int heap1[20],int i)
{
    int temp1;
    while(i>1&&heap1[i]<heap1[i/2])
    {
       temp1=heap1[i];
       heap1[i]=heap1[i/2];
       heap1[i/2]=temp1;
       i=i/2;
    }
}
void hp::minmax()
{
   cout<<"\n max marks"<<heap[1];
   cout<<"\n##";
   for(i=0;i<=n1;i++)
   {   cout<<"\n"<<heap[i];  }
   cout<<"\n min marks"<<heap1[1];
   cout<<"\n##";
   for(i=0;i<=n1;i++)
   {   cout<<"\n"<<heap1[i];  }
}
