use std::fs;

#[derive(Clone, Copy)]
enum Move {
    A,
    B,
    C,
}

#[derive(Clone, Copy)]
enum Choice {
    X,
    Y,
    Z,
}

fn score_part1(opponent: Move, my_choice: Choice) -> i32 {
    use Move::*;
    use Choice::*;

    match (opponent, my_choice) {
        (A, X) => 1 + 3,
        (A, Y) => 2 + 6,
        (A, Z) => 3 + 0,

        (B, X) => 1 + 0,
        (B, Y) => 2 + 3,
        (B, Z) => 3 + 6,

        (C, X) => 1 + 6,
        (C, Y) => 2 + 0,
        (C, Z) => 3 + 3,
    }
}

fn score_part2(opponent: Move, my_choice: Choice) -> i32 {
    use Move::*;
    use Choice::*;

    match (opponent, my_choice) {
        (A, X) => 3 + 0,
        (A, Y) => 1 + 3,
        (A, Z) => 2 + 6,

        (B, X) => 1 + 0,
        (B, Y) => 2 + 3,
        (B, Z) => 3 + 6,

        (C, X) => 2 + 0,
        (C, Y) => 3 + 3,
        (C, Z) => 1 + 6,
    }
}

fn main() {
    let contents = fs::read_to_string("./src/input/input2.txt")
        .expect("Failed to read input file!");

    let part1 = false;

    let mut win_score = 0;

    for line in contents.lines() {
        let opponent = match line.chars().nth(0).unwrap() {
            'A' => Move::A,
            'B' => Move::B,
            'C' => Move::C,
            other => panic!("Unexpected opponent char: {}", other),
        };

        let my_choice = match line.chars().nth(2).unwrap() {
            'X' => Choice::X,
            'Y' => Choice::Y,
            'Z' => Choice::Z,
            other => panic!("Unexpected my_choice char: {}", other),
        };

        win_score += if part1 {
            score_part1(opponent, my_choice)
        } else {
            score_part2(opponent, my_choice)
        };
    }

    println!("{win_score}");
}
