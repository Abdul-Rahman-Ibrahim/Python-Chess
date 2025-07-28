let latestMove = null;

var whiteSquareGrey = '#a9a9a9'
var blackSquareGrey = '#696969'

function removeGreySquares() {
    $('#board .square-55d63').css('background', '')
}

function greySquare(square) {
    var $square = $('#board .square-' + square)

    var background = whiteSquareGrey
    if ($square.hasClass('black-3c85d')) {
        background = blackSquareGrey
    }

    $square.css('background', background)
}


function onMouseoverSquare(square, piece) {
    fetch(`/legal-move/?square=${square}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    })
        .then(res => res.json())
        .then(moves => {
            if (!Array.isArray(moves) || moves.length === 0) return;

            greySquare(square);

            for (let move of moves) {
                greySquare(move);
            }
        })
        .catch(err => console.error("Failed to fetch legal moves:", err));
}

function onMouseoutSquare(square, piece) {
    removeGreySquares()
}

function onDrop(source, target, piece, newPos, oldPos, orientation) {
    latestMove = {
        piece: piece,
        source: source,
        target: target,
        oldPos: oldPos
    };
    return;
}

function onSnapEnd() {
    if (!latestMove) return;

    fetch("/check-move/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(latestMove),
    })
        .then((res) => res.json())
        .then((data) => {
            if (!data.move_valid) {
                console.log('Illegal move. Reverting...');
                board.position(latestMove.oldPos);
            } else {
                console.log('Legal move.');
            }

            latestMove = null;
        });
}


var board = Chessboard('board', {
    draggable: true,
    dropOffBoard: 'snapback',
    position: 'start',
    pieceTheme: 'static/imgs/{piece}.png',
    onDrop: onDrop,
    onSnapEnd: onSnapEnd,
    onMouseoverSquare: onMouseoverSquare,
    onMouseoutSquare: onMouseoutSquare

});