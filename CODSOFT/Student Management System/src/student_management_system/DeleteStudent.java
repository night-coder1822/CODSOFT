package student_management_system;

import javax.swing.*;

import net.proteanit.sql.DbUtils;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.ResultSet;

public class DeleteStudent extends JFrame implements ActionListener{

    JTable table;
    Choice crollno;
    JButton delete;

    DeleteStudent() {
        setSize(1100,650);
        setLocation(150,40);
        setLayout(null);

        JLabel heading = new JLabel("Delete Student Details");
        heading.setBounds(280,20,500,50);
        heading.setFont(new Font("Tahoma", Font.PLAIN, 35));
        add(heading);
        
        JLabel lblrollnumber = new JLabel("Select Roll Number -");
        lblrollnumber.setBounds(50,100,250,25);
        lblrollnumber.setFont(new Font("Tahoma", Font.PLAIN, 25));
        add(lblrollnumber);
        
        crollno = new Choice();
        crollno.setBounds(300,100,200,28);
        add(crollno);
        
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from STUDENT");
            while (rs.next()) {
                crollno.add(rs.getString("rollno"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        table = new JTable();
        
        try {
            Conn c = new Conn();
            ResultSet rs = c.s.executeQuery("select * from student");
            table.setModel(DbUtils.resultSetToTableModel(rs));
        } catch (Exception e) {
            e.printStackTrace();
        }
        
        JScrollPane jsp = new JScrollPane(table);
        jsp.setBounds(0, 200, 1100, 600);
        add(jsp);
        
        delete = new JButton("Delete");
        delete.setBounds(600, 100, 80, 30);
        delete.addActionListener(this);
        add(delete);
        

        setVisible(true);
    }

    public void actionPerformed (ActionEvent ae) {
        if (ae.getSource() == delete) {
            String query = "delete * from student where rollno = '"+crollno.getSelectedItem()+"'";
            try {
                Conn c = new Conn();
                ResultSet rs = c.s.executeQuery(query);
                table.setModel(DbUtils.resultSetToTableModel(rs));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    public static void main(String agrs[]) {
        new DeleteStudent();
    }
}
