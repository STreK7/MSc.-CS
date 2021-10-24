package robotwithobstacle;

import ch.aplu.robotsim.*;

public class RobotWithObstacle {
//Make a box obstacle

    static {
        RobotContext.useObstacle("sprites/bar0.gif", 250, 200);
        RobotContext.useObstacle("sprites/bar1.gif", 400, 250);
        RobotContext.useObstacle("sprites/bar2.gif", 250, 400);
        RobotContext.useObstacle("sprites/bar3.gif", 100, 250);
    }
// initiate a legorobot with touchsensor and gear

    public RobotWithObstacle() {
        LegoRobot robot = new LegoRobot();
        Gear gear = new Gear();
        TouchSensor ts = new TouchSensor(SensorPort.S3);
        robot.addPart(gear);
        robot.addPart(ts);
        gear.setSpeed(30);
        gear.forward();

        while (true) {
            if (ts.isPressed()) {
                gear.backward(1200);
                gear.left(750);
                gear.forward();
            }
        }
    }

    public static void main(String[] args) {
        new RobotWithObstacle();
    }

}
