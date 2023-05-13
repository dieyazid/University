from Code.simplex import *
import pyfiglet

##Variables Declaration
# Objective_Function=[40,30]
# Constraints=[1,2,2,1]
# Results=[12,16]
# Constraint_Type=['<=','<=']
# Variables_Number=2
# Constraints_Number=2

# Objective_Function=[30000,40000]
# Constraints=[2,1,1,2,0,1]
# Results=[800,700,300]
# Constraint_Type=['<=','<=','<=']
# Variables_Number=2
# Constraints_Number=3

Objective_Function=[2,1]
Constraints=[1,-1,2,-1]
Results=[10,40]
Constraint_Type=['<=','<=']
Variables_Number=2
Constraints_Number=2

##Printing Banner
ascii_banner = pyfiglet.figlet_format("Simplex Calculator")
print(ascii_banner)

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

