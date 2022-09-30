
import java.io.*;
import java.util.*;

class AMSA {

    public static int findCharCount(String stream, char XE, int random, int n) {
        int countOccurance = 0;
        for (int i = random; i < n; i++) {
            if (stream.charAt(i) == XE) {
                countOccurance++;//System.out.println(countOccurance+" "+i);
            }
        }
        return countOccurance;
    }

    public static int estimateValue(int XV1, int n) {
        int ExpValue;
        ExpValue = n * (2 * XV1 - 1);
        return ExpValue;
    }

    public static void main(String args[]) {
        int n = 15;
        String stream = "abcbdacdabdcaab";
        int random1 = 3, random2 = 8, random3 = 13;
        char XE1, XE2, XE3;
        int XV1, XV2, XV3;
        int ExpValuXE1, ExpValuXE2, ExpValuXE3;
        int apprSecondMomentValue;
        XE1 = stream.charAt(random1 - 1);
        XE2 = stream.charAt(random2 - 1);
        XE3 = stream.charAt(random3 - 1);
//System.out.println(XE1+" "+XE2+" "+XE3);
        XV1 = findCharCount(stream, XE1, random1 - 1, n);
        XV2 = findCharCount(stream, XE2, random2 - 1, n);
        XV3 = findCharCount(stream, XE3, random3 - 1, n);
        System.out.println(XE1 + "=" + XV1 + " " + XE2 + "=" + XV2 + " " + XE3 + "=" + XV3);
        ExpValuXE1 = estimateValue(XV1, n);
        ExpValuXE2 = estimateValue(XV2, n);
        ExpValuXE3 = estimateValue(XV3, n);
        System.out.println("Expected value for " + XE1 + " is :: " + ExpValuXE1);
        System.out.println("Expected value for " + XE2 + " is::  {} " + ExpValuXE2);
        System.out.println("Expected value for " + XE3 + " is :: " +ExpValuXE3);
        apprSecondMomentValue=(ExpValuXE1+ExpValuXE2+ExpValuXE3)/3;
        
        System.out.println("Approximate Second moment value using Alon-Matias-Szegedy is :: "+apprSecondMomentValue);
    }}
