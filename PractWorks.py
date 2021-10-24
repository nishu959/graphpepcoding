import random
from fractions import Fraction

total_student = random.randint(0, 10000)

fA = Fraction(random.uniform(0, 1)) 
fB = Fraction(random.uniform(0, 1))

fAb = Fraction(random.uniform(0, 1))
fBb = Fraction(random.uniform(0, 1))

fAg = Fraction(1 - fAb)

fBg = Fraction(1 - fBb)

total_girls_in_A = (fA.numerator * fAg.numerator * total_student) // (fA.denominator * fAg.denominator)
total_girls_in_B = (fB.numerator * fBg.numerator * total_student) // (fB.denominator * fBg.denominator)

print("Total student->", total_student)

print("Total girls in A->", total_girls_in_A)
print("Total girls in B->", total_girls_in_B) 

print("Fraction of Class B girls to whole class")

print("In Fraction->", Fraction(total_girls_in_A , total_student))
print("In decimal->", total_girls_in_A / total_student)

print("Fraction of Class A girls to whole class")
print("In Fraction->", Fraction(total_girls_in_B, total_student))
print("In decimal->", total_girls_in_B / total_student)