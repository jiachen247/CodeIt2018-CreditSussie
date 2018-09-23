const puzzle =  [1, 2, 3, 4, 8, 5, 7, 6, 0]
dimensions = Math.sqrt(puzzle.length)

state = []

function check(p){
    var sorted = true;

    for (var i = 0; i < p.length - 2; i++) {
        if (p[i] > p[i+1]) {
            sorted = false;
            break;
        }
    }

    return sorted && p[dimensions *  dimensions - 1] == 0
}

function find_zero(p){
    return p.indexOf(0)
}

function calculate_moves(zero_index){
    var moves = []
    if (zero_index >= dimensions){
        moves.push(zero_index - dimensions)
    }
        
    if (zero_index < (dimensions*dimensions) - dimensions)
        moves.push(zero_index + dimensions)


    mod = zero_index % dimensions
    if (mod > 0)
        moves.push(zero_index - 1)
    if (mod < dimensions - 1)
        moves.push(zero_index + 1)

    return moves
}

function swap_moves(p, zero_index, target){
    p[zero_index] = p[target]
    p[target] = 0
    return p;
}

function solve(p, history){
    console.log("solving: " + p)

    const key = p.join("")


    if ((state.indexOf(key) > -1)) {
        console.log("repeat")
        return false
    }

    state.push(key)

    if (check(p)){
        console.log("FOUND")
        return history
    }

    var z = find_zero(p)

    var moves = calculate_moves(z)

    moves.forEach(function(move){
        var newp = swap_moves(p.slice(0), z, move)
        const k = newp.join("")
        if (state.indexOf(key) > -1) {
            solve(newp.valueOf(), history + p[move])
        }
    });

}

solve(puzzle, "")