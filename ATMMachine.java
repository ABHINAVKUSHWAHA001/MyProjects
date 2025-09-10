import java.util.*;

class ATM {
    float Balance = 0;  // initial balance
    int PIN = 6391;

    // Method to check PIN
    public void checkpin() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your PIN: ");
        int enteredPin = sc.nextInt();

        if (enteredPin == PIN) {
            menu();
        } else {
            System.out.println(" Invalid PIN. Try again.");
            checkpin();   // ask again until correct
        }
    }

    // Menu
    void menu() {
        System.out.println("\n====(*-*) ATM Menu (*-*)=====");
        System.out.println("1. Check Balance");
        System.out.println("2. Withdraw Money");
        System.out.println("3. Deposit Money");
        System.out.println("4. EXIT");
        System.out.print("Enter Your Choice: ");

        Scanner sc = new Scanner(System.in);
        int opt = sc.nextInt();

        switch (opt) {
            case 1:
                checkBalance();
                break;
            case 2:
                withdrawMoney();
                break;
            case 3:
                depositMoney();
                break;
            case 4:
                System.out.println(" Thank you! Visit again.");
                return;
            default:
                System.out.println(" Invalid Choice! Try again.");
                menu();
        }
    }

    // Check Balance
    void checkBalance() {
        System.out.println(" Total Balance: " + Balance);
        menu();
    }

    // Withdraw
    void withdrawMoney() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Amount to Withdraw: ");
        float amount = sc.nextFloat();

        if (amount > Balance) {
            System.out.println(" Insufficient Balance!");
        } else {
            Balance -= amount;
            System.out.println(" Withdrawal Successful!");
        }
        menu();
    }

    // Deposit
    void depositMoney() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Amount to Deposit: ");
        float amount = sc.nextFloat();

        Balance += amount;
        System.out.println("Deposit Successful!");
        menu();
    }
}

// Main class
class ATMMachine {
    public static void main(String[] args) {
        ATM obj = new ATM();
        obj.checkpin();
    }
}
