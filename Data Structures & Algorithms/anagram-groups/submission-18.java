class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        List<List<String>> result = new ArrayList<>();

        Map<int[], List<String>> map = new HashMap<>();

        for (String str : strs) {
            int[] chars = new int[26];
            for (char c : str.toCharArray()) {
                chars[c - 'a']++;
            }

            boolean found = false;
            for (int[] arr : map.keySet()) {
                if (Arrays.equals(arr, chars)) {
                    List<String> list = map.get(arr);
                    list.add(str);
                    found = true;
                    break;
                }
            }

            if (!found) {
                List<String> list = new ArrayList<>();
                list.add(str);
                map.put(chars, list);
            }
        }

        for (int[] arr : map.keySet()) {
            result.add(map.get(arr));
        }

        return result;
        
    }
}
