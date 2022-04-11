use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut complements: HashMap<i32, i32> = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            match complements.get(num) {
                Some(&index) => return vec![index, i as i32],
                None => complements.insert(target - num, i as i32),
            };
        }
        
        vec![]
    }
}