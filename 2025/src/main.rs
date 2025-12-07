extern crate core;

set_day!(day6);

use std::fs;

#[macro_export]
macro_rules! set_day {
    ( $module:ident  ) => {
        mod $module;
        #[cfg(test)]
        use $module::PART1_TEST;
        #[cfg(test)]
        use $module::PART2_TEST;
        use $module::part1;
        use $module::part2;
        static DAY: &str = stringify!($module);
    };
}

fn main() -> anyhow::Result<()> {
    println!("{}", DAY);
    println!("======== PART 1 ========");
    println!(
        "RESULT: {}",
        part1(fs::File::open(format!("data/{}.txt", DAY))?)?
    );
    println!("======== PART 2 ========");
    println!(
        "RESULT: {}",
        part2(fs::File::open(format!("data/{}.txt", DAY))?)?
    );
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_part1() -> anyhow::Result<()> {
        assert_eq!(
            part1(fs::File::open(format!("data/{}-test.txt", DAY))?)?,
            PART1_TEST
        );
        Ok(())
    }

    #[test]
    fn test_part2() -> anyhow::Result<()> {
        assert_eq!(
            part2(fs::File::open(format!("data/{}-test.txt", DAY))?)?,
            PART2_TEST
        );
        Ok(())
    }
}
