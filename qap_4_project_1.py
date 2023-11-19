# This is a program to enter and calculate new insurance policy information for its customers.
# Program Author: Steve Sharpe
# Program Date: 2023-11-17

# Import required libraries.

import datetime
import format_values as FF

# Set up program contrants.

BASIC_PREMIUM = 869.00
ADD_CAR_DISC = 0.75
EXTRA_LIABILTY = 130.00
GLASS_COVERAGE = 86.00
LOANER_CAR_COVERAGE = 58.00
HST_RATE = 0.15
MONTHLY_PROC_FEES = 39.99
INV_DATE = datetime.datetime.now()

# Set up program functions.


def InsurPremium(NumCars):
    # Function to calculate the insurance premium based on number of cars.
    if NumCars >= 1:
        InsurPremium = BASIC_PREMIUM + ((BASIC_PREMIUM * ADD_CAR_DISC) * (NumCars - 1))
    return InsurPremium


def ExtraCosts(LiabilityOption, GlassOption, LoanerOption):
    # Function to calculate the extra costs based on the options selected.
    ExtraCosts = 0
    if LiabilityOption == "Y":
        ExtraCosts += EXTRA_LIABILTY
    if GlassOption == "Y":
        ExtraCosts += GLASS_COVERAGE
    if LoanerOption == "Y":
        ExtraCosts += LOANER_CAR_COVERAGE
    return ExtraCosts


def CalcHST(HST_RATE, InsurPremium, ExtraCosts):
    # Function to calculate the HST.
    HST = (InsurPremium + ExtraCosts) * HST_RATE
    return HST


def TotalCost(InsurPremium, ExtraCosts, HST, DownPayment):
    # Function to calculate the total cost including down payment.
    TotalCost = (InsurPremium + ExtraCosts + HST) - DownPayment
    return TotalCost


def MonthlyCost(TotalCost):
    # Function to calculate the monthly cost.
    MonthlyCost = (TotalCost / 8) + MONTHLY_PROC_FEES
    return MonthlyCost


def CalcPayDate(InvDate):
    # Calculate the payment date as the first of each month.

    if InvDate.day > 1:
        if InvDate.month == 12:
            PayDate = datetime.datetime(InvDate.year + 1, 1, 1)
        else:
            PayDate = datetime.datetime(InvDate.year, InvDate.month + 1, 1)
    else:
        PayDate = InvDate

    return PayDate


# Start the main program.

NextPolicyNum = "1944"
CustFirstName = "Michael"
CustLastName = "Myers"
StrAdd = "123 Elm Street"
City = "Haddonfield"
Province = "ON"
PostalCode = "A1A 1A1"
Phone = "416-555-1234"
NumCars = 2
LiabilityOption = "Y"
GlassOption = "Y"
LoanerOption = "Y"
PayOption = "D"
DownPayment = 1000.00
PrevClaimAmtLst = [1000.00, 500.00, 250.00]
PrevClaimDateLst = ["2021-01-01", "2021-02-01", "2021-03-01"]

# while True:
#     NextPolicyNum = "1944"
#     while True:
#         CustFirstName = input("Enter the customer's first name: ").title()
#         if CustFirstName == "":
#             print("You must enter a first name.")
#         else:
#             break

#     while True:
#         CustLastName = input("Enter the customer's last name: ").title()
#         if CustLastName == "":
#             print("You must enter a last name.")
#         else:
#             break

#     while True:
#         StrAdd = input("Enter the customer's street address: ").title()
#         if StrAdd == "":
#             print("You must enter a street address.")
#         else:
#             break

#     while True:
#         City = input("Enter the customer's city: ").title()
#         if City == "":
#             print("You must enter a city.")
#         else:
#             break

#     while True:
#         ProvList = [
#             "NL",
#             "NS",
#             "NB",
#             "PE",
#             "QC",
#             "ON",
#             "MB",
#             "SK",
#             "AB",
#             "BC",
#             "YT",
#             "NT",
#             "NU",
#         ]
#         Province = input("Enter the customer's province (XX): ").upper()
#         if Province == "":
#             print("You must enter a province.")
#         elif len(Province) != 2:
#             print("You must enter a province in XX format.")
#         elif Province not in ProvList:
#             print("You must enter a valid province.")
#         else:
#             break

#     while True:
#         Phone = input("Enter the customer's phone number (999-999-9999): ")
#         if Phone == "":
#             print("You must enter a phone number.")
#         elif len(Phone) != 12:
#             print("You must enter a phone number in 999-999-9999 format.")
#         elif Phone[3] != "-" or Phone[7] != "-":
#             print("You must enter a phone number in 999-999-9999 format.")
#         elif (
#             Phone[0:3].isnumeric() == False
#             or Phone[4:7].isnumeric() == False
#             or Phone[8:12].isnumeric() == False
#         ):
#             print("You must enter a phone number in 999-999-9999 format.")
#         else:
#             break

#     while True:
#         NumCars = input("Enter the number of cars: ")
#         if NumCars == "":
#             print("You must enter a number of cars.")
#         elif NumCars.isalpha() == True:
#             print("You must enter a number.")
#         elif int(NumCars) <= 0:
#             print("Number cannot be less than 1.")
#         else:
#             break

#     while True:
#         LiabilityOption = input(
#             f"Would you like optional extra liability up to $1,000,000 at a cost of {FF.FDollar2( EXTRA_LIABILTY)} (Y or N)?: "
#         ).upper()
#         if LiabilityOption == "":
#             print("You must enter Y for YES or N for NO.")
#         elif LiabilityOption != "Y" and LiabilityOption != "N":
#             print("You must enter Y for YES or N for No.")
#         else:
#             break

#     while True:
#         GlassOption = input(
#             f"Would you like optional glass coverage at a cost of {FF.FDollar2(GLASS_COVERAGE)} (Y or N)?: "
#         ).upper()
#         if GlassOption == "":
#             print("You must enter Y for YES or N for NO.")
#         elif GlassOption != "Y" and GlassOption != "N":
#             print("You must enter Y for YES or N for No.")
#         else:
#             break

#     while True:
#         LoanerOption = input(
#             f"Would you like optional loaner car coverage at a cost of {FF.FDollar2(LOANER_CAR_COVERAGE)} (Y or N)?: "
#         ).upper()
#         if LoanerOption == "":
#             print("You must enter Y for YES or N for NO.")
#         elif LoanerOption != "Y" and LoanerOption != "N":
#             print("You must enter Y for YES or N for No.")
#         else:
#             break

#     while True:
#         PayList = ["F", "M", "D"]
#         PayOption = input(
#             "Would you like to pay in (F)ull, (M)onthly, or monthly with a (D)own payment (F, M, or D)?: "
#         ).upper()
#         if PayOption == "":
#             print("You must enter F for FULL, M for MONTHLY, or D for DOWN.")
#         elif PayOption not in PayList:
#             print("You must enter F for FULL, M for MONTHLY, or D for DOWN.")
#         elif PayOption == "D":
#             DownPayment = float(input("Enter the down payment amount: "))
#             if DownPayment < 0:
#                 print("Down payment cannot be less than 0.")
#             else:
#                 break
#         else:
#             break

#     while True:
#         PrevClaimOption = input(
#             "Is there a previous claim to enter? (Y or N)?: "
#         ).upper()
#         while True:
#             PrevClaimAmtLst = []
#             PrevClaimDateLst = []
#             if PrevClaimOption == "":
#                 print("You must enter Y for YES or N for NO.")
#             elif PrevClaimOption != "Y" and PrevClaimOption != "N":
#                 print("You must enter Y for YES or N for No.")
#             elif PrevClaimOption == "Y":
#                 PrevClaimAmt = float(input("Enter the previous claim amount: "))
#                 PrevClaimDate = input("Enter the previous claim date (YYYY-MM-DD): ")
#                 PrevClaimAmtLst.append(PrevClaimAmt)
#                 PrevClaimDateLst.append(PrevClaimDate)
#                 PrevClaimOption = input(
#                     "Is there another previous claim to enter? (Y or N)?: "
#                 ).upper()
#                 if PrevClaimOption == "":
#                     print("You must enter Y for YES or N for NO.")
#                 elif PrevClaimOption != "Y" and PrevClaimOption != "N":
#                     print("You must enter Y for YES or N for No.")
#                 if PrevClaimOption == "Y":
#                     continue
#                 elif PrevClaimOption == "N":
#                     break
#             elif PrevClaimOption == "N":
#                 break
#             break
#         break
#     break

print()
print("***********************************************************")
print("**                                                       **")
print("**              ONE STOP INSURANCE COMPANY               **")
print("**                                                       **")
print("***********************************************************")
print(
    f"**  Policy Number: {NextPolicyNum}  ****  Invoice Date: {FF.FDateS(INV_DATE)}  **"
)
print("***********************************************************")
CustDSP = f"{CustFirstName} {CustLastName}"
print(f"**  Customer:  {CustDSP}{''.rjust(24 - len(CustDSP))} *Selections*     **")
print(f"**  Address:   {StrAdd}{'# of Cars:'.rjust(35 - len(StrAdd))} {NumCars}     **")
CityProvDSP = f"{City}, {Province}"
print(
    f"**             {CityProvDSP}{'Liability:'.rjust(35 - len(CityProvDSP))} {LiabilityOption}     **"
)
print(
    f"**             {PostalCode}{'Glass:    '.rjust(35 - len(PostalCode))} {GlassOption}     **"
)
print(
    f"**  Phone:     {Phone}{'Loaner:   '.rjust(35 - len(Phone))} {LoanerOption}     **"
)
print("***********************************************************")
while True:
    if PayOption == "F":
        print(f"**          You have selected to pay in FULL             **")
        break
    elif PayOption == "M":
        print(f"**          You have selected to pay MONTHLY             **")
        break
    elif PayOption == "D":
        print(
            f"**           You have selected to pay MONTHLY.{' ' * (14 - len('You have selected to pay MONTHLY.'))}           **"
        )
        down_payment_str = FF.FDollar2(DownPayment)
        print(
            f"**            Your down payment is {down_payment_str}.{' ' * (13 - len(down_payment_str))}        **"
        )
        break

print("***********************************************************")
print(
    f"**             Insurance Premium:  {FF.FDollar2(InsurPremium(NumCars))}{''.rjust(21 - len(FF.FDollar2(InsurPremium(NumCars))))} **"
)
print(
    f"**             Extra Costs:          {FF.FDollar2(ExtraCosts(LiabilityOption, GlassOption, LoanerOption))}{''.rjust(19 - len(FF.FDollar2(ExtraCosts(LiabilityOption, GlassOption, LoanerOption))))} **"
)

print(
    f"**             Subtotal:           {FF.FDollar2(InsurPremium(NumCars) + ExtraCosts(LiabilityOption, GlassOption, LoanerOption))}{''.rjust(21 - len(FF.FDollar2(InsurPremium(NumCars) + ExtraCosts(LiabilityOption, GlassOption, LoanerOption))))} **"
)

subtitle_cost = InsurPremium(NumCars) + ExtraCosts(
    LiabilityOption, GlassOption, LoanerOption
)
subtitle_cost_str = FF.FDollar2(subtitle_cost)
padding = " " * (21 - len(subtitle_cost_str))

print(f"**             Subtitle:           {subtitle_cost_str}{padding} **")


print(f"Payment Option: {PayOption}")
print(f"Down Payment: {FF.FDollar2(DownPayment)}")
print(f"Previous Claims: {PrevClaimAmtLst}")
print(f"Previous Claim Dates: {PrevClaimDateLst}")
