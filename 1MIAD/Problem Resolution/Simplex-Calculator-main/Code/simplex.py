from cmath import inf
import numpy as np
from Code.var_operations import *
from Code.colors import *
from simple_term_menu import TerminalMenu

options = ['=', '>=', '<=']

def Get_Data(Message,min,max):
    while True:
        try:
            Number=int(input(Message))
            if Number<min or Number>max:
                raise ValueError
            break
        except ValueError:
            print(f"{bcolors.FAIL}⚠️ Invalid input. Please enter a number between {min} and {max} ⚠️{bcolors.ENDC}\n")
    return Number

def Fill_Tables(Var_Number,Const_Number,Obj_Table,Const_Table,Results,Eq_Type):
    index=0
    counter=0
    for i in range(0,Var_Number):
        Obj_Table.append(input(f"Enter the coefficient of the variable X{str(i+1)} of the objective function: "))
    print("---------------------------------------------------")
    for i in range(0,Var_Number):
        for j in range (0,Const_Number):
            Const_Table.append(input(f"Enter the coefficient of the variable X{str(index+1)} of the constraint number {str(counter+1)}: "))
            index+=1
            if index==Var_Number:
                index=0
                terminal_menu = TerminalMenu(options,title=f"Select the type of the constraint number: {str(counter+1)}")
                menu_entry_index = terminal_menu.show()
                Eq_Type.append(options[menu_entry_index])
                Results.append(input(f"Enter the result of the constraint number {str(i+1)}:"))
                counter+=1
    return Obj_Table,Const_Table,Results,Eq_Type

def Show_Data(Var_Number,Obj_Table,Const_Table,Results,Eq_Type):
    Result_Index=0;index=0
    print("\n========================Objective Function========================")
    print("Max Z = ",end="")
    for i in range(0,len(Obj_Table)):
        print(str(Obj_Table[i])+" X"+str(i+1),end="")
        if(i<len(Obj_Table)-1):
            print(" + ",end="")
    print("\n____________________________Constraints____________________________\n")
    for i in range(0,len(Const_Table)):
        index+=1;
        print(str(Const_Table[i])+" X"+str(index) ,end="")
        if((i+1)%Var_Number==0):
            print(Eq_Type[Result_Index] + str(Results[Result_Index])+"\n")
            Result_Index+=1
        else:
            print(" + ",end="")
        if index==Var_Number:
                    index=0

def Preliminary_stage(Var_Number,Obj_Table,Const_Table,Results,Eq_Type):
    Var_counter=0;const_counter=0;Constraint=[];X_counter=0;j=0
    for i in range(0,len(Eq_Type)):
        if Eq_Type[i]==">=":
            Var_counter+=2
        elif Eq_Type[i]=="=" or Eq_Type[i]=="<=":
            Var_counter+=1
    Constraint.append([])
    for i in range(0,len(Const_Table)):
        Constraint[const_counter].append(Const_Table[i])
        if (i+1) % Var_Number == 0 and i != 0 or i == len(Const_Table)-1:
            Obj_Table.append(0)
            if Eq_Type[const_counter]==">=":
                while j!=X_counter:
                    Constraint[const_counter].append(0)
                    j+=1
                Constraint[const_counter].append(-1)
                Constraint[const_counter].append(1)
                X_counter+=1
            elif Eq_Type[const_counter]=="=" or Eq_Type[const_counter]=="<=":
                while j!=X_counter:
                    Constraint[const_counter].append(0)
                    j+=1
                X_counter+=1
                Constraint[const_counter].append(1)
            j=0
            while len(Constraint[const_counter])<(Var_counter+Var_Number):
                Constraint[const_counter].append(0)
            
            const_counter+=1
            if const_counter*2!=len(Const_Table):
                Constraint.append([])
    return Constraint,Obj_Table

def calculation(Constraint,Results,X_counter,Obj_Table):
    iteration=0;Z=0
    Base,Tms,Hold=([] for variable in range(0,3))
    print("\n========================Solution========================\n")
    print(f"==================Iteration number {iteration}====================")
    iteration+=1
    for i in range(0,len(Results)):
        Base.append(0)
    for i in range(0,len(Obj_Table)):
        Tms.append(Obj_Table[i])
    print("Results:",Results)
    print("Constraint Table:",Constraint)
    print("Tms:",Tms)
    while any(x>0 for x in Tms):
        Z=0
        In_Index=Tms.index(max(Tms))
        for i in range(0,len(Constraint)):
            try:
                Hold.append(Results[i]/Constraint[i][In_Index])
            except ZeroDivisionError:
                Hold.append(inf)
        arr=np.array(Hold)
        Out_Index=np.where(arr > 0, arr, np.inf).argmin()
        pivot=Constraint[Out_Index][In_Index]
        if any((x>0 and x!=inf) for x in Hold):
            print(f"==================Iteration number {iteration}====================")
            print(f"X{In_Index+1} In ->")
            print(f"X{Out_Index+X_counter} Out <-")
        else:
            print(f"{bcolors.FAIL}Unbounded solution{bcolors.ENDC}\n")
            exit()
        
        for i in range(0,len(Constraint[Out_Index])):
            Constraint[Out_Index][i]=Constraint[Out_Index][i]/pivot
        Results[Out_Index]=round(Results[Out_Index]/pivot,2)

        for i in range(0,len(Constraint)):
            if i!=Out_Index:
                temp=Constraint[i][In_Index]
                for j in range(0,len(Constraint[i])):
                    Constraint[i][j]=Constraint[i][j]-(Constraint[Out_Index][j]*temp)
                Results[i]=Results[i]-(Results[Out_Index]*temp)
        Tms_Pivot=Tms[In_Index]
        for i in range(0,len(Tms)):
            Tms[i]=round(Tms[i]-(Tms_Pivot*Constraint[Out_Index][i]),2)
        Constraint=Round(Constraint)
        Base[Out_Index]=Obj_Table[In_Index]
        for i in range(0,len(Results)):
            Z=Z+Results[i]*Base[i]

        print("Pivot = "+str(pivot))
        print("Tms:",Tms)
        print("Results:",Results)
        print("Z = "+str(Z))
        print("Base:",Base)
        Hold.clear()
        iteration+=1
    return Z