let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";

const cells = document.querySelectorAll(".cell");

cells.forEach((cell, index) => {
    cell.addEventListener("click", () => {
        if (!board[index]) {
            board[index] = currentPlayer;
            cell.innerHTML = currentPlayer;
            if (checkWin()) {
                alert(`Player ${currentPlayer} wins!`);
                resetBoard();
            } else if (board.every(cell => cell)) {
                alert("It's a tie!");
                resetBoard();
            } else {
                currentPlayer = currentPlayer === "X" ? "O" : "X";
            }
        }
    });
});

function checkWin() {
    const winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
        [0, 4, 8], [2, 4, 6]  // diagonals
    ];

    return winPatterns.some(pattern =>
        board[pattern[0]] === currentPlayer &&
        board[pattern[1]] === currentPlayer &&
        board[pattern[2]] === currentPlayer
    );
}

function resetBoard() {
    board = ["", "", "", "", "", "", "", "", ""];
    cells.forEach(cell => cell.innerHTML = "");
    currentPlayer = "X";
}
