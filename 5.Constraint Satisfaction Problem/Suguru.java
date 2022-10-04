import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.IntVar;

public class Suguru {
    public static void main(String[] args) {
        int i, j, k;

        // Create a Model
        Model model = new Model("201914039 CSP Assignment");

        // Create the 6x6 board with values in the range 1 to 5
        IntVar[][] bd = model.intVarMatrix("bd", 6, 6, 1, 5);

        // Create the blocks (1D array) with values in the range 1 to 5
        IntVar[] b0 = model.intVarArray("b0", 5, 1, 5);
        IntVar[] b1 = model.intVarArray("b1", 5, 1, 5);
        IntVar[] b2 = model.intVarArray("b2", 5, 1, 5);
        IntVar[] b3 = model.intVarArray("b3", 5, 1, 5);
        IntVar[] b4 = model.intVarArray("b4", 3, 1, 3);
        IntVar[] b5 = model.intVarArray("b5", 5, 1, 5);
        IntVar[] b6 = model.intVarArray("b6", 5, 1, 5);
        IntVar[] b7 = model.intVarArray("b7", 3, 1, 3);

        // Post constraints
        // Given constraints
        model.arithm(bd[0][5], "=", 5).post();
        model.arithm(bd[1][1], "=", 2).post();
        model.arithm(bd[1][3], "=", 5).post();
        model.arithm(bd[3][4], "=", 2).post();
        model.arithm(bd[4][1], "=", 1).post();
        model.arithm(bd[4][5], "=", 3).post();

        // Mapping the board with the blocks
        // 0th row
        model.arithm(bd[0][0], "=", b0[0]).post();
        model.arithm(bd[0][1], "=", b0[1]).post();
        model.arithm(bd[0][2], "=", b0[2]).post();
        model.arithm(bd[0][3], "=", b0[3]).post();
        model.arithm(bd[0][4], "=", b1[0]).post();
        model.arithm(bd[0][5], "=", b1[1]).post();

        // 1st row
        model.arithm(bd[1][0], "=", b2[0]).post();
        model.arithm(bd[1][1], "=", b2[1]).post();
        model.arithm(bd[1][2], "=", b3[0]).post();
        model.arithm(bd[1][3], "=", b0[4]).post();
        model.arithm(bd[1][4], "=", b1[2]).post();
        model.arithm(bd[1][5], "=", b1[3]).post();

        // 2nd row
        model.arithm(bd[2][0], "=", b2[2]).post();
        model.arithm(bd[2][1], "=", b3[1]).post();
        model.arithm(bd[2][2], "=", b3[2]).post();
        model.arithm(bd[2][3], "=", b3[3]).post();
        model.arithm(bd[2][4], "=", b4[0]).post();
        model.arithm(bd[2][5], "=", b1[4]).post();

        // 3rd row
        model.arithm(bd[3][0], "=", b2[3]).post();
        model.arithm(bd[3][1], "=", b5[0]).post();
        model.arithm(bd[3][2], "=", b3[4]).post();
        model.arithm(bd[3][3], "=", b6[0]).post();
        model.arithm(bd[3][4], "=", b4[1]).post();
        model.arithm(bd[3][5], "=", b4[2]).post();

        // 4th row
        model.arithm(bd[4][0], "=", b2[4]).post();
        model.arithm(bd[4][1], "=", b5[1]).post();
        model.arithm(bd[4][2], "=", b6[1]).post();
        model.arithm(bd[4][3], "=", b6[2]).post();
        model.arithm(bd[4][4], "=", b6[3]).post();
        model.arithm(bd[4][5], "=", b7[0]).post();

        // 5th row
        model.arithm(bd[5][0], "=", b5[2]).post();
        model.arithm(bd[5][1], "=", b5[3]).post();
        model.arithm(bd[5][2], "=", b5[4]).post();
        model.arithm(bd[5][3], "=", b6[4]).post();
        model.arithm(bd[5][4], "=", b7[1]).post();
        model.arithm(bd[5][5], "=", b7[2]).post();

        // direction array for locating the 8 adjacent cells of a cell
        int[] X = new int[] { 0, 0, 1, -1, -1, 1, -1, 1 };
        int[] Y = new int[] { -1, 1, 0, 0, 1, 1, -1, -1 };

        for (i = 0; i < 6; i++) {
            for (j = 0; j < 6; j++) {
                for (k = 0; k < 8; k++) {
                    int x = i + X[k];
                    int y = j + Y[k];
                    if (x < 0 || x > 5 || y < 0 || y > 5) {
                        continue;
                    }
                    // creating a temporary array consisting of a cell and its adjacent cell
                    IntVar[] dd = model.intVarArray("temp", 2, 1, 5);
                    // Mapping the cells with the board
                    model.arithm(bd[x][y], "=", dd[0]).post();
                    model.arithm(bd[i][j], "=", dd[1]).post();
                    // The values of cells are made diffeerent
                    model.allDifferent(dd).post();
                }
            }
        }

        // all the numbers in each blocks are made different
        model.allDifferent(b0).post();
        model.allDifferent(b1).post();
        model.allDifferent(b2).post();
        model.allDifferent(b3).post();
        model.allDifferent(b4).post();
        model.allDifferent(b5).post();
        model.allDifferent(b6).post();
        model.allDifferent(b7).post();

        // Solve the problem
        Solver solver = model.getSolver();
        solver.showStatistics();
        solver.showSolutions();
        solver.findSolution();

        // Print the solution
        for (i = 0; i < 6; i++) {
            for (j = 0; j < 6; j++) {
                System.out.print(" ");
                /* get the value for the board position [i][j] for the solved board */
                k = bd[i][j].getValue();
                System.out.print(k);
            }
            System.out.println();
        }
    }
}