import java.util.Scanner;

class UserBankAcc 
{
    private double balance;
    public UserBankAcc (double balance) {
        this.balance = balance;
    }
    // Method to Print the balance of User Bank Account
    public void checkBalance() {
        System.out.println("Balance = "+balance);
        return;
    }

    // Method to withdraw amount from User Bank Account
    public void withdraw (double withdrawAmt) {
        
        if (withdrawAmt > 0 && withdrawAmt <= balance){
            balance -= withdrawAmt;
            System.out.println("Amount Withdraw\n");
        } else {
            System.out.println("Insufficient Balance!!\n");
        } return;
    }

    // Method to Deposit amount in User Bank Account
    public void deposit (double depo) {
        balance += depo;
        System.out.println("Amount Deposited Successfully!!\n");
        return ;
    }
}

public class AtmClass 
{
    public static void main(String agrs[]) 
    {
        UserBankAcc uba = new UserBankAcc(10000); // UserBankAcc class object
        int num,chance=0;
        Scanner sc = new Scanner(System.in);

        while (chance < 3) {
            System.out.print("Enter Username : "); // Username = root
            String username = sc.next();
    
            System.out.print("Enter password : "); // Password = 5586
            int pwd = sc.nextInt();

            if (username.equals("root") && (pwd == 5586)) {
                System.out.println("\nWelcom to ATM ");
    
                do {
                    System.out.println("1. Withdram\n2. Deposite\n3. Check Balance\n4. Exit\n");
                    System.out.print("Enter Number : ");
                    num = sc.nextInt();
                    switch (num) {
                        case 1 : {
                            System.out.print("\nEnter Withdraw Amount : ");
                            int amt = sc.nextInt();
                            uba.withdraw(amt);
                        } break;
                        case 2 : {
                            System.out.print("\nEnter Deposit Amount : ");
                            int depo = sc.nextInt();
                            uba.deposit(depo);
                        } break;
                        case 3 : uba.checkBalance();
                            break;
                        default:
                            break;
                    }
                } while (num !=4);
            } else {
                chance++;
                System.out.println("\nInavlid Credentials!!");
            } 
            if (chance == 3) {
                System.out.println("System Locked!!");
            }
        }
        sc.close();
    }
}