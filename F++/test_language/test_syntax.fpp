int mat_1[4][4];
int mat_2[4][4];
int res[4][4];
int i, j, k;

main () {
    i = 2;
    j= 2;
    k = 2;
    res[i][j] = 10;
    mat_1[i][k] = 2;
    mat_2[k][j] = 6;
    res[i][j] = res[i][j] + mat_1[i][k] * mat_2[k][j];
    consoleWrite(res[i][j]);

}