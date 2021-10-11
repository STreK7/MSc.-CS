/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package robotwithgear;

import ch.aplu.robotsim.*;

public class RobotWithGear {
    public RobotWithGear(){
 
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
        new RobotWithGear();
     }
}
