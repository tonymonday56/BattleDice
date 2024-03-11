scorecard.py
class Scoring:
    def __init__(self, printScoreCard() {
        print();
        System.out.prin("*********************************");
        print("*      Yahtzee Score Card       *");
        print("*                               *");
        System.out.print("*  Ones:\t\t");
        if (ones == -1) System.out.print("__");
        else System.out.print(ones);
        print("\t*");
        System.out.print("*  Twos:\t\t");
        if (twos == -1) System.out.print("__");
        else System.out.print(twos);
        print("\t*");
        System.out.print("*  Threes:\t\t");
        if (threes == -1) System.out.print("__");
        else System.out.print(threes);
        print("\t*");
        System.out.print("*  Fours:\t\t");
        if (fours == -1) System.out.print("__");
        else System.out.print(fours);
        print("\t*");
        System.out.print("*  Fives:\t\t");
        if (fives == -1) System.out.print("__");
        else System.out.print(fives);
        print("\t*");
        System.out.print("*  Sixes:\t\t");
        if (sixes == -1) System.out.print("__");
        else System.out.print(sixes);
        print("\t*");
        print("*\t\t\t\t*");
        System.out.print("*  Upper Bonus:\t\t");
        if (bonus) System.out.print("35");
        else System.out.print("0");
        print("\t*");
        System.out.print("*  Upper Total:\t\t");
        System.out.print(this.getUpperTotal());
        print("\t*");
        print("*                               *");
        System.out.print("*  3 of Kind:\t\t");
        if (threeKind == -1) System.out.print("__");
        else System.out.print(threeKind);
        print("\t*");
        System.out.print("*  4 of Kind:\t\t");
        if (fourKind == -1) System.out.print("__");
        else System.out.print(fourKind);
        print("\t*");
        System.out.print("*  Full House:\t\t");
        if (fullHouse == -1) System.out.print("__");
        else System.out.print(fullHouse);
        print("\t*");
        System.out.print("*  Sm Straight:\t\t");
        if (smStraight == -1) System.out.print("__");
        else System.out.print(smStraight);
        print("\t*");
        System.out.print("*  Lg Straight:\t\t");
        if (lgStraight == -1) System.out.print("__");
        else System.out.print(lgStraight);
        print("\t*");
        System.out.print("*  Yahtzee:\t\t");
        if (fiveKind == -1) System.out.print("__");
        else System.out.print(fiveKind);
        print("\t*");
        System.out.print("*  Chance:\t\t");
        if (chance == -1) System.out.print("__");
        else System.out.print(chance);
        print("\t*");
        print("*                               *");
        System.out.print("*  Lower Total:\t\t");
        System.out.print(this.getLowerTotal());
        print("\t*");
        print("*                               *");
        System.out.print("*  Grand Total:\t\t");
        System.out.print(this.getGrandTotal());
        print("\t*");
        print("**********************************");
        print();
    }