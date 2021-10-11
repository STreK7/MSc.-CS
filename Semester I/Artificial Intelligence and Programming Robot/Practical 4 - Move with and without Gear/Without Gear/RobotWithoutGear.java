
package robotwithoutgear;

import ch.aplu.robotsim.*;

public class RobotWithoutGear {
    
    public RobotWithoutGear(){
 
            LegoRobot robot = new LegoRobot();
            Gear gear = new Gear();
            robot.addPart(gear);
            
            gear.forward(2000);
            gear.setSpeed(30);
            gear.left(200);
            gear.forward(2000);
            gear.right(200);
            gear.forward();
            Tools.delay(20);
            robot.exit();
            }
    

     public static void main(String[] args) {
        // TODO code application logic here
       
    }
    
}
