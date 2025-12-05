use std::fs::File;
use std::io::{self,BufRead};
use std::path::Path;

fn main(){
    let banks = read_banks("input.txt");
    let res_1 = part_one(&banks);
    let res_2 = part_two(&banks);

    println!("{}", res_1);
    println!("{}", res_2);
}

fn part_one(banks: &Vec<String>) -> u32 {
    let mut res = 0u32;
    for bank_str in banks{
        let mut bank = Vec::new();
        for digit in bank_str.chars(){
            bank.push(digit.to_digit(10));
        }

        let mut max = 0;
        let mut i_max = 0;

        for i in 0..bank.len()-1{
            if bank[i] > Some(max) {
                max = bank[i].expect("1");
                i_max = i
            }
        }

        let mut max_2 = 0;
        for i in i_max+1..bank.len(){
            if bank[i] > Some(max_2) {
                max_2 = bank[i].expect("1");
            }
        }

        //println!("{0}, {1}",max,max_2);

        res += max*10u32 + max_2;
    }

    return res
}

fn part_two(banks: &Vec<String>) -> u64 {
    let mut res = 0u64;
    let ten = 10u64;

    for bank_str in banks{
        let mut bank = Vec::new();
        for digit in bank_str.chars(){
            bank.push(digit.to_digit(10));
        }

        let mut i_max = -1isize;

        for k in (0..12).rev() {
            let mut max = 0;
            for i in ((i_max+1) as usize)..bank.len()-k{
                if bank[i] > Some(max) {
                    max = bank[i].expect("1");
                    i_max = i as isize
                }
            }
            res += (max as u64)*ten.pow(k as u32)
        }

    }

    return res
}

fn read_banks<P>(filename: P) -> Vec<String>
where P: AsRef<Path>, {
    let mut banks = Vec::new();
    if let Ok(lines) = read_lines(filename){
        for line in lines.map_while(Result::ok){
            //println!("{}",line);
            banks.push(line);
        }
    }
    return banks
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>());
}