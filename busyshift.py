#
#
#
#
#

def show_menu():
    print("========== Shift Predictor =========")
    print("1. Predict Shift Busyness")
    print("2. View Shift History")
    print("3. Record shift History")
    print("4. Run Customer Simulation")
    print("5. View Charts")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    # if choice == '1':
    #     #predict shift busyness
    #     pass
    # elif choice == '2':
    #     #view shift history
    #     pass
    # elif choice == '3':
    #     #record shift history
    #     pass
    # elif choice == '4':
    #     #run customer simulation
    #     pass
    # elif choice == '5':
    #     #view charts
    #     pass
    if choice == '6':
        print("Exiting... Thank you for using Shift Predictor!")
        break
    elif choice in ['1', '2', '3', '4', '5']:
        print(f"Under Construction... Coming soon!")    
    else:
        print("Invalid choice. Please enter a number from 1-6.")

