Each sample in this directory presents the use of built-in objects to create a  rebeca program. 

| Sample (`samples/basics/`) | What it demonstrates | Built-in object(s) used | How to run | Expected `trace(...)` output (high level) |
|---|---|---|---|---|
| `helloworld.rebeca` | Minimal “hello world” Rebeca model | — | `python apps/rebeca/rebeca.py samples/basics/helloworld.rebeca` | Prints `Hello world.` |
| `list.rebeca` | Using the **list** container: add/remove/index/count | `list` | `python apps/rebeca/rebeca.py samples/basics/list.rebeca` | Traces `4` (count), then elements by index after removing `"bad"`: `a`, `b`, `c` |
| `map.rebeca` | Using the **map** container: set/get key-value pairs | `map` | `python apps/rebeca/rebeca.py samples/basics/map.rebeca` | Traces the value for key `"jack"`: `4098` |
| `queue.rebeca` | Using the **queue** container: push/pop/count (FIFO) | `queue` | `python apps/rebeca/rebeca.py samples/basics/queue.rebeca` | Traces `12` (count), then pops in FIFO order: `0, 1, 2, …, 11` |
| `stack.rebeca` | Using the **stack** container: push/pop/count (LIFO) | `stack` | `python apps/rebeca/rebeca.py samples/basics/stack.rebeca` | Traces `12` (count), then pops in LIFO order: `11, 10, 9, …, 0` |
| `fsm.rebeca` (with `fsm.json`) | Using the **fsm** helper: load transitions from JSON, query current state, trigger transitions | `fsm` | `python apps/rebeca/rebeca.py samples/basics/fsm.rebeca` | Starting from default state in `fsm.json`, traces the current state after each transition: `A → B → C → A` (one trace per step) |
