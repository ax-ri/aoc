use std::{cmp, fs, io::Read, ops};

#[cfg(test)]
pub static PART1_TEST: u64 = 3;
#[cfg(test)]
pub static PART2_TEST: u64 = 14;

fn parse(mut file: fs::File) -> anyhow::Result<(Vec<ops::RangeInclusive<u64>>, Vec<u64>)> {
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    let mut parts = content.split("\n\n");
    let (head, body) = (parts.next().unwrap(), parts.next().unwrap());
    let ranges = head
        .split("\n")
        .map_while(|l| {
            if l.is_empty() {
                None
            } else {
                let mut parts = l.split("-");
                Some(
                    parts.next().unwrap().parse::<u64>().unwrap()
                        ..=parts.next().unwrap().parse::<u64>().unwrap(),
                )
            }
        })
        .collect::<Vec<_>>();
    let numbers = body
        .split("\n")
        .map(|n| n.parse::<u64>().unwrap())
        .collect::<Vec<_>>();
    Ok((ranges, numbers))
}

pub fn part1(file: fs::File) -> anyhow::Result<u64> {
    let (ranges, numbers) = parse(file)?;
    let result = numbers
        .iter()
        .filter(|n| ranges.iter().any(|r| r.contains(n)))
        .count() as u64;
    Ok(result)
}

pub fn part2(file: fs::File) -> anyhow::Result<u64> {
    let (mut ranges, _) = parse(file)?;
    loop {
        ranges.sort_by_key(|r| *r.start());

        let mut new_ranges: Vec<ops::RangeInclusive<u64>> = Vec::new();
        for cur in ranges.iter() {
            if let Some(r) = new_ranges
                .iter_mut()
                .find(|r| r.contains(cur.start()) || r.contains(cur.end()))
            {
                *r = cmp::min(*r.start(), *cur.start())..=cmp::max(*r.end(), *cur.end());
            } else {
                new_ranges.push(cur.clone())
            }
        }
        if ranges == new_ranges {
            break;
        }
        ranges = new_ranges;
    }
    let result = ranges.iter().map(|r| r.end() - r.start() + 1).sum();
    Ok(result)
}
