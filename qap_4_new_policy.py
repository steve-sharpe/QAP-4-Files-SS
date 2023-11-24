# This is a program to enter and calculate new insurance policy information for its customers.
# Program Author: Steve Sharpe
# Program Date: 2023-11-17

# Import required libraries.

import datetime
import format_values as FF

# Set up program constants.

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


def PreCost(InsurPremium, ExtraCosts, HST):
    # Function to calculate the total cost wity down payment.
    PreCost = InsurPremium + ExtraCosts + HST
    return PreCost


def TotalCost(InsurPremium, ExtraCosts, HST, Deposit):
    # Function to calculate the total cost wity down payment.
    TotalCost = (InsurPremium + ExtraCosts + HST) - Deposit
    return TotalCost


def MonthlyCost(TotalCost):
    # Function to calculate the monthly cost.
    MonthlyCost = (TotalCost + MONTHLY_PROC_FEES) / 8
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

print()


# NextPolicyNum = "1944"
# CustFirstName = "Sam"
# CustLastName = "Myers"
# StrAdd = "123 1st Ave"
# City = "Rio"
# Province = "ON"
# PostalCode = "A1A 1A1"
# Phone = "416-555-1234"
# NumCars = 2
# LiabilityOption = "Y"
# GlassOption = "Y"
# LoanerOption = "Y"
# PayOption = "D"
# Deposit = 1500.00
# PrevClaimAmtLst = [1000.00, 500.00, 250.00]
# PrevClaimDateLst = ["2021-01-01", "2021-02-01", "2021-03-01"]

while True:
    NextPolicyNum = "1944"
    while True:
        CustFirstName = input("Enter the customer's first name: ").title()
        if CustFirstName == "":
            print("You must enter a first name.")
        else:
            break

    while True:
        CustLastName = input("Enter the customer's last name: ").title()
        if CustLastName == "":
            print("You must enter a last name.")
        else:
            break

    while True:
        StrAdd = input("Enter the customer's street address: ").title()
        if StrAdd == "":
            print("You must enter a street address.")
        else:
            break

    while True:
        City = input("Enter the customer's city: ").title()
        if City == "":
            print("You must enter a city.")
        else:
            break

    while True:
        ProvList = [
            "NL",
            "NS",
            "NB",
            "PE",
            "QC",
            "ON",
            "MB",
            "SK",
            "AB",
            "BC",
            "YT",
            "NT",
            "NU",
        ]
        Province = input("Enter the customer's province (XX): ").upper()
        if Province == "":
            print("You must enter a province.")
        elif len(Province) != 2:
            print("You must enter a province in XX format.")
        elif Province not in ProvList:
            print("You must enter a valid province.")
        else:
            break

    while True:
        PostalCode = input("Enter the customer's postal code (X9X 9X9): ").upper()
        if PostalCode == "":
            print("You must enter a postal code.")
        elif len(PostalCode) != 7:
            print("You must enter a postal code in X9X 9X9 format.")
        elif PostalCode[3] != " ":
            print("You must enter a postal code in X9X 9X9 format.")
        elif (
            PostalCode[0].isalpha() == False
            or PostalCode[2].isalpha() == False
            or PostalCode[5].isalpha() == False
        ):
            print("You must enter a postal code in X9X 9X9 format.")
        elif (
            PostalCode[1].isnumeric() == False
            or PostalCode[4].isnumeric() == False
            or PostalCode[6].isnumeric() == False
        ):
            print("You must enter a postal code in X9X 9X9 format.")
        else:
            break

    while True:
        Phone = input("Enter the customer's phone number (999-999-9999): ")
        if Phone == "":
            print("You must enter a phone number.")
        elif len(Phone) != 12:
            print("You must enter a phone number in 999-999-9999 format.")
        elif Phone[3] != "-" or Phone[7] != "-":
            print("You must enter a phone number in 999-999-9999 format.")
        elif (
            Phone[0:3].isnumeric() == False
            or Phone[4:7].isnumeric() == False
            or Phone[8:12].isnumeric() == False
        ):
            print("You must enter a phone number in 999-999-9999 format.")
        else:
            break

    while True:
        NumCars = int(input("Enter the number of cars: "))
        if NumCars == "":
            print("You must enter a number of cars.")
        elif int(NumCars) > 5:
            print("Number cannot be greater than 5.")
        elif int(NumCars) <= 0:
            print("Number cannot be less than 1.")
        else:
            break

    while True:
        LiabilityOption = input(
            f"Would you like optional extra liability up to $1,000,000 at a cost of {FF.FDollar2( EXTRA_LIABILTY)} (Y or N)?: "
        ).upper()
        if LiabilityOption == "":
            print("You must enter Y for YES or N for NO.")
        elif LiabilityOption != "Y" and LiabilityOption != "N":
            print("You must enter Y for YES or N for No.")
        else:
            break

    while True:
        GlassOption = input(
            f"Would you like optional glass coverage at a cost of {FF.FDollar2(GLASS_COVERAGE)} (Y or N)?: "
        ).upper()
        if GlassOption == "":
            print("You must enter Y for YES or N for NO.")
        elif GlassOption != "Y" and GlassOption != "N":
            print("You must enter Y for YES or N for No.")
        else:
            break

    while True:
        LoanerOption = input(
            f"Would you like optional loaner car coverage at a cost of {FF.FDollar2(LOANER_CAR_COVERAGE)} (Y or N)?: "
        ).upper()
        if LoanerOption == "":
            print("You must enter Y for YES or N for NO.")
        elif LoanerOption != "Y" and LoanerOption != "N":
            print("You must enter Y for YES or N for No.")
        else:
            break

    while True:
        PayList = ["F", "M", "D"]
        PayOption = input(
            "Would you like to pay in (F)ull, (M)onthly, or monthly with a (D)eposit (F, M, or D)?: "
        ).upper()
        if PayOption == "":
            print("You must enter F for FULL, M for MONTHLY, or D for DEPOSIT.")
        elif PayOption not in PayList:
            print("You must enter F for FULL, M for MONTHLY, or D for DEPOSIT.")
        elif PayOption == "D":
            Deposit = float(input("Enter the deposit amount: "))
            if Deposit < 0:
                print("Deposit cannot be less than 0.")
            else:
                break
        else:
            break

    while True:
        PrevClaimOption = input(
            "Is there a previous claim to enter? (Y or N)?: "
        ).upper()
        while True:
            PrevClaimAmtLst = []
            PrevClaimDateLst = []
            if PrevClaimOption == "":
                print("You must enter Y for YES or N for NO.")
            elif PrevClaimOption != "Y" and PrevClaimOption != "N":
                print("You must enter Y for YES or N for No.")
            elif PrevClaimOption == "Y":
                PrevClaimAmt = input("Enter the previous claim amount in dollars: ")
                PrevClaimDate = input("Enter the previous claim date (YYYY-MM-DD): ")
                PrevClaimAmtLst.append(PrevClaimAmt)
                PrevClaimDateLst.append(PrevClaimDate)
                PrevClaimOption = input(
                    "Is there another previous claim to enter? (Y or N)?: "
                ).upper()
                if PrevClaimOption == "":
                    print("You must enter Y for YES or N for NO.")
                elif PrevClaimOption != "Y" and PrevClaimOption != "N":
                    print("You must enter Y for YES or N for No.")
                if PrevClaimOption == "Y":
                    continue
                elif PrevClaimOption == "N":
                    break
            elif PrevClaimOption == "N":
                break
            break
        break
    break

print()
print("**  --------------------------  **")
print("**                              **")
print("**  ONE STOP INSURANCE COMPANY  **")
print("**     'We got you, baby!'      **")
print(f"**      Date: {FF.FDateS(INV_DATE):<10}        **")
print(f"**        Pol No: {NextPolicyNum:<10}    **")
print("**                              **")
print("**  --------------------------  **")
CustDSP = f"{CustFirstName} {CustLastName}"
print(f"**  Cust:  {CustDSP:<19}  **")
print(f"**  Addr:  {StrAdd:<19}  **")
CityProvDSP = f"{City}, {Province}"
print(f"**         {CityProvDSP:<19}  **")
print(f"**         {PostalCode:<19}  **")
print(f"**  Phone: {Phone:<19}  **")
print("**  --------------------------  **")

print(f"**  Number of Cars: {NumCars:>10}  **")
CityProvDSP = f"{City}, {Province}"
print(f"**  Liability: {LiabilityOption:>15}  **")
print(f"**  Glass Option?: {GlassOption:>11}  **")
print(f"**  Loaner: {LoanerOption:>18}  **")
print("**  --------------------------  **")

while True:
    if PayOption == "F":
        print(f"**          PAY IN FULL         **")
        break
    elif PayOption == "M":
        print(f"**   PAY MONTHLY, NO DEPOSIT    **")
        break
    elif PayOption == "D":
        print(f"**   PAY MONTHLY WITH DEPOSIT   **")
        down_payment_str = FF.FDollar2(Deposit)
        print(f"**      DEPOSIT: {down_payment_str:>9}      **")
        break

print("**  --------------------------  **")
insurance_premium = InsurPremium(NumCars)
insurance_premium_str = FF.FDollar2(insurance_premium)
print(f"**  Premium: {insurance_premium_str:>17}  **")

extra_costs = ExtraCosts(LiabilityOption, GlassOption, LoanerOption)
extra_costs_str = FF.FDollar2(extra_costs)
print(f"**  Extra Costs: {extra_costs_str:>13}  **")

subtotal = InsurPremium(NumCars) + ExtraCosts(
    LiabilityOption, GlassOption, LoanerOption
)
subtotal_str = FF.FDollar2(subtotal)
print(f"**  Service Total: {subtotal_str:>11}  **")

hst = CalcHST(
    HST_RATE,
    InsurPremium(NumCars),
    ExtraCosts(LiabilityOption, GlassOption, LoanerOption),
)
hst_str = FF.FDollar2(hst)
print(f"**  HST: {hst_str:>21}  **")

pre_cost = PreCost(
    InsurPremium(NumCars), ExtraCosts(LiabilityOption, GlassOption, LoanerOption), hst
)
pre_cost_str = FF.FDollar2(pre_cost)
print(f"**  Sub-Total: {pre_cost_str:>15}  **")

print("**  --------------------------  **")

total_cost = TotalCost(
    InsurPremium(NumCars),
    ExtraCosts(LiabilityOption, GlassOption, LoanerOption),
    hst,
    Deposit,
)

deposit_str = FF.FDollar2(Deposit)
print(f"**  Deposit: {deposit_str:>17}  **")

total_cost_str = FF.FDollar2(total_cost)
print(f"**  Final Total: {total_cost_str:>13}  **")

print("**  --------------------------  **")

monthly_cost = MonthlyCost(total_cost)
monthly_cost_str = FF.FDollar2(monthly_cost)
print(f"**  Monthly Payment: {monthly_cost_str:>9}  **")

print("**  --------------------------  **")

pay_date = CalcPayDate(INV_DATE)
print(f"**  First Payment: {FF.FDateS(pay_date):>11}  **")
print("**  --------------------------  **")

print(f"**       Previous Claims:       **")
for i in range(len(PrevClaimAmtLst)):
    claim_date_str = PrevClaimDateLst[i]
    claim_amt_str = FF.FDollar2(PrevClaimAmtLst[i])
    print(f"**    {claim_date_str} - {claim_amt_str:>9}    **")

print("**  --------------------------  **")
print()
