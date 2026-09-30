#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void uniform(char *str, int len) {
    int i;
    FILE *fp;
    fp = fopen(str, "w");
    for (i = 0; i < len; i++) {
        fprintf(fp, "%lf\n", (double)rand() / RAND_MAX);
    }
    fclose(fp);
}

void solveMinesweeper(int n, int m) {
    int total = n * m;
    
    // 1. Generate random values using uniform()
    uniform("binary.dat", total);

    FILE *fp = fopen("binary.dat", "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    int grid[100][100];
    int result[100][100];
    double x;

    // 2. Read values and convert to binary mine grid (0 or 1)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            fscanf(fp, "%lf", &x);
            grid[i][j] = (x < 0.5) ? 0 : 1;
        }
    }
    fclose(fp);

    // Print the randomly generated initial minefield
    printf("\nInitial Minefield (0 = empty, 1 = mine):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }

    // 3. Direction vectors to check all 8 neighboring cells
    int dx[] = {-1, -1, -1,  0, 0,  1, 1, 1};
    int dy[] = {-1,  0,  1, -1, 1, -1, 0, 1};

    // 4. Calculate Minesweeper numbers
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                result[i][j] = -1; // -1 for cells with a mine
            } else {
                int mine_count = 0;
                for (int d = 0; d < 8; d++) {
                    int ni = i + dx[d];
                    int nj = j + dy[d];

                    // Check boundaries and count neighboring mines
                    if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
                        if (grid[ni][nj] == 1) {
                            mine_count++;
                        }
                    }
                }
                result[i][j] = mine_count;
            }
        }
    }

    // 5. Print the solved Minesweeper output matrix
    printf("\nSolved Minesweeper Output:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%2d ", result[i][j]);
        }
        printf("\n");
    }
}

int main(void) {
    srand(time(NULL));

    int n, m;
    printf("Enter rows (n) and columns (m): ");
    scanf("%d %d", &n, &m);

    solveMinesweeper(n, m);

    return 0;
}

