function patternMatch(string1, string2) {
    const words = string1.split(' ');
    const chars = string2.split('');

    const wordsMap = new Map();
    const charsMap = new Set();

    let wordsPtr = 0;
    let charsPtr = 0;

    while (wordsPtr < words.length && charsPtr < chars.length) {
       if (wordsMap.has(words[wordsPtr])) {
           if (wordsMap.get(words[wordsPtr]) !== chars[charsPtr]) {
               return false;
           }
       } else if (charsMap.has(chars[charsPtr])) {
           return false;
       } else {
           wordsMap.set(words[wordsPtr], chars[charsPtr]);
           charsMap.add(chars[charsPtr]);
       }
       wordsPtr++;
       charsPtr++;
    }

    return true;
}