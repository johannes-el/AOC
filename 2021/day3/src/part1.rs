use std::fs;

fn convert_to_dec(binary: String) -> i32 {
    let mut result = 0;
    let mut power = 0;

    for ch in binary.chars().rev() {
        if ch == '1' {
            result += 2_i32.pow(power);
        }
        power += 1;
    }

    result
}

pub fn run() {
    let contents = fs::read_to_string("./input.txt").expect("Failed to read file!");

    let mut length_in_bytes = 0;

    if let Some(first_line) = contents.lines().next() {
        length_in_bytes = first_line.len();
    }

    let mut gamma_rate = String::new();
    let mut epsilon_rate = String::new();

    for i in 0..length_in_bytes {
        let mut zero_count = 0;
        let mut one_count = 0;
        for line in contents.lines() {
            if line.chars().nth(i).unwrap() == '0' {
                zero_count += 1;
            } else {
                one_count += 1;
            }
        }

        if zero_count < one_count {
            gamma_rate.push('1');
        } else {
            gamma_rate.push('0');
        }
    }

    for i in gamma_rate.chars() {
        if i == '0' {
            epsilon_rate.push('1');
        } else {
            epsilon_rate.push('0');
        }
    }

    let result = convert_to_dec(gamma_rate) * convert_to_dec(epsilon_rate);
    println!("{result}");
}
