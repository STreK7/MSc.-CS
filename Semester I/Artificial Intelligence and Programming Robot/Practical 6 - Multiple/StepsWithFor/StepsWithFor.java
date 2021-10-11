/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package stepswithfor;

import ch.aplu.robotsim.*;

public class StepsWithFor {

    static {
        RobotContext.setStartDirection(90);
        RobotContext.setStartPosition(100, 100);
    }

    public StepsWithFor() {

        LegoRobot robot = new LegoRobot();
        Gear gear = new Gear();
        robot.addPart(gear);
        gear.setSpeed(100);
        while (true) {
            gear.forward(1000);
            gear.left(90);
        }
    }

    public static void main(String[] args) {
        // TODO code application logic here
        new StepsWithFor();
    }
}
