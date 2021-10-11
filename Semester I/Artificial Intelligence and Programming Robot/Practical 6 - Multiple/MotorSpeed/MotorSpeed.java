/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package motorspeed;

/**
 *
 * @author STreK
 */
import ch.aplu.robotsim.*;

public class MotorSpeed {

    public MotorSpeed() {

        LegoRobot robot = new LegoRobot();
        Gear gear = new Gear();
        robot.addPart(gear);
        int speed = 0;
        while (true) {
            for (int i = 1; i < 6; i++) {
                switch (i) {
                    case 1:
                        speed = 10;
                        break;
                    case 2:
                        speed = 25;
                        break;
                    case 3:
                        speed = 50;
                        break;
                    case 4:
                        speed = 75;
                        break;
                    case 5:
                        speed = 100;
                        break;
                    default:
                        speed = 0;
                        break;
                }
                gear.setSpeed(speed);
                gear.forward();
                Tools.delay(1000);
                gear.left((int)(6000/speed));
            }
        }
  
    }

    public static void main(String[] args) {
        // TODO code application logic here
        new MotorSpeed();
    }

}
