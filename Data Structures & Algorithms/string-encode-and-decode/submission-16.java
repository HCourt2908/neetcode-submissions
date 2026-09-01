class Solution {

    public String encode(List<String> strs) {

        String str = "";

        for (String string : strs) {
            str += String.valueOf(string.length());
            str += ".";
            str += string;
        }

        //System.out.println(str);
        return str;

    }

    public List<String> decode(String str) {

        List<String> strs = new ArrayList<>();

        int i = 0;

        while (i < str.length()) {
            int length = 0;

            while(str.charAt(i) != '.') {
                length = length * 10 + (str.charAt(i) - '0');
                i++;
            }

            i++;

            String currentString = str.substring(i, i + length);

            strs.add(currentString);
            i+= length;
        }

        return strs;

    }
}
