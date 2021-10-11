package robotwithlightsensor;

import ch.aplu.robotsim.*;

public class RobotWithLighSensor {

    static {
        RobotContext.setStartDirection(90);
        RobotContext.setStartPosition(250, 10);
        RobotContext.useBackground("sprites/black_white.gif");
    }
//    Making gear global to be used in handlers
    private Gear gear = new Gear();

// initiate a legorobot with lighsensor and gear
    public RobotWithLighSensor() {
        LegoRobot robot = new LegoRobot();
        LightSensor ls = new LightSensor(SensorPort.S3);
        robot.addPart(gear);
        robot.addPart(ls);
        gear.forward();
        while (true) {
            if (ls.getValue() > 500) {
                gear.leftArc(0.1);
            } else {
                gear.rightArc(0.1);
            }
        }
    }

    public static void main(String[] args) {
        new RobotWithLighSensor();
    }

}
