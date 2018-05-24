# Event emitter

We're going to make our own event emitter application! The application must perform three types of operations:

1.  Subscribe. Store the callback to be invoked when the event is triggered. This must store the callback as a new entry for the event.
2.  Unsubscribe. Removes the callback specified or all of the callbacks stored for a given event.
3.  Emit. Invoke all callbacks subscribed to the event emitted with the aruments provided.

Given n sequential add and get operations, perform each operation in order.

## Example

**Operation, Action, Callback**
subscribe, print, console.log

**Operation, Action, Arguments**
emit print "Test"

**Operation, Action, Callback**
unsubscribe, print, console.log

**Operation, Action, Arguments**
emit print "Test"

### Output:

Test

## Run the program

In the folder run the command:

```
node event-emitter.js
```
