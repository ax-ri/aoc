use std::fs;
use std::io::Read;

#[cfg(test)]
pub static PART1_TEST: u64 = 13;
#[cfg(test)]
pub static PART2_TEST: u64 = 43;

static DIRS: [(i32, i32); 8] = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
];

fn parse_grid(mut file: fs::File) -> anyhow::Result<Vec<Vec<bool>>> {
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    Ok(content
        .split("\n")
        .map(|line| line.chars().map(|c| c == '@').collect())
        .collect())
}

fn count_cells(y: usize, x: usize, grid: &Vec<Vec<bool>>) -> i32 {
    let mut count = 0;
    for (dy, dx) in DIRS {
        let (y, x) = ((y as i32) + dy, (x as i32) + dx);
        if y < 0 || y >= grid.len() as i32 || x < 0 || x >= grid[y as usize].len() as i32 {
            continue;
        }
        if grid[y as usize][x as usize] {
            count += 1;
        }
    }
    count
}

pub fn part1(file: fs::File) -> anyhow::Result<u64> {
    let grid = parse_grid(file)?;
    let mut result = 0;
    for y in 0..grid.len() {
        for x in 0..grid[y].len() {
            if !grid[y][x] {
                continue;
            }
            let count = count_cells(y, x, &grid);
            if count < 4 {
                result += 1;
            }
        }
    }

    Ok(result)
}

pub fn part2(file: fs::File) -> anyhow::Result<u64> {
    let mut grid = parse_grid(file)?;
    let mut result = 0;
    loop {
        let mut new_grid = grid.clone();
        for y in 0..grid.len() {
            for x in 0..grid[y].len() {
                if !grid[y][x] {
                    continue;
                }
                let count = count_cells(y, x, &grid);
                if count < 4 {
                    result += 1;
                    new_grid[y][x] = false;
                }
            }
        }
        if new_grid == grid {
            break;
        }
        grid = new_grid;
    }
    Ok(result)
}
