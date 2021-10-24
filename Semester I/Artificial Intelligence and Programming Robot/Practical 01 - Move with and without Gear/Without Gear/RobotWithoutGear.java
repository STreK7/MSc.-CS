
package robotwithoutgear;

import ch.aplu.robotsim.*;

public class RobotWithoutGear {
    
    public RobotWithoutGear(){      
        
        TurtleRobot robot=new TurtleRobot();
        robot.forward(100);
        robot.left(45);
        robot.forward(100);
        robot.right(90);
        robot.backward(100);
        robot.exit();
            }
    

     public static void main(String[] args) {
        // TODO code application logic here
        new RobotWithoutGear();
       
    }
    
}
