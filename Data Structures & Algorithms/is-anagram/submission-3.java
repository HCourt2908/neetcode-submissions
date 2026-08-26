class Solution {
    public boolean isAnagram(String s, String t) {

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        if (s.length() != t.length()) return false;

        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();

        for (int i = 0; i < sChar.length; i++) {
            if (sMap.containsKey(sChar[i])) {
                sMap.put(sChar[i], sMap.get(sChar[i])+1);
            } else sMap.put(sChar[i], 1);

            if (tMap.containsKey(tChar[i])) {
                tMap.put(tChar[i], tMap.get(tChar[i])+1);
            } else tMap.put(tChar[i], 1);
        }

        return sMap.equals(tMap);

    }
}
