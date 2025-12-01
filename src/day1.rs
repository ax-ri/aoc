use std::io::BufRead;
use std::{fs, io};

pub fn part1() {
    let mut total = 50;
    let mut count = 0;
    let lines = io::BufReader::new(fs::File::open("data/day1-1.txt").unwrap()).lines();
    for line in lines.map_while(|l| Some(l.unwrap())) {
        let is_left = line.chars().nth(0).unwrap() == 'L';
        let n = &line[1..].parse::<i32>().unwrap();
        if is_left {
            total -= n;
        } else {
            total += n;
        }
        total = total.rem_euclid(100);
        if total == 0 {
            count += 1;
        }
    }
    println!("result: {} (total {})", count, total);
}

pub fn part2() {
    let mut total = 50;
    let mut count = 0;
    let lines = io::BufReader::new(fs::File::open("data/day1-1.txt").unwrap()).lines();
    for line in lines.map_while(|l| Some(l.unwrap())) {
        let is_left = line.chars().nth(0).unwrap() == 'L';
        let n = &line[1..].parse::<i32>().unwrap();
        let prev_total = total;
        println!("result: {} (total {})", count, total);
        if is_left {
            total -= n;
        } else {
            total += n;
        }
        if total < 0 || total > 100 {
            let mut m = total.div_euclid(100).abs();
            println!("m: {}", m);
            if prev_total == 0 && is_left {
                m -= 1;
            }
            println!("yes, {}", m);
            count += m;
        } else if total.rem_euclid(100) == 0 {
            count += 1;
            println!("zero exact");
        }
        println!("result: {} (total {})", count, total);
        println!("-----------");

        total = total.rem_euclid(100);
    }
    println!("result: {} (total {})", count, total);
}

// 6236 too low
// 7223 too high
// 6990 nope
