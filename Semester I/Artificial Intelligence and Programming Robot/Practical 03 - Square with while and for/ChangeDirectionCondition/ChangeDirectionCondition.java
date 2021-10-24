/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package changecirectioncondition;

import ch.aplu.robotsim.*;

public class ChangeDirectionCondition {

    static {
        RobotContext.setStartDirection(90);
        RobotContext.setStartPosition(100, 100);
    }

    public ChangeDirectionCondition() {

        LegoRobot robot = new LegoRobot();
        Gear gear = new Gear();
        robot.addPart(gear);
        gear.forward();
        gear.setSpeed(50);
        while (true) {
            if (robot.isRightHit()) {
                gear.left(540);
            }
            if (robot.isLeftHit()) {
                gear.right(540);
            }
            if (robot.isDownHit()) {
                gear.backward();
            }
            if (robot.isUpHit()) {
                gear.forward();
            }

        }
    }

    public static void main(String[] args) {
        // TODO code application logic here
        new ChangeDirectionCondition();
    }
}
