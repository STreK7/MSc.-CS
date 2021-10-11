/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package movewithmotor;

/**
 *
 * @author STreK
 */
import ch.aplu.robotsim.*;
public class MoveWithMotor {
    public MoveWithMotor(){
 
 LegoRobot robot = new LegoRobot();
    Motor motA = new Motor(MotorPort.A);
    Motor motB = new Motor(MotorPort.B);
    robot.addPart(motA);
    robot.addPart(motB);

    motA.forward();
    motB.forward();
    Tools.delay(2000);

    motA.stop();
    Tools.delay(2000);

    motB.stop();
    Tools.delay(2000);

    motA.backward();
    motB.forward();
    Tools.delay(2000);

    motB.backward();
    Tools.delay(2000);

    robot.exit();
  }
    
    public static void main(String[] args) {
        // TODO code application logic here
         new MoveWithMotor();
    }
    
}
