use std::fs;
use std::io::Read;
use std::ops::RangeInclusive;

#[cfg(test)]
pub static PART1_TEST: u64 = 1227775554;
#[cfg(test)]
pub static PART2_TEST: u64 = 4174379265;

fn parse(mut file: fs::File) -> anyhow::Result<Vec<RangeInclusive<u64>>> {
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    Ok(content
        .split(",")
        .map_while(|s| match *s.split('-').collect::<Vec<_>>().as_slice() {
            [x, y] => Some((x.parse::<u64>().unwrap(), y.parse::<u64>().unwrap())),
            _ => None,
        })
        .map(|(x, y)| x..=y)
        .collect())
}

pub fn is_invalid_part1(n: &u64) -> bool {
    let s = n.to_string();
    if !s.len().is_multiple_of(2) {
        return false;
    }
    let l = s.len() / 2;
    s[..l] == s[l..]
}

pub fn part1(file: fs::File) -> anyhow::Result<u64> {
    let intervals = parse(file)?;
    Ok(intervals
        .iter()
        .map(|i| i.clone().filter(is_invalid_part1).sum::<u64>())
        .sum::<u64>())
}

pub fn is_invalid_part2(n: &u64) -> bool {
    if *n < 10 {
        return false;
    }
    let s = n.to_string();
    for l in 1..=(s.len() / 2) {
        let mut c = s.as_bytes().chunks(l);
        let r = c.clone().next().unwrap();
        if c.all(|c| c == r) {
            return true;
        }
    }
    false
}

pub fn part2(file: fs::File) -> anyhow::Result<u64> {
    // println!("s: {}", is_invalid_part2(&12341234));

    let intervals = parse(file)?;
    Ok(intervals
        .iter()
        .map(|i| i.clone().filter(is_invalid_part2).sum::<u64>())
        .sum::<u64>())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    pub fn is_invalid_part_1_test() {
        assert!(is_invalid_part1(&11));
        assert!(is_invalid_part1(&22));
        assert!(is_invalid_part1(&1212));
        assert!(is_invalid_part1(&123123));
        assert!(!is_invalid_part1(&142345));
        assert!(!is_invalid_part1(&101));
    }

    #[test]
    pub fn is_invalid_part_2_test() {
        // assert!(is_invalid_part2(&11));
        // assert!(is_invalid_part2(&22));
        // assert!(is_invalid_part2(&1212));
        // assert!(is_invalid_part2(&123123));
        // assert!(!is_invalid_part2(&142345));
        // assert!(!is_invalid_part2(&101));

        assert!(is_invalid_part2(&12341234));
        // assert!(is_invalid_part2(&123123123));
        // assert!(is_invalid_part2(&1212121212));
        // assert!(is_invalid_part2(&1111111));
    }
}
