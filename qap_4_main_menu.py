import runpy

while True:
    print()
    print("**  --------------------------  **")
    print("**  ONE STOP INSURANCE COMPANY  **")
    print("**     'We got you, baby!'      **")
    print("**  --------------------------  **")
    print("**     Make Your Selection      **")
    print("**                              **")
    print("**       (N)ew Policy           **")
    print("**       (M)onthly Sales        **")
    print("**       (Q)uit                 **")
    print("**  --------------------------  **")
    print()

    while True:
        Choice = input("Make Your Selection: ").upper()
        if Choice == "N" or Choice == "M" or Choice == "Q":
            break
        else:
            print("Invalid choice. Try again.")

    if Choice == "N":
        runpy.run_path("QAP 4 Files ss/qap_4_new_policy.py")
    elif Choice == "M":
        runpy.run_path("QAP 4 Files ss/qap_4_monthly_sales.py")
    elif Choice == "Q":
        print()
        print(" Until next time, 'We got you, baby'!")
        print()
        break
