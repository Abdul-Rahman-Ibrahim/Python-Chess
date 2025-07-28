let latestMove = null;

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
    onSnapEnd: onSnapEnd
});