// Add an event listener for the DOMContentLoaded event to ensure the script runs
// after the DOM (Document Object Model) is fully loaded.
document.addEventListener("DOMContentLoaded", () => {
    // Select all elements with the class 'cell' and store them in the 'cells' variable.
    const cells = document.querySelectorAll(".cell");

    // Initialize a variable to track the current player, starting with 'X'.
    let currentPlayer = "X";

    // Iterate over each cell element.
    cells.forEach(cell => {
        // Add a click event listener to each cell.
        cell.addEventListener("click", () => {
            // Check if the clicked cell is empty (has no text content).
            if (cell.textContent === "") {
                // If empty, set its text content to the current player's symbol ('X' or 'O').
                cell.textContent = currentPlayer;

                // Toggle the current player.
                // If the current player is 'X', change to 'O', and vice versa.
                currentPlayer = currentPlayer === "X" ? "O" : "X";
            }
        });
    });
});
