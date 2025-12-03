use std::fs;
use std::io::{BufRead, BufReader};

#[cfg(test)]
pub static PART1_TEST: u32 = 357;
#[cfg(test)]
pub static PART2_TEST: u64 = 3121910778619;

pub fn part1(file: fs::File) -> anyhow::Result<u32> {
    let reader = BufReader::new(file);
    let result = reader
        .lines()
        .map(|l| {
            let digits = l
                .unwrap()
                .chars()
                .map(|c| c.to_digit(10).unwrap())
                .collect::<Vec<_>>();
            let (max_idx, m1) = digits
                .iter()
                .copied()
                .rev()
                .skip(1)
                .rev()
                .enumerate()
                .rev()
                .max_by_key(|(_idx, val)| *val)
                .unwrap();
            let m2 = digits[(max_idx + 1)..].iter().max().unwrap();
            m1 * 10 + *m2
        })
        .sum();
    Ok(result)
}

pub fn part2(file: fs::File) -> anyhow::Result<u64> {
    let reader = BufReader::new(file);
    let result = reader
        .lines()
        .map(|l| {
            let mut digits = l
                .unwrap()
                .chars()
                .map(|c| c.to_digit(10).unwrap())
                .collect::<Vec<_>>();
            let mut result: u64 = 0;
            for k in 1..=12 {
                let end_idx = digits.len() - (12 - k);
                let (max_idx, m) = digits[0..end_idx]
                    .iter()
                    .copied()
                    .enumerate()
                    .rev()
                    .max_by_key(|(_idx, val)| *val)
                    .unwrap();
                digits = digits.iter().skip(max_idx + 1).copied().collect::<Vec<_>>();
                result = result * 10 + (m as u64);
            }
            result
        })
        .sum();
    Ok(result)
}
