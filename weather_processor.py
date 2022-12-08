import plot_operations
import db_operations

def menu():
    print("[1] Scrape all weather data.")
    print("[2] Update weather data.")
    print("[3] Generate a box plot.")
    print("[4] Generate a line plot.")
    print("[5] Exit.")

menu()
option = int(input("Enter your option: "))
while option != 0:
    if option == 1:
        db_operations.DBOperations().purge_data()
        print("🔃 Starting scraping...")
        db_operations.DBOperations().save_data()
        print("✅ Data successfully added to database!")
        break
    elif option == 2:
        print("🔃 Starting scraping...")
        db_operations.DBOperations().save_update_data()
        print("✅ Data has been successfully updated.")
        break
    elif option == 3:
      plot_operations.PlotOperations().box_plot()
      break
    elif option == 4:
      plot_operations.PlotOperations().line_plot()
      break
    elif option == 5:
      break
    else:
      print("❌ Invalid option. Please try again.")
      menu()
      option = int(input("Enter your option: "))

print("Program has be closed. Thank you 😊")
