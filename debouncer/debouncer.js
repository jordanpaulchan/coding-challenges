/*
Implement a debounce function in javascript
When a user types into an input field, trigger a function to an api endpoint after 500ms 
Timer resets on each key press within 500ms window
*/

function debouncer() {
  let timer = null;

  return (callback, immediately, ...payload) => {
    clearTimeout(timer);

    if (immediately) {
      callback(...payload);
    } else {
      timer = setTimeout(() => {
        callback(...payload);
      }, 500);
    }
  };
}

function print(string1, string2) {
  console.log(string1 + string2);
}

const debounce = debouncer();
debounce(console.log, false, "Hello World");
setTimeout(() => {
  debounce(print, false, "Hello World log 1", " additional string");
}, 300);
setTimeout(() => {
  debounce(console.log, false, "Hello World do not log");
}, 900);
setTimeout(() => {
  debounce(console.log, true, "Hello World log still log this");
}, 1000);
setTimeout(() => {
  debounce(console.log, false, "Hello World log will be logged");
}, 1000);
