use std::fs;
use std::io::Read;

#[cfg(test)]
pub static PART1_TEST: u64 = 21;
#[cfg(test)]
pub static PART2_TEST: u64 = 40;

fn parse_grid(mut file: fs::File) -> anyhow::Result<Vec<Vec<char>>> {
    let mut content = String::new();
    file.read_to_string(&mut content)?;
    let grid = content
        .split("\n")
        .map(|s| s.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();
    Ok(grid)
}

pub fn part1(file: fs::File) -> anyhow::Result<u64> {
    let mut grid = parse_grid(file)?;

    let mut result = 0;
    for y in 0..grid.len() - 1 {
        for x in 0..grid[0].len() {
            match grid[y][x] {
                'S' => grid[y + 1][x] = '|',
                '|' if y + 1 < grid.len() => match grid[y + 1][x] {
                    '.' => grid[y + 1][x] = '|',
                    '^' => {
                        if x > 0 {
                            grid[y + 1][x - 1] = '|';
                        }
                        if x < grid[0].len() - 1 {
                            grid[y + 1][x + 1] = '|';
                        }
                        result += 1;
                    }
                    _ => (),
                },
                _ => (),
            }
        }
    }

    Ok(result)
}

fn add_to_cell(grid: &mut [Vec<String>], x: usize, y: usize, v: u64) {
    let n = grid[y][x].parse::<u64>().unwrap_or_default();
    grid[y][x] = (n + v).to_string();
}

pub fn part2(file: fs::File) -> anyhow::Result<u64> {
    let grid = parse_grid(file)?;
    let mut grid = grid
        .iter()
        .map(|v| {
            v.iter()
                .map(|c| match *c {
                    'S' => "1".to_string(),
                    '.' => "0".to_string(),
                    _ => c.to_string(),
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    for y in 0..grid.len() - 1 {
        for x in 0..grid[0].len() {
            if let Ok(n) = grid[y][x].parse::<u64>() {
                if grid[y + 1][x].as_str() == "^" {
                    if x > 0 {
                        add_to_cell(&mut grid, x - 1, y + 1, n);
                    }
                    if x < grid[0].len() - 1 {
                        add_to_cell(&mut grid, x + 1, y + 1, n);
                    }
                } else {
                    add_to_cell(&mut grid, x, y + 1, n);
                }
            }
        }
    }

    let result = grid[grid.len() - 1]
        .iter()
        .map(|r| r.parse::<u64>().unwrap())
        .sum::<u64>();
    Ok(result)
}
