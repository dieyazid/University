from Code.simplex import *
import pyfiglet

##Variables Declaration
Objective_Function,Constraints,Results,Constraint_Type= ([] for i in range(4))
Variables_Number=0;Constraints_Number=0

##Printing Banner
ascii_banner = pyfiglet.figlet_format("Simplex Calculator")
print(ascii_banner)

##Get the Number of Variables and Constraints
Variables_Number=Get_Data("How many variables are there?\n",2,20)
Constraints_Number=Get_Data("How many constraints are there?\n",1,20)

##Fill Arrays with user inputs
Objective_Function,Constraints,Results,Constraint_Type=Fill_Tables(Variables_Number,Constraints_Number,Objective_Function,Constraints,Results,Constraint_Type)

##Show Data to user
Show_Data(Variables_Number,Objective_Function,Constraints,Results,Constraint_Type)

##Prepare Arrays for the calculation part
Constraints,Objective_Function=Preliminary_stage(Variables_Number,Objective_Function,Constraints,Results,Constraint_Type)

##Convert Arrays values to Integers
Objective_Function=ToInt(Objective_Function)
Constraint=ToIntMatrix(Constraints)
Results=ToInt(Results)

##Calculation + Printing the result
print(f"Max Z = {round(calculation(Constraint,Results,Variables_Number+1,Objective_Function),2)}")
