use std::io::BufRead;
use std::{fs, io};

#[cfg(test)]
pub static PART1_TEST: i32 = 3;
#[cfg(test)]
pub static PART2_TEST: i32 = 6;

pub fn part1(file: fs::File) -> anyhow::Result<i32> {
    let mut total = 50;
    let mut count = 0;
    let lines = io::BufReader::new(file).lines();
    for line in lines.map_while(|l| Some(l.unwrap())) {
        let is_left = line.starts_with('L');
        let n = &line[1..].parse::<i32>()?;
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
    Ok(count)
}

pub fn part2(file: fs::File) -> anyhow::Result<i32> {
    let mut total = 50;
    let mut count = 0;
    let lines = io::BufReader::new(file).lines();
    for line in lines.map_while(|l| Some(l.unwrap())) {
        let is_left = line.starts_with('L');
        let n = &line[1..].parse::<i32>()?;
        let prev_total = total;
        if is_left {
            total -= n;
        } else {
            total += n;
        }

        let m = total.div_euclid(100);
        if prev_total == 0 && is_left {
            count -= 1;
        }
        count += m.abs();

        total = total.rem_euclid(100);
        if total == 0 && m <= 0 {
            count += 1;
        }
    }
    Ok(count)
}
