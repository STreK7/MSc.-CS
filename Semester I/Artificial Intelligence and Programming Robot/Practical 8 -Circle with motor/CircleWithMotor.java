/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package circlewithmotor;
/**
 *
 * @author STreK
 */
import ch.aplu.robotsim.*;
public class CircleWithMotor {
    public CircleWithMotor(){
 
 LegoRobot robot = new LegoRobot();
    Motor mot1 = new Motor(MotorPort.A);
    Motor mot2 = new Motor(MotorPort.B);
    robot.addPart(mot1);
    robot.addPart(mot2);

    while(true){
    mot1.forward();
    mot1.setSpeed(100);
    mot2.forward();
    mot2.setSpeed(50);
    }
  }
    
    public static void main(String[] args) {
         new CircleWithMotor();
    }
    
}
