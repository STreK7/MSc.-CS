package pathfollowingrobot;

import ch.aplu.robotsim.*;
import ch.aplu.jgamegrid.*;
import java.awt.*;

public class PathFollowingRobot {

    static {
        RobotContext.setStartDirection(10);
    }

    public PathFollowingRobot() {

        LegoRobot robot = new LegoRobot();
        Gear gear = new Gear();
        LightSensor ls1 = new LightSensor(SensorPort.S1);
        LightSensor ls2 = new LightSensor(SensorPort.S2);

//      Adding Parts
        robot.addPart(gear);
        robot.addPart(ls1);
        robot.addPart(ls2);
//      initial movement
        gear.forward();

//      Trigger Level
        int intensity = 500;
//      turning arch
        double arch = 0.1;

        while (true) {
//          get values of light sensors
            int ls1v = ls1.getValue();
            int ls2v = ls2.getValue();

//          Driver Logic for movement
//          if lighsensor1 and lighsensor2 are on track move forward
            if (ls1v < intensity && ls2v < intensity) {
                gear.forward();
            }
//          if lighsensor1 is on track and lighsensor2 is not on track turn right by arch
            if (ls1v < intensity && ls2v > intensity) {
                gear.rightArc(arch);
            }
//          if  lighsensor1 is not on track and lighsensor2 is on track turn left by arch            
            if (ls1v > intensity && ls2v < intensity) {
                gear.leftArc(arch);
            }
//          if lighsensor1 and lighsensor2 are not on track move backward
            if (ls1v > intensity && ls2v > intensity) {
                gear.backward();
            }
        }
    }

//    Creating a track
    private static void _init(GameGrid gg) {
        GGBackground bg = gg.getBg();
//    Tracks
        bg.setPaintColor(Color.black);
        bg.fillArc(new Point(250, 150), 120, 0, 360);
        bg.fillArc(new Point(250, 350), 120, 0, 360);
        bg.fillArc(new Point(150, 250), 120, 0, 360);
        bg.fillArc(new Point(350, 250), 120, 0, 360);
//    Gaps
        bg.setPaintColor(Color.white);
        bg.fillArc(new Point(250, 350), 60, 0, 360);
        bg.fillArc(new Point(250, 150), 60, 0, 360);
        bg.fillArc(new Point(150, 250), 60, 0, 360);
        bg.fillArc(new Point(350, 250), 60, 0, 360);
    }

    public static void main(String[] args) {
        new PathFollowingRobot();
    }

}
