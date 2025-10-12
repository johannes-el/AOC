use std::fs;

fn main() {
    let contents = fs::read_to_string("./src/input/input1.txt")
        .expect("Could not read the input file!");

    let mut max_1 = 0;
    let mut max_2 = 0;
    let mut max_3 = 0;

    let mut current_sum = 0;

    for line in contents.lines() {
	if line.is_empty() {
	    if current_sum > max_1 {
		max_3 = max_2;
		max_2 = max_1;
		max_1 = current_sum;
	    }
	    else if current_sum > max_2 {
		max_3 = max_2;
		max_2 = current_sum;
	    }
	    else if current_sum > max_3 {
		max_3 = current_sum;
	    }
	    current_sum = 0;
	}
	else {
	    current_sum += line.parse::<i32>().expect("Could not parse input!");
	}
    }

    let sum = max_1 + max_2 + max_3;
    println!("The maximum sum is: {sum}");
}
