#include <iostream>
#include <vector>

using namespace std;

// Define the two sequences
string seq1 = "ACAGTCGAACG";
string seq2 = "ACCGTCCG";

// Define the match, mismatch and gap penalty scores
int match_score = 2, mismatch_score = -1, gap_penalty = -2;

// Define a function to print the dynamic programming matrix
void print_matrix(vector<vector<int>>& matrix) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
}

// Define a function to perform pairwise alignment using Needleman-Wunsch algorithm
void needleman_wunsch(string seq1, string seq2, int match_score, int mismatch_score, int gap_penalty, vector<vector<int>>& dp_matrix, vector<vector<int>>& pointer_matrix) {
    int m = seq1.length(), n = seq2.length();

    for (int i = 0; i <= m; i++) {
        dp_matrix[i][0] = i * gap_penalty;
        pointer_matrix[i][0] = 1;
    }
    for (int j = 0; j <= n; j++) {
        dp_matrix[0][j] = j * gap_penalty;
        pointer_matrix[0][j] = 2;
    }

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int match = dp_matrix[i-1][j-1] + (seq1[i-1] == seq2[j-1] ? match_score : mismatch_score);
            int delete_op = dp_matrix[i-1][j] + gap_penalty;
            int insert_op = dp_matrix[i][j-1] + gap_penalty;
            dp_matrix[i][j] = max({match, delete_op, insert_op});

            if (dp_matrix[i][j] == match) {
                pointer_matrix[i][j] = 3;
            }
            else if (dp_matrix[i][j] == delete_op) {
                pointer_matrix[i][j] = 1;
            }
            else {
                pointer_matrix[i][j] = 2;
            }
        }
    }
}

int main() {
    // Allocate the memory for the dynamic programming matrices
    int m = seq1.length(), n = seq2.length();
    vector<vector<int>> dp_matrix(m+1, vector<int>(n+1));
    vector<vector<int>> pointer_matrix(m+1, vector<int>(n+1));

    // Perform pairwise alignment of the two sequences
    needleman_wunsch(seq1, seq2, match_score, mismatch_score, gap_penalty, dp_matrix, pointer_matrix);

    // Print the dynamic programming matrix
    cout << "Dynamic Programming Matrix:" << endl;
    print_matrix(dp_matrix);

    return 0;
}
