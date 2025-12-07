use std::io::BufRead;
use std::{fs, io};

#[cfg(test)]
pub static PART1_TEST: u64 = 4277556;
#[cfg(test)]
pub static PART2_TEST: u64 = 3263827;

pub fn part1(file: fs::File) -> anyhow::Result<u64> {
    let reader = io::BufReader::new(file);
    let lines = reader.lines().map(|l| l.unwrap()).collect::<Vec<_>>();
    let mut terms = Vec::new();
    for c in lines[0].split_whitespace() {
        terms.push(vec![c.parse::<u64>()?]);
    }
    for line in lines[1..(lines.len() - 1)].iter() {
        for (idx, c) in line.split_whitespace().enumerate() {
            terms[idx].push(c.parse::<u64>()?);
        }
    }
    let mut result = 0u64;
    for (idx, op) in lines[lines.len() - 1].split_whitespace().enumerate() {
        let t = terms[idx].iter();
        result += if op == "+" {
            t.sum::<u64>()
        } else {
            t.product::<u64>()
        };
    }

    Ok(result)
}

pub fn part2(file: fs::File) -> anyhow::Result<u64> {
    let reader = io::BufReader::new(file);
    let mut lines = reader.lines().map(|l| l.unwrap()).collect::<Vec<_>>();
    let line_count = lines.len();
    lines[line_count - 1].push_str(" x");
    let last_line_chars = lines[lines.len() - 1].clone().chars().collect::<Vec<_>>();
    let mut cols_width = Vec::new();
    let mut idx = 1;
    let mut w: usize;
    loop {
        w = 0;
        while last_line_chars[idx].is_whitespace() {
            idx += 1;
            w += 1;
        }
        idx += 1;
        cols_width.push(w);
        if idx >= last_line_chars.len() || w == 0 {
            break;
        }
    }
    let ops = lines[lines.len() - 1]
        .split_whitespace()
        .map(|s| s.chars().next().unwrap())
        .collect::<Vec<_>>();

    let mut digit_mat = Vec::new();
    for line in lines[0..(lines.len() - 1)].iter() {
        digit_mat.push(line.chars().collect::<Vec<_>>());
    }

    let mut result = 0u64;
    let mut offset = 0;
    for (op_idx, col_width) in cols_width.iter().cloned().enumerate() {
        let op = ops[op_idx];
        let mut acc = if op == '+' { 0 } else { 1 };
        for idx in 0..col_width {
            let mut n = 0u64;
            for row in digit_mat.iter() {
                if let Some(d) = row[idx + offset].to_digit(10) {
                    n = n * 10 + (d as u64)
                }
            }
            if op == '+' {
                acc += n;
            } else {
                acc *= n;
            }
        }
        offset += col_width + 1;
        result += acc;
    }
    Ok(result)
}
