import java.util.*;

public class StudentGradeCalculator {
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        int num,j=0;
        
        System.out.print("Enter the number of subjects : ");
        num = sc.nextInt();
        System.out.println();
        
        int marks[] = new int[num];
        String subject_name[] = new String[num];
        for (int i=1; i<=num; i++) {
            System.out.print("Enter the name of Subject "+i+" : ");
            subject_name[j] = sc.next();
            System.out.print("Enter "+subject_name[j]+" marks (outoff 100) : ");
            marks[j] = sc.nextInt();
            System.out.println();
            j++;
        }
        
        int total_marks = 0;
        for (int i = 0; i < num; i++) {
            total_marks += marks[i];
        }
        double avg_percent = ((double)total_marks/num);
        
        System.out.println("Total Marks = "+total_marks);
        System.out.println("Average Percentage = "+avg_percent+"%");
        if (avg_percent <=100 && avg_percent > 90) {
            System.out.println("Grade = A+");
        } else if (avg_percent <=90 && avg_percent > 80) {
            System.out.println("Grade = A");
        } else if (avg_percent <=80 && avg_percent > 70) {
            System.out.println("Grade = B");
        } else if (avg_percent <=70 && avg_percent > 60) {
            System.out.println("Grade = C");
        } else if (avg_percent <=60 && avg_percent > 50) {
            System.out.println("Grade = D");
        } else if (avg_percent <=50 && avg_percent > 40) {
            System.out.println("Grade = E");
        } else {
            System.out.println("Failed");
        }
        sc.close();
    }
}

