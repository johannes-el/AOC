const fs = require('fs');

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }

    let sum = 0;
    let current_digit = "";
    let digit_before = false;
    let negative = false;

    for (let i = 0; i < data.length; i++) {
        let char = data[i];

        if (char === '-') {
            negative = true;
        } else if (char >= '0' && char <= '9') {
            if (digit_before) {
                current_digit += char;
            } else {
                current_digit = char;
                digit_before = true;
            }
        } else if (digit_before) {
            sum += negative ? -parseInt(current_digit) : parseInt(current_digit);

            digit_before = false;
            negative = false;
            current_digit = "";
        }
    }

    if (digit_before) {
        sum += negative ? -parseInt(current_digit) : parseInt(current_digit);
    }

    console.log(sum);
});
