
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
        for (int i = 1; i <= 4; i++) {
            gear.forward(1000);
            gear.left(90);
        }
        Tools.delay(2000);
        robot.exit();

    }

    public static void main(String[] args) {
        new StepsWithFor();
    }
}
