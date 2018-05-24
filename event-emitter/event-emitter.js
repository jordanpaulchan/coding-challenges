class EventEmitter {
  constructor() {
    this.map = new Map();
  }

  subscribe(eventName, callback, options) {
    if (this.map.has(eventName)) {
      this.map.get(eventName).push(callback);
    } else {
      this.map.set(eventName, [callback]);
    }
  }

  emit(eventName, ...args) {
    if (this.map.has(eventName)) {
      for (let callback of this.map.get(eventName)) {
        callback(...args);
      }
    }
  }

  unsubscribe(eventName, callback = null) {
    if (this.map.has(eventName)) {
      if (callback) {
        this.map.set(
          eventName,
          this.map.get(eventName).filter(callback => callback !== callback)
        );
      } else {
        this.map.delete(eventName);
      }
    }
  }
}

const eventEmitter = new EventEmitter();
const callback = console.log;
eventEmitter.subscribe("print", callback);
eventEmitter.emit("print", "Hello World");
eventEmitter.subscribe("print", callback);
eventEmitter.emit("print", "Test");
eventEmitter.unsubscribe("print");
eventEmitter.emit("print", "Don't print");
eventEmitter.subscribe("print", callback);
eventEmitter.emit("print", "Print");
eventEmitter.unsubscribe("print", callback);
eventEmitter.emit("print", "Don't print");
