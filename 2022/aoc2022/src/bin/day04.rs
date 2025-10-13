use std::fs;

fn part_1(contents: String) -> i32 {

    let mut count_fully_contained_pairs = 0;

    for line in contents.lines() {
        let parts: Vec<&str> = line
            .split(|c: char| c == ',' || c == '-')
            .filter(|p| !p.is_empty())
            .collect();
        
        if parts.len() != 4 {
            eprintln!("Skipping malformed line: {}", line);
            continue;
        }

        let r1_start: i32 = parts[0].parse().expect("Failed to parse R1 start");
        let r1_end: i32 = parts[1].parse().expect("Failed to parse R1 end");
        let r2_start: i32 = parts[2].parse().expect("Failed to parse R2 start");
        let r2_end: i32 = parts[3].parse().expect("Failed to parse R2 end");
        
	let r1_in_r2 = r2_start >= r1_start && r2_end <= r1_end;
	let r2_in_r1 = r1_start >= r2_start && r1_end <= r2_end;

	if r1_in_r2 || r2_in_r1 {
	    count_fully_contained_pairs += 1;
	}
    }

    count_fully_contained_pairs
}

fn part_2(contents: String) -> i32 {
    let mut count_any_overlaps = 0;

    for line in contents.lines() {
        let parts: Vec<&str> = line
            .split(|c: char| c == ',' || c == '-')
            .filter(|p| !p.is_empty())
            .collect();
        
        if parts.len() != 4 {
            eprintln!("Skipping malformed line: {}", line);
            continue;
        }

        let r1_start: i32 = parts[0].parse().expect("Failed to parse R1 start");
        let r1_end: i32 = parts[1].parse().expect("Failed to parse R1 end");
        let r2_start: i32 = parts[2].parse().expect("Failed to parse R2 start");
        let r2_end: i32 = parts[3].parse().expect("Failed to parse R2 end");
        
	let no_overlap = r1_end < r2_start || r2_end < r1_start;
	let any_overlap = !no_overlap;

	if any_overlap {
	    count_any_overlaps += 1;
	}
    }

    count_any_overlaps
}

fn main() {
    let contents = fs::read_to_string("./src/input/input4.txt")
        .expect("Failed to read input file!");

    let part1 = false;

    if part1 {
	let sum: i32 = part_1(contents);
	println!("The solution to part1 is: {sum}");
    }
    else {
	let sum: i32 = part_2(contents);
	println!("The solution to part2 is: {sum}");
    }
}
