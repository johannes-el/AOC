use std::collections::HashSet;
use std::fs;

fn get_priority(letter: char) -> u8 {

    // Matches characters to 1..26 and 27..52 range
    match letter {
	'a'..='z' => (letter as u8) - ('a' as u8) + 1,
	'A'..='Z' => (letter as u8) - ('A' as u8) + 27,
	_ => panic!("Invalid character for priority matching: {letter}!")
    }
}

fn part_one(contents: String) -> u32 {

    let mut prio_sum: u32 = 0;

    for line in contents.lines() {

	let length = line.len();
	let mid = length / 2;
	let mut set = HashSet::new();

	for idx in 0..mid {
	    let prio = get_priority(line.chars().nth(idx).expect("Rucksack is empty"));
	    set.insert(prio);
	}

	for idx in mid..length {
	    let prio = get_priority(line.chars().nth(idx).expect("Rucksack is empty"));
	    if set.contains(&prio) {
		prio_sum += prio as u32;
		break;
	    }
	}
    }

    prio_sum
}

fn part_two(contents: String) -> u32 {
    let lines: Vec<&str> = contents.lines().collect();
    let mut prio_sum = 0;

    for window in lines.windows(3).step_by(3) {
        let a: HashSet<char> = window[0].chars().collect();
        let b: HashSet<char> = window[1].chars().collect();
        let c: HashSet<char> = window[2].chars().collect();

        let ab: HashSet<char> = a.intersection(&b).copied().collect();
        let abc: HashSet<char> = ab.intersection(&c).copied().collect();

        if let Some(&badge) = abc.iter().next() {
            let prio = get_priority(badge);
            prio_sum += prio as u32;
        } else {
            panic!("No common badge found for group: {:?}", window);
        }
    }

    prio_sum
}


fn main() {
    let contents = fs::read_to_string("./src/input/input3.txt")
        .expect("Failed to read input file!");

    let part1 = false;

    if part1 {
	let sum = part_one(contents);
	println!("{sum}");
    }

    else {
	let sum = part_two(contents);
	println!("{sum}");
    }
}
